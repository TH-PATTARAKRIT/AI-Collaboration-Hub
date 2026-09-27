# SMEsPlus ENTERPRISE SUITE
## GMVQ — G02 IDENTITY_ACCESS / auth_timeout Module Adversarial MVQ Bank

**Document ID:** GMVQ-G02-AUTH_TIMEOUT-MVQ48-V1.00
**Group:** G02 IDENTITY_ACCESS
**Module Metadata:** `auth_timeout`
**Wave:** W1
**Author Cell:** TEAM 11 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded
**Standing Authorization:** SMEPLUS-GMVQ-25TEAM-ACCELERATION-20260927-001

## Purpose

This bank extends the 55 Standard Questions with 48 hard, module-specific behavioural
questions for `auth_timeout` — inactivity and absolute session limits. It targets what
expiry actually ends (the interactive session, issued tokens, background work the session
started, open locks), in-flight work and unsaved data at the moment of expiry, whether
activity on one surface silently extends another, per-tenant configuration of the limits,
clock skew and timezone effects, privileged and impersonation sessions expiring on the same
terms, and the auditability of forced termination.

The question text is source-neutral: it does not expose vendor names, model names, field
names, method names, XML IDs, API shapes, or any implementation detail. `MODULE:` carries
the metadata name; the metadata name never appears in question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that is a failure state, not a restatement of the hypothesis.
- No padding: 48 questions exist because each tests a distinct material hypothesis.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence from Lane A or Lane B.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This bank is DRAFT / AUTHORING COMPLETE / NOT FROZEN. It is not approved, not verified, not MASTER-ready.

## G02-AUTH_TIMEOUT-Q001

```yaml
QID: G02-AUTH_TIMEOUT-Q001
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The inactivity timer must be reset only by genuine user-initiated activity, not by
  background or automated requests the user did not initiate.
WHY_IT_MATTERS: >
  If automated traffic resets the clock, the inactivity limit stops reflecting actual user
  presence and becomes meaningless as a control.
DISCONFIRMING_OBSERVATION: >
  A session's inactivity timer is observed to reset due to a background or automated request
  occurring with no genuine user action.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Leave a session idle from the user's perspective while background/automated calls continue,
  and measure whether the inactivity timer resets.
```

## G02-AUTH_TIMEOUT-Q002

```yaml
QID: G02-AUTH_TIMEOUT-Q002
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The absolute session limit must terminate the session at its configured duration regardless
  of how much genuine activity occurred within that window.
WHY_IT_MATTERS: >
  An absolute limit that can be indefinitely postponed by continued activity is not actually
  an absolute limit and defeats its governance purpose.
DISCONFIRMING_OBSERVATION: >
  A session with continuous genuine activity remains valid past the configured absolute
  limit.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Maintain continuous genuine activity in a session past its configured absolute limit and
  observe whether it is terminated on schedule.
```

## G02-AUTH_TIMEOUT-Q003

```yaml
QID: G02-AUTH_TIMEOUT-Q003
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a session expires, every token issued under that session that the client could use to
  act as the identity must also stop being honored, not only the primary interactive session
  marker.
WHY_IT_MATTERS: >
  A session that appears expired but leaves other usable tokens alive is not actually
  terminated, just cosmetically so.
DISCONFIRMING_OBSERVATION: >
  After the interactive session is confirmed expired, a token issued earlier under that same
  session is still accepted for an action.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Capture any secondary tokens issued during a session, let the session expire, and attempt to
  use each captured token.
```

## G02-AUTH_TIMEOUT-Q004

```yaml
QID: G02-AUTH_TIMEOUT-Q004
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Background or scheduled work initiated by a session before it expires may continue, but must
  not silently continue to act with the terminated session's live authority for tasks that
  were not already committed at expiry.
WHY_IT_MATTERS: >
  Work quietly running under authority that no longer legitimately exists is an unaudited
  privilege that outlives its own justification.
DISCONFIRMING_OBSERVATION: >
  Background work initiated by an expired session continues to acquire or exercise fresh
  authority-dependent capability after the session's expiry, beyond completing what was
  already committed.
EXPECTED_SURFACE: S4,S8
PRECONDITIONS: >
  Initiate a long-running background task from a session, let the session expire mid-task,
  and inspect what authority the task exercises afterward.
```

## G02-AUTH_TIMEOUT-Q005

