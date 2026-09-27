# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_sms Module MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_SMS-MVQ48-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `project_sms`
**Module Class:** Bridge (project management + outbound SMS notification channel) — seam-only per
`GMVQ_BRIDGE_MODULE_RULE_V1.00`
**Wave:** W3
**Author Cell:** GMVQ Control Desk (gap-fill — module was omitted from the original P12 cell
dispatch; self-identified and corrected same session)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the seam between project management and an
outbound SMS notification channel: what triggers a text message about a project event, who may
authorize it, what happens when delivery is ambiguous, delayed, throttled, refused, or misdirected,
and how the resulting send is governed and audited. Per the Bridge Module Rule, every question below
fails ONLY at that seam — a question about project events in general, or about SMS delivery in
general, with the bridge's name simply attached, was cut before authoring.

Question text is source-neutral. It does not name the module, any vendor or product, or any
technical identifier (field, model, method, XML ID, API path).

## Control

- Bridge seam test applied to every question: removal-of-capability test per
  `GMVQ_BRIDGE_MODULE_RULE_V1.00` section 2.
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because each tests a distinct material seam hypothesis, spread
  across triggering, recipient resolution, consent/opt-out, cost, timing, content, delivery-state
  reconciliation, authority, retry/duplication, and audit.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G12-PROJECT_SMS-Q001

```yaml
QID: G12-PROJECT_SMS-Q001
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a project event that is configured to notify by SMS occurs while the recipient has no valid
  phone number on file, the system produces a discoverable failure rather than silently skipping the
  notification with no trace.
WHY_IT_MATTERS: >
  A silently dropped notification leaves a stakeholder unaware of a project event they were meant to
  be alerted to, with nothing in the record to reveal that the alert never went out.
DISCONFIRMING_OBSERVATION: >
  A qualifying project event occurs for a recipient with no valid phone number and no failure, log
  entry, or discoverable trace is produced anywhere.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure an SMS-notifying project event for a recipient who has no phone number on file, trigger
  the event, and inspect whether any discoverable failure record exists.
```

## G12-PROJECT_SMS-Q002

```yaml
QID: G12-PROJECT_SMS-Q002
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a stakeholder has more than one phone number associated with a project (e.g. through multiple
  roles or contact records), the system resolves a single, discoverable, deterministic destination
  rather than an arbitrary or duplicated send.
WHY_IT_MATTERS: >
  An arbitrary choice between multiple numbers can send a sensitive project alert to a number the
  stakeholder no longer uses, or duplicate the same alert to two numbers with no visible reason why.
DISCONFIRMING_OBSERVATION: >
  A stakeholder with two valid phone numbers on file receives either zero, or more than one, copies
  of the same triggered notification with no discoverable resolution rule shown.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attach two valid phone numbers to the same stakeholder in the context of one project, trigger a
  notifying event, and observe which number(s) receive the message.
```

## G12-PROJECT_SMS-Q003

```yaml
QID: G12-PROJECT_SMS-Q003
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A stakeholder who has withdrawn consent to receive SMS notifications for a project does not
  receive further messages triggered by that project once the withdrawal is recorded.
WHY_IT_MATTERS: >
  Continuing to text someone after they have opted out is both a compliance exposure and a trust
  failure with no legitimate business justification.
DISCONFIRMING_OBSERVATION: >
  A stakeholder who has recorded an SMS opt-out for a project still receives a triggered
  notification from that project afterward.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Record an SMS opt-out for a stakeholder on a given project, then trigger a qualifying event on
  that project and observe whether a message is sent.
```

## G12-PROJECT_SMS-Q004

```yaml
QID: G12-PROJECT_SMS-Q004
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Which project events are eligible to trigger an SMS at all is a configurable, discoverable list
  rather than an implicit, undocumented set baked into behaviour.
WHY_IT_MATTERS: >
  If nobody can see which events send texts, the organisation cannot budget for, audit, or tune the
  channel without trial and error against real stakeholders.
DISCONFIRMING_OBSERVATION: >
  No discoverable list or setting exists showing which project event types are eligible to trigger
  an SMS notification.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Inspect the configuration surface available to a project administrator for any listing of
  SMS-eligible event types.
```

## G12-PROJECT_SMS-Q005

```yaml
QID: G12-PROJECT_SMS-Q005
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an SMS provider reports a delivery failure after the message was already recorded as "sent"
  in the project's activity trail, the project record is reconciled to reflect the failure rather
  than permanently showing a successful send that never arrived.
WHY_IT_MATTERS: >
  A project record that claims a stakeholder was notified, when they were not, can cause a real
  business decision to proceed on a false assumption that someone was informed.
DISCONFIRMING_OBSERVATION: >
  A message is shown as sent in the project's activity trail, the provider later reports non-
  delivery, and the project record is never updated to reflect that.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Trigger a notification, simulate or wait for a downstream delivery failure report, and check
  whether the project's own record of the send is later reconciled.
```

