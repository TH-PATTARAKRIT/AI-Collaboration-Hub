# SMEsPlus ENTERPRISE SUITE
## GMVQ — G02 IDENTITY_ACCESS / auth_totp_portal Module Adversarial MVQ Bank

**Document ID:** GMVQ-G02-AUTH_TOTP_PORTAL-MVQ48-V1.00
**Group:** G02 IDENTITY_ACCESS
**Module Metadata:** `auth_totp_portal`
**Wave:** W1
**Author Cell:** TEAM 13 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN / REVISED R1
**CHANGE_REASON (R1):** Returned by GMVQ MASTER AUDIT TEAM M2 under Boss directive SMEPLUS-GMVQ-20P-5AUDIT-20260927-004 — closed-vocabulary (RISK_TIER / OUTPUT_CLASS) field-value defect(s) corrected by production (R1). 13 OUTPUT_CLASS values outside the enum (STATE TRANSITION x7, AUDIT x6) reclassified per-question from HYPOTHESIS content.
**Standing Authorization:** governs this production run under directive SMEPLUS-GMVQ-25TEAM-ACCELERATION-20260927-001
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded
**actual_mvq_count:** 48

## Purpose

This bank supplies module-specific research questions for the second-factor regime applied to
external (customer-facing, non-employee) users. It targets the ground where an external-facing
enforcement layer diverges from an internal one: unverifiable enrolment, unattended recovery,
multi-tenant identity, non-interactive entry paths, machine credentials, per-tenant configuration
authority, abuse economics, and auditability of the authentication decision itself.

The question text is source-neutral. It does not expose vendor or product names, model or field
names, method names, XML IDs, API shapes, or any other implementation identifier, and it never
repeats the module's own metadata name outside the `MODULE:` field.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a failure state,
  never a restatement of the hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across
  enrolment, policy divergence, recovery, tenancy, non-interactive access, machine credentials,
  administrative control, abuse/denial-of-service, and auditability.
- Questions are not evidence. A later ANSWERED state requires an actual artifact or observation.
- `MODULE + QID` is a Research Evidence Join Key only; it does not by itself constitute coverage.
- This bank is DRAFT / AUTHORING COMPLETE / NOT FROZEN. It is not approved, not verified, and not
  MASTER-ready.

## G02-AUTH_TOTP_PORTAL-Q001

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q001
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Completing second-factor enrolment for an external identity does not by itself establish that
  the enrolling party is the person the relationship was formed with.
WHY_IT_MATTERS: >
  If enrolment is treated as proof of identity, an unverified party can lock out the legitimate
  external user or impersonate them for every future session.
DISCONFIRMING_OBSERVATION: >
  A newly self-enrolled external identity is granted the same ongoing trust as one whose identity
  was independently confirmed, with no distinguishing record of how the enrolment was reached.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Create an external account with no prior verified interaction, complete self-service enrolment
  of the factor, and inspect what assurance level, if any, is recorded against that enrolment.
```

## G02-AUTH_TOTP_PORTAL-Q002

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q002
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an external identity holds more than one concurrently enrolled factor, exactly one
  authoritative outcome governs each authentication attempt.
WHY_IT_MATTERS: >
  Ambiguous handling of multiple enrolments can let an attacker-registered factor stand alongside
  the legitimate one indefinitely.
DISCONFIRMING_OBSERVATION: >
  Two concurrently enrolled factors for the same identity produce inconsistent accept/reject
  outcomes for otherwise identical attempts, or a second enrolment silently supersedes the first
  with no notice to the account holder.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Enrol a second factor instance on an external identity that already has one enrolled, then
  exercise authentication with each.
```

## G02-AUTH_TOTP_PORTAL-Q003

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q003
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Self-registration for an external identity and enrolment of its second factor are separated by
  at least one independently checkable step, rather than being a single unchecked flow.
WHY_IT_MATTERS: >
  Collapsing registration and enrolment into one unchecked step lets anyone create a fully
  trusted external identity with no external verification whatsoever.
DISCONFIRMING_OBSERVATION: >
  A single unattended flow produces a self-registered external identity with its second factor
  already enrolled and fully authorized for sensitive actions, with no intervening check.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Walk the self-registration path for a new external identity end to end without any manual
  intervention and note where, if anywhere, an independent check is required.