```yaml
QID: G02-AUTH_TIMEOUT-Q005
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A lock or reservation a session holds on a record must be released, or at least become
  contestable, once that session has expired.
WHY_IT_MATTERS: >
  A lock held by a session that no longer exists blocks legitimate users indefinitely with no
  clear path to recovery.
DISCONFIRMING_OBSERVATION: >
  A record remains locked by a session well after that session's expiry, with no mechanism to
  release or contest the lock.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Acquire a lock on a record within a session, let the session expire without explicitly
  releasing the lock, and attempt access from another session.
```

## G02-AUTH_TIMEOUT-Q006

```yaml
QID: G02-AUTH_TIMEOUT-Q006
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The behaviour when a session expires mid-edit — whether unsaved input is preserved,
  discarded, or recoverable — must be a defined, consistent behaviour rather than differing
  unpredictably by surface or timing.
WHY_IT_MATTERS: >
  Inconsistent handling of in-progress work at expiry causes silent data loss that users
  cannot anticipate or prepare for.
DISCONFIRMING_OBSERVATION: >
  Identical mid-edit states at expiry produce different outcomes, preserved versus lost,
  depending on surface or repetition, with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Begin an edit, allow the session to reach expiry mid-edit on more than one surface, and
  compare what happens to the unsaved input in each case.
```

## G02-AUTH_TIMEOUT-Q007

```yaml
QID: G02-AUTH_TIMEOUT-Q007
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Activity performed on one client surface under a shared identity must not silently extend
  the timeout of a separate, otherwise-idle session on a different surface unless that sharing
  is an explicit, documented design.
WHY_IT_MATTERS: >
  Unintended cross-surface extension defeats the purpose of a per-surface inactivity control
  and can keep a genuinely abandoned session alive.
DISCONFIRMING_OBSERVATION: >
  A session left idle on one surface has its expiry postponed purely because of activity
  occurring on a separate surface, with no documented shared-session design.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Leave a session idle on one surface while generating genuine activity on a different surface
  under the same identity, and measure whether the idle session's timer is affected.
```

## G02-AUTH_TIMEOUT-Q008

```yaml
QID: G02-AUTH_TIMEOUT-Q008
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The inactivity and absolute timeout durations configured for one tenant must not apply to,
  or be influenced by, another tenant's configuration.
WHY_IT_MATTERS: >
  Cross-tenant leakage of timeout configuration would let one customer's choice silently
  override another's governance decision.
DISCONFIRMING_OBSERVATION: >
  A session under one tenant is observed to expire according to a duration that matches a
  different tenant's configuration rather than its own.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Configure two tenants with materially different timeout durations and measure actual expiry
  timing for sessions under each.
```

## G02-AUTH_TIMEOUT-Q009

```yaml
QID: G02-AUTH_TIMEOUT-Q009
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The determination of whether a session has expired must rely on server-side time, not on a
  client-reported clock, so that a skewed client clock cannot change the actual expiry
  outcome.
WHY_IT_MATTERS: >
  If a client's clock can influence the expiry decision, a user or attacker with control over
  that clock can extend or falsely trigger session expiry.
DISCONFIRMING_OBSERVATION: >
  Altering the client's clock changes whether the server considers a session expired.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Alter the client-side clock forward and backward relative to real time and observe whether
  the server's expiry decision changes accordingly.
```

## G02-AUTH_TIMEOUT-Q010

```yaml
QID: G02-AUTH_TIMEOUT-Q010
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An absolute session limit must be computed from a single, timezone-independent basis so that
  sessions started under different timezone configurations with equal real elapsed time expire
  at the same real elapsed time.
WHY_IT_MATTERS: >
  A timezone-dependent computation makes the actual duration of the absolute limit different
  for users in different regions, undermining a uniform policy.
DISCONFIRMING_OBSERVATION: >
  Two sessions started with equal real elapsed time, under different timezone configurations,
  are found to expire at different real elapsed durations.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Start sessions under distinct timezone configurations and compare the real elapsed time each
  takes to reach its absolute limit.
```

## G02-AUTH_TIMEOUT-Q011

```yaml
QID: G02-AUTH_TIMEOUT-Q011
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A privileged administrative session must be subject to timeout limits at least as strict as
  an ordinary session, unless a longer limit for such sessions is an explicit, documented
  governance decision.
WHY_IT_MATTERS: >
  A privileged session with a looser, undocumented timeout is a larger, longer-lived attack
  surface exactly where the impact of compromise is highest.
DISCONFIRMING_OBSERVATION: >
  A privileged administrative session is found to have a longer effective timeout than an
  ordinary session, with no documented decision authorizing the difference.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Compare the actual configured and observed timeout behaviour of a privileged session against
  an ordinary one under the same tenant.
```