## G12-PROJECT_SMS-Q006

```yaml
QID: G12-PROJECT_SMS-Q006
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the same project event is edited or corrected before the SMS actually leaves the outbound
  queue, the message content reflects the corrected state rather than a stale snapshot taken at the
  moment the event first fired.
WHY_IT_MATTERS: >
  A text that reports a value the sender already corrected internally misinforms the stakeholder
  about the true state of the project.
DISCONFIRMING_OBSERVATION: >
  A project event is corrected before its SMS leaves the queue, and the delivered message still
  shows the original, now-incorrect, value.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger a notifying event, correct the underlying project data before the message is confirmed
  sent, and inspect the delivered message content.
```

## G12-PROJECT_SMS-Q007

```yaml
QID: G12-PROJECT_SMS-Q007
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A project stakeholder in a different company/tenant scope than the project itself does not
  silently receive an SMS about that project's internal events.
WHY_IT_MATTERS: >
  Cross-tenant notification leakage could disclose that a project exists, and details about it, to
  a party outside the organisation that owns it.
DISCONFIRMING_OBSERVATION: >
  A stakeholder whose company/tenant scope differs from the project's owning tenant still receives
  an SMS triggered by that project's internal event.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Configure a stakeholder in a different tenant/company scope than the project, trigger a notifying
  event, and observe whether they receive a message.
```

## G12-PROJECT_SMS-Q008

```yaml
QID: G12-PROJECT_SMS-Q008
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Free-text content entered into a project record (e.g. a task description) that is included in an
  SMS is not capable of injecting content that changes how the message is routed or how the provider
  interprets the payload.
WHY_IT_MATTERS: >
  If stakeholder-editable project text can alter delivery routing or payload interpretation, a
  malicious or careless edit could redirect or corrupt notifications system-wide.
DISCONFIRMING_OBSERVATION: >
  Text containing delivery-control-like sequences, entered into a project field that feeds an SMS
  body, changes where or how the message is routed.
EXPECTED_SURFACE: S2,S8
PRECONDITIONS: >
  Enter content resembling delivery-control syntax into a project field used in an SMS template,
  trigger the notification, and observe routing/interpretation behaviour.
```

## G12-PROJECT_SMS-Q009

```yaml
QID: G12-PROJECT_SMS-Q009
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When project content intended for SMS exceeds a single message's character limit, the system
  produces a discoverable, deliberate segmentation or truncation behaviour rather than an
  unpredictable cut that could drop the most important part of the message.
WHY_IT_MATTERS: >
  An unpredictable truncation could cut off the actionable part of a message (e.g. a deadline or a
  decision needed) while leaving less important text intact.
DISCONFIRMING_OBSERVATION: >
  Content exceeding one message's length is truncated at a point that removes information the
  sender configured as the primary purpose of the alert, with no discoverable rule governing where
  the cut occurs.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure an SMS template whose rendered content exceeds a single message's character limit and
  trigger it.
```

## G12-PROJECT_SMS-Q010

```yaml
QID: G12-PROJECT_SMS-Q010
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Which language or locale an SMS notification is rendered in is derived from a discoverable,
  documented rule (e.g. the stakeholder's own locale) rather than an undocumented default that may
  not match the recipient.
WHY_IT_MATTERS: >
  A message rendered in a language the recipient cannot read defeats the purpose of the
  notification and may cause the underlying project event to go unaddressed.
DISCONFIRMING_OBSERVATION: >
  A stakeholder with a clearly recorded locale different from a system default receives a
  notification in the wrong language with no discoverable rule explaining why.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Set a stakeholder's locale to a non-default language, trigger a notification, and inspect the
  rendered language against the documented rule.
```

## G12-PROJECT_SMS-Q011

```yaml
QID: G12-PROJECT_SMS-Q011
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the outbound SMS provider is unreachable or rate-limited at the moment of triggering, the
  notification is queued and retried on a discoverable policy rather than being silently and
  permanently dropped.
WHY_IT_MATTERS: >
  A transient provider outage should not translate into a permanent, invisible loss of a business
  notification that the stakeholder never learns was owed to them.
DISCONFIRMING_OBSERVATION: >
  A notification triggered during a provider outage is never retried and no discoverable record
  shows it was ever attempted.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Simulate provider unavailability at the moment of trigger and inspect whether the message is
  queued, retried, or lost.
```

## G12-PROJECT_SMS-Q012