```

## G02-AUTH_TOTP_PORTAL-Q004

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q004
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Replacing an already-enrolled second factor requires proof at least as strong as the proof
  required for initial enrolment.
WHY_IT_MATTERS: >
  A weaker replacement path turns factor replacement into the easiest way to take over an
  external account.
DISCONFIRMING_OBSERVATION: >
  An external identity can replace its enrolled factor through a path that demands less proof
  than the original enrolment required.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Compare the proof demanded at initial enrolment against the proof demanded when an already
  enrolled external identity replaces its factor.
```

## G02-AUTH_TOTP_PORTAL-Q005

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q005
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When operator or support staff perform enrolment on behalf of an external user, the action is
  distinguishable from a self-service enrolment and does not silently hand the operator ongoing
  control of the factor.
WHY_IT_MATTERS: >
  An indistinguishable staff-assisted enrolment is a standing insider bypass of the external
  user's own control over their credential.
DISCONFIRMING_OBSERVATION: >
  A factor enrolled by staff on behalf of an external user is recorded identically to a
  self-service enrolment, or the assisting staff member retains a usable copy of the factor.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Have a support-privileged account perform enrolment for an external identity and inspect the
  resulting record and any residual access held by the assisting account.
```

## G02-AUTH_TOTP_PORTAL-Q006

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q006
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where an operator is permitted to configure the external second-factor regime more leniently
  than the internal one, that leniency is an explicit, recorded decision rather than an
  unreviewed default.
WHY_IT_MATTERS: >
  An unreviewed weaker default for external users understates the actual exposure of
  customer-facing access.
DISCONFIRMING_OBSERVATION: >
  The external regime is materially weaker than the internal regime with no explicit
  configuration record showing that the difference was a deliberate operator choice.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Inspect the internal and external policy configurations side by side and locate the record, if
  any, that justifies a difference between them.
```

## G02-AUTH_TOTP_PORTAL-Q007

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q007
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An identity that holds both an internal (employee-type) relationship and an external
  (customer-facing) relationship is held to at least the stronger of the two enforcement regimes
  for every session, regardless of which relationship the session is entered through.
WHY_IT_MATTERS: >
  Without this, the weaker external regime becomes the practical security level for a dual-role
  identity, undermining the internal regime entirely.
DISCONFIRMING_OBSERVATION: >
  An identity holding both relationship types can reach internal-scope actions through a session
  that only satisfied the weaker external enforcement.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Configure one identity with both an internal and an external relationship under diverging
  policies, then attempt internal-scope actions from a session authenticated only to the external
  standard.
```

## G02-AUTH_TOTP_PORTAL-Q008

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q008
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an external identity is later granted an internal-style scope of access, its enforcement
  regime is re-evaluated rather than carrying forward the weaker external enrolment unchanged.
WHY_IT_MATTERS: >
  A carried-forward weak enrolment becomes a standing gap the moment an external party's access
  is broadened.
DISCONFIRMING_OBSERVATION: >
  An identity promoted from external to internal-style scope keeps operating under its original
  external-strength enrolment with no re-enrolment or re-evaluation triggered.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Promote an external identity to an internal-style scope and observe whether the second-factor
  regime is re-evaluated at that transition.
```

## G02-AUTH_TOTP_PORTAL-Q009

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q009
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If an operator scope defines no explicit external second-factor policy, the identity does not
  silently fall back to the weakest configuration available anywhere in the platform.
WHY_IT_MATTERS: >
  A silent weakest-available fallback turns an oversight in configuration into a security
  regression that nobody decided on.
DISCONFIRMING_OBSERVATION: >
  An operator scope with no explicit external policy set is found enforcing the weakest available
  regime rather than a safe, documented default.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Create an operator scope that leaves the external second-factor policy unset and observe which
  regime actually governs external authentication.