## G02-AUTH_TIMEOUT-Q012

```yaml
QID: G02-AUTH_TIMEOUT-Q012
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When an impersonation or support-access session expires, control must return cleanly to the
  original identity's own session state, without leaving an ambiguous or elevated residual
  state.
WHY_IT_MATTERS: >
  An ambiguous handoff at the end of impersonation is exactly the kind of edge case where
  elevated privilege can leak past its intended window.
DISCONFIRMING_OBSERVATION: >
  After an impersonation session expires, the resulting session state is ambiguous, retains
  elevated capability, or does not clearly return to the original identity.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Begin an impersonation/support-access session, let it reach expiry, and inspect the
  resulting session state and available capability.
```
## G02-AUTH_TIMEOUT-Q013

```yaml
QID: G02-AUTH_TIMEOUT-Q013
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A session ended by timeout must be recorded in the audit trail as distinct from a session
  ended by the user's own explicit logout action.
WHY_IT_MATTERS: >
  Conflating the two prevents any later analysis of how often sessions are actually being left
  idle versus deliberately closed.
DISCONFIRMING_OBSERVATION: >
  The audit trail records a timeout-ended session and a voluntarily-logged-out session in an
  indistinguishable way.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Produce one session ended by timeout and one ended by explicit logout, and compare what the
  audit trail records for each.
```

## G02-AUTH_TIMEOUT-Q014

```yaml
QID: G02-AUTH_TIMEOUT-Q014
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where both an inactivity limit and an absolute limit exist, the audit record of a
  termination must indicate which of the two actually triggered it.
WHY_IT_MATTERS: >
  Without this distinction, nobody can tell whether users are being cut off by inactivity or
  simply by the passage of time regardless of activity, which are very different governance
  and support signals.
DISCONFIRMING_OBSERVATION: >
  A termination's audit record does not indicate, or indicates incorrectly, whether inactivity
  or the absolute limit was the actual cause.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Deliberately trigger termination once by pure inactivity and once by the absolute limit
  despite continuous activity, and compare the audit record produced in each case.
```

## G02-AUTH_TIMEOUT-Q015

```yaml
QID: G02-AUTH_TIMEOUT-Q015
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether re-authenticating after an expiry resumes the prior work context or starts clean
  must be a consistent, defined behaviour rather than varying unpredictably.
WHY_IT_MATTERS: >
  Unpredictable resumption behaviour can either silently discard work the user expected to be
  preserved, or unexpectedly restore a state the user believed was closed.
DISCONFIRMING_OBSERVATION: >
  Repeating the same expiry-then-reauthenticate sequence under identical conditions produces
  different resumption behaviour on different occasions.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Let a session expire mid-task, re-authenticate, and repeat this sequence more than once
  under identical conditions, comparing the resulting context each time.
```

## G02-AUTH_TIMEOUT-Q016

```yaml
QID: G02-AUTH_TIMEOUT-Q016
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A long-lived token issued for integration or automated use must be governed by an explicit,
  separately stated policy, and must not simply inherit an interactive session's inactivity
  timeout by accident, in either direction.
WHY_IT_MATTERS: >
  An accidental inheritance in either direction — an integration token expiring unexpectedly
  from inactivity, or an interactive session never expiring because it resembles an
  integration token — undermines the reliability of both.
DISCONFIRMING_OBSERVATION: >
  An integration-issued token's expiry behaviour matches the interactive inactivity policy
  with no documented decision establishing that as the intended design.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Compare the observed expiry behaviour of an integration-issued token against the
  interactive session's stated inactivity policy under identical elapsed idle time.
```

## G02-AUTH_TIMEOUT-Q017

```yaml
QID: G02-AUTH_TIMEOUT-Q017
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the client performs any automated background renewal call, the effect of that call on the
  inactivity timer must be an explicit, documented design choice, not an accidental side
  effect indistinguishable from genuine user activity.
WHY_IT_MATTERS: >
  An undocumented renewal call effectively disables the inactivity control while giving the
  appearance that it is still functioning.
DISCONFIRMING_OBSERVATION: >
  An automated renewal call with no genuine user action behind it is found to extend the
  session identically to genuine activity, with no documented design stating this is
  intended.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Identify any automated background call the client makes and measure its effect on the
  session's inactivity timer when no genuine user action occurs.
```

