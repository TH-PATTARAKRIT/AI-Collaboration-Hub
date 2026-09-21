# SMEsPlus ENTERPRISE SUITE
## GMVQ — G01 PLATFORM_BASE / portal Module Adversarial MVQ Bank

**Document ID:** GMVQ-G01-PORTAL-MVQ40-V1.00  
**Group:** G01 PLATFORM_BASE  
**Module Metadata:** `portal`  
**Destination:** SAAS_FOUNDATION  
**Authoring Team:** OVQDT / GMVQ  
**Status:** DRAFT / AUTHORING COMPLETE / PENDING ROLLING FREEZE  
**Standing Authorization:** Boss APPROVE ALL — continuous GMVQ authoring and rolling freeze  
**Lane A / Lane B:** NOT STARTED until this bank is frozen

## Control
Behavioral/source-neutral questions only. Every question is falsifiable. No question count is Formal Coverage.


## G01-PORTAL-Q001

```yaml
QID: G01-PORTAL-Q001
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An external user can reach only records explicitly shared with their authorized identity and customer context.
WHY_IT_MATTERS: >
  External access must not weaken the primary SaaS boundary.
DISCONFIRMING_OBSERVATION: >
  An external user opens, searches, downloads or acts on a record belonging only to another customer or unrelated account.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Create distinguishable shared and unshared records across two independent customer contexts.
```

## G01-PORTAL-Q002

```yaml
QID: G01-PORTAL-Q002
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Direct knowledge of a record address or identifier does not bypass external-user authorization.
WHY_IT_MATTERS: >
  Predictable identifiers must not become sharing credentials.
DISCONFIRMING_OBSERVATION: >
  Changing or reusing an identifier opens a protected record that is absent from the user's normal navigation.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Record permitted and restricted identifiers, then attempt direct navigation from the restricted account.
```

## G01-PORTAL-Q003

```yaml
QID: G01-PORTAL-Q003
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Revoking external access takes effect across open tabs, saved links, cached pages, downloads and deferred actions.
WHY_IT_MATTERS: >
  External sessions often remain open for long periods.
DISCONFIRMING_OBSERVATION: >
  A revoked external user can still read or change protected data through a path prepared before revocation.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Open multiple access paths, revoke access, then exercise each without regranting.
```

## G01-PORTAL-Q004

```yaml
QID: G01-PORTAL-Q004
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A share or access credential is scoped to the intended record/action and does not grant broader customer access.
WHY_IT_MATTERS: >
  Bearer-style access links must be least-privilege.
DISCONFIRMING_OBSERVATION: >
  One shared link reveals sibling records, other documents, unrelated attachments or broader customer navigation.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Create a controlled shared link for one record and probe neighboring resources.
```

## G01-PORTAL-Q005

```yaml
QID: G01-PORTAL-Q005
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A temporary external access credential expires and revokes according to a deterministic policy.
WHY_IT_MATTERS: >
  Long-lived bearer links become persistent unauthorized access.
DISCONFIRMING_OBSERVATION: >
  A link remains usable after expiry/revocation or behaves inconsistently across sessions.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Test one controlled link before and after expiry/revocation from fresh sessions.
```

## G01-PORTAL-Q006

```yaml
QID: G01-PORTAL-Q006
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Forwarding a shared link does not provide more authority than the sharing policy intended.
WHY_IT_MATTERS: >
  Forwardable links can escape the intended recipient.
DISCONFIRMING_OBSERVATION: >
  A different recipient obtains protected access when the policy required identity-bound access.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Open the same link from the intended identity and a separate controlled identity/device.
```

## G01-PORTAL-Q007

```yaml
QID: G01-PORTAL-Q007
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  External navigation exposes only menus, counters and shortcuts backed by currently permitted records.
WHY_IT_MATTERS: >
  Navigation metadata can leak hidden business activity.
DISCONFIRMING_OBSERVATION: >
  A menu badge, count, recent item or shortcut reveals the existence of protected records.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Generate hidden records with distinguishable counts and inspect external navigation.
```

## G01-PORTAL-Q008

```yaml
QID: G01-PORTAL-Q008
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Search and autocomplete for external users return only authorized records and values.
WHY_IT_MATTERS: >
  Search indexes are common leakage paths.
DISCONFIRMING_OBSERVATION: >
  Restricted names, identifiers, snippets or records appear in external search/suggestions.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Index distinctive values in permitted and restricted records and search from the external account.
```

## G01-PORTAL-Q009

```yaml
QID: G01-PORTAL-Q009
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Aggregates, totals and dashboards for external users are computed only from visible data.
WHY_IT_MATTERS: >
  A system can hide rows while leaking confidential totals.
DISCONFIRMING_OBSERVATION: >
  A total/count/graph changes because of records the external user cannot otherwise access.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Prepare visible and hidden records with materially different totals.
```