```

## G02-AUTH_TOTP_PORTAL-Q010

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q010
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An external user who has no administrator or support contact to call still has a recovery path
  that does not amount to an unconditional bypass of the second factor.
WHY_IT_MATTERS: >
  An unattended external population routinely needs recovery; if the only workable path is a full
  bypass, that bypass is the real, permanent policy for that population.
DISCONFIRMING_OBSERVATION: >
  The only recovery path reachable without human assistance grants full access without any
  equivalent-strength check standing in for the lost factor.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Lose access to the enrolled factor for an external identity with no assisted-support channel
  available and walk the self-service recovery path to its conclusion.
```

## G02-AUTH_TOTP_PORTAL-Q011

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q011
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Recovery artifacts issued to stand in for a lost second factor have a bounded number of uses
  and a bounded lifetime, rather than functioning as a permanent alternate credential.
WHY_IT_MATTERS: >
  An unbounded recovery artifact is a second, weaker, forgotten credential attached to the
  account indefinitely.
DISCONFIRMING_OBSERVATION: >
  A recovery artifact issued to an external identity continues to grant access after its intended
  single use, or remains usable long after the recovery event it was issued for.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Trigger a recovery event for an external identity, capture the resulting artifact, and attempt
  to reuse it after the recovery has already completed.
```

## G02-AUTH_TOTP_PORTAL-Q012

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q012
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where recovery relies on a channel weaker than the enrolled factor itself, that channel is not,
  in practice, the everyday path for accessing the account.
WHY_IT_MATTERS: >
  If the weak recovery channel becomes the routine path, the enrolled strong factor is
  security theatre rather than the real control.
DISCONFIRMING_OBSERVATION: >
  A material share of successful external authentications is found completing through the
  recovery channel rather than the enrolled factor, with no control limiting how often recovery
  may substitute for normal authentication.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Review authentication outcomes for a population of external identities and separate those
  completed via the enrolled factor from those completed via the recovery channel.
```

## G02-AUTH_TOTP_PORTAL-Q013

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q013
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Attempts against the recovery path itself are rate-limited at least as tightly as attempts
  against the primary factor.
WHY_IT_MATTERS: >
  An unthrottled recovery path becomes the weakest point of the whole regime, defeating a strong
  primary factor by simply not attacking it.
DISCONFIRMING_OBSERVATION: >
  Repeated recovery attempts against one external identity are allowed at a materially higher
  rate, or with no bound at all, compared to attempts against the primary factor.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Drive repeated recovery attempts against one external identity and compare the throttling
  behaviour to repeated primary-factor attempts against the same identity.
```

## G02-AUTH_TOTP_PORTAL-Q014

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q014
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Completing recovery invalidates every previously issued, unused recovery artifact for that
  identity rather than leaving them live.
WHY_IT_MATTERS: >
  A recovery artifact left live after recovery completes is a standing, forgotten credential an
  attacker could still hold.
DISCONFIRMING_OBSERVATION: >
  A recovery artifact issued in an earlier recovery event still succeeds after a later recovery
  event for the same identity has already completed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger two recovery events in sequence for one external identity, retaining the artifact from
  the first, and attempt to use it after the second has completed.
```

## G02-AUTH_TOTP_PORTAL-Q015

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q015
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the business relationship that made an external identity eligible for access ends, the
  previously enrolled factor stops being sufficient to authenticate that identity.
WHY_IT_MATTERS: >
  A factor that keeps working after the relationship ends is a standing access grant the business
  believes it has already withdrawn.
DISCONFIRMING_OBSERVATION: >
  An external identity whose underlying relationship has ended can still complete authentication
  using the factor enrolled while the relationship was active.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  End the business relationship behind an external identity that has an enrolled factor, then
  attempt authentication for that identity afterward.
```

## G02-AUTH_TOTP_PORTAL-Q016

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q016
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Ending the underlying relationship from the business side triggers, directly or through a
  detectable dependency, revocation of the associated authentication enrolment.
WHY_IT_MATTERS: >
  A business-side ending event that does not cascade to authentication leaves two systems
  disagreeing about whether access still exists.
DISCONFIRMING_OBSERVATION: >
  The business relationship is marked ended while the associated factor enrolment remains active,
  with no automatic or flagged dependency between the two events.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  End a business relationship through its normal business-side path and inspect the authentication
  enrolment record for a resulting change or an explicit unresolved-dependency flag.
```

## G02-AUTH_TOTP_PORTAL-Q017

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q017
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An external identity that has been inactive for an extended period is not left with an enrolled
  factor treated as still fully current with no re-validation requirement.