## G02-AUTH_TIMEOUT-Q018

```yaml
QID: G02-AUTH_TIMEOUT-Q018
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The client's belief about whether a session is still valid must never remain positive after
  the server has already invalidated that session.
WHY_IT_MATTERS: >
  A client that believes a dead session is alive will let a user act on stale assumptions,
  including exposing whether locally cached data is still protected.
DISCONFIRMING_OBSERVATION: >
  The client continues to present the session as valid, or allows further interaction as if
  valid, after the server has already expired it.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Force server-side expiry of a session directly, without a corresponding client action, and
  observe how long the client continues to behave as though it were valid.
```

## G02-AUTH_TIMEOUT-Q019

```yaml
QID: G02-AUTH_TIMEOUT-Q019
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A request submitted just before expiry but processed after the expiry boundary must have a
  clearly defined outcome, either honoured as pre-expiry or cleanly rejected, not an outcome
  that depends on unpredictable timing.
WHY_IT_MATTERS: >
  An ambiguous in-flight outcome can either silently drop a legitimate action or silently
  honour one that should have been rejected.
DISCONFIRMING_OBSERVATION: >
  Requests submitted at nearly identical times relative to the expiry boundary are handled
  inconsistently, some honoured and some rejected with no discernible rule.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit requests timed very close to a session's expiry boundary repeatedly and compare the
  outcomes.
```

## G02-AUTH_TIMEOUT-Q020

```yaml
QID: G02-AUTH_TIMEOUT-Q020
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether the platform allows a defined grace action after the inactivity threshold is
  crossed, or applies a hard cutoff, must be a stated, consistent behaviour.
WHY_IT_MATTERS: >
  An undocumented, inconsistent grace window creates unpredictable user experience and an
  unclear actual security boundary.
DISCONFIRMING_OBSERVATION: >
  Actions attempted just after the inactivity threshold succeed on some occasions and are
  rejected on others under materially identical conditions.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Repeat an action attempted just after crossing the inactivity threshold across multiple
  trials under materially identical conditions.
```

## G02-AUTH_TIMEOUT-Q021

```yaml
QID: G02-AUTH_TIMEOUT-Q021
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Terminating one session for an identity, whether by timeout or otherwise, must not silently
  terminate other concurrent sessions for the same identity unless that shared termination is
  an explicit, documented design.
WHY_IT_MATTERS: >
  Unintended cross-session termination can unexpectedly disrupt a user's other active work
  with no clear cause.
DISCONFIRMING_OBSERVATION: >
  Timeout of one session for an identity is observed to also terminate a separate,
  independently active session for the same identity, with no documented design for shared
  termination.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Establish two independent concurrent sessions for the same identity, let one reach expiry,
  and check the state of the other.
```

## G02-AUTH_TIMEOUT-Q022

```yaml
QID: G02-AUTH_TIMEOUT-Q022
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a change to the configured timeout duration applies immediately to sessions already
  active, or only to sessions established after the change, must be an explicit, documented
  behaviour.
WHY_IT_MATTERS: >
  An undocumented choice here means administrators cannot predict or verify the actual effect
  of a policy change they make.
DISCONFIRMING_OBSERVATION: >
  Active sessions are observed to be affected inconsistently by a configuration change, some
  picking up the new duration and others not, with no documented rule explaining which.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Establish sessions, change the configured timeout duration, and observe whether and how the
  change is applied to the already-active sessions versus newly established ones.
```

## G02-AUTH_TIMEOUT-Q023

```yaml
QID: G02-AUTH_TIMEOUT-Q023
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The determination of how long a session has been idle must be computed by the server from
  server-observed activity, not trusted from any value the client itself reports.
WHY_IT_MATTERS: >
  If the client can report its own idle state, that self-report can be manipulated to keep an
  otherwise-idle session alive indefinitely.
DISCONFIRMING_OBSERVATION: >
  A session's measured idle time can be manipulated by altering what the client reports,
  independent of actual server-observed request activity.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to influence the server's idle-time determination by manipulating client-reported
  values while making no genuine requests, and observe the effect.
```

## G02-AUTH_TIMEOUT-Q024