```yaml
QID: G12-PROJECT_SMS-Q012
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A retried notification (after a transient failure) is discoverably marked as a retry rather than
  appearing identical to an original send, so the activity trail does not overstate how many times
  the stakeholder was actually alerted.
WHY_IT_MATTERS: >
  If retries look identical to fresh sends, anyone reviewing the project's notification history will
  overcount how many separate alerts actually reached the stakeholder.
DISCONFIRMING_OBSERVATION: >
  A retried send appears in the activity trail with no discoverable distinction from an original,
  first-attempt send.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Force a transient failure and retry, then inspect the activity trail for a distinguishing marker
  between the original attempt and the retry.
```

## G12-PROJECT_SMS-Q013

```yaml
QID: G12-PROJECT_SMS-Q013
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Configuring or changing which project events trigger SMS notifications, and to whom, requires a
  discoverable authority check rather than being open to any project participant regardless of role.
WHY_IT_MATTERS: >
  Unrestricted ability to redirect notification recipients could be used to divert alerts about a
  project away from the people meant to see them.
DISCONFIRMING_OBSERVATION: >
  A project participant with no configuration authority is able to change the SMS recipient list or
  trigger rules for that project.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Attempt to change SMS trigger/recipient configuration as a participant without configuration
  authority and observe whether the attempt is blocked.
```

## G12-PROJECT_SMS-Q014

```yaml
QID: G12-PROJECT_SMS-Q014
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a project is closed, cancelled, or archived, previously scheduled but not-yet-sent SMS
  notifications tied to it are discoverably cancelled rather than firing afterward for a project
  that no longer exists in an active state.
WHY_IT_MATTERS: >
  Receiving an alert about a project that was already cancelled confuses stakeholders and may
  prompt action on a project that no longer needs it.
DISCONFIRMING_OBSERVATION: >
  A project is cancelled or archived and a notification queued before that moment still fires
  afterward with no acknowledgement of the project's changed state.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Schedule a notification, then cancel or archive the project before it fires, and observe whether
  it still sends.
```

## G12-PROJECT_SMS-Q015

```yaml
QID: G12-PROJECT_SMS-Q015
MODULE: project_sms
TYPE: MODULE
AUTHOR: GMVQ-CONTROL-DESK
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a stakeholder is removed from a project's participant list, notifications already scheduled
  for that project no longer include them going forward.
WHY_IT_MATTERS: >
  Someone removed from a project (e.g. reassigned elsewhere) continuing to receive its alerts is
  both a nuisance and a potential information-boundary problem if the removal was for cause.
DISCONFIRMING_OBSERVATION: >
  A stakeholder removed from a project's participant list still receives an SMS triggered by that
  project afterward.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Remove a stakeholder from a project's participant list, trigger a qualifying event, and observe
  whether they still receive a message.
```


## G12-PROJECT_SMS-Q016

```yaml
QID: G12-PROJECT_SMS-Q016
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a single project event is configured to notify many stakeholders at once, a delivery failure
  for one recipient does not block or delay delivery to the other recipients of the same event.
WHY_IT_MATTERS: >
  If one bad number or one failed delivery can stall an entire round of notifications, a project-wide
  alert (e.g. a schedule change affecting the whole team) could reach almost nobody in time because of
  a single unrelated failure.
DISCONFIRMING_OBSERVATION: >
  One recipient among many configured for the same triggered event has an undeliverable number, and
  the other recipients' messages are delayed well beyond their own normal delivery time or never sent.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure a project event to notify several stakeholders at once, make one recipient's number
  undeliverable, trigger the event, and compare delivery timing/outcome for the other recipients.
```

## G12-PROJECT_SMS-Q017

```yaml
QID: G12-PROJECT_SMS-Q017
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a project tracks its own cost or budget, the cost of an SMS notification triggered by that
  project's events is discoverably attributable to that project's own cost record, rather than being
  an invisible overhead absent from the project's financial picture.
WHY_IT_MATTERS: >
  A project whose true cost includes an active notification channel, but whose record never shows it,
  makes the project look cheaper to run than it actually is when that spend is compared across
  projects.
DISCONFIRMING_OBSERVATION: >
  A project with its own cost or budget tracking triggers SMS notifications, and no discoverable
  attribution of that notification's cost to the project's own cost record exists anywhere.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  On a project with cost/budget tracking enabled, trigger an SMS-notifying event and inspect the
  project's cost record for any reference to the notification's cost.
```

## G12-PROJECT_SMS-Q018

```yaml
QID: G12-PROJECT_SMS-Q018
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A stakeholder's phone number recorded in an international or foreign format is sent as a correctly
  addressed message rather than being silently mishandled (e.g. a dropped or misapplied country
  prefix) because the triggering project event originated in a different locale or company.
WHY_IT_MATTERS: >
  A misaddressed international number either fails outright or, worse, could reach an unrelated
  person in a different country who happens to hold the malformed number, exposing project content
  to a stranger.
DISCONFIRMING_OBSERVATION: >
  A stakeholder with a validly recorded international-format number receives no message, or a
  malformed send, when the triggering project event originates from a different company/locale
  context than the stakeholder's own number format.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Set a stakeholder's phone number in an international format different from the project's own
  operating locale, trigger a notifying event, and inspect the outgoing message's addressing.
```