WHY_IT_MATTERS: >
  A long-dormant enrolment is an unmonitored credential; the longer it goes unchecked, the less
  confidence the operator can have in who actually controls it.
DISCONFIRMING_OBSERVATION: >
  An external identity dormant for a materially long period authenticates successfully with no
  re-validation step and no record noting the dormancy at all.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Leave an external identity's factor enrolled and unused for an extended period, then attempt
  authentication and inspect whether dormancy is checked or recorded.
```

## G02-AUTH_TOTP_PORTAL-Q018

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q018
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reactivating a previously ended relationship does not silently restore trust in whatever factor
  was enrolled before the relationship ended.
WHY_IT_MATTERS: >
  Silent restoration reopens exactly the access the business decided to withdraw, using a
  credential nobody has re-checked since.
DISCONFIRMING_OBSERVATION: >
  Reactivating a relationship for an external identity immediately allows authentication with the
  factor from before the ending, with no re-enrolment or re-verification step interposed.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  End and then reactivate the relationship behind an external identity that has a pre-existing
  enrolled factor, then attempt authentication.
```

## G02-AUTH_TOTP_PORTAL-Q019

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q019
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When one external identity holds relationships with more than one tenant, exactly one
  determinable policy version governs each authentication attempt, tied to the tenant the
  attempt is made against.
WHY_IT_MATTERS: >
  An indeterminate or cross-tenant-leaking policy choice would let the identity's access to one
  tenant be governed by a different, possibly weaker, tenant's rules.
DISCONFIRMING_OBSERVATION: >
  Authenticating the same external identity against two different tenants applies a policy that
  is not attributable to the tenant being accessed, or the two attempts disagree about which
  policy applied.
EXPECTED_SURFACE: S4,S6,S7
PRECONDITIONS: >
  Link one external identity to two tenants with different second-factor policies, then
  authenticate that identity against each tenant and compare which policy was actually applied.
```

## G02-AUTH_TOTP_PORTAL-Q020

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q020
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Resetting or replacing the enrolled factor in the context of one tenant relationship does not
  change the identity's ability to authenticate against a different tenant relationship.
WHY_IT_MATTERS: >
  A cross-tenant side effect from a single-tenant factor reset would let one tenant's support
  action affect another tenant's security state without either tenant knowing.
DISCONFIRMING_OBSERVATION: >
  Resetting the factor while acting in the context of one tenant changes what is required to
  authenticate against a different tenant relationship held by the same identity.
EXPECTED_SURFACE: S4,S6,S7
PRECONDITIONS: >
  Reset the enrolled factor for an identity while scoped to one tenant, then attempt
  authentication against a second tenant relationship held by the same identity.
```

## G02-AUTH_TOTP_PORTAL-Q021

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q021
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Suspending an external identity's access at one tenant does not leave that identity's active
  sessions at a different tenant unaffected in a way that outlives the intended suspension scope.
WHY_IT_MATTERS: >
  If suspension is scoped correctly, a live session at an unrelated tenant is expected to
  continue; the risk is a suspension that is supposed to be broader but is not honoured.
DISCONFIRMING_OBSERVATION: >
  A suspension explicitly intended to cover every tenant relationship for an identity leaves a
  live session at one of those tenants active and unaffected.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Establish live sessions for one external identity at two tenants, then apply a suspension
  intended to cover both, and check whether each session actually terminates.
```

## G02-AUTH_TOTP_PORTAL-Q022

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q022
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The system prevents, or at minimum flags, two distinguishable external identities being mapped
  to a single local account through the enrolment or linking process.
WHY_IT_MATTERS: >
  An unflagged collision lets a second, unrelated party inherit the access and factor trust of
  the first.
DISCONFIRMING_OBSERVATION: >
  Two distinguishable external identities become linked to one local account through ordinary
  enrolment or linking steps with no conflict raised and no record of the collision.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Attempt to link a second, distinguishable external identity to a local account that already has
  one linked identity and enrolled factor.
```

## G02-AUTH_TOTP_PORTAL-Q023

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q023
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  One external identity split across two local accounts is held to the same enforcement regime on
  both, rather than being usable through whichever account enforces the factor more weakly.