```yaml
QID: G02-AUTH_TIMEOUT-Q024
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a session-initiated background task legitimately needs longer to complete than the
  absolute session limit allows, the platform must have an explicit mechanism for that task's
  continuation that does not depend on the original session remaining valid.
WHY_IT_MATTERS: >
  Without an explicit mechanism, a long task either silently fails partway or silently runs on
  borrowed, expired authority.
DISCONFIRMING_OBSERVATION: >
  A background task initiated by a session that exceeds the absolute limit either fails
  silently with no clear cause, or continues to run using the expired session's authority.
EXPECTED_SURFACE: S4,S8
PRECONDITIONS: >
  Initiate a background task expected to run longer than the configured absolute session
  limit and observe its behaviour once that limit passes.
```
## G02-AUTH_TIMEOUT-Q025

```yaml
QID: G02-AUTH_TIMEOUT-Q025
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Closing one browser tab or client window under a shared session must not, by itself, alter
  the inactivity calculation for other open tabs or windows under the same session.
WHY_IT_MATTERS: >
  An unexpected interaction between tab lifecycle and session timing produces confusing,
  hard-to-reproduce session loss for users working across multiple tabs.
DISCONFIRMING_OBSERVATION: >
  Closing one tab measurably changes the remaining time before the session, as observed from
  another open tab, expires.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Open a session across multiple tabs, close one, and measure the remaining session's expiry
  timing from another tab before and after.
```

## G02-AUTH_TIMEOUT-Q026

```yaml
QID: G02-AUTH_TIMEOUT-Q026
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A record lock held by an expired session must not persist in a way that blocks legitimate
  access indefinitely with no automatic recovery path.
WHY_IT_MATTERS: >
  A permanently stuck lock from a dead session becomes an operational incident requiring
  manual intervention every time it happens.
DISCONFIRMING_OBSERVATION: >
  A lock from an expired session remains in place with no automatic recovery mechanism,
  requiring manual intervention to clear.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Acquire a lock, allow the owning session to expire, and observe whether and how the lock is
  eventually released without manual action.
```

## G02-AUTH_TIMEOUT-Q027

```yaml
QID: G02-AUTH_TIMEOUT-Q027
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the platform warns a user of imminent expiry, the mere display of that warning must not
  itself count as activity that resets the inactivity timer, unless the user takes an
  affirmative action in response.
WHY_IT_MATTERS: >
  A warning that silently extends the session on its own defeats the inactivity control it is
  meant to support.
DISCONFIRMING_OBSERVATION: >
  The inactivity timer is observed to reset purely because a warning was displayed, with no
  affirmative user response to it.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Allow a session to reach the point where an expiry warning appears, take no further action,
  and measure whether the timer resets regardless.
```

## G02-AUTH_TIMEOUT-Q028

```yaml
QID: G02-AUTH_TIMEOUT-Q028
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If an autosave mechanism exists for in-progress work, its saved state must not be purged or
  made unreachable purely as a consequence of the owning session's forced expiry.
WHY_IT_MATTERS: >
  Losing autosaved work at the same moment as session expiry defeats the purpose of having
  autosave at all.
DISCONFIRMING_OBSERVATION: >
  Autosaved in-progress work becomes permanently unreachable specifically because the session
  that created it has expired.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Trigger autosave of in-progress work, allow the owning session to expire, then
  re-authenticate and check whether the autosaved work is still reachable.
```

## G02-AUTH_TIMEOUT-Q029

```yaml
QID: G02-AUTH_TIMEOUT-Q029
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A session established through delegated or federated authentication must be subject to the
  same local timeout policy as a session established with local credentials, unless a
  difference is an explicit, documented decision.
WHY_IT_MATTERS: >
  An undocumented difference in timeout behaviour by authentication origin creates an
  inconsistent security posture across otherwise-equivalent sessions.
DISCONFIRMING_OBSERVATION: >
  A session established via a delegated or federated method has different observed timeout
  behaviour than a locally authenticated session, with no documented decision authorizing the
  difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Establish sessions via each available authentication origin under the same tenant and
  compare their actual timeout behaviour.
```

## G02-AUTH_TIMEOUT-Q030

```yaml
QID: G02-AUTH_TIMEOUT-Q030
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Any difference in effective session duration correlated with a user's role must trace to an
  explicit, documented governance decision rather than an incidental configuration
  difference.
WHY_IT_MATTERS: >
  An accidental role-correlated difference in session duration is a policy nobody actually
  decided on, and elevated roles are the worst place for that to be true.
DISCONFIRMING_OBSERVATION: >
  Sessions under different roles are found to have different effective timeout durations with
  no documented decision explaining the difference.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Compare the actual observed timeout duration for sessions under at least two different roles
  within the same tenant configuration.
```

## G02-AUTH_TIMEOUT-Q031

