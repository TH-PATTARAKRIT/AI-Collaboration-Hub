# SMEsPlus ENTERPRISE SUITE
## GMVQ — G02 IDENTITY_ACCESS / authentication-delegated-to-external-identity-provider Module Adversarial MVQ Bank

**Document ID:** GMVQ-G02-AUTH_OAUTH-MVQ48-V1.00
**Group:** G02 IDENTITY_ACCESS
**Module Metadata:** `auth_oauth`
**Wave:** W1
**Author Cell:** TEAM 08 (GMVQ Question Factory — Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN / REVISED R2
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded
**CHANGE_REASON (R2):** Independent Master Audit team M5 (XG_DUPLICATE_OVERLAP_REGISTER_M5.tsv, finding type NEAR_DUPLICATE_CROSS_MODULE / NOUN_SWAPPED_TEMPLATE) found 12 of this bank's 48 questions were noun-swapped templates of the corresponding auth_ldap bank. Production remediation cell R2, under directive SMEPLUS-GMVQ-20P-5AUDIT-20260927-004, rewrote the HYPOTHESIS / WHY_IT_MATTERS / DISCONFIRMING_OBSERVATION / PRECONDITIONS of the 12 affected questions to test ground specific to delegated authentication against an external identity provider. QIDs are unchanged; no question was added or removed (actual_mvq_count remains 48). See 02_REGISTERS/DEFECT_CLOSURE_R2.tsv for the per-QID before/after record.

## Purpose

This bank extends the 35 Standard Questions with 48 module-specific, falsifiable questions
covering authentication delegated to an external identity provider: matching a provider-issued
identity to a local account, the lifetime and validity of issued credentials, account linking
and unlinking, and provider-side revocation reaching the local system. Coverage spans every
material dimension in the Group Brief for G02 (entry-path enforcement, retroactivity of policy
change, per-tenant isolation, fail-open/fail-closed, identity collision, de-provisioning lag,
weak recovery paths, lockout-as-DoS, session termination semantics, internal/external regime
divergence, auditability, and clock/timezone effects).

The question text is source-neutral. It does not name the module, any vendor or product, or
any technical identifier (model, table, field, method, XML ID, API path). "External identity
provider" and "delegated authentication" are used throughout in place of any protocol name.

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

## G02-AUTH_OAUTH-Q001

```yaml
QID: G02-AUTH_OAUTH-Q001
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the attribute used to match an external identity to a local account is
  one the provider does not itself guarantee to be verified, unique, or
  permanent for that identity, matching does not rely on it alone; a
  materially more stable proof of identity is required.
WHY_IT_MATTERS: >
  An attribute the provider does not guarantee to be verified, unique, or
  permanent can be asserted by more than one identity over time, or
  reassigned, letting authentication silently resolve to the wrong local
  account.
DISCONFIRMING_OBSERVATION: >
  A local account is matched, or re-matched, using an attribute the provider
  explicitly does not guarantee to be verified, unique, or permanent, with no
  additional, more stable proof of identity involved in the decision.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Identify which attribute the provider marks as unverified, non-unique, or
  reassignable for a given identity. Present that attribute value under a
  different identity, or after it has changed, and observe whether the match
  still succeeds on that basis alone.
```

## G02-AUTH_OAUTH-Q002

```yaml
QID: G02-AUTH_OAUTH-Q002
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external identity provider is unreachable, slow, or returns a
  malformed response during authentication, the system resolves to an
  explicit, configured fail-closed outcome by default.
WHY_IT_MATTERS: >
  A silent fail-open during a provider outage grants access nobody decided
  to grant, at exactly the moment verification cannot occur.
DISCONFIRMING_OBSERVATION: >
  During a simulated provider outage, timeout, or malformed response, the
  system grants access without any distinct successful verification having
  occurred, or the outcome differs between two otherwise identical
  attempts.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Simulate provider unreachability, timeout, and a malformed authentication
  response separately; attempt authentication under each and compare the
  outcome against the configured policy.
```

## G02-AUTH_OAUTH-Q003

```yaml
QID: G02-AUTH_OAUTH-Q003
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a single local account can be reached through more than one external
  identity provider, the privilege granted to that account is governed by one
  defined, auditable precedence, not by whichever provider's assertion is most
  generous at the moment of authentication.
WHY_IT_MATTERS: >
  Without a defined precedence, an account's effective privilege can be
  inflated simply by authenticating through whichever connected provider
  currently asserts the broadest access, defeating least-privilege review.
DISCONFIRMING_OBSERVATION: >
  The same local account, reached through two different external providers
  that assert different privilege, ends up with the more generous of the two
  privilege sets, with no recorded precedence rule explaining why.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Link one local account to two external providers configured to assert
  different privilege for the same account. Authenticate through each in turn
  and compare the resulting effective privilege and its audit trail.
```

## G02-AUTH_OAUTH-Q004

```yaml
QID: G02-AUTH_OAUTH-Q004
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the external provider ever reissues a previously-used stable identifier
  to a different real-world person, that new person does not automatically
  inherit the local account, data, or privilege that the identifier's original
  holder had.
WHY_IT_MATTERS: >
  Identifier reuse at the provider is outside this system's control; treating
  a reissued identifier as the same identity silently hands one person's
  account and privilege to someone else.
DISCONFIRMING_OBSERVATION: >
  A stable identifier previously bound to one local account is presented by a
  different real-world identity and the system grants that identity the
  original account's access, with nothing detecting or flagging the
  substitution.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Simulate the provider reissuing a previously-used stable identifier to a new
  identity (a distinguishable set of asserted attributes under the same
  identifier). Authenticate as the new identity and observe what account and
  privilege result.
```

## G02-AUTH_OAUTH-Q005

```yaml
QID: G02-AUTH_OAUTH-Q005
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the external provider's stable identifier for an already-matched identity
  changes (for example, following a provider-side migration or reissue for the
  same person), the local account continues to be recognised as the same
  account rather than being duplicated or orphaned.
WHY_IT_MATTERS: >
  Treating a changed stable identifier as a brand-new identity silently
  strands the original account's history and access, or creates a second
  account with none of it.
DISCONFIRMING_OBSERVATION: >
  After the provider's stable identifier for a matched identity changes for
  the same underlying person, authentication either creates a second local
  account or fails to recognise the identity at all, rather than continuing to
  resolve to the original account.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  For an identity already matched to a local account, change the stable
  identifier the provider asserts for that same person, then authenticate
  again and observe which account, if any, is reached.
```

## G02-AUTH_OAUTH-Q006

```yaml
QID: G02-AUTH_OAUTH-Q006
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Revocation of access at the external identity provider (withdrawn consent
  or a disabled provider account) reaches the local account and any active
  local session within a defined, bounded time, rather than remaining
  unnoticed until the credential's natural expiry.
WHY_IT_MATTERS: >
  Provider-side revocation that never reaches the local system defeats the
  purpose of delegating identity lifecycle to the provider.
DISCONFIRMING_OBSERVATION: >
  An identity whose access was revoked at the provider continues to hold a
  live local session or continues to authenticate successfully well beyond
  the documented bound for that effect to take hold.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Establish a live session for a provider-authenticated identity, revoke
  that identity's access at the provider, and observe the session and
  subsequent authentication attempts over the documented bound period.
```

## G02-AUTH_OAUTH-Q007

```yaml
QID: G02-AUTH_OAUTH-Q007
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An issued access credential's usable lifetime is enforced by the system
  itself, independent of whether the client presenting it claims the
  credential is still valid.
WHY_IT_MATTERS: >
  Trusting a client's own claim of validity turns an expiry policy into an
  honour system with no real enforcement.
DISCONFIRMING_OBSERVATION: >
  A credential presented after its documented lifetime has elapsed is still
  accepted by the system.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Obtain a credential, wait past its documented lifetime (or otherwise
  advance past it in a controlled test), and attempt to use it.
```

## G02-AUTH_OAUTH-Q008

```yaml
QID: G02-AUTH_OAUTH-Q008
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A refresh credential used to obtain a new access credential does not
  extend access indefinitely beyond any absolute session or
  re-authentication limit configured for the account.
WHY_IT_MATTERS: >
  An unbounded refresh chain defeats any absolute session limit set as a
  security control.
DISCONFIRMING_OBSERVATION: >
  Repeated use of a refresh credential continues to yield valid access
  credentials past the account's documented absolute session or
  re-authentication limit.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Configure an absolute session limit, repeatedly use a refresh credential
  to obtain new access credentials across that limit, and observe whether
  refresh eventually stops succeeding.
```

## G02-AUTH_OAUTH-Q009

```yaml
QID: G02-AUTH_OAUTH-Q009
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Linking an existing local account to a provider-issued identity requires
  proof of ownership of the existing local account (such as being already
  signed into it), not merely presentation of a matching contact attribute.
WHY_IT_MATTERS: >
  Linking on attribute match alone lets anyone who controls a matching
  provider identity take over an existing local account.
DISCONFIRMING_OBSERVATION: >
  A provider identity is able to link itself to an existing local account
  that it does not already own, based solely on a matching attribute and
  with no proof-of-ownership step for the existing account.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Attempt to link a provider identity to an existing local account without
  first being authenticated into that existing account, using only a
  matching attribute as the basis.
```

## G02-AUTH_OAUTH-Q010

```yaml
QID: G02-AUTH_OAUTH-Q010
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Unlinking a provider-issued identity from a local account leaves the
  account in a defined, still-authenticatable state, not stranded with no
  valid way to sign in.
WHY_IT_MATTERS: >
  A stranding unlink is an unplanned lockout the account owner cannot
  self-resolve.
DISCONFIRMING_OBSERVATION: >
  After unlinking the only authentication method an account has, the
  account has no remaining way to authenticate through any documented path.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Unlink the sole authentication method from an account and attempt to
  authenticate immediately afterward through every documented path.
```

## G02-AUTH_OAUTH-Q011

```yaml
QID: G02-AUTH_OAUTH-Q011
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Unlinking a provider-issued identity from a local account does not
  silently revoke roles or data ownership that have nothing to do with the
  authentication method itself.
WHY_IT_MATTERS: >
  Coupling authentication method to unrelated privilege or ownership causes
  an administrative action about sign-in to have unintended business
  consequences.
DISCONFIRMING_OBSERVATION: >
  Unlinking a provider identity from an account causes a role assignment or
  data ownership unrelated to authentication to change or disappear.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Assign a role and record ownership unrelated to authentication method,
  unlink the account's provider identity, and inspect the role and
  ownership afterward.
```

## G02-AUTH_OAUTH-Q012

```yaml
QID: G02-AUTH_OAUTH-Q012
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Provider delegation configured for the internal-user population does not,
  through account linking, become reachable from or extend privilege into
  the separate external-user (customer-facing) regime.
WHY_IT_MATTERS: >
  Merging the two regimes would let an external-facing identity reach
  internal data, or let internal delegation controls be bypassed from
  outside.
DISCONFIRMING_OBSERVATION: >
  An external-facing account is able to link to, or inherit privilege from,
  the internal provider delegation configuration.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Attempt to link or authenticate an external-user account through the
  internal provider delegation configuration and inspect whether any
  internal privilege becomes reachable.
```

## G02-AUTH_OAUTH-Q013

```yaml
QID: G02-AUTH_OAUTH-Q013
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A background, integration, or API access path acting on behalf of a
  provider-authenticated identity does not persist access beyond what the
  provider's revocation or the credential's expiry would allow for the
  interactive path.
WHY_IT_MATTERS: >
  An unenforced side door defeats every control placed on the interactive
  login path, including provider-side revocation.
DISCONFIRMING_OBSERVATION: >
  After an identity's provider access is revoked, an API or integration
  path tied to that identity continues to succeed beyond the documented
  bound.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Establish an API or integration access path for a provider-authenticated
  identity, revoke that identity's access at the provider, and attempt use
  of the API/integration path.
```

## G02-AUTH_OAUTH-Q014

```yaml
QID: G02-AUTH_OAUTH-Q014
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A scheduled or background process that depends on a previously issued
  credential has a defined behaviour when that credential is revoked or
  expires mid-run, rather than continuing silently on stale authority.
WHY_IT_MATTERS: >
  A process continuing on stale authority can act after the underlying
  permission has actually ended.
DISCONFIRMING_OBSERVATION: >
  A background process continues performing privileged actions after its
  underlying credential has been revoked or has expired mid-run, with no
  defined halt or flag.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Start a long-running background process using an issued credential,
  revoke or let the credential expire mid-run, and observe the process's
  continued behaviour.
```

## G02-AUTH_OAUTH-Q015

```yaml
QID: G02-AUTH_OAUTH-Q015
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A support or impersonation access path is not able to mint or reuse a
  provider-issued credential to act as the user without a distinctly logged
  basis for doing so.
WHY_IT_MATTERS: >
  An unlogged ability to reuse a provider credential turns impersonation
  into a way to act with the user's external identity undetected.
DISCONFIRMING_OBSERVATION: >
  Support or impersonation tooling is able to obtain or reuse a
  provider-issued credential for the target user with no distinct log
  entry marking the action as impersonated.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Use the support/impersonation path against a provider-authenticated
  identity and inspect whether any provider credential is reused or minted,
  and how it is logged.
```

## G02-AUTH_OAUTH-Q016

```yaml
QID: G02-AUTH_OAUTH-Q016
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Every authentication decision made through provider delegation (accepted,
  rejected, linked, or unlinked) is recorded with enough detail to identify
  which policy or provider configuration version was in force.
WHY_IT_MATTERS: >
  Without this, a disputed access or linking decision cannot be
  reconstructed or attributed to the rule that produced it.
DISCONFIRMING_OBSERVATION: >
  One of the four kinds of decision has no corresponding audit record, or
  its record does not identify the configuration version in force at that
  time.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Produce one instance of each of the four decision kinds under a known
  configuration version, then inspect the audit trail for each.
```
## G02-AUTH_OAUTH-Q017

```yaml
QID: G02-AUTH_OAUTH-Q017
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change to the external identity provider connection configuration is
  itself recorded with who made the change and when.
WHY_IT_MATTERS: >
  Configuration is where trust in an entire external provider is decided; an
  unattributed change to it is a serious audit gap.
DISCONFIRMING_OBSERVATION: >
  A change made to the provider connection configuration produces no audit
  record, or the record omits who made it or when.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Make a distinguishable change to the provider connection configuration
  and inspect the resulting audit record.
```

## G02-AUTH_OAUTH-Q018

```yaml
QID: G02-AUTH_OAUTH-Q018
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external provider is unreachable, slow, or returns a malformed
  response, the system applies one explicit, documented policy, either denying
  authentication or falling back in a defined, equally-verified way, rather
  than an accidental lockout of legitimate identities or an accidental bypass
  of verification.
WHY_IT_MATTERS: >
  An undocumented reaction to provider trouble becomes either a denial-of-
  service against every legitimate user of that provider, or a silent hole
  that admits anyone when the provider degrades.
DISCONFIRMING_OBSERVATION: >
  With the external provider made unreachable, slow, or made to return a
  malformed response, authentication either locks out identities that should
  still have access or admits an identity without completing verification, and
  no explicit policy governs which occurs.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Make the external provider unreachable, artificially slow, or force it to
  return a malformed response, then attempt authentication for a known-good
  identity and observe the outcome and whether it matches a documented policy.
```

## G02-AUTH_OAUTH-Q019

```yaml
QID: G02-AUTH_OAUTH-Q019
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A lockout or failure state produced by a provider-authentication attempt
  does not silently apply to a different, independent authentication method
  available on the same account.
WHY_IT_MATTERS: >
  Cross-method lockout coupling can deny a user every way into their account
  because of a failure in only one of them.
DISCONFIRMING_OBSERVATION: >
  Triggering a lockout condition through the provider-authentication path
  also blocks a different, independent authentication method on the same
  account.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  On an account with two independent authentication methods, trigger a
  lockout condition through provider authentication and immediately attempt
  the other method.
```

## G02-AUTH_OAUTH-Q020

```yaml
QID: G02-AUTH_OAUTH-Q020
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Ending a session established through provider delegation has a defined
  effect on in-flight work, on any background job launched by that session,
  and on any credential issued from it.
WHY_IT_MATTERS: >
  An undefined effect leaves either orphaned in-flight work or a
  still-usable credential outliving the session it came from.
DISCONFIRMING_OBSERVATION: >
  After a provider-delegated session is explicitly ended, a credential
  issued from it continues to be accepted, or in-flight work started under
  it continues with no defined handling.
EXPECTED_SURFACE: S1,S3,S6,S8
PRECONDITIONS: >
  Establish a provider-delegated session, issue a credential and start a
  long-running action from it, then end the session and observe both the
  credential and the in-flight action.
```

## G02-AUTH_OAUTH-Q021

```yaml
QID: G02-AUTH_OAUTH-Q021
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Expiry checks on an issued credential use a consistent time reference
  between the moment of issuance and the moment of verification, regardless
  of the time zone of either party.
WHY_IT_MATTERS: >
  A time-zone mismatch can cause a credential to be honoured too long, or
  rejected too soon, relative to its actual issued lifetime.
DISCONFIRMING_OBSERVATION: >
  A credential's accept/reject outcome at verification depends on the time
  zone configured on the verifying component, with the underlying issued
  instant and elapsed time unchanged.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Issue a credential, then verify it from components set to different time
  zones at the same underlying instant, and compare the accept/reject
  outcome.
```

## G02-AUTH_OAUTH-Q022

```yaml
QID: G02-AUTH_OAUTH-Q022
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When a group or access-level attribute that a privilege-mapping rule depends
  on is simply absent from what the provider asserts, the mapping produces one
  defined, auditable fallback outcome, typically the least privilege, not an
  unreviewed default grant.
WHY_IT_MATTERS: >
  An absent attribute silently defaulting to a permissive outcome turns an
  incomplete provider response into an unintended privilege grant that no one
  configured or reviewed.
DISCONFIRMING_OBSERVATION: >
  Authenticating an identity for whom the provider omits the group or access-
  level attribute a mapping rule depends on results in a privileged outcome
  being granted anyway, with no recorded fallback rule explaining why.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Configure a privilege-mapping rule that depends on a specific group or
  access-level attribute, then authenticate an identity for which the
  provider's response omits that attribute, and inspect the resulting
  privilege and its audit trail.
```

## G02-AUTH_OAUTH-Q023

```yaml
QID: G02-AUTH_OAUTH-Q023
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When access is withdrawn at the external provider for an identity, any local
  session already established for that identity is also ended, or re-verified,
  within a bounded time; it does not continue granting access indefinitely on
  the strength of the original authentication alone.
WHY_IT_MATTERS: >
  A provider-side revocation that never reaches an already-open local session
  leaves the exact access the revocation intended to remove fully usable,
  defeating the purpose of revoking it.
DISCONFIRMING_OBSERVATION: >
  After access is withdrawn at the external provider for an identity, a local
  session already established for that identity continues to grant access well
  beyond any bounded re-verification window, with nothing in the system re-
  checking or ending it.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Authenticate an identity and keep its local session active. Withdraw that
  identity's access at the external provider without ending the local session
  directly, then continue using the session and observe how long it keeps
  working.
```

## G02-AUTH_OAUTH-Q024

```yaml
QID: G02-AUTH_OAUTH-Q024
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A provider response asserting attributes that satisfy no configured
  account-matching rule defaults to an explicit, documented
  minimal-privilege or denied outcome, not an undefined one.
WHY_IT_MATTERS: >
  An undefined default is a coin flip between "denied" and "fully
  privileged," and the latter is a serious exposure.
DISCONFIRMING_OBSERVATION: >
  A provider response matching no configured rule results in access being
  granted, or in a role beyond the documented minimal default.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Authenticate a provider identity whose asserted attributes are
  deliberately constructed to match no configured account-matching rule,
  and inspect the outcome.
```

## G02-AUTH_OAUTH-Q025

```yaml
QID: G02-AUTH_OAUTH-Q025
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A role or permission derived from provider-asserted information composes
  correctly with a role or restriction assigned independently within the
  local system, without either one silently overriding the other in a way
  nobody reviewed.
WHY_IT_MATTERS: >
  Unreviewed override in either direction produces either an unintended
  restriction or an unintended grant of privilege.
DISCONFIRMING_OBSERVATION: >
  A locally-assigned restriction on an identity is silently overridden by a
  provider-derived role, or a provider-derived role is silently discarded
  by an unrelated local assignment, with the composition rule undocumented.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Assign a provider-derived role and an independent local restriction to
  the same identity that would conflict, and inspect which one takes
  effect and whether that outcome is documented.
```

## G02-AUTH_OAUTH-Q026

```yaml
QID: G02-AUTH_OAUTH-Q026
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Once the external provider withdraws an identity's underlying authorization,
  any step the system uses to renew or extend that identity's access without
  fresh interactive proof also stops succeeding; it does not keep minting
  extended access on the strength of a renewal credential issued before the
  withdrawal.
WHY_IT_MATTERS: >
  A renewal mechanism that keeps working after the underlying authorization is
  gone turns a one-time revocation into something that must also be separately
  hunted down and revoked, or access silently continues.
DISCONFIRMING_OBSERVATION: >
  After the external provider withdraws an identity's underlying
  authorization, a renewal step performed with a credential issued before the
  withdrawal still succeeds and extends that identity's local access.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Establish access for an identity and obtain a renewal credential issued
  during that access. Withdraw the identity's underlying authorization at the
  provider, then attempt to use the renewal credential and observe whether it
  still succeeds.
```

## G02-AUTH_OAUTH-Q027

```yaml
QID: G02-AUTH_OAUTH-Q027
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When account-linking rules are left unconfigured, the resulting default
  behaviour for a first-time provider-authenticated identity (auto-create,
  deny, or require manual linking) is an explicit, documented default.
WHY_IT_MATTERS: >
  An incidental default (such as silently auto-creating accounts) can grant
  unintended access the first time someone forgets to configure linking.
DISCONFIRMING_OBSERVATION: >
  With account-linking rules left unconfigured, a first-time
  provider-authenticated identity is handled in a way that matches none of
  the documented default behaviours.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Leave account-linking rules unconfigured, authenticate a new provider
  identity for the first time, and compare the resulting behaviour to the
  documented default.
```

## G02-AUTH_OAUTH-Q028

```yaml
QID: G02-AUTH_OAUTH-Q028
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Once a local account is disabled, a provider-issued assertion or grant
  obtained before the disablement can no longer be used to reach that account
  or anything it could access; disabling the local account also closes every
  path that assertion could still open.
WHY_IT_MATTERS: >
  A local disablement that does not reach previously-issued provider grants
  leaves the exact access the disablement intended to remove fully usable
  through a side door.
DISCONFIRMING_OBSERVATION: >
  After a local account is disabled, a provider-issued assertion or grant
  obtained before the disablement is still accepted and still reaches that
  account or its access.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Authenticate an identity and retain the provider-issued assertion or grant
  produced by that authentication. Disable the corresponding local account,
  then attempt to use the retained assertion or grant and observe whether it
  still succeeds.
```

## G02-AUTH_OAUTH-Q029

```yaml
QID: G02-AUTH_OAUTH-Q029
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Once provider delegation is disabled at the configuration level, its
  entry path is actually unreachable at runtime, not merely hidden from the
  interface.
WHY_IT_MATTERS: >
  A hidden-but-reachable path is a false sense of closure: the control
  appears off but is not.
DISCONFIRMING_OBSERVATION: >
  With provider delegation disabled in configuration, a direct call to its
  underlying entry path (bypassing the interface) still succeeds.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Disable provider delegation in configuration, then invoke its underlying
  entry path directly rather than through the normal interface.
```

## G02-AUTH_OAUTH-Q030

```yaml
QID: G02-AUTH_OAUTH-Q030
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A provider connection that is configured but points at an invalid or
  decommissioned provider endpoint fails in a way distinguishable, in both
  the user-facing outcome and the audit trail, from delegation being
  deliberately disabled.
WHY_IT_MATTERS: >
  Conflating the two makes an operational outage look like an intentional
  policy state, delaying detection and response.
DISCONFIRMING_OBSERVATION: >
  Pointing the provider connection at an invalid endpoint produces the same
  outcome and audit signature as deliberately disabling delegation.
EXPECTED_SURFACE: S3,S6,S7
PRECONDITIONS: >
  Compare the outcome and audit trail of (a) an invalid provider endpoint
  and (b) delegation deliberately disabled, under an otherwise identical
  authentication attempt.
```

## G02-AUTH_OAUTH-Q031

```yaml
QID: G02-AUTH_OAUTH-Q031
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The account-matching and permission rules actually applied at runtime
  always match the rules as currently configured, with no stale cached rule
  set surviving a configuration change.
WHY_IT_MATTERS: >
  A stale cached rule set means a reviewed and approved configuration change
  is not actually the rule being enforced.
DISCONFIRMING_OBSERVATION: >
  After a matching or permission rule is changed, an authentication that
  should be affected by the change instead continues to reflect the
  previous rule.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Change a matching or permission rule, then immediately authenticate an
  identity affected by the change and inspect which rule version actually
  applied.
```

## G02-AUTH_OAUTH-Q032

```yaml
QID: G02-AUTH_OAUTH-Q032
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a local account is unlinked from an external provider identity, every
  privilege and every standing grant that existed only because of that link is
  removed at the same time; nothing tied to the link is left reachable
  afterward.
WHY_IT_MATTERS: >
  A link that is undone in name only, while the privilege or grants it created
  keep working, leaves exactly the access the unlink was meant to remove.
DISCONFIRMING_OBSERVATION: >
  After a local account is unlinked from an external provider identity, some
  privilege or standing grant that existed solely because of that link remains
  usable, with nothing having removed it at the time of the unlink.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Link a local account to an external provider identity and let it acquire
  privilege or a standing grant because of that link. Unlink the identity,
  then check whether that privilege or grant is still usable.
```
## G02-AUTH_OAUTH-Q033

```yaml
QID: G02-AUTH_OAUTH-Q033
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A user who abandons or cancels an in-progress provider authentication or
  linking flow does not leave a partially created local account or a
  partially completed link behind.
WHY_IT_MATTERS: >
  An orphaned partial account or half-completed link is an unowned record
  with unclear privilege and lifecycle status.
DISCONFIRMING_OBSERVATION: >
  Cancelling a provider authentication or linking flow part-way through
  leaves a local account record or a partial link in existence with no
  completed authentication or linking behind it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Begin a first-time provider authentication or an account-linking flow and
  cancel it before completion, then inspect whether a local account record
  or partial link was created.
```

## G02-AUTH_OAUTH-Q034

```yaml
QID: G02-AUTH_OAUTH-Q034
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A provider-issued identity whose underlying provider account is only
  temporarily suspended (not deleted) is denied access for the full
  duration of that suspension, not merely from the next scheduled check
  onward.
WHY_IT_MATTERS: >
  A gap between a temporary suspension and its enforcement is a window where
  a suspended identity retains full access.
DISCONFIRMING_OBSERVATION: >
  An identity is able to authenticate successfully during a window after
  its provider account was temporarily suspended but before the next
  scheduled check.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Temporarily suspend a provider identity's account mid-cycle (not at a
  scheduled check boundary) and immediately attempt authentication as that
  identity.
```

## G02-AUTH_OAUTH-Q035

```yaml
QID: G02-AUTH_OAUTH-Q035
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Case or formatting differences in a provider-asserted contact attribute
  used incidentally in matching do not create a second, unintended local
  account for what is the same real-world identity.
WHY_IT_MATTERS: >
  A formatting-sensitive match silently fragments one identity's history and
  privilege across multiple accounts.
DISCONFIRMING_OBSERVATION: >
  Authenticating with the same provider identity, where an incidental
  matching attribute differs only in case or formatting between attempts,
  creates a second local account instead of resolving to the existing one.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Provision a local account via provider match with one formatting of an
  incidental attribute, then authenticate again where the provider asserts
  a differently-cased or differently-formatted but semantically identical
  value.
```

## G02-AUTH_OAUTH-Q036

```yaml
QID: G02-AUTH_OAUTH-Q036
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Access granted to a person on one tenant through provider-delegated
  matching does not automatically extend to a different tenant that happens
  to use the same external identity provider, absent an explicit
  configuration link between the two.
WHY_IT_MATTERS: >
  Implicit cross-tenant privilege from a shared provider undermines the
  entire multi-tenant isolation model.
DISCONFIRMING_OBSERVATION: >
  A person with provider-delegated access on tenant A gains equivalent
  access on tenant B, which independently uses the same external identity
  provider, with no explicit link configured between the two tenants'
  matching rules.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure two tenants against the same external identity provider with
  independent, unlinked matching rules; authenticate a shared identity
  against each and compare granted access.
```

## G02-AUTH_OAUTH-Q037

```yaml
QID: G02-AUTH_OAUTH-Q037
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Consent a user granted once, for a specific, limited extent of access, is
  not silently treated later as covering a broader extent than what was
  actually granted; any expansion requires a new, visible consent event.
WHY_IT_MATTERS: >
  Silently widening what an old consent is treated as covering lets access
  grow past what the user actually agreed to, with no record of the user ever
  agreeing to the wider extent.
DISCONFIRMING_OBSERVATION: >
  Access broader than what a user's recorded consent covers is granted using
  that same, older consent, with no new consent event recorded for the broader
  extent.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Record a user's consent for a narrow, specific extent of access. Later,
  request or grant access at a broader extent for the same identity without a
  new consent interaction, and observe whether it is allowed on the strength
  of the original consent.
```

## G02-AUTH_OAUTH-Q038

```yaml
QID: G02-AUTH_OAUTH-Q038
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Removing an account-matching or permission rule from configuration has a
  defined, documented effect (immediate revocation, or revocation only at
  next authentication) on identities who obtained access solely through
  that rule.
WHY_IT_MATTERS: >
  An undocumented timing leaves reviewers unable to say when a removed
  privilege actually stops applying.
DISCONFIRMING_OBSERVATION: >
  After a matching or permission rule is removed, an identity who held
  access solely through it retains it for longer, or has it removed sooner,
  than the documented timing states.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Remove a matching or permission rule that is the sole source of access
  for a given identity, and check the timing of the removal against the
  documented behaviour.
```

## G02-AUTH_OAUTH-Q039

```yaml
QID: G02-AUTH_OAUTH-Q039
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A signature or trust validation failure when communicating with the
  external identity provider produces a failure state distinguishable, in
  the audit trail, from a simple authentication rejection.
WHY_IT_MATTERS: >
  Hiding a trust failure inside a generic denial masks a potential
  interception or misconfiguration from the people who would investigate
  denials.
DISCONFIRMING_OBSERVATION: >
  A deliberately broken trust or signature relationship with the provider
  produces the same audit signature as an ordinary rejected authentication.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Break the trust or signature relationship with the provider, attempt
  authentication, and inspect the resulting audit entry against an ordinary
  rejected-authentication entry.
```

## G02-AUTH_OAUTH-Q040

```yaml
QID: G02-AUTH_OAUTH-Q040
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where multiple identity provider connections are configured for the same
  tenant, an identity from a lower-trust provider cannot silently satisfy a
  matching rule that was intended for a higher-trust provider.
WHY_IT_MATTERS: >
  Without provider-aware evaluation, adding a lower-trust provider can
  silently widen who qualifies for a sensitive matching rule.
DISCONFIRMING_OBSERVATION: >
  An identity authenticated through a lower-trust provider connection
  receives a role or access that configuration intended to restrict to a
  higher-trust provider connection.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure two provider connections with differing trust intent and a
  matching rule scoped to only one; authenticate a matching identity
  through the other connection and inspect the outcome.
```

## G02-AUTH_OAUTH-Q041

```yaml
QID: G02-AUTH_OAUTH-Q041
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reuse of a previously issued credential after the user has explicitly
  unlinked or revoked the provider connection is detected and rejected, not
  silently honoured.
WHY_IT_MATTERS: >
  Honouring a credential after an explicit unlink defeats the entire point
  of the user's own revocation action.
DISCONFIRMING_OBSERVATION: >
  A credential issued before an explicit unlink or revocation continues to
  be accepted after that unlink or revocation has completed.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Obtain a credential, explicitly unlink or revoke the provider connection
  for that account, then attempt to use the previously issued credential.
```

## G02-AUTH_OAUTH-Q042

```yaml
QID: G02-AUTH_OAUTH-Q042
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An authorization the user granted for one specific integration with the
  external provider is not accepted as valid for a different, separate
  integration under the same provider identity; each integration's grant is
  checked against the integration it was actually issued for.
WHY_IT_MATTERS: >
  If a grant issued for one integration is honoured by another, a lower-trust
  or unrelated integration can obtain the access the user only ever agreed to
  give a specific, higher-trust one.
DISCONFIRMING_OBSERVATION: >
  An authorization the user granted for one integration is presented to, and
  accepted by, a different integration under the same provider identity,
  without the user having granted that separate integration anything.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Have a user grant authorization scoped to one specific integration with the
  external provider. Present that same authorization to a second, distinct
  integration and observe whether it is accepted.
```

## G02-AUTH_OAUTH-Q043

```yaml
QID: G02-AUTH_OAUTH-Q043
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A provider-asserted group or role claim used for mapping in one tenant's
  configuration does not implicitly grant a matching role in a different
  tenant's independent configuration solely because the claim value is
  identical.
WHY_IT_MATTERS: >
  Value-based coupling across tenants is an accidental cross-tenant
  privilege channel that has nothing to do with actual provider-side
  structure for that tenant.
DISCONFIRMING_OBSERVATION: >
  An identity carrying a claim value in tenant A's provider context receives
  a role mapped to the same claim value in tenant B's independent
  configuration.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure a matching rule in tenant B referencing a claim value that
  coincidentally also appears in tenant A's provider context; authenticate
  a tenant-A-only identity carrying that value and inspect whether tenant
  B's role is granted.
```

## G02-AUTH_OAUTH-Q044

```yaml
QID: G02-AUTH_OAUTH-Q044
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A user who has linked more than one external identity provider to the
  same local account has a defined outcome when the two providers disagree
  on an attribute used for authorization.
WHY_IT_MATTERS: >
  An undefined outcome for conflicting multi-provider claims makes
  authorization depend on which provider happened to be used last, without
  that being a documented rule.
DISCONFIRMING_OBSERVATION: >
  Authenticating through two linked providers that assert conflicting
  values for an authorization-relevant attribute produces different
  effective authorization depending on which provider was used, with no
  documented precedence rule.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Link two external identity providers to one account, configure them to
  assert conflicting values for an authorization-relevant attribute, and
  authenticate through each in turn.
```

## G02-AUTH_OAUTH-Q045

```yaml
QID: G02-AUTH_OAUTH-Q045
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An account created through provider delegation is not treated as
  pre-verified for a purpose that ordinarily requires a distinct
  verification step, unless that equivalence is an explicit, documented
  decision.
WHY_IT_MATTERS: >
  Assuming provider sign-in equals verification for an unrelated purpose can
  silently skip a control that purpose was relying on.
DISCONFIRMING_OBSERVATION: >
  An account created solely through provider delegation is treated as
  satisfying a distinct verification requirement it never separately
  completed, with no documented decision stating the two are equivalent.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Create an account solely through provider delegation and attempt to
  access a function that documentation says requires a distinct
  verification step, without completing that step separately.
```

## G02-AUTH_OAUTH-Q046

```yaml
QID: G02-AUTH_OAUTH-Q046
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A revocation notice from the provider that is delivered asynchronously
  after the fact is handled idempotently; processing the same notice twice
  does not produce an inconsistent account state.
WHY_IT_MATTERS: >
  Asynchronous delivery is commonly retried by the sender; non-idempotent
  handling can leave an account in a state that depends on how many times a
  duplicate notice happened to arrive.
DISCONFIRMING_OBSERVATION: >
  Delivering the same asynchronous revocation notice twice produces a
  different or inconsistent account state compared to delivering it once.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Trigger an asynchronous revocation notice for an identity, allow it to be
  processed, then deliver the identical notice a second time and compare
  the resulting account state.
```

## G02-AUTH_OAUTH-Q047

```yaml
QID: G02-AUTH_OAUTH-Q047
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A token or credential issued for one tenant's provider connection is not
  accepted as valid for a request scoped to a different tenant, even where
  the underlying provider identity is the same real person.
WHY_IT_MATTERS: >
  Accepting a credential across a tenant boundary defeats tenant isolation
  regardless of how correctly the identity itself was verified.
DISCONFIRMING_OBSERVATION: >
  A credential issued in the context of tenant A's provider connection is
  accepted for a request explicitly scoped to tenant B.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Obtain a credential issued under tenant A's provider connection for a
  person who also has an account on tenant B, and present that credential
  for a request scoped to tenant B.
```

## G02-AUTH_OAUTH-Q048

```yaml
QID: G02-AUTH_OAUTH-Q048
MODULE: auth_oauth
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A partial failure during the account-linking transaction (the local
  account updated but provider-side confirmation not completed, or the
  reverse) does not leave the account in an ambiguous linked/unlinked
  state.
WHY_IT_MATTERS: >
  An ambiguous half-linked state is unpredictable both for the user's next
  sign-in attempt and for anyone auditing the account's authentication
  methods.
DISCONFIRMING_OBSERVATION: >
  Interrupting the linking transaction between its local and provider-side
  steps leaves the account reporting different link states depending on
  which part of the system is asked.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Interrupt the account-linking transaction after its local-side step but
  before its provider-side confirmation completes, then inspect the
  account's link state from every surface that reports it.
```