## G12-PROJECT_SMS-Q019

```yaml
QID: G12-PROJECT_SMS-Q019
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where sending is restricted to a defined business-hours or calendar window, a project event that
  fires outside that window in the recipient's own time context results in the message being queued
  to send within the next allowed window, rather than being sent immediately outside the window or
  silently dropped.
WHY_IT_MATTERS: >
  A text that arrives in the middle of the night because the sending system ignored the stakeholder's
  own hours is intrusive, and a message dropped outright because it fell outside the window is a
  silent loss of a business notification.
DISCONFIRMING_OBSERVATION: >
  An event fired outside the configured sending window results in either an immediate out-of-window
  send with no queuing logic, or the message disappearing with no record that it was ever due.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure a business-hours sending window, trigger a qualifying event outside that window, and
  observe whether and when the message is actually sent.
```

## G12-PROJECT_SMS-Q020

```yaml
QID: G12-PROJECT_SMS-Q020
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  After a stakeholder's notifications have failed delivery a number of consecutive times, this is
  discoverably surfaced to someone with authority over the project (e.g. as a flagged condition),
  rather than the system continuing indefinite silent attempts with no visible signal to anyone
  responsible for the project.
WHY_IT_MATTERS: >
  A stakeholder who has effectively become unreachable should not stay silently unreachable forever;
  someone accountable for the project needs a way to notice and correct the situation.
DISCONFIRMING_OBSERVATION: >
  A stakeholder's notifications fail delivery many consecutive times and no discoverable flag, notice,
  or escalation appears anywhere for a person with authority over the project.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Force repeated consecutive delivery failures for one stakeholder's notifications on a project and
  inspect whether the condition becomes visible to someone with project authority.
```

## G12-PROJECT_SMS-Q021

```yaml
QID: G12-PROJECT_SMS-Q021
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the same qualifying project event is technically triggered twice in rapid succession (for
  example because an underlying process is retried), the stakeholder does not receive two separate
  SMS notifications for what is a single underlying business event.
WHY_IT_MATTERS: >
  Duplicate texts about the same underlying fact erode trust in the channel and can make a
  stakeholder believe two separate things happened when only one did.
DISCONFIRMING_OBSERVATION: >
  A single business event, technically fired twice in quick succession, results in two separate SMS
  deliveries to the same stakeholder with no de-duplication marker anywhere in the record.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Force the same underlying project event to be technically triggered twice in rapid succession and
  observe whether the stakeholder receives one message or two.
```

## G12-PROJECT_SMS-Q022

```yaml
QID: G12-PROJECT_SMS-Q022
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When the wording template used for an event type is changed while an earlier notification for that
  same event type is already queued but not yet sent, which template version the queued message
  actually uses follows a discoverable, documented rule rather than an unpredictable mix.
WHY_IT_MATTERS: >
  If two messages queued moments apart can render from different, undocumented template versions
  with no rule governing which applies, nobody can predict or explain what a stakeholder will
  actually receive.
DISCONFIRMING_OBSERVATION: >
  Two notifications for the same event type, queued moments apart, render using different template
  content after an edit, with no discoverable rule explaining which version applied to which.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Queue a notification, edit the wording template for that event type before it sends, queue a
  second notification of the same type, and compare the rendered content of both once sent.
```

## G12-PROJECT_SMS-Q023

```yaml
QID: G12-PROJECT_SMS-Q023
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The complete history of SMS notifications triggered by a specific project — recipient, content or
  a reference to it, timestamp, and outcome — can be reconstructed from the project's own record
  alone, without needing to separately query the outbound messaging channel itself.
WHY_IT_MATTERS: >
  If a project's own record cannot answer "who was texted, when, and did it arrive" on its own, an
  audit or an incident review depends on a separate system the project team may not control or be
  able to reach.
DISCONFIRMING_OBSERVATION: >
  For a project with known prior SMS sends, the project's own record is missing the recipient,
  content reference, timestamp, or outcome for at least one of them.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger several SMS notifications on a project over time, then attempt to reconstruct the full
  send history using only the project's own record.
```

## G12-PROJECT_SMS-Q024

```yaml
QID: G12-PROJECT_SMS-Q024
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user who can view a project's general record but has not been granted permission to view its SMS
  notification history cannot see the content or recipient list of that project's past SMS sends
  through the general project view.
WHY_IT_MATTERS: >
  SMS content can carry sensitive project detail (names, numbers, timing); leaking it through the
  ordinary project view defeats a permission boundary someone deliberately set up.
DISCONFIRMING_OBSERVATION: >
  A user with general project view access but no SMS-history permission is able to see the content
  or recipient list of a past SMS send through ordinary project navigation.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user granted general project view access but explicitly denied SMS-history view permission,
  attempt to view the content or recipients of a past send through the project record.
```