```yaml
QID: G02-AUTH_TIMEOUT-Q031
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where both a platform-wide default and a tenant-specific timeout configuration exist, which
  one governs a given session must be deterministic and consistent, not dependent on
  unrelated factors such as which surface or path established the session.
WHY_IT_MATTERS: >
  A non-deterministic precedence rule means the effective timeout for a given tenant cannot be
  reliably stated or verified.
DISCONFIRMING_OBSERVATION: >
  Sessions established for the same tenant through different surfaces or paths are found to be
  governed by different timeout values despite identical tenant configuration.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Establish sessions for one tenant through more than one surface or path and compare which
  timeout value actually governs each.
```

## G02-AUTH_TIMEOUT-Q032

```yaml
QID: G02-AUTH_TIMEOUT-Q032
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Entitlements or permissions relevant to an action must be evaluated at the time of that
  action, not solely trusted from what was cached at session start, for the duration up until
  timeout.
WHY_IT_MATTERS: >
  A long window of trusting stale cached permissions creates a gap where a revoked or reduced
  entitlement remains effectively usable until the session happens to expire.
DISCONFIRMING_OBSERVATION: >
  An entitlement revoked partway through a still-active session continues to be honored for
  actions taken later in that same session, before timeout.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Revoke or reduce an entitlement partway through an active session and attempt an action
  depending on that entitlement before the session would otherwise time out.
```

## G02-AUTH_TIMEOUT-Q033

```yaml
QID: G02-AUTH_TIMEOUT-Q033
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A background job enqueued by a session before it expires must retain accurate, auditable
  identity and context information for the work it performs, independent of whether the
  initiating session still exists by the time it runs.
WHY_IT_MATTERS: >
  A background job that loses or misattributes its originating identity after the session
  ends breaks the audit trail for anything that job does.
DISCONFIRMING_OBSERVATION: >
  A background job's audit record misattributes, loses, or cannot establish the identity and
  context under which it was originally enqueued, once the initiating session has expired.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Enqueue a background job from a session, let the session expire before the job completes,
  and inspect the audit record the job produces.
```

## G02-AUTH_TIMEOUT-Q034

```yaml
QID: G02-AUTH_TIMEOUT-Q034
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If a stricter timeout applies to a sensitive area accessed within a broader session, that
  stricter timeout must actually take effect independently and must not be silently overridden
  by the general session's longer timeout.
WHY_IT_MATTERS: >
  A stricter control that is silently overridden by a looser general setting provides no
  actual protection while appearing to.
DISCONFIRMING_OBSERVATION: >
  Access to the sensitive area remains available past its stated stricter timeout, governed
  instead by the general session's longer duration.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Access a sensitive area with a documented stricter timeout, remain idle within it past that
  stricter duration but within the general session duration, and observe whether access is
  actually cut off.
```

## G02-AUTH_TIMEOUT-Q035

```yaml
QID: G02-AUTH_TIMEOUT-Q035
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A server-side clock adjustment, such as a daylight-saving transition or a
  time-synchronization correction, must not cause an active session to expire earlier or
  later than its configured duration in real elapsed terms.
WHY_IT_MATTERS: >
  A clock-change-induced expiry anomaly is a source of unpredictable, hard-to-reproduce
  incidents tied to a specific date or time rather than to actual session duration.
DISCONFIRMING_OBSERVATION: >
  A session's actual expiry, measured in real elapsed time, is observably shifted around a
  server clock adjustment event compared to sessions unaffected by such an event.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare the real elapsed expiry duration of sessions active across a clock-adjustment event
  against sessions of the same configured duration not spanning such an event.
```

## G02-AUTH_TIMEOUT-Q036

```yaml
QID: G02-AUTH_TIMEOUT-Q036
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a client device is suspended and later resumed, the real elapsed wall-clock time during
  suspension must be counted toward inactivity in the same way it would be for a device that
  stayed continuously awake but idle.
WHY_IT_MATTERS: >
  If suspension time is not counted, a session could remain effectively alive far longer than
  intended simply because the device was asleep rather than idle.
DISCONFIRMING_OBSERVATION: >
  A session that spans a period of device suspension is found to still be valid upon resume,
  despite the total elapsed wall-clock time exceeding the inactivity limit.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Establish a session, suspend the client device for longer than the inactivity limit, resume
  it, and observe whether the session is still considered valid.
```
## G02-AUTH_TIMEOUT-Q037