## G01-PORTAL-Q010

```yaml
QID: G01-PORTAL-Q010
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Attachments and generated documents inherit the same external access boundary as their parent record.
WHY_IT_MATTERS: >
  Files often remain accessible after record access is blocked.
DISCONFIRMING_OBSERVATION: >
  An external user retrieves a file, preview or generated document whose parent record they cannot access.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Attach distinctive files to protected records and probe all external file paths.
```

## G01-PORTAL-Q011

```yaml
QID: G01-PORTAL-Q011
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Previously downloaded or generated links are reauthorized when reused after access revocation where policy requires current authorization.
WHY_IT_MATTERS: >
  Long-lived download links can survive record revocation.
DISCONFIRMING_OBSERVATION: >
  A prior download link remains valid after the user loses access contrary to policy.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Generate link while authorized, revoke record access, reuse exact link from a fresh session.
```

## G01-PORTAL-Q012

```yaml
QID: G01-PORTAL-Q012
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  External comments or messages cannot be posted to records outside the user's authorized scope by altering hidden identifiers.
WHY_IT_MATTERS: >
  Write paths must enforce the same boundary as reads.
DISCONFIRMING_OBSERVATION: >
  A crafted comment/message attaches to another customer's protected record.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Use permitted and restricted target records and alter only the submitted target reference.
```

## G01-PORTAL-Q013

```yaml
QID: G01-PORTAL-Q013
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  External content is clearly attributable to the external actor and distinguishable from internal staff content.
WHY_IT_MATTERS: >
  Trust level matters for approvals and audit.
DISCONFIRMING_OBSERVATION: >
  An external post appears as internal/trusted staff activity or loses actor identity.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Create comparable external and internal comments and inspect audit/presentation.
```

## G01-PORTAL-Q014

```yaml
QID: G01-PORTAL-Q014
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  User-supplied external content remains inert and cannot execute active browser behavior for internal viewers.
WHY_IT_MATTERS: >
  Stored external content is untrusted.
DISCONFIRMING_OBSERVATION: >
  A crafted external value executes script, unsafe navigation or privileged browser action when staff view it.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Submit controlled active-content variants then view them under an internal test account.
```

## G01-PORTAL-Q015

```yaml
QID: G01-PORTAL-Q015
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An external user cannot alter ownership, company, customer, approval or other protected control fields through hidden request values.
WHY_IT_MATTERS: >
  Non-editable presentation is not authorization.
DISCONFIRMING_OBSERVATION: >
  Changing a hidden/control value in the request changes protected scope or lifecycle state.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Alter protected client-held values while performing an otherwise valid external edit.
```

## G01-PORTAL-Q016

```yaml
QID: G01-PORTAL-Q016
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Editable self-service fields are validated at the authoritative boundary, not only in the browser.
WHY_IT_MATTERS: >
  External requests are fully user-controlled.
DISCONFIRMING_OBSERVATION: >
  A value blocked by the visible form is accepted when the same supported request bypasses client validation.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Submit controlled invalid boundary values with and without client validation.
```

## G01-PORTAL-Q017

```yaml
QID: G01-PORTAL-Q017
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  External updates cannot silently approve, execute or post a business transaction when governance requires separate internal control.
WHY_IT_MATTERS: >
  Self-service must not collapse approval/execution/posting separation.
DISCONFIRMING_OBSERVATION: >
  An external edit directly creates final posted/approved effect without the required internal control stage.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform a controlled external update on a workflow that has internal approval/execution requirements.
```

## G01-PORTAL-Q018

```yaml
QID: G01-PORTAL-Q018
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Concurrent external and internal edits to the same record resolve deterministically without silent lost updates.
WHY_IT_MATTERS: >
  Customer and staff may work on the same object simultaneously.
DISCONFIRMING_OBSERVATION: >
  One save silently overwrites the other's committed changes with no conflict or audit evidence.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Open same record externally and internally, edit overlapping values, save nearly simultaneously.
```

## G01-PORTAL-Q019

```yaml
QID: G01-PORTAL-Q019
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing external user's customer/contact relationship re-evaluates all record access instead of preserving stale inherited access.
WHY_IT_MATTERS: >
  Relationship-based access can become stale.
DISCONFIRMING_OBSERVATION: >
  A user moved to another customer/contact context retains records from the former relationship.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Grant access through a relationship, change that relationship, then retest old records.
```

## G01-PORTAL-Q020