WHY_IT_MATTERS: >
  If enforcement is decided per local account rather than per identity, a split identity can pick
  the weaker account as its practical path in.
DISCONFIRMING_OBSERVATION: >
  The same external identity, present as two local accounts, can complete sensitive access
  through the account with the weaker enrolment while the stronger account exists in parallel.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Create two local accounts associated with the same external identity under differing enrolment
  strength and attempt access through each.
```

## G02-AUTH_TOTP_PORTAL-Q024

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q024
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A document-download or direct-reference link that skips the interactive sign-in screen still
  passes through the same second-factor enforcement decision as the interactive path, for
  resources the policy is meant to protect.
WHY_IT_MATTERS: >
  A direct link is exactly the kind of path an operator forgets to gate when enforcement is
  wired only into the interactive screen.
DISCONFIRMING_OBSERVATION: >
  A protected resource is retrievable through a direct-reference or download link by a session
  that has not satisfied the second-factor requirement the interactive path would have enforced.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Obtain a direct-reference or download link to a protected resource and request it from a
  session that has not completed second-factor verification.
```

## G02-AUTH_TOTP_PORTAL-Q025

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q025
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A direct-reference link forwarded to a third party does not carry forward the originating
  session's verified state beyond a short, bounded window.
WHY_IT_MATTERS: >
  An unbounded carried-forward verified state turns a single verified session into a durable,
  shareable bypass for anyone holding the link.
DISCONFIRMING_OBSERVATION: >
  A direct-reference link generated from a verified session still grants access long after that
  session's own factor-verified state would ordinarily have expired.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Generate a direct-reference link from a verified external session, let the originating session's
  normal validity window pass, and then request the link from a different context.
```

## G02-AUTH_TOTP_PORTAL-Q026

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q026
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Browsing outward from an already-verified external session does not reach resources whose
  protection level exceeds what that session's verification actually satisfied.
WHY_IT_MATTERS: >
  A verified session is supposed to certify a specific level of assurance; letting it reach
  higher-protection resources without a fresh check silently upgrades that assurance.
DISCONFIRMING_OBSERVATION: >
  A session verified only against a lower-protection path is able to reach a resource that the
  policy marks as requiring a higher, unmet level of verification.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  From a session verified at one protection level, attempt to navigate or link directly to a
  resource the policy assigns a stricter requirement.
```

## G02-AUTH_TOTP_PORTAL-Q027

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q027
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A deep link opened in a fresh, otherwise unauthenticated context is not honoured on the strength
  of a cached or pre-authorized token alone, without the second-factor check the equivalent
  interactive entry would require.
WHY_IT_MATTERS: >
  A cached-token shortcut is a durable way to skip enforcement entirely for anyone who obtains the
  token, independent of the human ever presenting a factor.
DISCONFIRMING_OBSERVATION: >
  A deep link opened with no active interactive session succeeds against a protected resource
  purely on a cached or pre-authorized token, with no second-factor check performed in that
  request.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Capture a cached or pre-authorized token associated with an external identity and present a deep
  link using only that token, with no live interactive session.
```

## G02-AUTH_TOTP_PORTAL-Q028

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q028
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An exported or cached representation of a protected resource retains a record of which
  enforcement policy and verification state gated its original creation.
WHY_IT_MATTERS: >
  Without that record, an exported copy that leaks cannot later be traced back to whether it was
  ever properly gated at all.
DISCONFIRMING_OBSERVATION: >
  An exported or cached copy of a protected resource carries no retrievable record of the policy
  or verification state under which it was produced.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Export or cache a protected resource from a verified session and inspect whether the export
  carries any traceable record of the gating policy and verification state.
```

## G02-AUTH_TOTP_PORTAL-Q029

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q029
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An integration or programmatic credential issued to an external party carries an assurance level
  the operator has explicitly decided is equivalent to, or a deliberate substitute for, the
  human second-factor requirement.
WHY_IT_MATTERS: >
  An unexamined programmatic credential can become the practical way to reach the same data a
  human would need a factor to reach, without anyone having decided that trade-off.