```yaml
QID: G02-AUTH_TIMEOUT-Q037
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  No combination of automatic silent renewal mechanisms available to a client must be able to
  extend a session past its stated absolute limit.
WHY_IT_MATTERS: >
  If silent renewal can defeat the absolute limit, the stated absolute limit is fiction and
  the actual maximum session life is unbounded.
DISCONFIRMING_OBSERVATION: >
  A session maintained purely through automatic silent renewal, with no further genuine user
  action, is found to remain valid past its stated absolute limit.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Maintain a session using only its available automatic renewal mechanisms, with no genuine
  user interaction, past the configured absolute limit, and observe whether it remains valid.
```

## G02-AUTH_TIMEOUT-Q038

```yaml
QID: G02-AUTH_TIMEOUT-Q038
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The response given to a client whose session has naturally expired must be distinguishable,
  at least in the audit trail if not to the end user, from the response given when a session
  was explicitly force-terminated by an administrator.
WHY_IT_MATTERS: >
  Without this distinction, an investigation cannot tell whether a session ended through
  routine policy or through a deliberate administrative action, which is a materially
  different event.
DISCONFIRMING_OBSERVATION: >
  A naturally expired session and an administrator-force-terminated session produce records
  that cannot be distinguished after the fact.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Produce one naturally expired session and one administrator-terminated session and compare
  what is recorded for each.
```

## G02-AUTH_TIMEOUT-Q039

```yaml
QID: G02-AUTH_TIMEOUT-Q039
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a session is forcibly terminated, its outstanding background work must be handled by an
  explicit, defined rule — terminated, allowed to complete under clearly recorded authority,
  or otherwise — not left in an undefined state.
WHY_IT_MATTERS: >
  An undefined outcome for outstanding work at forced termination is precisely the scenario a
  security-driven termination is trying to prevent from continuing unmonitored.
DISCONFIRMING_OBSERVATION: >
  Outstanding background work from a forcibly terminated session is found to continue with no
  clear, recorded rule governing whether and under what authority it does so.
EXPECTED_SURFACE: S4,S6,S8
PRECONDITIONS: >
  Initiate background work from a session, forcibly terminate that session by an
  administrative or security action, and inspect what happens to the outstanding work and its
  recorded authority.
```

## G02-AUTH_TIMEOUT-Q040

```yaml
QID: G02-AUTH_TIMEOUT-Q040
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The timeout treatment of a session must not differ based solely on whether the session's
  current activity is read-only versus holding a lock or reservation on a resource, unless
  that difference is an explicit, documented design.
WHY_IT_MATTERS: >
  An undocumented difference here could either release a lock prematurely during legitimate
  ongoing work, or keep a lock alive far longer than a read-only session would be permitted to
  remain idle.
DISCONFIRMING_OBSERVATION: >
  A session holding a lock is observed to time out on a different schedule than an otherwise
  identical read-only session, with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Compare the actual timeout behaviour of a session performing only read-only activity against
  one holding a lock, under otherwise identical idle conditions.
```

## G02-AUTH_TIMEOUT-Q041

```yaml
QID: G02-AUTH_TIMEOUT-Q041
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Any mechanism that keeps a session alive during a long, legitimate multi-step operation must
  be an intentional, documented allowance, not an accidental side effect of unrelated calls
  the operation happens to make.
WHY_IT_MATTERS: >
  An accidental allowance is not something anyone can rely on, verify, or govern, even though
  it may currently produce a convenient result.
DISCONFIRMING_OBSERVATION: >
  A session is kept alive during a long operation by calls unrelated to session maintenance,
  with no documented design establishing this as an intended allowance.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Perform a long multi-step legitimate operation without any explicit keep-alive action and
  determine which calls, if any, are actually keeping the session alive.
```

## G02-AUTH_TIMEOUT-Q042

```yaml
QID: G02-AUTH_TIMEOUT-Q042
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether concurrent sessions for one identity share a single absolute-limit clock or run
  independent clocks per session must be a consistent, defined behaviour.
WHY_IT_MATTERS: >
  An inconsistent answer here means the actual maximum session lifetime for a user with
  multiple devices cannot be reliably stated.
DISCONFIRMING_OBSERVATION: >
  Concurrent sessions for the same identity are found to expire according to inconsistent
  combinations of shared and independent absolute-limit clocks.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Establish two concurrent sessions for one identity at different start times and observe
  whether their absolute expiry points are independent or tied together.
```

## G02-AUTH_TIMEOUT-Q043

