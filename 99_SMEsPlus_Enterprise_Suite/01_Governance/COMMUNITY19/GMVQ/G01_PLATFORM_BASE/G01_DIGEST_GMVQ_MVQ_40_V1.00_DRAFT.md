# SMEsPlus ENTERPRISE SUITE
## GMVQ — G01 PLATFORM_BASE / digest Module Adversarial MVQ Bank

**Document ID:** GMVQ-G01-DIGEST-MVQ40-V1.00  
**Group:** G01 PLATFORM_BASE  
**Module Metadata:** `digest`  
**Destination:** SAAS_FOUNDATION  
**Authoring Team:** OVQDT / GMVQ  
**Status:** DRAFT / AUTHORING COMPLETE / PENDING ROLLING FREEZE  
**Standing Authorization:** Boss APPROVE ALL — continuous GMVQ authoring and rolling freeze  
**Lane A / Lane B:** NOT STARTED until this bank is frozen

## Control
Behavioral/source-neutral questions only. Every question is falsifiable. No question count is Formal Coverage.


## G01-DIGEST-Q001

```yaml
QID: G01-DIGEST-Q001
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A periodic summary sent to a user contains only metrics and records currently authorized for that user and business scope.
WHY_IT_MATTERS: >
  Summaries can leak aggregate data even when raw rows are protected.
DISCONFIRMING_OBSERVATION: >
  A recipient sees a metric, name, count or value attributable to data they cannot otherwise access.
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: >
  Prepare distinguishable permitted and restricted data, then generate a summary for a restricted user.
```

## G01-DIGEST-Q002

```yaml
QID: G01-DIGEST-Q002
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Aggregate values in a periodic summary are computed only from the recipient's permitted customer/company context.
WHY_IT_MATTERS: >
  Cross-company totals are confidential even without row details.
DISCONFIRMING_OBSERVATION: >
  A total changes because of records from another company/customer the recipient cannot access.
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: >
  Create materially different totals in two scopes and compare recipient summaries.
```

## G01-DIGEST-Q003

```yaml
QID: G01-DIGEST-Q003
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  The summary has an explicit as-of/cutoff time so late-arriving data is treated deterministically.
WHY_IT_MATTERS: >
  Without cutoff semantics, metrics cannot be reconciled.
DISCONFIRMING_OBSERVATION: >
  Two runs for the same stated period include different records solely because processing time differed, with no cutoff evidence.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Create records immediately around the scheduled cutoff and compare repeated controlled runs.
```

## G01-DIGEST-Q004

```yaml
QID: G01-DIGEST-Q004
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Scheduling uses a defined business timezone and handles daylight/time-boundary changes deterministically.
WHY_IT_MATTERS: >
  Periodic summaries are date-sensitive.
DISCONFIRMING_OBSERVATION: >
  The same configured schedule maps to unintended business dates or fires twice/misses solely due to timezone handling.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Use controlled timezone/date-boundary cases around schedule execution.
```

## G01-DIGEST-Q005

```yaml
QID: G01-DIGEST-Q005
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing company/customer context for a multi-scope user does not cause one summary to mix metrics from parallel contexts unless explicitly configured.
WHY_IT_MATTERS: >
  Multi-scope membership is not multi-scope execution context.
DISCONFIRMING_OBSERVATION: >
  One summary silently combines unrelated scopes without an explicit cross-scope report rule.
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: >
  Use one user with memberships in two isolated scopes and generate context-specific summaries.
```

## G01-DIGEST-Q006

```yaml
QID: G01-DIGEST-Q006
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Each metric has a stable business definition and can be reconciled to underlying authoritative data.
WHY_IT_MATTERS: >
  Pretty numbers without definition are not evidence.
DISCONFIRMING_OBSERVATION: >
  A displayed metric cannot be reproduced from the underlying records or changes meaning without a defined version.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Select representative metrics and independently reconstruct them from authoritative data.
```

## G01-DIGEST-Q007