DISCONFIRMING_OBSERVATION: >
  An external integration credential reaches the same protected data a human session would need
  the second factor for, with no recorded decision establishing that credential's assurance level
  as equivalent.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Issue an integration credential to an external party and compare what it can reach against what
  an equivalent human session can reach only after satisfying the second factor.
```

## G02-AUTH_TOTP_PORTAL-Q030

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q030
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Revoking or rotating the second factor held by an external human is reflected in, or at minimum
  flagged against, any integration credential issued under the same identity.
WHY_IT_MATTERS: >
  An integration credential left untouched by a human factor revocation is a standing path back
  into the account the revocation was meant to close.
DISCONFIRMING_OBSERVATION: >
  Revoking an external human's factor leaves an integration credential issued under the same
  identity fully functional with no flag or dependency noted between the two.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Issue both a human factor and an integration credential under one external identity, revoke the
  human factor, then exercise the integration credential.
```

## G02-AUTH_TOTP_PORTAL-Q031

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q031
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Scheduled or background work started under an external integration credential is subject to the
  same revocation as the identity's interactive access, rather than continuing to run beyond it.
WHY_IT_MATTERS: >
  Work that outlives the revocation of the identity that started it is a way for withdrawn access
  to keep having effect.
DISCONFIRMING_OBSERVATION: >
  Background or scheduled work started under an external integration credential continues to
  execute, or to produce effects, after the identity's access has been revoked.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Start a background or scheduled task under an external integration credential, revoke the
  identity's access mid-run, and observe whether the task is halted or continues.
```

## G02-AUTH_TOTP_PORTAL-Q032

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q032
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An integration or programmatic credential cannot be substituted for the human factor in an
  otherwise ordinary interactive sign-in flow.
WHY_IT_MATTERS: >
  If a programmatic credential can stand in for the human factor interactively, the second-factor
  requirement is trivially bypassed by anyone holding that credential.
DISCONFIRMING_OBSERVATION: >
  Presenting an integration or programmatic credential at the point where the interactive flow
  expects the human second factor is accepted as satisfying that requirement.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Attempt to complete an interactive sign-in's second-factor step using an integration credential
  in place of the human factor.
```

## G02-AUTH_TOTP_PORTAL-Q033

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q033
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A tenant administrator's authority to configure the external second-factor regime is confined to
  their own tenant and cannot reach or alter enforcement for a different tenant.
WHY_IT_MATTERS: >
  Cross-tenant configuration authority would let one tenant's administrator weaken security for
  customers of an unrelated business.
DISCONFIRMING_OBSERVATION: >
  A change made by one tenant's administrator to the external second-factor configuration is
  observed to affect enforcement for a different tenant.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Have an administrator scoped to one tenant change the external second-factor configuration and
  check enforcement for a second, unrelated tenant.
```

## G02-AUTH_TOTP_PORTAL-Q034

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q034
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An enforcement exemption configured for one named external partner applies only to that partner
  and does not widen to the tenant's external user population generally.
WHY_IT_MATTERS: >
  A narrowly intended exemption that silently widens turns a single deliberate exception into a
  general weakening nobody chose.
DISCONFIRMING_OBSERVATION: >
  An exemption configured against one named external partner is found also applying to external
  users unrelated to that partner.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Configure a second-factor exemption naming one specific external partner, then test enforcement
  against an unrelated external user of the same tenant.
```

## G02-AUTH_TOTP_PORTAL-Q035

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q035
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A tenant-level exemption from the external second-factor requirement does not survive a
  configuration reset or rollback without being explicitly reasserted.
WHY_IT_MATTERS: >
  An exemption that silently survives a reset can outlive the circumstances that justified it and
  become invisible to whoever performs the reset.
DISCONFIRMING_OBSERVATION: >
  A tenant-level exemption is still in force after a configuration reset or rollback with no
  matching entry reasserting it in the restored configuration.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Configure a tenant-level exemption, perform a configuration reset or rollback for that tenant,
  and check whether the exemption is still in force.
