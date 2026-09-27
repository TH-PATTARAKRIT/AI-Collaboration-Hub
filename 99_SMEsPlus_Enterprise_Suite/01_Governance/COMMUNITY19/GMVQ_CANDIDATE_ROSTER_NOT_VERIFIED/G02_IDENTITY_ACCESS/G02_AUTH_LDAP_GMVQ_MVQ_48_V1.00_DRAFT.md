# SMEsPlus ENTERPRISE SUITE
## GMVQ — G02 IDENTITY_ACCESS / authentication-delegated-to-external-directory-service Module Adversarial MVQ Bank

**Document ID:** GMVQ-G02-AUTH_LDAP-MVQ48-V1.00
**Group:** G02 IDENTITY_ACCESS
**Module Metadata:** `auth_ldap`
**Wave:** W1
**Author Cell:** TEAM 08 (GMVQ Question Factory — Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded

## Purpose

This bank extends the 35 Standard Questions with 48 module-specific, falsifiable questions
covering authentication delegated to an external directory service: identity matching between
the directory and the local account, group/role mapping derived from directory membership,
behaviour when the directory service is unreachable or degraded, and the local fallback path.
Coverage spans every material dimension in the Group Brief for G02 (entry-path enforcement,
retroactivity of policy change, per-tenant isolation, fail-open/fail-closed, identity collision,
de-provisioning lag, weak recovery paths, lockout-as-DoS, session termination semantics,
internal/external regime divergence, auditability, and clock/timezone effects).

The question text is source-neutral. It does not name the module, any vendor or product, or
any technical identifier (model, table, field, method, XML ID, API path). "External directory
service" and "delegated authentication" are used throughout in place of any protocol name.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that is a concrete failure
  state, not a restatement of the `HYPOTHESIS`.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread
  across business capability, business rule, state transition, configuration dependency,
  role/permission, exception path, cancellation, reversal, negative case, cross-module
  dependency, optional behaviour, auditability, tenant/company boundary, concurrency and
  ordering, runtime reachability, configuration reachability, and source/runtime
  contradiction potential.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/evidence.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from
  this bank by itself.
- This document is PREPARED ONLY / DRAFT. It carries no Boss approval and authorizes no
  batch freeze, no Lane A/Lane B start, and no gate closure.

## G02-AUTH_LDAP-Q001

```yaml
QID: G02-AUTH_LDAP-Q001
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Matching a directory-asserted identity to a local account uses a stable, unique
  directory-issued key, not a mutable display or contact attribute.
WHY_IT_MATTERS: >
  Matching on a mutable attribute lets a directory-side rename or reissue silently
  redirect authentication to the wrong local account.
DISCONFIRMING_OBSERVATION: >
  Changing a mutable attribute of a directory identity (its display name or contact
  address) while leaving its stable key unchanged causes the system to stop
  recognising it, split it into a second local account, or attach it to a
  different existing account.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  A directory identity already matched to a local account has its mutable
  attribute changed at the directory. Re-authenticate and observe which local
  account, if any, the session resolves to.
```

## G02-AUTH_LDAP-Q002

```yaml
QID: G02-AUTH_LDAP-Q002
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external directory service is unreachable, slow, or returns a
  malformed answer, the system resolves to an explicit, configured fail-open or
  fail-closed outcome rather than an accidental one.
WHY_IT_MATTERS: >
  An accidental fail-open during an outage grants access nobody decided to
  grant; an accidental fail-closed locks out every delegated user without
  warning.
DISCONFIRMING_OBSERVATION: >
  During a simulated outage or malformed response, the observed behaviour
  (access granted or denied) does not match any documented configuration
  setting for that condition, or differs between two otherwise identical
  attempts.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Simulate directory unreachability, timeout, and a truncated/malformed
  response separately; attempt authentication under each and compare the
  outcome against the configured policy.
```

## G02-AUTH_LDAP-Q003

```yaml
QID: G02-AUTH_LDAP-Q003
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A role granted solely because of current directory group membership is
  revoked once that membership is revoked at the directory, without requiring
  a separate manual step.
WHY_IT_MATTERS: >
  A sticky role that survives membership revocation is a silent privilege
  escalation that audit would not expect to find.
DISCONFIRMING_OBSERVATION: >
  After a directory group membership is removed and the mapped identity's
  session or account state is refreshed through its normal cycle, the
  previously granted role remains in effect.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Grant a role via directory group mapping, remove the identity from the
  group at the directory, allow the normal refresh/re-authentication cycle to
  occur, then inspect the account's effective role.
```

## G02-AUTH_LDAP-Q004

```yaml
QID: G02-AUTH_LDAP-Q004
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The local fallback authentication path remains a deliberate, bounded
  exception once delegated authentication is configured as primary, not a
  permanent unmonitored bypass usable interchangeably with delegation.
WHY_IT_MATTERS: >
  An unmonitored fallback defeats the purpose of centralising authentication
  at the directory, including its lockout, policy and revocation controls.
DISCONFIRMING_OBSERVATION: >
  An account for which delegated authentication succeeds can also be
  authenticated at will through the local fallback path with no distinct
  logging, restriction, or configuration boundary separating the two paths.
EXPECTED_SURFACE: S3,S6,S7
PRECONDITIONS: >
  With delegated authentication configured and working for a test identity,
  attempt authentication through the local fallback path for the same
  identity and compare logging and restrictions between the two paths.
```

## G02-AUTH_LDAP-Q005

```yaml
QID: G02-AUTH_LDAP-Q005
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Per-tenant directory connection configuration, including its connection
  credentials, is not reachable or visible to an administrator of a
  different tenant.
WHY_IT_MATTERS: >
  Cross-tenant visibility of another tenant's directory connection details
  is both a data boundary breach and a path to impersonating that tenant's
  authentication.
DISCONFIRMING_OBSERVATION: >
  An administrative user scoped to tenant A can view, export, or reuse
  tenant B's directory connection configuration or its stored credentials
  through any supported interface.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure distinguishable directory connections for two tenants; using an
  administrator account scoped to one tenant, attempt to view or use the
  other tenant's connection configuration.
```

## G02-AUTH_LDAP-Q006

```yaml
QID: G02-AUTH_LDAP-Q006
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Disabling delegated authentication defines an explicit resulting state for
  accounts that were provisioned through it: either they retain access
  through an alternative path, or that access is explicitly and visibly
  suspended.
WHY_IT_MATTERS: >
  An undefined outcome leaves affected users either silently stranded or
  silently retaining access nobody reviewed after the policy change.
DISCONFIRMING_OBSERVATION: >
  After delegated authentication is disabled, accounts that were only ever
  provisioned through it are left in a state (fully working with no
  alternative credential, or fully broken with no notice) that matches
  neither of the two documented outcomes.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Provision an account solely through delegated authentication, then disable
  delegated authentication at the configuration level and inspect the
  account's resulting authentication state.
```

## G02-AUTH_LDAP-Q007

```yaml
QID: G02-AUTH_LDAP-Q007
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two distinct directory identities cannot both resolve to the same existing
  local account without an explicit, logged decision to merge them.
WHY_IT_MATTERS: >
  A silent merge lets a second directory identity inherit the full
  privilege and data access of an unrelated existing account.
DISCONFIRMING_OBSERVATION: >
  A second, distinct directory identity is able to authenticate into an
  existing local account that was previously matched to a different
  directory identity, with no explicit linking action recorded.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Establish a local account matched to directory identity A. Attempt
  authentication as unrelated directory identity B whose matching attribute
  could plausibly collide, and observe whether it resolves to account A.
```

## G02-AUTH_LDAP-Q008

```yaml
QID: G02-AUTH_LDAP-Q008
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A single directory identity cannot be bound to two different local
  accounts at the same time.
WHY_IT_MATTERS: >
  Dual binding creates two independent privilege sets under one real-world
  identity, undermining both audit and least-privilege review.
DISCONFIRMING_OBSERVATION: >
  The same directory identity, authenticating through two different
  supported entry paths or at two different times, resolves to two
  different local accounts that remain simultaneously active.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Attempt to create a second local-account binding for a directory identity
  already matched to an existing local account, through every entry path
  that performs matching.
```

## G02-AUTH_LDAP-Q009

```yaml
QID: G02-AUTH_LDAP-Q009
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Disabling or deleting an identity at the external directory service has a
  defined, bounded-time effect on that identity's already-established local
  session and account, rather than being ignored until an unrelated event.
WHY_IT_MATTERS: >
  De-provisioning that never reaches the local system defeats the entire
  purpose of centralising identity lifecycle at the directory.
DISCONFIRMING_OBSERVATION: >
  An identity disabled or deleted at the directory continues to hold a
  live, usable local session or continues to authenticate successfully
  well beyond the documented bound for that effect to take hold.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Establish a live session for a directory-matched identity, disable that
  identity at the directory, and observe the session and subsequent
  authentication attempts over the documented bound period.
```

## G02-AUTH_LDAP-Q010

```yaml
QID: G02-AUTH_LDAP-Q010
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Renaming or deleting a directory group used in a role-mapping rule does
  not leave identities that were matched under the old group name silently
  retaining the previously granted privilege.
WHY_IT_MATTERS: >
  A rename or deletion is a natural directory-side event; if privilege
  survives it, the mapping rule is not actually being re-evaluated.
DISCONFIRMING_OBSERVATION: >
  After a mapped directory group is renamed or deleted, an identity that
  held the associated role continues to hold it through the account's
  normal refresh cycle, with no matching rule any longer referencing that
  group.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Map a role to a directory group, rename or delete that group at the
  directory, allow the normal refresh cycle, and inspect the mapped
  identity's effective role.
```

## G02-AUTH_LDAP-Q011

```yaml
QID: G02-AUTH_LDAP-Q011
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Role-mapping evaluation defines a consistent, documented behaviour for
  indirect (nested) group membership, rather than an inconsistent or
  undefined one.
WHY_IT_MATTERS: >
  Undefined handling of indirect membership means the same real-world
  membership structure can grant or withhold a role unpredictably.
DISCONFIRMING_OBSERVATION: >
  An identity that is an indirect member of a mapped group (through another
  group) receives a role mapping outcome that differs from the documented
  behaviour, or differs between two structurally equivalent nesting
  arrangements.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Construct a nested group membership at the directory where the mapped
  group is reached only indirectly, and compare the resulting role mapping
  to the documented rule for indirect membership.
```

## G02-AUTH_LDAP-Q012

```yaml
QID: G02-AUTH_LDAP-Q012
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A non-interactive entry path (an API credential or integration path) tied
  to a directory-matched identity is subject to the same delegated
  authentication and revocation enforcement as the interactive login path
  for that identity.
WHY_IT_MATTERS: >
  An unenforced side door defeats every control placed on the interactive
  login path, including directory-side de-provisioning.
DISCONFIRMING_OBSERVATION: >
  After an identity's delegated access is revoked or its directory account
  disabled, an API credential or integration path tied to that identity
  continues to succeed.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Issue an API credential for a directory-matched identity, revoke that
  identity's directory-based access, and attempt use of the API credential.
```

## G02-AUTH_LDAP-Q013

```yaml
QID: G02-AUTH_LDAP-Q013
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A scheduled or background process that acts under a directory-mapped
  identity runs with that identity's currently valid, currently mapped
  privilege, not a cached or unauthenticated service-level privilege.
WHY_IT_MATTERS: >
  A background process running on stale privilege can perform actions the
  identity no longer has, or is no longer allowed to have, at the time the
  action runs.
DISCONFIRMING_OBSERVATION: >
  A scheduled job tied to a directory-mapped identity continues to perform
  privileged actions after that identity's directory-side privilege has
  been reduced or revoked, using the identity's original privilege at
  scheduling time.
EXPECTED_SURFACE: S4,S6,S8
PRECONDITIONS: >
  Schedule a background action under a directory-mapped identity with a
  given privilege, reduce that identity's privilege at the directory before
  the job runs, and inspect what privilege the job actually exercises.
```

## G02-AUTH_LDAP-Q014

```yaml
QID: G02-AUTH_LDAP-Q014
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A support or impersonation access path acting as a directory-mapped
  identity is subject to the same authorization checks that would apply if
  that identity were acting normally, and is distinctly logged.
WHY_IT_MATTERS: >
  An impersonation path that skips normal checks becomes an unaudited way
  to exceed the impersonated identity's actual privilege.
DISCONFIRMING_OBSERVATION: >
  An action performed through impersonation of a directory-mapped identity
  succeeds even though the same action would be denied to that identity
  acting directly, with no distinct log entry marking it as impersonated.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Identify an action the target identity is not authorized to perform
  directly; attempt the same action through the support/impersonation path
  and inspect both the outcome and the audit trail.
```

## G02-AUTH_LDAP-Q015

```yaml
QID: G02-AUTH_LDAP-Q015
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Repeated failed delegated-authentication attempts against one identity do
  not degrade or lock delegated authentication for unrelated identities or
  for the tenant as a whole.
WHY_IT_MATTERS: >
  A shared lockout mechanism turns a single targeted identity into a
  denial-of-service lever against everyone else relying on the same
  connection.
DISCONFIRMING_OBSERVATION: >
  Deliberately failing authentication repeatedly for one identity causes
  authentication to fail, slow materially, or lock out for a different,
  unrelated identity using the same directory connection.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Repeatedly fail authentication for a test identity up to and beyond any
  observed lockout threshold, then immediately attempt authentication for
  a second, unrelated identity on the same connection.
```

## G02-AUTH_LDAP-Q016

```yaml
QID: G02-AUTH_LDAP-Q016
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A lockout triggered under one tenant or company context does not apply to
  the same real-world person's access in an unrelated tenant or company
  context, when those scopes are meant to be independent.
WHY_IT_MATTERS: >
  A shared lockout state across independent scopes is an unintended
  cross-tenant coupling and a denial-of-service path between unrelated
  customers.
DISCONFIRMING_OBSERVATION: >
  Triggering a lockout for a person's identity in one tenant's scope causes
  a visible authentication failure or delay for the same person's
  independently-scoped identity in a different tenant.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Using an identity that has independent accounts in two tenant scopes,
  trigger a lockout in one scope and immediately attempt authentication in
  the other scope.
```
## G02-AUTH_LDAP-Q017

```yaml
QID: G02-AUTH_LDAP-Q017
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Ending or revoking a session established through delegated authentication
  has a defined effect on any in-flight work and on any credential or token
  already issued from that session.
WHY_IT_MATTERS: >
  An undefined effect leaves either orphaned in-flight work or a
  still-usable credential outliving the session it came from.
DISCONFIRMING_OBSERVATION: >
  After a delegated session is explicitly ended or revoked, a credential
  issued from it continues to be accepted, or in-flight work started under
  it continues without any defined handling.
EXPECTED_SURFACE: S1,S3,S6,S8
PRECONDITIONS: >
  Establish a delegated session, issue a credential and start a long-running
  action from it, then revoke the session and observe both the credential
  and the in-flight action.
```

## G02-AUTH_LDAP-Q018

```yaml
QID: G02-AUTH_LDAP-Q018
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A background job started under a delegated-authentication session has a
  defined behaviour when that session later ends or is revoked while the job
  is still running.
WHY_IT_MATTERS: >
  Without a defined behaviour, a job can either fail silently or keep
  running on authority that no longer exists.
DISCONFIRMING_OBSERVATION: >
  A background job started under a session continues running to completion,
  using privileges from that session, after the session has been revoked,
  with no record of the contradiction.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Start a long-running background job under a delegated session, revoke the
  session mid-run, and observe whether the job continues, is halted, or is
  flagged.
```

## G02-AUTH_LDAP-Q019

```yaml
QID: G02-AUTH_LDAP-Q019
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Directory delegation configured for the internal-user population does not
  become reachable from, or extend privilege into, the separate
  external-user authentication regime.
WHY_IT_MATTERS: >
  Merging the two regimes would let an internal control surface (or its
  weaknesses) reach external-facing accounts, or vice versa.
DISCONFIRMING_OBSERVATION: >
  An external-facing account is able to authenticate through, or inherit a
  role from, the internal directory delegation configuration.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Attempt to authenticate an external-user account through the internal
  directory delegation path, and inspect whether any role from that mapping
  becomes available to it.
```

## G02-AUTH_LDAP-Q020

```yaml
QID: G02-AUTH_LDAP-Q020
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Every authentication decision made through directory delegation (accepted,
  rejected, or resolved via fallback) is recorded with enough detail to
  identify which policy version was in force at the time.
WHY_IT_MATTERS: >
  Without this, a disputed access decision cannot be reconstructed or
  attributed to the rule that produced it.
DISCONFIRMING_OBSERVATION: >
  An authentication decision (of any of the three kinds) has no
  corresponding record, or its record does not identify the policy version
  in force at that time.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Produce one authentication of each kind (accepted, rejected, fallback)
  under a known policy version, then inspect the audit trail for each.
```

## G02-AUTH_LDAP-Q021

```yaml
QID: G02-AUTH_LDAP-Q021
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change to the directory connection or group/role mapping configuration
  is itself recorded with who made the change and when.
WHY_IT_MATTERS: >
  Configuration is where privilege is actually decided; an unattributed
  change to it is a bigger audit gap than an unattributed data change.
DISCONFIRMING_OBSERVATION: >
  A change made to the directory connection or mapping configuration
  produces no audit record, or the record omits who made it or when.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Make a distinguishable change to the directory connection or mapping
  configuration and inspect the resulting audit record.
```

## G02-AUTH_LDAP-Q022

```yaml
QID: G02-AUTH_LDAP-Q022
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Any time-bound aspect of the delegated connection (such as a validity
  window on a trust artifact or a cached-mapping expiry) is evaluated using
  a consistent time reference regardless of the time zone of the system
  components involved.
WHY_IT_MATTERS: >
  A time-zone mismatch can cause a validity window to be honoured too early,
  too late, or inconsistently between components.
DISCONFIRMING_OBSERVATION: >
  A time-bound aspect of the connection is accepted or rejected differently
  depending only on the time-zone configuration of the checking component,
  with the underlying instant unchanged.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Set components involved in the time-bound check to different time zones
  and observe whether the same underlying instant produces a consistent
  accept/reject outcome.
```

## G02-AUTH_LDAP-Q023

```yaml
QID: G02-AUTH_LDAP-Q023
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A malformed or truncated response from the external directory service
  (such as an interrupted membership list) is treated as a fault, not as a
  valid but empty answer that silently drops previously held privileges.
WHY_IT_MATTERS: >
  Treating a fault as "no memberships" silently revokes access based on a
  transport problem rather than an actual directory-side change.
DISCONFIRMING_OBSERVATION: >
  A truncated or malformed membership response causes an identity's roles
  to be silently reduced to none, with no distinct fault indication in the
  audit trail.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Simulate a truncated or malformed response to a membership query for an
  identity with existing role mappings, then inspect the resulting role
  state and audit trail.
```

## G02-AUTH_LDAP-Q024

```yaml
QID: G02-AUTH_LDAP-Q024
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A slow response from the external directory service is subject to a
  bounded, configured timeout that resolves to a distinct outcome from an
  outright connection failure.
WHY_IT_MATTERS: >
  Without a bound, a slow directory can hang the authentication path
  indefinitely instead of failing predictably.
DISCONFIRMING_OBSERVATION: >
  A deliberately slow (but eventually responsive) directory connection
  causes the authentication attempt to hang past any documented timeout, or
  to fail in a way indistinguishable from a hard connection failure.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Introduce an artificial response delay on the directory connection that
  exceeds the documented timeout and observe the authentication outcome and
  timing.
```

## G02-AUTH_LDAP-Q025

```yaml
QID: G02-AUTH_LDAP-Q025
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When delegated authentication is configured but not fully enabled, every
  entry path is consistently blocked; the feature is not reachable through
  some paths while blocked on others.
WHY_IT_MATTERS: >
  Partial reachability during a not-fully-enabled state is a gap between
  the intended and actual security posture.
DISCONFIRMING_OBSERVATION: >
  With delegated authentication configured but marked not fully enabled, at
  least one entry path (interactive, API, or integration) still accepts a
  delegated authentication attempt while another correctly rejects it.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Configure delegated authentication in a not-fully-enabled state and
  attempt authentication through every distinct entry path that could carry
  it.
```

## G02-AUTH_LDAP-Q026

```yaml
QID: G02-AUTH_LDAP-Q026
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Per-tenant external connection credentials for the directory connection
  are never displayed in a configuration surface to an administrator of a
  different tenant, including a broad or superuser-style administrator.
WHY_IT_MATTERS: >
  Exposure of connection credentials across a tenant boundary is a direct
  path to impersonating that tenant's authentication.
DISCONFIRMING_OBSERVATION: >
  A broad administrative account not scoped to tenant B is able to view or
  export tenant B's directory connection credentials through any
  configuration surface.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Using a broad administrative account not scoped to a specific tenant,
  attempt to view or export another tenant's directory connection
  credentials.
```

## G02-AUTH_LDAP-Q027

```yaml
QID: G02-AUTH_LDAP-Q027
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Converting an existing local-credential account into a directory-managed
  account (linking) follows a defined path that can itself be reversed.
WHY_IT_MATTERS: >
  A one-way or undefined linking step removes the account owner's ability to
  recover if the directory connection later becomes unavailable to them.
DISCONFIRMING_OBSERVATION: >
  Linking an existing account to directory-managed authentication succeeds,
  but no defined path exists to reverse that link back to local-credential
  authentication.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Link an existing local-credential account to directory-managed
  authentication, then attempt to reverse the link through every documented
  or discoverable path.
```

## G02-AUTH_LDAP-Q028

```yaml
QID: G02-AUTH_LDAP-Q028
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reversing a directory-managed account back to local credentials leaves the
  account in a safe, defined authentication state: either a fresh local
  secret must be set before further access, or a previously valid one is
  restored, but never left unauthenticatable with no way in.
WHY_IT_MATTERS: >
  An account left with no valid credential of any kind is an unplanned
  lockout; an account silently left with a stale credential is an unplanned
  exposure.
DISCONFIRMING_OBSERVATION: >
  After reversing directory-managed authentication back to local
  credentials, the account has no way to authenticate, or authenticates
  with a secret the account owner never set or confirmed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Reverse a directory-managed account to local credentials and attempt to
  authenticate immediately afterward using every path the system offers for
  establishing the new local credential.
```

## G02-AUTH_LDAP-Q029

```yaml
QID: G02-AUTH_LDAP-Q029
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A directory-asserted identity whose attributes match no configured
  group/role mapping rule defaults to an explicit, documented minimal-
  privilege outcome, not an undefined or maximal one.
WHY_IT_MATTERS: >
  An undefined default is a coin flip between "denied" and "fully
  privileged," and the latter is a serious exposure.
DISCONFIRMING_OBSERVATION: >
  An identity matching no configured mapping rule is granted a role or
  privilege beyond the documented minimal default.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Authenticate a directory identity whose attributes are deliberately
  constructed to match no configured mapping rule, and inspect the
  resulting role.
```

## G02-AUTH_LDAP-Q030

```yaml
QID: G02-AUTH_LDAP-Q030
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A role granted through directory group mapping composes correctly with a
  restriction or role assigned independently within the local system,
  without either one silently overriding the other in a way nobody
  reviewed.
WHY_IT_MATTERS: >
  Unreviewed override in either direction produces either an unintended
  restriction or an unintended grant of privilege.
DISCONFIRMING_OBSERVATION: >
  A locally-assigned restriction on an identity is silently overridden by a
  directory-mapped role, or a directory-mapped role is silently discarded by
  an unrelated local assignment, with the composition rule undocumented.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Assign a directory-mapped role and an independent local restriction to
  the same identity that would conflict, and inspect which one takes
  effect and whether that outcome is documented.
```

## G02-AUTH_LDAP-Q031

```yaml
QID: G02-AUTH_LDAP-Q031
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The recovery path offered when delegated authentication cannot be
  completed is not materially weaker (in verification strength) than
  delegated authentication itself.
WHY_IT_MATTERS: >
  A weak recovery path becomes the attacker's preferred route, defeating the
  strength of the primary delegated path entirely.
DISCONFIRMING_OBSERVATION: >
  An identity that could not complete delegated authentication is able to
  gain equivalent account access through a recovery path that requires
  materially less proof of identity.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Compare the verification steps required by the delegated path against the
  recovery path offered when delegation fails, for the same identity.
```

## G02-AUTH_LDAP-Q032

```yaml
QID: G02-AUTH_LDAP-Q032
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When directory-based role mapping is left unconfigured, the default role
  assigned to a newly matched identity is an explicit, documented default,
  not an incidental side effect of some other setting.
WHY_IT_MATTERS: >
  An incidental default can grant unintended privilege the first time
  someone forgets to configure mapping.
DISCONFIRMING_OBSERVATION: >
  With role mapping left unconfigured, a newly matched identity receives a
  role that does not match any documented default, or receives a
  meaningfully privileged role at all.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Leave group/role mapping unconfigured, authenticate a new directory
  identity for the first time, and inspect the role it receives against the
  documented default.
```
## G02-AUTH_LDAP-Q033

```yaml
QID: G02-AUTH_LDAP-Q033
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two concurrent first-time authentication attempts for the same directory
  identity, racing to provision a local account, resolve to exactly one
  local account, never two and never a corrupted single account.
WHY_IT_MATTERS: >
  A race condition here can create duplicate accounts with split history, or
  a partially-written account record.
DISCONFIRMING_OBSERVATION: >
  Two concurrent first-time authentications for the same directory identity
  result in two separate local accounts, or in one account with
  inconsistent or partially-populated data.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger two near-simultaneous first-time authentication attempts for the
  same not-yet-provisioned directory identity and inspect the resulting
  account(s).
```

## G02-AUTH_LDAP-Q034

```yaml
QID: G02-AUTH_LDAP-Q034
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Once delegated authentication is disabled at the configuration level, its
  entry path is actually unreachable at runtime, not merely hidden from the
  interface.
WHY_IT_MATTERS: >
  A hidden-but-reachable path is a false sense of closure: the control
  appears off but is not.
DISCONFIRMING_OBSERVATION: >
  With delegated authentication disabled in configuration, a direct call to
  its entry path (bypassing the interface) still succeeds.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Disable delegated authentication in configuration, then invoke its
  underlying entry path directly rather than through the normal interface.
```

## G02-AUTH_LDAP-Q035

```yaml
QID: G02-AUTH_LDAP-Q035
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A directory connection that is configured but points at an unreachable or
  decommissioned service fails in a way distinguishable, in both the user-
  facing outcome and the audit trail, from delegated authentication being
  deliberately disabled.
WHY_IT_MATTERS: >
  Conflating the two makes an operational outage look like an intentional
  policy state, delaying detection and response.
DISCONFIRMING_OBSERVATION: >
  Pointing the directory connection at an unreachable endpoint produces the
  same outcome and audit signature as deliberately disabling delegated
  authentication.
EXPECTED_SURFACE: S3,S6,S7
PRECONDITIONS: >
  Compare the outcome and audit trail of (a) an unreachable directory
  endpoint and (b) delegated authentication deliberately disabled, under an
  otherwise identical authentication attempt.
```

## G02-AUTH_LDAP-Q036

```yaml
QID: G02-AUTH_LDAP-Q036
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The group/role mapping rules actually applied at runtime always match the
  rules as currently configured, with no stale or cached rule set surviving
  a configuration change.
WHY_IT_MATTERS: >
  A stale cached rule set means a reviewed and approved configuration change
  is not actually the rule being enforced.
DISCONFIRMING_OBSERVATION: >
  After a mapping rule is changed, an authentication that should be affected
  by the change instead continues to reflect the previous rule.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Change a mapping rule, then immediately authenticate an identity affected
  by the change and inspect which rule version actually applied.
```

## G02-AUTH_LDAP-Q037

```yaml
QID: G02-AUTH_LDAP-Q037
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reverting a directory connection or mapping configuration to a previous
  state does not leave already-matched accounts in an inconsistent mixture
  of role outcomes from the old and new configurations.
WHY_IT_MATTERS: >
  A mixed state after a revert is harder to detect than either configuration
  alone and can silently persist elevated privilege.
DISCONFIRMING_OBSERVATION: >
  After reverting configuration to a previous version, some already-matched
  accounts reflect the role outcome of the interim (now-reverted)
  configuration while others reflect the restored one.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Change mapping configuration, allow it to take effect for a set of
  accounts, then revert to the prior configuration and inspect the
  resulting role state across those accounts.
```

## G02-AUTH_LDAP-Q038

```yaml
QID: G02-AUTH_LDAP-Q038
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A delegated authentication attempt that is abandoned or explicitly
  cancelled by the user before completion does not leave a partially
  created local account behind.
WHY_IT_MATTERS: >
  An orphaned partial account is an unowned record with unclear privilege
  and lifecycle status.
DISCONFIRMING_OBSERVATION: >
  Cancelling a delegated authentication attempt part-way through leaves a
  local account record in existence with no completed authentication behind
  it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Begin a first-time delegated authentication attempt and cancel it before
  completion, then inspect whether a local account record was created.
```

## G02-AUTH_LDAP-Q039

```yaml
QID: G02-AUTH_LDAP-Q039
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An identity whose directory account is temporarily disabled (not deleted)
  is denied access for the full duration of that disablement, not only from
  the next scheduled full synchronisation onward.
WHY_IT_MATTERS: >
  A gap between a temporary disablement and its enforcement is a window
  where a suspended identity retains full access.
DISCONFIRMING_OBSERVATION: >
  An identity is able to authenticate successfully during a window after
  its directory account was temporarily disabled but before the next
  scheduled synchronisation.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Temporarily disable a directory identity's account mid-cycle (not at a
  scheduled sync boundary) and immediately attempt authentication as that
  identity.
```

## G02-AUTH_LDAP-Q040

```yaml
QID: G02-AUTH_LDAP-Q040
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Case or formatting differences in the identifier used for matching (such
  as differing capitalisation) do not create a second, unintended local
  account for what is the same real-world directory identity.
WHY_IT_MATTERS: >
  A formatting-sensitive match silently fragments one identity's history and
  privilege across multiple accounts.
DISCONFIRMING_OBSERVATION: >
  Authenticating with the matching identifier in a different case or
  formatting than was used at first provisioning creates a second local
  account instead of resolving to the existing one.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Provision a local account via directory match using one formatting of the
  identifier, then authenticate again using a differently-cased or
  differently-formatted but semantically identical identifier.
```

## G02-AUTH_LDAP-Q041

```yaml
QID: G02-AUTH_LDAP-Q041
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Access granted to a person on one tenant through directory-mapped role
  assignment does not automatically extend to a different tenant that
  happens to use the same external directory service, absent an explicit
  configuration link between the two.
WHY_IT_MATTERS: >
  Implicit cross-tenant privilege from a shared directory undermines the
  entire multi-tenant isolation model.
DISCONFIRMING_OBSERVATION: >
  A person with a directory-mapped role on tenant A gains an equivalent role
  on tenant B, which independently uses the same directory service, with no
  explicit link configured between the two tenants' mapping rules.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure two tenants against the same external directory service with
  independent, unlinked mapping rules; authenticate a shared identity
  against each and compare granted roles.
```

## G02-AUTH_LDAP-Q042

```yaml
QID: G02-AUTH_LDAP-Q042
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A mapping rule that grants a highly privileged role is distinguishable, in
  the configuration and its audit trail, from a mapping rule that grants an
  ordinary role, so that an overly broad rule is detectable on review.
WHY_IT_MATTERS: >
  An accidental "matches everyone" rule tied to a high-privilege role is one
  of the most damaging possible misconfigurations, and must be reviewable.
DISCONFIRMING_OBSERVATION: >
  A mapping rule granting a highly privileged role is recorded identically
  to an ordinary mapping rule, with nothing in the configuration or its
  audit trail flagging the elevated grant for review.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Create a mapping rule granting a highly privileged role and inspect
  whether the configuration listing or audit trail distinguishes it from an
  ordinary mapping rule.
```

## G02-AUTH_LDAP-Q043

```yaml
QID: G02-AUTH_LDAP-Q043
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Removing a group/role mapping rule from configuration has a defined,
  documented effect (immediate revocation, or revocation only at next
  authentication) on identities who held the role solely because of that
  rule.
WHY_IT_MATTERS: >
  An undocumented timing leaves reviewers unable to say when a removed
  privilege actually stops applying.
DISCONFIRMING_OBSERVATION: >
  After a mapping rule is removed, an identity who held the role solely
  through it retains the role for longer, or has it removed sooner, than
  the documented timing states.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Remove a mapping rule that is the sole source of a role for a given
  identity, and check the timing of the role's removal against the
  documented behaviour.
```

## G02-AUTH_LDAP-Q044

```yaml
QID: G02-AUTH_LDAP-Q044
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A trust or certificate validation failure between the system and the
  external directory service produces a failure state distinguishable, in
  the audit trail, from a simple credential rejection.
WHY_IT_MATTERS: >
  Hiding a trust failure inside a generic denial masks a potential
  interception or misconfiguration from the people who would investigate
  denials.
DISCONFIRMING_OBSERVATION: >
  A deliberately broken trust/certificate relationship with the directory
  service produces the same audit signature as an ordinary rejected
  credential.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Break the trust relationship (e.g., an expired or mismatched trust
  artifact) between the system and the directory service, attempt
  authentication, and inspect the resulting audit entry against an ordinary
  rejected-credential entry.
```

## G02-AUTH_LDAP-Q045

```yaml
QID: G02-AUTH_LDAP-Q045
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where multiple directory connections are configured for redundancy or
  multiple domains, an identity from a lower-trust connection cannot
  silently satisfy a mapping rule that was intended for a higher-trust
  connection.
WHY_IT_MATTERS: >
  Without connection-aware evaluation, adding a lower-trust connection can
  silently widen who qualifies for a sensitive mapping rule.
DISCONFIRMING_OBSERVATION: >
  An identity authenticated through a lower-trust directory connection
  receives a role mapping that configuration intended to restrict to a
  higher-trust connection.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure two directory connections with differing trust intent and a
  mapping rule scoped to only one; authenticate a matching identity through
  the other connection and inspect the outcome.
```

## G02-AUTH_LDAP-Q046

```yaml
QID: G02-AUTH_LDAP-Q046
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Use of the local fallback path is logged distinctly from a normal
  successful delegated authentication, so fallback usage can be reviewed
  independently.
WHY_IT_MATTERS: >
  Indistinguishable logging makes it impossible to monitor how often, and by
  whom, the intended-primary control is being bypassed.
DISCONFIRMING_OBSERVATION: >
  A successful authentication via the local fallback path produces an audit
  entry indistinguishable from a successful delegated authentication.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Authenticate once via delegated authentication and once via local
  fallback for comparable identities, and compare the two audit entries.
```

## G02-AUTH_LDAP-Q047

```yaml
QID: G02-AUTH_LDAP-Q047
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a directory-matched account already carries a conflicting locally-set
  attribute, a defined precedence rule (directory-asserted vs. locally-set)
  governs the outcome, rather than an undefined last-write-wins result.
WHY_IT_MATTERS: >
  An undefined precedence means the same conflict can resolve differently
  on different days, defeating predictable behaviour.
DISCONFIRMING_OBSERVATION: >
  A conflict between a directory-asserted attribute and a locally-set one on
  the same account resolves inconsistently across repeated, otherwise
  identical authentication attempts.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Set a locally-set attribute on an account, then authenticate via the
  directory with a conflicting value for the same attribute, repeated
  several times, and compare outcomes.
```

## G02-AUTH_LDAP-Q048

```yaml
QID: G02-AUTH_LDAP-Q048
MODULE: auth_ldap
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A directory group used for role mapping in one tenant's configuration does
  not implicitly grant a matching role in a different tenant's independent
  configuration solely because the group name string is identical.
WHY_IT_MATTERS: >
  Name-based coupling across tenants is an accidental cross-tenant privilege
  channel that has nothing to do with actual directory structure.
DISCONFIRMING_OBSERVATION: >
  An identity belonging to a group with a given name in tenant A's directory
  context receives a role mapped to a same-named group in tenant B's
  independent configuration.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure a mapping rule in tenant B referencing a group name that
  coincidentally also exists in tenant A's directory context; authenticate
  a tenant-A-only identity that is a member of that group and inspect
  whether tenant B's role is granted.
```