```yaml
QID: G01-DIGEST-Q007
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cached summary values never broaden visibility when a recipient loses access.
WHY_IT_MATTERS: >
  Cached aggregates can leak revoked information.
DISCONFIRMING_OBSERVATION: >
  After access reduction, a newly generated summary still includes a previously visible protected metric.
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: >
  Generate summary with broad access, revoke access, regenerate after cache boundary.
```

## G01-DIGEST-Q008

```yaml
QID: G01-DIGEST-Q008
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Empty and zero-data conditions are distinguishable from processing failure.
WHY_IT_MATTERS: >
  A missing number should not be mistaken for zero business activity.
DISCONFIRMING_OBSERVATION: >
  A failed metric is presented as zero/empty with no error or uncertainty indication.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Force one metric source to fail while another valid metric is truly zero.
```

## G01-DIGEST-Q009

```yaml
QID: G01-DIGEST-Q009
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A failed summary run does not send a partially inconsistent mixture of old and new metrics without explicit stale-data labeling.
WHY_IT_MATTERS: >
  Mixed snapshots mislead management.
DISCONFIRMING_OBSERVATION: >
  Some metrics are current and others silently reused from prior runs with no trace.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Force a late-stage metric failure after earlier metrics have computed.
```

## G01-DIGEST-Q010

```yaml
QID: G01-DIGEST-Q010
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Retrying a failed summary delivery does not send duplicate messages or duplicate downstream actions.
WHY_IT_MATTERS: >
  Delivery retries are normal.
DISCONFIRMING_OBSERVATION: >
  One logical summary is delivered multiple times because the first outcome was ambiguous.
EXPECTED_SURFACE: S5,S6
PRECONDITIONS: >
  Force an ambiguous delivery failure and allow automatic retry.
```

## G01-DIGEST-Q011

```yaml
QID: G01-DIGEST-Q011
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A recipient removed from the organization/customer before delivery does not receive protected scheduled summaries.
WHY_IT_MATTERS: >
  Queued delivery can outlive authorization.
DISCONFIRMING_OBSERVATION: >
  A removed/deactivated recipient still receives a protected summary after revocation.
EXPECTED_SURFACE: S4,S5,S6
PRECONDITIONS: >
  Queue/generate summary, revoke recipient access before delivery.
```

## G01-DIGEST-Q012

```yaml
QID: G01-DIGEST-Q012
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Recipient preferences or unsubscribe settings are evaluated according to a clear effective time.
WHY_IT_MATTERS: >
  Preference races can cause unwanted or missing communications.
DISCONFIRMING_OBSERVATION: >
  A preference change near generation/delivery yields inconsistent outcome with no defined rule.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Change summary preference around the scheduled run boundary.
```

## G01-DIGEST-Q013

```yaml
QID: G01-DIGEST-Q013
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A user cannot subscribe another unauthorized person to protected summaries without required authority.
WHY_IT_MATTERS: >
  Subscription configuration is an access grant.
DISCONFIRMING_OBSERVATION: >
  A low-privilege user adds an external/unrelated recipient who then receives protected metrics.
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: >
  Attempt subscription changes under narrow roles and with cross-scope recipients.
```

## G01-DIGEST-Q014

```yaml
QID: G01-DIGEST-Q014
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  A summary link opens underlying detail only if the recipient currently has permission at click time.
WHY_IT_MATTERS: >
  Email possession must not replace application authorization.
DISCONFIRMING_OBSERVATION: >
  A recipient who lost access can open protected detail from an old summary link.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Generate link while authorized, revoke access, then click from a fresh session.
```

## G01-DIGEST-Q015

```yaml
QID: G01-DIGEST-Q015
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A summary message itself does not include protected details that the recipient would be denied when opening the application.
WHY_IT_MATTERS: >
  Outbound content is outside the application boundary.
DISCONFIRMING_OBSERVATION: >
  The message body/attachment contains protected row-level data beyond the recipient's current access.
EXPECTED_SURFACE: S1,S4,S5
PRECONDITIONS: >
  Compare summary content with recipient's permitted detail view.
```