## G12-PROJECT_SMS-Q025

```yaml
QID: G12-PROJECT_SMS-Q025
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Granting a user permission to view a project's SMS notification history does not, as a side effect,
  expose other confidential project data to them that is unrelated to the content of those
  notifications.
WHY_IT_MATTERS: >
  A permission meant to be narrow (see the SMS log) should not turn out to be a backdoor into
  broader project confidentiality that a project owner never intended to grant.
DISCONFIRMING_OBSERVATION: >
  A user granted only SMS-history view permission is able to see confidential project data that was
  never part of any notification's content.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Grant a user only SMS-history view permission on a project and attempt to access confidential
  project data unrelated to any notification's content.
```

## G12-PROJECT_SMS-Q026

```yaml
QID: G12-PROJECT_SMS-Q026
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A stakeholder's SMS opt-out recorded on one project follows a documented, discoverable scope rule
  — either applying only to that project or explicitly to all projects — rather than an undocumented
  behaviour where the same stakeholder's status differs unpredictably between projects.
WHY_IT_MATTERS: >
  If nobody can tell whether an opt-out is per-project or organisation-wide, the same stakeholder
  could be unexpectedly texted on a second project despite having clearly opted out on the first, or
  wrongly blocked from a project where they never opted out at all.
DISCONFIRMING_OBSERVATION: >
  A stakeholder who is a participant on two different projects opts out on one, and their resulting
  notification status on the other project shows no discoverable, documented scope rule for why it
  is what it is.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Add the same stakeholder to two different projects, record an opt-out on one, and inspect their
  notification status on the other against the documented scope rule.
```

## G12-PROJECT_SMS-Q027

```yaml
QID: G12-PROJECT_SMS-Q027
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the project event that triggered an already-sent SMS is later reversed or undone, the
  project's own record of that earlier notification is discoverably marked as superseded by the
  reversal, rather than continuing to represent the original message as current and accurate.
WHY_IT_MATTERS: >
  Anyone reviewing the project afterward could otherwise be misled into thinking a stakeholder was
  informed of something that is no longer true, with nothing in the record to warn them.
DISCONFIRMING_OBSERVATION: >
  A project event whose SMS already sent is later reversed, and the project's record of that earlier
  notification shows no discoverable indication that the underlying event was undone.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger a notifying event to completion, then reverse or undo that same event on the project, and
  inspect the earlier notification's record for any indication of the reversal.
```

## G12-PROJECT_SMS-Q028

```yaml
QID: G12-PROJECT_SMS-Q028
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When responsibility for a project is transferred to a new manager, the previously configured SMS
  notification rules for that project continue to operate under the new manager's own authority,
  rather than silently remaining tied to the departed manager's identity for approval purposes.
WHY_IT_MATTERS: >
  Notification rules that stay invisibly bound to someone who no longer manages the project could
  leave nobody currently accountable able to see or change how the project communicates by SMS.
DISCONFIRMING_OBSERVATION: >
  After a project's management is transferred, the SMS notification configuration still shows the
  departed manager as its governing authority with no discoverable way for the new manager to take
  it over.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Transfer a project's management to a different user, then inspect whether the new manager has
  discoverable authority over the existing SMS notification configuration.
```

## G12-PROJECT_SMS-Q029

```yaml
QID: G12-PROJECT_SMS-Q029
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a stakeholder's role on a project changes between the moment a notifying event fires and the
  moment the message actually sends, who is treated as the recipient follows a documented point-in-
  time rule (e.g. role at trigger time, or role at send time), rather than an arbitrary, undocumented
  choice.
WHY_IT_MATTERS: >
  Without a documented rule, the same sequence of events could sometimes notify the old role and
  sometimes the new one, making it impossible to predict or explain who actually gets alerted.
DISCONFIRMING_OBSERVATION: >
  A stakeholder's role changes between an event firing and its message sending, and the resulting
  recipient treatment shows no discoverable, documented rule for which point in time governed it.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Trigger a notifying event, change the stakeholder's role on the project before the message sends,
  and inspect which role's notification treatment the delivered message reflects.
```

## G12-PROJECT_SMS-Q030