```yaml
QID: G01-PORTAL-Q020
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A shared contact identity used across multiple companies/customers does not collapse otherwise separate record access.
WHY_IT_MATTERS: >
  Shared identities must not imply shared tenancy.
DISCONFIRMING_OBSERVATION: >
  The same identity sees private records from multiple unrelated customer contexts without explicit separate memberships.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Use one controlled identity associated to distinguishable customer contexts and test active context boundaries.
```

## G01-PORTAL-Q021

```yaml
QID: G01-PORTAL-Q021
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Archived or closed records remain externally visible or hidden according to an explicit lifecycle rule.
WHY_IT_MATTERS: >
  Lifecycle state must not unexpectedly change confidentiality.
DISCONFIRMING_OBSERVATION: >
  Archiving/closing makes a previously private record public or removes required historical access without policy.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Compare external access before and after controlled archive/close transitions.
```

## G01-PORTAL-Q022

```yaml
QID: G01-PORTAL-Q022
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting a parent record does not leave orphan external links or files usable unless retention policy explicitly allows it.
WHY_IT_MATTERS: >
  Orphan links can become uncontrolled access channels.
DISCONFIRMING_OBSERVATION: >
  An external user accesses content through an old link after the parent is removed contrary to policy.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Create external links/files, delete parent in controlled environment, then reuse old links.
```

## G01-PORTAL-Q023

```yaml
QID: G01-PORTAL-Q023
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  External account switch or logout clears prior customer-specific cached pages and local state.
WHY_IT_MATTERS: >
  Shared devices are common for external access.
DISCONFIRMING_OBSERVATION: >
  After logout/account switch, protected data from the prior user is revealed through back navigation/cache/local state.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  View protected data, logout, log in as another user, then inspect browser history/cache behavior.
```

## G01-PORTAL-Q024

```yaml
QID: G01-PORTAL-Q024
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Session timeout during an external state-changing action leaves a knowable atomic outcome.
WHY_IT_MATTERS: >
  Ambiguous outcomes cause duplicate customer actions.
DISCONFIRMING_OBSERVATION: >
  Some effects commit while others do not, or retry after timeout creates a duplicate durable effect.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Force expiry/timeout near final submission of a controlled state-changing action.
```

## G01-PORTAL-Q025

```yaml
QID: G01-PORTAL-Q025
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Repeated external submission caused by double-click, refresh or retry is idempotent for one-time effects.
WHY_IT_MATTERS: >
  Customers often retry when feedback is slow.
DISCONFIRMING_OBSERVATION: >
  One intended action creates duplicate requests/documents/messages with no warning.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Repeat the same supported submission through double-click/refresh/retry.
```

## G01-PORTAL-Q026

```yaml
QID: G01-PORTAL-Q026
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  External bulk download or print paths enforce per-record authorization rather than trusting the visible list.
WHY_IT_MATTERS: >
  Bulk paths can bypass individual checks.
DISCONFIRMING_OBSERVATION: >
  A package/export/print contains at least one record or field the external user cannot open individually.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Prepare mixed permitted/restricted records and exercise every supported bulk output.
```

## G01-PORTAL-Q027

```yaml
QID: G01-PORTAL-Q027
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  External notification links resolve under current authorization and do not themselves reveal protected data before access is checked.
WHY_IT_MATTERS: >
  Notification channels may leave the application boundary.
DISCONFIRMING_OBSERVATION: >
  A link, subject or preview reveals protected record details to a recipient lacking current access.
EXPECTED_SURFACE: S1,S4,S5
PRECONDITIONS: >
  Queue notification, revoke recipient access, then inspect message and link behavior.
```

## G01-PORTAL-Q028

```yaml
QID: G01-PORTAL-Q028
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A queued external notification revalidates the intended recipient/customer context at delivery according to policy.
WHY_IT_MATTERS: >
  Deferred delivery can outlive membership changes.
DISCONFIRMING_OBSERVATION: >
  A user removed from the customer context still receives protected content at delivery.
EXPECTED_SURFACE: S4,S5,S6
PRECONDITIONS: >
  Queue notification, change membership before delivery, then process it.
```

## G01-PORTAL-Q029

```yaml
QID: G01-PORTAL-Q029
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Personalization or localization of external pages changes presentation only, not authorization or stored business truth.
WHY_IT_MATTERS: >
  Locale must not become a security or data-integrity input.
DISCONFIRMING_OBSERVATION: >
  Changing language/timezone makes a protected action available or changes stored value unexpectedly.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Use two locales/timezones on the same permitted record and compare authorization/state.
```

## G01-PORTAL-Q030

```yaml
QID: G01-PORTAL-Q030
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A portal-specific route does not provide weaker authorization than the equivalent internal route for the same record.
WHY_IT_MATTERS: >
  Alternate presentation layers must share security semantics.
DISCONFIRMING_OBSERVATION: >
  The external route exposes or changes a record that equivalent authorization would block elsewhere.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Compare matched access to the same protected record through supported internal/external paths.
```