## G01-DIGEST-Q016

```yaml
QID: G01-DIGEST-Q016
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Metric personalization is isolated per recipient and does not reuse rendered private values from another recipient.
WHY_IT_MATTERS: >
  Batch rendering can cross-contaminate data.
DISCONFIRMING_OBSERVATION: >
  Recipient B receives a metric, name or link computed for Recipient A.
EXPECTED_SURFACE: S5,S6
PRECONDITIONS: >
  Batch-generate summaries for recipients with deliberately distinct data.
```

## G01-DIGEST-Q017

```yaml
QID: G01-DIGEST-Q017
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Dynamically generated attachments are produced under the intended recipient/company context for each delivery.
WHY_IT_MATTERS: >
  Attachment generation can leak whole reports.
DISCONFIRMING_OBSERVATION: >
  A recipient receives a report file generated for another company/customer.
EXPECTED_SURFACE: S4,S5,S6
PRECONDITIONS: >
  Generate multiple scope-specific attachments in one batch and compare.
```

## G01-DIGEST-Q018

```yaml
QID: G01-DIGEST-Q018
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Changing metric configuration during a long summary batch has a deterministic version boundary.
WHY_IT_MATTERS: >
  Mixed metric definitions make one batch irreconcilable.
DISCONFIRMING_OBSERVATION: >
  Early and late recipients in the same logical batch receive materially different definitions with no version trace.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Start multi-recipient run, change metric configuration mid-run.
```

## G01-DIGEST-Q019

```yaml
QID: G01-DIGEST-Q019
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Changing the schedule does not unexpectedly backfill or duplicate already completed periods unless catch-up is explicit.
WHY_IT_MATTERS: >
  Schedule edits should be prospective by rule.
DISCONFIRMING_OBSERVATION: >
  Editing frequency/time causes old periods to be resent or skipped unpredictably.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Complete scheduled run, change frequency/time, observe next executions.
```

## G01-DIGEST-Q020

```yaml
QID: G01-DIGEST-Q020
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  After downtime, missed summary runs follow an explicit catch-up policy and do not flood recipients or silently disappear.
WHY_IT_MATTERS: >
  Recovery from downtime is part of scheduling semantics.
DISCONFIRMING_OBSERVATION: >
  Overdue summaries are unpredictably lost or all sent at once with no stated policy.
EXPECTED_SURFACE: S5,S6
PRECONDITIONS: >
  Pause service through one or more scheduled times then recover.
```

## G01-DIGEST-Q021

```yaml
QID: G01-DIGEST-Q021
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  One customer's expensive summary computation cannot starve unrelated customers' scheduled reporting.
WHY_IT_MATTERS: >
  Shared reporting is a noisy-neighbor surface.
DISCONFIRMING_OBSERVATION: >
  A heavy Scope A summary causes sustained delay/failure in Scope B's normal summary.
EXPECTED_SURFACE: S5,S6
PRECONDITIONS: >
  Generate heavy controlled dataset in one scope while measuring another.
```

## G01-DIGEST-Q022

```yaml
QID: G01-DIGEST-Q022
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Protective limits for expensive summaries contain the heavy scope rather than globally disabling all customers.
WHY_IT_MATTERS: >
  Fairness controls must preserve tenant isolation.
DISCONFIRMING_OBSERVATION: >
  One scope hitting a limit blocks unrelated scopes' summaries.
EXPECTED_SURFACE: S5,S6
PRECONDITIONS: >
  Drive one scope to threshold while another remains normal.
```

## G01-DIGEST-Q023

```yaml
QID: G01-DIGEST-Q023
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Archived or deleted records affect historical versus current summary metrics according to an explicit rule.
WHY_IT_MATTERS: >
  Lifecycle changes can rewrite historical management reports.
DISCONFIRMING_OBSERVATION: >
  Archiving/deleting today silently changes a prior period's already-reported metric without a restatement rule.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Generate period summary, change record lifecycle later, reconstruct prior period.
```

## G01-DIGEST-Q024