```yaml
QID: G12-PROJECT_SMS-Q030
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a single event triggers notifications to many stakeholders at once, the timestamp recorded
  for each individual stakeholder's notification reflects that message's own actual send time,
  rather than a single batch-level timestamp applied uniformly to every recipient regardless of when
  their particular message actually went out.
WHY_IT_MATTERS: >
  If every recipient in a batch shows the same timestamp regardless of actual send time, a later
  review cannot tell whether a specific stakeholder was notified promptly or only after a
  significant delay within that batch.
DISCONFIRMING_OBSERVATION: >
  A batch of notifications sent to many stakeholders from one event shows a single identical
  timestamp for every recipient even though their messages did not all actually go out at the same
  moment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger an event that notifies many stakeholders at once, introduce a way for individual sends to
  complete at different times, and compare the recorded timestamps across recipients.
```

## G12-PROJECT_SMS-Q031

```yaml
QID: G12-PROJECT_SMS-Q031
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a project's SMS sends have already incurred a recorded cost, cancelling or archiving the
  project afterward preserves that historical cost attribution rather than removing or orphaning the
  record of what was already spent.
WHY_IT_MATTERS: >
  A cancelled project that silently loses its already-incurred notification cost understates what
  the organisation actually spent on it, distorting any later review of the project's true cost.
DISCONFIRMING_OBSERVATION: >
  A project's SMS spend was recorded prior to cancellation, and after the project is cancelled or
  archived that cost record is no longer discoverable anywhere.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  On a project with recorded SMS spend, cancel or archive the project and check whether the earlier
  cost record remains discoverable afterward.
```

## G12-PROJECT_SMS-Q032

```yaml
QID: G12-PROJECT_SMS-Q032
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a stakeholder qualifies for the same triggered notification through two independent
  notification rules at once (for example, holding two distinct roles on the project that would each
  separately warrant an alert), they receive a single message for that event rather than one per
  matching rule.
WHY_IT_MATTERS: >
  A stakeholder who happens to hold two qualifying roles should not be penalised with duplicate
  texts for a single real-world event just because more than one rule happened to match them.
DISCONFIRMING_OBSERVATION: >
  A stakeholder holding two independent roles that each separately qualify for the same triggered
  event receives two separate SMS messages for that one event.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Give one stakeholder two distinct roles on a project that would each independently trigger a
  notification for the same event, trigger it, and count the messages they receive.
```

## G12-PROJECT_SMS-Q033

```yaml
QID: G12-PROJECT_SMS-Q033
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two different project events for the same stakeholder are processed at the same time, the
  content delivered for each event remains correctly attributed to its own event, with no content
  from one message bleeding into the other.
WHY_IT_MATTERS: >
  Cross-contaminated message content could tell a stakeholder something false about one project
  event by mixing in detail that actually belongs to an unrelated event.
DISCONFIRMING_OBSERVATION: >
  Two different events for the same stakeholder are triggered at the same time and at least one
  delivered message contains content that actually belongs to the other event.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger two distinct notifying events for the same stakeholder at the same time and inspect both
  delivered messages for cross-contaminated content.
```

## G12-PROJECT_SMS-Q034

```yaml
QID: G12-PROJECT_SMS-Q034
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A reference to a specific project artifact included in an SMS (for example, a task or milestone
  identifier) remains a valid, resolvable reference even if that artifact is later renamed or
  renumbered on the project.
WHY_IT_MATTERS: >
  A stakeholder who tries to follow up on a text using the reference it gave them should not find
  that the reference now points to nothing, or to the wrong thing, because of an unrelated later
  change.
DISCONFIRMING_OBSERVATION: >
  A project artifact referenced in a previously sent SMS is renamed or renumbered, and the reference
  in that earlier message no longer resolves to the correct artifact.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Send a notification referencing a specific project artifact, rename or renumber that artifact
  afterward, and check whether the earlier message's reference still resolves correctly.
```

## G12-PROJECT_SMS-Q035

```yaml
QID: G12-PROJECT_SMS-Q035
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A stakeholder who only holds limited, portal-style external access to a project does not receive
  SMS content that discloses more project detail than that limited access level would otherwise show
  them.
WHY_IT_MATTERS: >
  A notification channel that ignores the access boundary already set for an external stakeholder
  could hand them, by text, detail they were deliberately never given through their normal access.
DISCONFIRMING_OBSERVATION: >
  A stakeholder with limited, portal-style external access to a project receives an SMS containing
  project detail that their access level does not otherwise expose to them.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure a stakeholder with limited external/portal-style access to a project, trigger a
  notifying event, and compare the SMS content against what their access level otherwise shows.
```

## G12-PROJECT_SMS-Q036

```yaml
QID: G12-PROJECT_SMS-Q036
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The wording used for a given event type's SMS can be customised per project or per company rather
  than being a single fixed global wording applied uniformly regardless of which project or company
  context the event occurred in.
WHY_IT_MATTERS: >
  Different projects and companies can have materially different stakeholders, tone, and legal
  requirements; a wording that cannot be adapted to that context may be unsuitable for at least some
  of them.
DISCONFIRMING_OBSERVATION: >
  No discoverable setting exists that allows the wording of a given event type's SMS to be
  customised for a specific project or company rather than the organisation-wide default.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Inspect the configuration surface available to a project or company administrator for any setting
  that customises event-type wording at that level.
```