## G01-PORTAL-Q031

```yaml
QID: G01-PORTAL-Q031
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Error pages do not disclose protected object existence, internal identifiers or staff-only details.
WHY_IT_MATTERS: >
  External users can probe arbitrary inputs.
DISCONFIRMING_OBSERVATION: >
  Differences in errors reliably reveal that a hidden record/user exists or expose internal implementation/data.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Probe known restricted and guaranteed nonexistent identifiers with the same external user.
```

## G01-PORTAL-Q032

```yaml
QID: G01-PORTAL-Q032
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  One external customer's high-volume downloads/search/refresh traffic cannot starve unrelated customers without protective controls.
WHY_IT_MATTERS: >
  External endpoints are noisy-neighbor surfaces.
DISCONFIRMING_OBSERVATION: >
  Load from Customer A causes sustained critical failure or correctness problems for Customer B.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Generate controlled high load in one context while running a stable reference scenario in another.
```

## G01-PORTAL-Q033

```yaml
QID: G01-PORTAL-Q033
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Protective rate limits are scoped so abusive external traffic is contained without globally blocking unrelated customers.
WHY_IT_MATTERS: >
  Bad rate-limit scope can create cross-tenant denial of service.
DISCONFIRMING_OBSERVATION: >
  One customer's threshold causes unrelated customers to be throttled.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Drive one context to limit while measuring low-rate traffic in another.
```

## G01-PORTAL-Q034

```yaml
QID: G01-PORTAL-Q034
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A restore or migration preserves external sharing boundaries, revoked links and account relationships.
WHY_IT_MATTERS: >
  Recovery tooling can bypass application controls.
DISCONFIRMING_OBSERVATION: >
  A restored/migrated user regains revoked access or a protected link becomes valid in the wrong scope.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Capture access before changes, revoke it, perform controlled restore/migration, then retest.
```

## G01-PORTAL-Q035

```yaml
QID: G01-PORTAL-Q035
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cloned non-production environment does not expose real customer external links or send live notifications without explicit isolation.
WHY_IT_MATTERS: >
  Clones can accidentally interact with customers.
DISCONFIRMING_OBSERVATION: >
  Test/staging produces usable links to real protected data or sends to live recipients.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Clone controlled configuration with safe interception and inspect external destinations/links.
```

## G01-PORTAL-Q036

```yaml
QID: G01-PORTAL-Q036
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  External user profile changes that affect identity or routing require appropriate verification and audit.
WHY_IT_MATTERS: >
  Self-service identity changes can enable takeover.
DISCONFIRMING_OBSERVATION: >
  A user changes a controlling identifier/destination and retains full access without required verification/evidence.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Change a controlled external account's primary identity/contact destination and withhold verification.
```

## G01-PORTAL-Q037

```yaml
QID: G01-PORTAL-Q037
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  External users cannot invite or delegate access beyond the scope and authority explicitly granted to them.
WHY_IT_MATTERS: >
  Delegation can become privilege propagation.
DISCONFIRMING_OBSERVATION: >
  A user creates a new external member with broader access than their own authorized delegation rights.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Exercise all supported sharing/delegation paths from a narrowly authorized external user.
```

## G01-PORTAL-Q038

```yaml
QID: G01-PORTAL-Q038
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Every material external access grant, revoke and self-service change is auditable with actor and time.
WHY_IT_MATTERS: >
  Customer-facing changes can drive contractual disputes.
DISCONFIRMING_OBSERVATION: >
  A material external access/state change has no durable attributable evidence.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Perform grant, revoke and self-service changes with distinct actors and inspect history.
```

## G01-PORTAL-Q039

```yaml
QID: G01-PORTAL-Q039
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Equivalent external paths—navigation, direct link, notification link, search, download and self-service action—converge on the same authorization boundary.
WHY_IT_MATTERS: >
  Path divergence is the core risk of external access.
DISCONFIRMING_OBSERVATION: >
  One supported path exposes or changes protected data that another correctly blocks.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Execute matched access attempts through every supported external entry path.
```

## G01-PORTAL-Q040

```yaml
QID: G01-PORTAL-Q040
MODULE: portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  External access remains a view/action layer over authoritative business state and cannot create an independent contradictory source of truth.
WHY_IT_MATTERS: >
  Self-service must reconcile to the governed source module.
DISCONFIRMING_OBSERVATION: >
  External UI reports a final state or value that contradicts authoritative business state with no pending/reconciliation explanation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cause controlled concurrent or interrupted changes and compare external display to authoritative state.
```

---
**Disposition:** AUTHORING COMPLETE / STRUCTURAL QA NEXT