```yaml
QID: G02-AUTH_TIMEOUT-Q043
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If timeout durations are changed while a session is active, the audit trail must be able to
  show which policy version actually governed that session's eventual termination.
WHY_IT_MATTERS: >
  Without this, an investigation into an unexpectedly early or late termination cannot
  determine whether a mid-session policy change was the cause.
DISCONFIRMING_OBSERVATION: >
  A session that spans a policy change terminates in a way that cannot be attributed, from the
  audit trail, to either the old or new policy version.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Change the timeout configuration while a session is active, allow it to terminate, and
  attempt to determine from the audit trail which policy version governed the termination.
```

## G02-AUTH_TIMEOUT-Q044

```yaml
QID: G02-AUTH_TIMEOUT-Q044
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If a non-interactive service or integration account's session is exempt from the inactivity
  timeout, that exemption must be an explicit, documented policy rather than an incidental
  effect of how such sessions happen to be implemented.
WHY_IT_MATTERS: >
  An undocumented exemption is a standing, unreviewed gap in the timeout control that nobody
  has actually approved.
DISCONFIRMING_OBSERVATION: >
  A non-interactive service session is found to be exempt from the inactivity timeout with no
  documented policy establishing that exemption.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Establish a non-interactive service/integration session, leave it idle past the interactive
  inactivity limit, and determine whether an exemption exists and whether it is documented.
```

## G02-AUTH_TIMEOUT-Q045

```yaml
QID: G02-AUTH_TIMEOUT-Q045
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Reducing the configured timeout duration must have a defined, consistent effect on sessions
  already active beyond the new, shorter limit — either immediate termination or application
  only to future activity checks — not an inconsistent mix of both.
WHY_IT_MATTERS: >
  An inconsistent effect means administrators cannot predict the actual security benefit of
  tightening the policy, nor can users predict when they will be logged out.
DISCONFIRMING_OBSERVATION: >
  Sessions already active beyond a newly reduced limit are affected inconsistently, some
  terminated immediately and others not, under otherwise identical conditions.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Establish sessions, reduce the configured timeout to below their current elapsed duration,
  and observe whether and when each is affected.
```

## G02-AUTH_TIMEOUT-Q046

```yaml
QID: G02-AUTH_TIMEOUT-Q046
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether a session that has crossed the inactivity threshold is proactively terminated at
  that moment or only recognized as expired when next used must be a consistent, defined
  behaviour, observable the same way every time.
WHY_IT_MATTERS: >
  An inconsistent answer here affects whether resources like locks are released promptly or
  only whenever the expired session happens to be touched again, with real operational
  consequences either way.
DISCONFIRMING_OBSERVATION: >
  Repeating the same idle-past-threshold scenario produces inconsistent results as to whether
  the session is already terminated versus still appearing valid until next touched.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Let a session cross the inactivity threshold without further use, wait, and then check its
  state through more than one means, such as a status check versus an actual action, to see if
  the answer is consistent.
```

## G02-AUTH_TIMEOUT-Q047

```yaml
QID: G02-AUTH_TIMEOUT-Q047
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The audit trail must be able to distinguish, for any given session's end, among at least
  reaching the absolute limit, reaching the inactivity limit, and explicit administrative
  termination, as three separate recorded causes.
WHY_IT_MATTERS: >
  Collapsing these into a single generic "ended" event removes the ability to diagnose
  patterns such as a role being disproportionately affected by one cause over another.
DISCONFIRMING_OBSERVATION: >
  Two or more of these three distinct termination causes are recorded identically or
  ambiguously in the audit trail, such that they cannot be told apart afterward.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Deliberately produce one session ending by each of the three causes and compare what the
  audit trail records for each.
```

## G02-AUTH_TIMEOUT-Q048

```yaml
QID: G02-AUTH_TIMEOUT-Q048
MODULE: auth_timeout
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A user's response to an imminent-expiry prompt, choosing to extend the session, must be
  authenticated and authorized to the same standard as any other session-extending action, not
  treated as a lower-trust special case.
WHY_IT_MATTERS: >
  If the extension response bypasses normal checks, it becomes a distinct, potentially weaker
  path to keeping a session alive indefinitely.
DISCONFIRMING_OBSERVATION: >
  The mechanism used to respond to an expiry-warning prompt succeeds in extending the session
  through a path that would not independently satisfy the same authentication or authorization
  check applied to ordinary actions.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Trigger an expiry warning, respond to it through the normal mechanism, and separately
  attempt to replay or forge that same extension response outside the normal flow.
```