## G12-PROJECT_SMS-Q037

```yaml
QID: G12-PROJECT_SMS-Q037
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Triggering an event type that exists generally but has not been enabled for a specific project
  results in no message being sent and no record that falsely represents a send as having occurred.
WHY_IT_MATTERS: >
  A false-success record for a notification that was never actually configured to send would mislead
  anyone checking whether a stakeholder was alerted about that project.
DISCONFIRMING_OBSERVATION: >
  An event type not enabled for a specific project is triggered on that project, and a record
  appears indicating a message was sent when none actually was.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  On a project where a given event type's notification is not enabled, trigger that event type and
  inspect whether any record falsely shows a message as sent.
```

## G12-PROJECT_SMS-Q038

```yaml
QID: G12-PROJECT_SMS-Q038
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the underlying project record is deleted outright, rather than merely archived, between an
  event firing and its queued message actually sending, the system does not send a message
  referencing project data that no longer exists.
WHY_IT_MATTERS: >
  A message built around, or linking to, a project that has been permanently removed could confuse
  or mislead a stakeholder and reference something they can never actually reach.
DISCONFIRMING_OBSERVATION: >
  A project record is deleted after an event fires but before its queued message sends, and the
  message still sends referencing the now-nonexistent project.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger a notifying event, delete the underlying project record outright before the queued message
  sends, and observe whether the message still sends.
```

## G12-PROJECT_SMS-Q039

```yaml
QID: G12-PROJECT_SMS-Q039
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The volume of SMS messages a single project can trigger within a short period is bounded by a
  documented limit, rather than one project's activity being able to consume an unbounded share of
  the organisation's shared sending capacity.
WHY_IT_MATTERS: >
  One misconfigured or unusually active project should not be able to starve every other project's
  notifications, or run up unbounded shared sending cost, with no limit in place.
DISCONFIRMING_OBSERVATION: >
  A single project is able to trigger an unbounded volume of messages in a short period with no
  discoverable limit anywhere in the system.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Trigger a rapid, high-volume sequence of notifying events on a single project and observe whether
  any documented limit is enforced.
```

## G12-PROJECT_SMS-Q040

```yaml
QID: G12-PROJECT_SMS-Q040
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Notifications queued while a project was in a test or sandbox configuration do not leak out as
  real SMS sends to real stakeholders after that project is switched into live, production
  notification mode.
WHY_IT_MATTERS: >
  Test-mode traffic reaching real people once a project goes live would send confusing, inaccurate,
  or premature content to actual stakeholders who never agreed to receive test material.
DISCONFIRMING_OBSERVATION: >
  A notification queued while a project was in test/sandbox mode is delivered to a real stakeholder's
  real number after the project is switched to live mode.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Queue a notification while a project is in test/sandbox mode, switch the project to live mode
  before that message sends, and observe whether it is delivered to a real recipient.
```

## G12-PROJECT_SMS-Q041

```yaml
QID: G12-PROJECT_SMS-Q041
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A stakeholder's phone number that is present but recorded in an invalid or malformed format is
  discoverably distinguished, as its own failure state, from a stakeholder who has no phone number
  recorded at all.
WHY_IT_MATTERS: >
  Treating "malformed" the same as "missing" hides a data-quality problem that a project
  administrator could otherwise notice and correct, versus a stakeholder who genuinely needs a
  number added.
DISCONFIRMING_OBSERVATION: >
  A stakeholder with a present but malformed phone number produces the same discoverable failure
  state as a stakeholder with no phone number at all, with no way to tell the two apart.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record a malformed phone number for one stakeholder and no phone number for another, trigger a
  notifying event for both, and compare the resulting failure states.
```

## G12-PROJECT_SMS-Q042

```yaml
QID: G12-PROJECT_SMS-Q042
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When outbound SMS capability itself is disabled or unavailable at the organisation level, any
  project's own SMS notification configuration is discoverably shown as inactive, rather than still
  appearing enabled while nothing it configures can ever actually be sent.
WHY_IT_MATTERS: >
  A project administrator who sees notification rules displayed as active, while the underlying
  channel is actually switched off entirely, would wrongly believe stakeholders are being alerted
  when none are.
DISCONFIRMING_OBSERVATION: >
  Outbound SMS capability is disabled at the organisation level, and a project's own notification
  configuration still displays as fully active with no discoverable indication that nothing can
  actually send.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Disable outbound SMS capability at the organisation level and inspect how an existing project's
  notification configuration is displayed afterward.
```

## G12-PROJECT_SMS-Q043