```yaml
QID: G01-DIGEST-Q024
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Corrections to historical source data have a defined effect on previously delivered summaries and restatement evidence.
WHY_IT_MATTERS: >
  Management reports need reproducibility.
DISCONFIRMING_OBSERVATION: >
  A corrected source changes historical metric with no way to tell original versus restated result.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Deliver summary, correct underlying historical data, regenerate and compare.
```

## G01-DIGEST-Q025

```yaml
QID: G01-DIGEST-Q025
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Restoring an older snapshot does not resend previously delivered summaries as new without deduplication/reconciliation.
WHY_IT_MATTERS: >
  Recovery can duplicate outbound reporting.
DISCONFIRMING_OBSERVATION: >
  After restore, old logical runs are delivered again with no replay policy.
EXPECTED_SURFACE: S3,S5,S6
PRECONDITIONS: >
  Complete a summary, restore earlier checkpoint in controlled environment, observe scheduler.
```

## G01-DIGEST-Q026

```yaml
QID: G01-DIGEST-Q026
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cloned non-production environment cannot send real customer summaries unless explicitly isolated.
WHY_IT_MATTERS: >
  Clones frequently preserve schedules and recipients.
DISCONFIRMING_OBSERVATION: >
  Test/staging sends a summary to live destinations or links to live data.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Clone controlled configuration with safe mail interception and inspect destinations/links.
```

## G01-DIGEST-Q027

```yaml
QID: G01-DIGEST-Q027
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Summary generation and delivery create auditable evidence of run time, scope, definition/version and recipients.
WHY_IT_MATTERS: >
  Without run provenance, disputes cannot be reconstructed.
DISCONFIRMING_OBSERVATION: >
  A delivered summary cannot be tied to a specific run/scope/configuration/recipient set.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Generate controlled summaries and reconstruct run provenance from evidence.
```

## G01-DIGEST-Q028

```yaml
QID: G01-DIGEST-Q028
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A privileged configuration change to summary metrics or recipients is auditable and cannot be silently altered by ordinary users.
WHY_IT_MATTERS: >
  Summary configuration can disclose executive data.
DISCONFIRMING_OBSERVATION: >
  A low-privilege user changes sensitive metric/recipient configuration or the change leaves no durable trace.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Attempt configuration changes under different roles and inspect history.
```

## G01-DIGEST-Q029

```yaml
QID: G01-DIGEST-Q029
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Localization changes labels and formatting without changing the underlying metric amount or included record set.
WHY_IT_MATTERS: >
  Locale should not alter business truth.
DISCONFIRMING_OBSERVATION: >
  Changing locale changes metric value, inclusion set or authorization outcome.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate same summary for equivalent users with different locales.
```

## G01-DIGEST-Q030

```yaml
QID: G01-DIGEST-Q030
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Currency presentation identifies conversion basis and does not silently aggregate incompatible currencies as one number.
WHY_IT_MATTERS: >
  Mixed-currency totals can mislead decision makers.
DISCONFIRMING_OBSERVATION: >
  Amounts in different currencies are added without explicit conversion/basis or a displayed converted total cannot be reconciled.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Use controlled multi-currency records and reconstruct displayed totals.
```

## G01-DIGEST-Q031

```yaml
QID: G01-DIGEST-Q031
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A summary cannot reveal another user's private activity merely because the recipient is a manager or administrator unless that relationship explicitly grants it.
WHY_IT_MATTERS: >
  Role labels must not replace record-level authorization.
DISCONFIRMING_OBSERVATION: >
  A broad-role recipient sees private metrics outside the defined managerial/business scope.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Create private activity outside recipient's governed reporting scope and generate summary.
```

## G01-DIGEST-Q032

```yaml
QID: G01-DIGEST-Q032
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Changing reporting membership or team structure re-evaluates recipient metrics according to a defined effective point.
WHY_IT_MATTERS: >
  Organizational changes must not create unexplained historical drift.
DISCONFIRMING_OBSERVATION: >
  A current summary includes/excludes records based on stale membership with no effective-date rule.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Change team/reporting relationships around the cutoff and compare runs.
```