```

## G02-AUTH_TOTP_PORTAL-Q036

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q036
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change to the external second-factor enforcement policy takes effect at a single, deterministic
  point rather than leaving already-open sessions in a mixed state that neither the old nor the new
  policy fully describes.
WHY_IT_MATTERS: >
  Indeterminate rollout of a policy change makes incidents involving it irreproducible and makes
  it impossible to say, after the fact, which rule actually applied.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical open sessions are found enforcing different outcomes after a policy
  change is committed, with no explicit rule describing which sessions transition when.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Open sessions before a policy change, commit the change, and compare enforcement behaviour
  across the pre-existing sessions and freshly opened ones.
```

## G02-AUTH_TOTP_PORTAL-Q037

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q037
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A tenant administrator cannot configure the external second-factor regime below a floor the
  operator has set as the platform-wide minimum.
WHY_IT_MATTERS: >
  Without an enforced floor, a single tenant's local choice can undercut a platform-wide security
  commitment made to every customer.
DISCONFIRMING_OBSERVATION: >
  A tenant administrator succeeds in configuring the external regime below the operator-declared
  platform-wide minimum.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  As a tenant administrator, attempt to configure the external second-factor regime below the
  documented platform-wide floor.
```

## G02-AUTH_TOTP_PORTAL-Q038

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q038
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Repeated failed second-factor attempts against one external identity cannot be used by a third
  party to lock out the legitimate holder for a materially long or indefinite period.
WHY_IT_MATTERS: >
  A factor meant to protect the account becomes a denial-of-service weapon against the account's
  own legitimate owner if lockout has no bound reachable by an unauthenticated attacker.
DISCONFIRMING_OBSERVATION: >
  An unauthenticated party can drive an external identity into a lockout state that lasts
  materially longer than a bounded cooldown, or indefinitely, with no independent unlock path for
  the legitimate holder.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Submit repeated failing second-factor attempts against a target external identity without
  authenticating as that identity, and observe the resulting lockout duration and unlock options.
```

## G02-AUTH_TOTP_PORTAL-Q039

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q039
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A third party cannot repeatedly trigger delivery of a second-factor code or prompt to an
  external identity without that identity itself attempting to authenticate.
WHY_IT_MATTERS: >
  Unbounded, attacker-triggerable delivery turns the factor-delivery mechanism into a nuisance and
  cost vector against the operator and the external user, independent of any real login attempt.
DISCONFIRMING_OBSERVATION: >
  Repeated delivery of a second-factor code or prompt to a target external identity is triggered
  by a third party with no meaningful rate limit and no requirement that the identity itself is
  attempting to sign in.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Repeatedly initiate the step that causes a second-factor code or prompt to be delivered to a
  target external identity and observe whether delivery is throttled.
```

## G02-AUTH_TOTP_PORTAL-Q040

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q040
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A locked-out external account has a bounded, self-service or business-appropriate path back to
  access that does not require an unresourced escalation the business has no capacity to service.
WHY_IT_MATTERS: >
  A recovery path that assumes support capacity the business does not actually have effectively
  strands legitimate external users indefinitely.
DISCONFIRMING_OBSERVATION: >
  The only path out of lockout for an external identity requires an escalation channel that is not
  actually staffed or bounded in response time.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Drive an external identity into lockout and attempt every documented unlock path available to
  that identity without assistance.
```

## G02-AUTH_TOTP_PORTAL-Q041

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q041
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  For any given external action, the operator can determine which second-factor mechanism was
  presented to authenticate the session that performed it.
WHY_IT_MATTERS: >
  Without this, an incident review cannot distinguish an action taken under strong verification
  from one taken through a weaker fallback.
DISCONFIRMING_OBSERVATION: >
  Reviewing the record of a specific external action provides no way to determine which
  second-factor mechanism authenticated the session that performed it.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Perform an external action after authenticating with a specific factor mechanism, then attempt
  to determine that mechanism from the resulting record alone.
```

## G02-AUTH_TOTP_PORTAL-Q042

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q042
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  For any given authentication decision, the operator can determine which version of the external
  second-factor policy was in force at the moment the decision was made.
WHY_IT_MATTERS: >
  Without a policy-version record tied to the decision, a later policy change makes it impossible
  to know what rule actually applied to a past incident.
DISCONFIRMING_OBSERVATION: >
  Reviewing a past authentication decision provides no way to determine which policy version was
  in force at the time, once the policy has since changed.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Record an authentication decision, change the external second-factor policy afterward, then
  attempt to determine from the record which policy version actually applied.
```