```yaml
QID: G12-PROJECT_SMS-Q043
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a notification preference can be set at both the organisation/company level and the
  individual project level, a project-level override is discoverably honoured rather than being
  silently ignored in favour of the broader-level setting.
WHY_IT_MATTERS: >
  A project administrator who deliberately overrides an organisation-wide default for their own
  project should be able to trust that the override actually takes effect, not silently lose to a
  broader setting they cannot even see is winning.
DISCONFIRMING_OBSERVATION: >
  A project-level notification preference is set differently from the organisation/company-level
  default, and the resulting behaviour follows the broader-level setting with no discoverable
  indication that the project-level override was ignored.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Set a project-level notification preference that differs from the organisation/company default,
  trigger a qualifying event, and observe which setting the resulting behaviour actually follows.
```

## G12-PROJECT_SMS-Q044

```yaml
QID: G12-PROJECT_SMS-Q044
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a project can be put into a paused or on-hold state distinct from being cancelled or
  archived, the effect of that paused state on already-queued but not-yet-sent notifications is
  discoverable and documented, rather than left to an implicit, unstated default.
WHY_IT_MATTERS: >
  Without a documented rule, nobody can predict whether pausing a project will suppress its
  in-flight notifications or let them continue as though the project were still fully active.
DISCONFIRMING_OBSERVATION: >
  A project is put into a paused/on-hold state with a notification already queued, and no
  discoverable, documented statement exists of what happens to that queued notification as a
  result.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Queue a notification, put the project into a paused/on-hold state before it sends, and check for a
  documented, discoverable statement of the resulting effect.
```

## G12-PROJECT_SMS-Q045

```yaml
QID: G12-PROJECT_SMS-Q045
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a phone number recorded against a project stakeholder is later reassigned, outside the
  system, to a different real-world person, a subsequently triggered notification does not continue
  to be sent to that number without the project's own record ever being asked to confirm the number
  still belongs to the original stakeholder.
WHY_IT_MATTERS: >
  A stale number that has changed hands could deliver confidential project content straight to a
  stranger, with the project team believing the original stakeholder was informed.
DISCONFIRMING_OBSERVATION: >
  A project keeps sending notifications to a stakeholder's recorded number with no discoverable
  mechanism that would ever prompt a check on whether that number still belongs to them.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Inspect whether the system has any discoverable mechanism to periodically confirm, or prompt
  reconfirmation of, phone number ownership for a long-standing project stakeholder.
```

## G12-PROJECT_SMS-Q046

```yaml
QID: G12-PROJECT_SMS-Q046
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Editing the wording template used for an event type within the context of one company/tenant does
  not alter how that same event type renders for projects belonging to a different company/tenant.
WHY_IT_MATTERS: >
  A shared underlying template that leaks edits across tenant boundaries would let one organisation's
  wording change silently affect what another, unrelated organisation's stakeholders receive.
DISCONFIRMING_OBSERVATION: >
  A wording template is edited within one company/tenant's context, and a project belonging to a
  different company/tenant subsequently renders the same event type using the edited wording.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Edit an event type's wording template within one company/tenant context, then trigger the same
  event type on a project belonging to a different company/tenant and compare the rendered wording.
```

## G12-PROJECT_SMS-Q047

```yaml
QID: G12-PROJECT_SMS-Q047
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Which specific user enabled or last approved SMS notifications for a given project is a
  discoverable, attributable fact, rather than the configuration appearing with no record of who
  authorised it.
WHY_IT_MATTERS: >
  If nobody can tell who turned on a channel that texts real people, accountability for that
  decision, and for correcting it if it was wrong, has nowhere to land.
DISCONFIRMING_OBSERVATION: >
  A project has SMS notifications enabled, and no discoverable record exists of which user enabled
  or last approved that configuration.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Enable SMS notifications for a project as a specific user and inspect whether that action is
  discoverably attributed to them afterward.
```

## G12-PROJECT_SMS-Q048

```yaml
QID: G12-PROJECT_SMS-Q048
MODULE: project_sms
TYPE: MODULE
AUTHOR: P12-6
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a piece of information a wording template expects is not actually available at the moment a
  message is rendered, the system produces a discoverable fallback or a blocked send, rather than
  delivering a message that exposes an unresolved placeholder to the recipient.
WHY_IT_MATTERS: >
  A stakeholder who receives a message with a raw, unresolved placeholder instead of real content
  learns nothing useful and sees a visible sign of an internal fault in what should be a routine
  business alert.
DISCONFIRMING_OBSERVATION: >
  A wording template's expected information is unavailable at render time, and the resulting message
  is still delivered containing an unresolved placeholder instead of a discoverable fallback or a
  blocked send.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger a notification in a state where a piece of information the wording template expects is
  unavailable, and inspect the rendered message for a fallback versus an exposed placeholder.
```