## G01-DIGEST-Q033

```yaml
QID: G01-DIGEST-Q033
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A saved or forwarded summary message does not function as an enduring authorization token to protected live detail.
WHY_IT_MATTERS: >
  Reports may be forwarded externally.
DISCONFIRMING_OBSERVATION: >
  A person with only the forwarded message can access protected application data without current authorization.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Forward a controlled summary to an unauthorized identity and test all embedded links.
```

## G01-DIGEST-Q034

```yaml
QID: G01-DIGEST-Q034
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Search/indexing of delivered summaries does not expose protected content to users lacking the original recipient authorization.
WHY_IT_MATTERS: >
  Stored outbound artifacts can become a secondary data store.
DISCONFIRMING_OBSERVATION: >
  A restricted user discovers summary content through application search/history/index.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Create summary with distinctive protected text then search from a restricted user.
```

## G01-DIGEST-Q035

```yaml
QID: G01-DIGEST-Q035
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting or deactivating a recipient stops future delivery and queued work according to explicit policy.
WHY_IT_MATTERS: >
  Stale recipient records can leak future data.
DISCONFIRMING_OBSERVATION: >
  A deactivated user continues receiving new summaries through previously queued schedules.
EXPECTED_SURFACE: S4,S5,S6
PRECONDITIONS: >
  Deactivate recipient before next generation/delivery.
```

## G01-DIGEST-Q036

```yaml
QID: G01-DIGEST-Q036
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Manual 'send now' and scheduled generation apply equivalent scope, metric and recipient controls.
WHY_IT_MATTERS: >
  Manual shortcuts must not be weaker than schedule paths.
DISCONFIRMING_OBSERVATION: >
  A manual send exposes broader data/recipients or uses different definitions without explicit policy.
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: >
  Generate matched summary manually and via schedule under same context.
```

## G01-DIGEST-Q037

```yaml
QID: G01-DIGEST-Q037
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Concurrent generation of the same period does not create contradictory or duplicate authoritative summaries without clear run identity.
WHY_IT_MATTERS: >
  Overlapping scheduler/manual runs can race.
DISCONFIRMING_OBSERVATION: >
  Two runs for the same period produce different untraceable values or duplicate delivery with no run distinction.
EXPECTED_SURFACE: S5,S6
PRECONDITIONS: >
  Trigger manual and scheduled generation nearly simultaneously.
```

## G01-DIGEST-Q038

```yaml
QID: G01-DIGEST-Q038
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  A metric that depends on unavailable data is marked unavailable/pending rather than estimated silently unless estimation is explicitly defined.
WHY_IT_MATTERS: >
  Silent estimates undermine trust.
DISCONFIRMING_OBSERVATION: >
  The summary shows a normal-looking number derived from missing/incomplete data with no indication.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Make a required source unavailable during generation.
```

## G01-DIGEST-Q039

```yaml
QID: G01-DIGEST-Q039
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Every summary metric can be traced to authoritative business evidence without making the summary itself a posting/execution source.
WHY_IT_MATTERS: >
  Reporting must observe business truth, not create it.
DISCONFIRMING_OBSERVATION: >
  Generating or opening a summary changes underlying business state or a metric cannot be reconciled to authoritative records.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Generate/view summaries while monitoring authoritative records for side effects and reconstruct selected metrics.
```

## G01-DIGEST-Q040

```yaml
QID: G01-DIGEST-Q040
MODULE: digest
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Equivalent summary paths—scheduled, manual, retry and catch-up—converge on the same authorization, cutoff and audit rules.
WHY_IT_MATTERS: >
  Path divergence creates hidden reporting leaks.
DISCONFIRMING_OBSERVATION: >
  One supported generation path includes data or recipients that another correctly excludes under matched conditions.
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: >
  Execute matched scenarios across every supported generation path.
```

---
**Disposition:** AUTHORING COMPLETE / STRUCTURAL QA NEXT