## G02-AUTH_TOTP_PORTAL-Q043

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q043
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to who is authorized to alter the external second-factor policy is itself captured in a
  record distinguishable from an ordinary policy value change.
WHY_IT_MATTERS: >
  Without this, an unauthorized widening of who can weaken the policy is indistinguishable from a
  routine configuration edit.
DISCONFIRMING_OBSERVATION: >
  A change to the set of parties authorized to alter the external second-factor policy leaves no
  record distinct from an ordinary value change to the policy itself.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Change who is authorized to alter the external second-factor policy and inspect whether that
  change is recorded distinctly from a routine policy-value edit.
```

## G02-AUTH_TOTP_PORTAL-Q044

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q044
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Authentication completed through a recovery or fallback path is distinguishable in the record
  from authentication completed through ordinary verification of the enrolled factor.
WHY_IT_MATTERS: >
  If the two are indistinguishable, the operator cannot tell how often the weaker path is actually
  being used, or investigate an incident that turns on which path was taken.
DISCONFIRMING_OBSERVATION: >
  The record of a successful authentication gives no indication of whether it was completed via
  the enrolled factor or via a recovery or fallback path.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Complete one authentication via the enrolled factor and one via the recovery path for the same
  identity, then compare what the two records show.
```

## G02-AUTH_TOTP_PORTAL-Q045

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q045
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The record of an external authentication decision cannot be altered after the fact without that
  alteration itself being detectable.
WHY_IT_MATTERS: >
  A silently alterable authentication record defeats every other audit guarantee built on top of
  it, including proof of which factor or policy version applied.
DISCONFIRMING_OBSERVATION: >
  An existing external authentication record is modified after the fact with no trace of the
  modification left in any accessible log or integrity check.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Attempt to modify an existing authentication record after it has been written and check for any
  detectable trace of the change.
```

## G02-AUTH_TOTP_PORTAL-Q046

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q046
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A session established before an external second-factor policy is tightened is required to meet
  the new policy at its next natural re-check point, rather than continuing indefinitely under the
  older, weaker policy.
WHY_IT_MATTERS: >
  A grandfathered session that never re-checks turns every policy tightening into a change that
  only ever protects future sessions, not the ones already open when the risk was identified.
DISCONFIRMING_OBSERVATION: >
  A session opened under the old, weaker policy remains fully privileged well past its normal
  re-check point after the policy has been tightened, with no re-verification applied.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Open a session under the current policy, tighten the external policy, and observe whether the
  open session is required to re-verify at its next natural check point.
```

## G02-AUTH_TOTP_PORTAL-Q047

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q047
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Clock or time-zone difference between the party generating a time-bound factor and the system
  verifying it stays within a documented tolerance rather than producing unpredictable accept or
  reject outcomes.
WHY_IT_MATTERS: >
  An undocumented, unpredictable tolerance either locks out legitimate external users through no
  fault of their own or quietly widens the acceptance window far beyond what the factor is
  supposed to guarantee.
DISCONFIRMING_OBSERVATION: >
  A time-bound factor generated with a known, modest clock offset either is rejected within the
  documented tolerance or is accepted well outside it.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Generate a time-bound factor value under a known, deliberately offset clock and submit it for
  verification, comparing the outcome to the documented tolerance.
```

## G02-AUTH_TOTP_PORTAL-Q048

```yaml
QID: G02-AUTH_TOTP_PORTAL-Q048
MODULE: auth_totp_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Support-initiated or impersonation access into an external identity's session is subject to the
  same second-factor accountability as the external user's own sign-in, rather than bypassing it
  entirely through an internal-only path.
WHY_IT_MATTERS: >
  An impersonation path that skips the external factor and leaves no equivalent record is an
  unlogged, unauthenticated door into every external account at once.
DISCONFIRMING_OBSERVATION: >
  A support-initiated or impersonation session reaches the same protected external actions as the
  user's own session would, without satisfying an equivalent factor check and without a
  distinguishing record that impersonation, not the external user, performed the action.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Use a support or impersonation path to enter an external identity's session and attempt a
  factor-gated action, then inspect the resulting record for whether it distinguishes
  impersonation from the external user's own action.
```
