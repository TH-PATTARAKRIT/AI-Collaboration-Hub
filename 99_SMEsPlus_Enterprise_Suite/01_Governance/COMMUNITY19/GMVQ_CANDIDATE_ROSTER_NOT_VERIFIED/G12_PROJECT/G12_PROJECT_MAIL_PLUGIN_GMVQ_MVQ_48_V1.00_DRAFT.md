# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_mail_plugin Module MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_MAIL_PLUGIN-MVQ48-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `project_mail_plugin`
**Module Class:** Bridge (project management + inbound message capture) — seam-only per
`GMVQ_BRIDGE_MODULE_RULE_V1.00`
**Wave:** W3
**Author Cell:** P12-2 (GMVQ Question Factory — Production Cell P12-2)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the seam between project management and an
inbound message-capture channel: how an external message becomes a project task or an update to one,
who may cause that, what happens when the capture is ambiguous, delayed, duplicated, or fails, and
how the resulting record is governed once created. Per the Bridge Module Rule, every question below
fails ONLY at that seam — a question about project tasks in general, or about message handling in
general, with the bridge's specific name simply attached, was cut before authoring.

Question text is source-neutral. It does not name the module, any vendor or product, or any
technical identifier (field, model, method, XML ID, API path).

## Control

- Bridge seam test applied to every question: removal-of-capability test per
  `GMVQ_BRIDGE_MODULE_RULE_V1.00` section 2.
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because each tests a distinct material seam hypothesis, spread
  across ordering, partiality, ownership, timing, reversal, error asymmetry, authority, lifecycle
  mismatch, and boundary.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G12-PROJECT_MAIL_PLUGIN-Q001

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q001
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an incoming message's routing address could plausibly match more than one project, the system
  produces a defined, discoverable resolution rather than an arbitrary, unexplainable pick of one
  project over another.
WHY_IT_MATTERS: >
  A silently arbitrary attribution of an external message to the wrong project misroutes real
  business communication with no way to know it happened.
DISCONFIRMING_OBSERVATION: >
  An incoming message with an ambiguous routing address is attributed to one of several plausible
  projects with no discoverable reason for that choice.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure routing such that an incoming message's address could plausibly match more than one
  project, then send it and inspect how the ambiguity is resolved.
```

## G12-PROJECT_MAIL_PLUGIN-Q002

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q002
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When two replies to the same original message arrive out of their original sending order, the
  resulting task update reflects the actual chronological content rather than silently applying the
  later-arriving reply as if it were the most recent statement.
WHY_IT_MATTERS: >
  Applying messages in arrival order rather than actual chronological order can make an update look
  more current than it really is, or overwrite a more recent statement with an older one.
DISCONFIRMING_OBSERVATION: >
  Two replies to the same message arrive out of chronological order and the task ends up reflecting
  the later-arriving one as the most recent, even though it was actually sent earlier.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Send two replies to the same message out of their true chronological order and inspect which one
  the resulting task treats as most recent.
```

## G12-PROJECT_MAIL_PLUGIN-Q003

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q003
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A message whose attachment fails to transfer completely at capture time still creates a task with
  the available content and a visible indication that an attachment is missing, rather than silently
  dropping the whole message.
WHY_IT_MATTERS: >
  Silently dropping a message because one part of it failed to capture loses potentially
  time-sensitive project communication entirely, with nothing to alert anyone it happened.
DISCONFIRMING_OBSERVATION: >
  A message with a failed attachment transfer produces no resulting task at all, with no trace that a
  message was ever received.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Send a message with an attachment engineered to fail transfer partway through and inspect whether
  any task or record results.
```

## G12-PROJECT_MAIL_PLUGIN-Q004

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q004
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A task created from a captured message is treated by the audit trail as originating from an
  external message rather than indistinguishable from a task a project member typed in directly.
WHY_IT_MATTERS: >
  Losing the distinction between externally originated and internally authored content removes a
  reviewer's ability to judge the reliability and provenance of a task's origin.
DISCONFIRMING_OBSERVATION: >
  A task created from a captured external message shows no indication in its record that it
  originated from an external message rather than direct manual entry.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Capture an external message into a new task and inspect the task's record for an origin indicator.
```

## G12-PROJECT_MAIL_PLUGIN-Q005

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q005
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Attempting to capture a message into a project that has been closed or archived produces an
  explicit exception rather than silently creating a new task on a project the team considers no
  longer active.
WHY_IT_MATTERS: >
  A task silently added to an archived project is unlikely to ever be seen by anyone actually
  monitoring current work.
DISCONFIRMING_OBSERVATION: >
  A message routed to a closed or archived project's capture address results in a new task with no
  exception or warning raised anywhere.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Close or archive a project, then send a message to its capture address and observe the outcome.
```

## G12-PROJECT_MAIL_PLUGIN-Q006

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q006
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If message capture succeeds at the transport level but the subsequent task-creation step fails, the
  message is not silently lost; it is retried, queued visibly, or bounced back in a way that alerts
  someone.
WHY_IT_MATTERS: >
  A message accepted by the channel but never actually turned into project work vanishes with no
  trace and no one aware it ever arrived.
DISCONFIRMING_OBSERVATION: >
  A message accepted at the transport level, whose task creation subsequently fails, leaves no trace,
  retry, or notification anywhere.
EXPECTED_SURFACE: S3,S6,S8
PRECONDITIONS: >
  Cause the task-creation step to fail after a message is accepted at the transport level and check
  for any trace, retry, or notification.
```

## G12-PROJECT_MAIL_PLUGIN-Q007

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q007
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Whether an incoming message can automatically create a task, versus only being queued for manual
  review before becoming one, is governed by an explicit, configurable authority setting, not
  identical behaviour regardless of sender.
WHY_IT_MATTERS: >
  Treating every sender as equally trusted to auto-create project work removes any control over who
  can inject tasks into a team's workload.
DISCONFIRMING_OBSERVATION: >
  A message from an untrusted or external sender automatically creates a task identically to one from
  a fully trusted internal sender, with no distinguishing authority check.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Send comparable messages from a trusted internal sender and an untrusted external sender and
  compare whether task creation is gated differently.
```

## G12-PROJECT_MAIL_PLUGIN-Q008

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q008
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A forwarded copy of a message already captured once does not create a second, duplicate task for
  the same underlying content.
WHY_IT_MATTERS: >
  Duplicate tasks from forwarded copies clutter a project with noise and can cause the same request
  to be worked twice or tracked inconsistently.
DISCONFIRMING_OBSERVATION: >
  Forwarding a message that already created a task results in a second, separate task for the same
  underlying content.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Capture a message into a task, then forward the same message content again to the same capture
  address and inspect whether a duplicate task is created.
```

## G12-PROJECT_MAIL_PLUGIN-Q009

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q009
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A single message with multiple recipients addressed to two different project capture addresses
  does not silently create a single task attributed to only one of the two projects with no trace of
  the other.
WHY_IT_MATTERS: >
  Silently favoring one of two addressed projects loses the other project's legitimate claim to that
  same piece of communication.
DISCONFIRMING_OBSERVATION: >
  A message addressed to two different project capture addresses results in a task on only one
  project, with no trace of the message reaching the other.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Send a single message addressed to two different project capture addresses and inspect the
  resulting tasks on each project.
```

## G12-PROJECT_MAIL_PLUGIN-Q010

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q010
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A reply to a task-related message updates the existing task rather than always creating a new,
  disconnected task, when the reply can be clearly matched to its origin.
WHY_IT_MATTERS: >
  Splitting an ongoing conversation into disconnected tasks fragments the record of what was actually
  discussed and decided.
DISCONFIRMING_OBSERVATION: >
  A clearly identifiable reply to a message that created a task instead creates a wholly separate,
  unrelated task with no link back to the original.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Reply to a message that previously created a task and inspect whether the reply updates that task
  or creates an unrelated new one.
```

## G12-PROJECT_MAIL_PLUGIN-Q011

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q011
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A capture channel's authentication credential expiring or being revoked stops new messages from
  being captured in a way that produces a visible failure indicator, rather than silently and
  invisibly halting capture with the project team unaware anything changed.
WHY_IT_MATTERS: >
  A capture channel that silently stops working leaves a project team believing all incoming
  communication is still being tracked when in fact nothing new is arriving.
DISCONFIRMING_OBSERVATION: >
  Expiring or revoking the capture channel's authentication credential silently stops new message
  capture with no visible failure indicator anywhere.
EXPECTED_SURFACE: S3,S6,S7
PRECONDITIONS: >
  Expire or revoke the capture channel's authentication credential and observe whether any visible
  failure indicator appears.
```

## G12-PROJECT_MAIL_PLUGIN-Q012

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q012
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An automated out-of-office or bulk auto-reply captured by the channel does not itself create a
  project task, since it carries no genuine project content.
WHY_IT_MATTERS: >
  Letting automated auto-replies create tasks fills a project with noise that has no actual work
  content behind it.
DISCONFIRMING_OBSERVATION: >
  An automated out-of-office or bulk auto-reply captured by the channel results in a new project task
  being created.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Send an automated out-of-office style auto-reply to a project's capture address and inspect whether
  a task results.
```

## G12-PROJECT_MAIL_PLUGIN-Q013

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q013
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An oversized attachment on a captured message either is rejected with an explicit notice to the
  sender or handled through a defined size-limit behaviour, not silently truncated or silently
  dropped with the resulting task giving no indication anything was cut.
WHY_IT_MATTERS: >
  A silently truncated attachment can leave a task looking complete while actually missing
  potentially critical content.
DISCONFIRMING_OBSERVATION: >
  A message with an attachment exceeding any defined size limit produces a task with a silently
  truncated or missing attachment and no indication that anything was cut.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Send a message with an attachment exceeding a configured size limit and inspect the resulting task
  and any notice given.
```

## G12-PROJECT_MAIL_PLUGIN-Q014

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q014
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A task created via message capture inherits the project's own configured default visibility, not a
  wider or narrower default unrelated to that project's own settings.
WHY_IT_MATTERS: >
  A captured task defaulting to the wrong visibility could either hide it from the team that needs to
  see it or expose it more broadly than the project intends.
DISCONFIRMING_OBSERVATION: >
  A task created from a captured message has a visibility setting different from the project's own
  configured default, with no explanation for the difference.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure a project's default task visibility, capture a message into it, and inspect the resulting
  task's actual visibility.
```

## G12-PROJECT_MAIL_PLUGIN-Q015

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q015
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Encoding or language-specific corruption in a captured message's subject or body does not silently
  corrupt the resulting task's title or content without any visible indication that corruption
  occurred.
WHY_IT_MATTERS: >
  A silently corrupted title or body can misrepresent a request badly enough to send the work in the
  wrong direction entirely.
DISCONFIRMING_OBSERVATION: >
  A message using characters likely to stress encoding handling produces a visibly corrupted task
  title or body with no indication that anything went wrong.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Send a message with subject and body content likely to stress encoding handling and inspect the
  resulting task for corruption or any warning.
```

## G12-PROJECT_MAIL_PLUGIN-Q016

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q016
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Attachments captured through this channel are subject to the same security scanning as any other
  document entering the system, not a separate, less-governed path that skips it.
WHY_IT_MATTERS: >
  An attachment channel that bypasses standard scanning is an easy, overlooked way for malicious
  content to enter the system.
DISCONFIRMING_OBSERVATION: >
  An attachment captured through an incoming message reaches the project's document space without
  going through the same scanning applied to a directly uploaded document.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Send a message with an attachment and compare the scanning behaviour applied to it against a
  directly uploaded document.
```

## G12-PROJECT_MAIL_PLUGIN-Q017

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q017
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A message whose claimed sender address fails an authenticity check is treated distinctly from a
  verified sender, rather than trusted identically for purposes such as automatic task creation.
WHY_IT_MATTERS: >
  Trusting an unverified, potentially spoofed sender identically to a verified one opens a path for
  impersonated communication to inject trusted-looking work into a project.
DISCONFIRMING_OBSERVATION: >
  A message that fails a sender-authenticity check is captured and treated identically to one from a
  verified sender.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Send a message engineered to fail a sender-authenticity check and compare its handling to a verified
  message.
```

## G12-PROJECT_MAIL_PLUGIN-Q018

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q018
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A confidentiality or sensitivity marking present on a captured message is preserved on the
  resulting task, not silently stripped during capture.
WHY_IT_MATTERS: >
  Losing a sensitivity marking during capture removes a signal that should have governed how the
  resulting task is handled and who can see it.
DISCONFIRMING_OBSERVATION: >
  A message carrying an explicit confidentiality marking produces a task with no trace of that
  marking.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Send a message carrying an explicit confidentiality marking and inspect whether the resulting task
  preserves it.
```

## G12-PROJECT_MAIL_PLUGIN-Q019

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q019
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A project that is archived and later reactivated resumes accepting captured messages without
  requiring the capture channel to be manually reconfigured from scratch.
WHY_IT_MATTERS: >
  A channel that silently stays broken after reactivation means the team believes capture has resumed
  when it has not, and no one is prompted to check.
DISCONFIRMING_OBSERVATION: >
  A reactivated project's capture channel remains non-functional and no indication tells anyone that
  reconfiguration is required.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Archive a project with an active capture channel, reactivate it, and test whether message capture
  resumes.
```

## G12-PROJECT_MAIL_PLUGIN-Q020

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q020
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Re-authenticating a capture channel's credential after a disconnect does not silently repoint that
  channel at a different, wrong project.
WHY_IT_MATTERS: >
  A silently mis-repointed channel would route an entire project's future incoming communication to
  the wrong place, with neither project team aware.
DISCONFIRMING_OBSERVATION: >
  Re-authenticating a disconnected capture channel results in it becoming associated with a different
  project than the one it originally served, with no confirmation step.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Disconnect a project's capture channel credential, then re-authenticate it and verify which project
  it is now associated with.
```

## G12-PROJECT_MAIL_PLUGIN-Q021

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q021
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A batch or bulk import of old, previously forwarded messages assigns each resulting task a timestamp
  reflecting the original message's own date, not the date of the import itself.
WHY_IT_MATTERS: >
  Timestamps reflecting the import date rather than the original message date would mislead any
  audit that assumes chronological ordering of when communication actually happened.
DISCONFIRMING_OBSERVATION: >
  A bulk-imported old message's resulting task is timestamped with the import date rather than the
  message's own original date.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Bulk-import an old, previously sent message and inspect the timestamp on the resulting task.
```

## G12-PROJECT_MAIL_PLUGIN-Q022

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q022
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A different email client's distinct conversation-thread identifier for what is actually the same
  underlying message content does not cause that content to be captured as two unrelated tasks.
WHY_IT_MATTERS: >
  Splitting one underlying communication into two unrelated tasks purely because of a client-specific
  threading quirk fragments a record that should have stayed together.
DISCONFIRMING_OBSERVATION: >
  The same underlying message content, forwarded from a different client with a different thread
  identifier, is captured as a second, unrelated task rather than recognized as the same content.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Send the same underlying message content from two different email clients producing different
  thread identifiers and compare the resulting captured tasks.
```

## G12-PROJECT_MAIL_PLUGIN-Q023

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q023
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An auto-created task's default assignee follows a defined, documented rule, not an arbitrary or
  effectively random pick among project members.
WHY_IT_MATTERS: >
  An unexplainable default assignee means work can land on the wrong person with no rule anyone can
  point to as the cause.
DISCONFIRMING_OBSERVATION: >
  Two comparable captured messages result in tasks defaulting to different assignees with no
  documented rule explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Capture two comparable messages into the same project under similar conditions and compare the
  default assignee each results in.
```

## G12-PROJECT_MAIL_PLUGIN-Q024

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q024
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A message sent to a project's capture address using different letter casing than the address was
  originally configured with is still captured, rather than silently lost due to case sensitivity.
WHY_IT_MATTERS: >
  A message silently lost purely due to letter case is a subtle, hard-to-diagnose way for legitimate
  communication to disappear.
DISCONFIRMING_OBSERVATION: >
  A message sent to a capture address with different letter casing than configured is not captured
  and produces no task.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Send a message to a project's capture address using different letter casing than it was configured
  with and check whether it is captured.
```

## G12-PROJECT_MAIL_PLUGIN-Q025

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q025
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Unlinking an erroneously auto-created task from its originating message preserves the origin
  evidence — what triggered the mistaken creation — rather than losing all trace of why it happened.
WHY_IT_MATTERS: >
  Losing the origin evidence of an erroneous auto-creation prevents anyone from later understanding
  and fixing the root cause of the error.
DISCONFIRMING_OBSERVATION: >
  Unlinking a mistakenly auto-created task from its originating message leaves no retrievable trace of
  what message triggered its creation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Auto-create a task from a message, unlink it as erroneous, and check whether the originating message
  reference is still retrievable.
```

## G12-PROJECT_MAIL_PLUGIN-Q026

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q026
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A task auto-created from an external message is subject to the same required-field validation as a
  manually created task, not exempted from fields the project otherwise requires.
WHY_IT_MATTERS: >
  An exemption for auto-created tasks would let a whole category of project work skip data quality
  rules the team otherwise relies on.
DISCONFIRMING_OBSERVATION: >
  A task auto-created from a captured message is missing a field the project otherwise requires for
  every manually created task, with no validation applied.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure a required field for tasks on a project, capture a message that would not naturally supply
  it, and inspect the resulting task.
```

## G12-PROJECT_MAIL_PLUGIN-Q027

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q027
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a project's capture address is not yet configured, such as immediately after creation from a
  template, a message sent to what would be its address fails safely and visibly, rather than
  disappearing silently with the sender given no indication of failure.
WHY_IT_MATTERS: >
  A silent failure with no bounce or indication leaves the sender believing their message reached the
  project when it never did.
DISCONFIRMING_OBSERVATION: >
  A message sent to a project's not-yet-configured capture address disappears with no bounce, error,
  or any other visible indication of failure.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Create a new project whose capture address is not yet configured, send a message to what would be
  its address, and observe the outcome.
```

## G12-PROJECT_MAIL_PLUGIN-Q028

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q028
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A message containing content marked confidential or internal is not exposed through a
  customer-facing portal view of the resulting task without an explicit visibility decision.
WHY_IT_MATTERS: >
  Automatically surfacing internally marked content to a customer through capture is a direct
  disclosure the business never actually decided to make.
DISCONFIRMING_OBSERVATION: >
  A captured message marked confidential or internal results in content visible through a
  customer-facing portal view with no explicit visibility decision made.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Capture a message marked confidential or internal into a task on a project with a customer-facing
  portal and inspect what the portal view exposes.
```

## G12-PROJECT_MAIL_PLUGIN-Q029

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q029
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The default internal-only versus customer-visible status a captured task receives matches the
  specific project's own configured default, not an unrelated system-wide default that ignores
  per-project configuration.
WHY_IT_MATTERS: >
  A system-wide default that overrides a project's own configured visibility choice defeats the
  purpose of letting each project set that choice at all.
DISCONFIRMING_OBSERVATION: >
  A captured task's internal/customer-visible default does not match the specific project's own
  configured setting.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a project-specific default visibility different from the general system default, capture
  a message into it, and inspect the resulting task's actual visibility.
```

## G12-PROJECT_MAIL_PLUGIN-Q030

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q030
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A reply-notification sent from a task update back to the original external sender does not create
  an unbounded loop when that external system also sends automatic replies of its own.
WHY_IT_MATTERS: >
  An unbounded notification loop between two automated systems can flood both sides and obscure
  genuine communication in the noise.
DISCONFIRMING_OBSERVATION: >
  A reply-notification sent to an external sender whose own system auto-replies results in an
  unbounded cycle of notifications with no loop-prevention observed.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Set up an external sender whose system automatically replies to any incoming notification, trigger a
  task update notification to that sender, and observe whether a loop forms.
```

## G12-PROJECT_MAIL_PLUGIN-Q031

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q031
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The rate at which a single external sender can trigger new task creation is bounded by a defined
  limit, so a flood of messages from one source does not overwhelm a project with an unbounded number
  of new tasks.
WHY_IT_MATTERS: >
  An unbounded flood of auto-created tasks from one misbehaving or malicious source can bury genuine
  project work under noise.
DISCONFIRMING_OBSERVATION: >
  A rapid flood of messages from a single external sender each creates a separate task with no rate
  limit or throttling observed.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Send a rapid succession of messages from a single external sender to a project's capture address and
  observe whether any limit applies.
```

## G12-PROJECT_MAIL_PLUGIN-Q032

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q032
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When message capture is disabled temporarily for maintenance, messages sent during that window are
  queued and processed afterward rather than lost outright.
WHY_IT_MATTERS: >
  Losing every message sent during a maintenance window means legitimate communication disappears for
  a reason entirely unrelated to the sender.
DISCONFIRMING_OBSERVATION: >
  A message sent while capture is disabled for maintenance is never processed once capture resumes.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Disable capture temporarily, send a message during the window, re-enable capture, and check whether
  the message is eventually processed.
```

## G12-PROJECT_MAIL_PLUGIN-Q033

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q033
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A message captured into the wrong project by sender error can be reassigned to the correct project
  through a defined action that preserves its original content and origin trace, distinct from having
  to manually recreate it as a brand-new task.
WHY_IT_MATTERS: >
  Forcing a manual recreation of a misrouted message loses its original origin trace and duplicates
  effort that a proper reassignment would avoid.
DISCONFIRMING_OBSERVATION: >
  Correcting a misrouted captured message requires deleting the wrong task and manually recreating it,
  losing its original origin trace, rather than a defined reassignment action.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Capture a message into the wrong project by simulated sender error, then attempt to correct the
  routing to the right project.
```

## G12-PROJECT_MAIL_PLUGIN-Q034

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q034
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A captured task's title, when auto-derived from a message's subject line, does not silently
  truncate meaningful content without any indication that truncation occurred.
WHY_IT_MATTERS: >
  A silently truncated title can hide the actual substance of a request from anyone scanning a task
  list.
DISCONFIRMING_OBSERVATION: >
  A message with a long subject line produces a task title that is truncated with no indication that
  truncation happened.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Send a message with a subject line long enough to test any title-length limit and inspect the
  resulting task title.
```

## G12-PROJECT_MAIL_PLUGIN-Q035

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q035
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A project's capture address, once retired or changed, does not allow a message sent to the old
  address to be captured into an unrelated, later-created project that happens to reuse a similar
  address pattern.
WHY_IT_MATTERS: >
  A retired address that silently feeds an unrelated new project misroutes communication meant for
  one business context into a completely different one.
DISCONFIRMING_OBSERVATION: >
  A message sent to a retired capture address is captured into a different, unrelated project that
  later reused a similar address pattern.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Retire a project's capture address, create an unrelated new project with a similarly patterned
  address, and send a message to the old, retired address.
```

## G12-PROJECT_MAIL_PLUGIN-Q036

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q036
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Concurrent processing of two unrelated incoming messages does not result in content from one being
  attributed to the task created for the other.
WHY_IT_MATTERS: >
  Cross-attributed content between two unrelated messages could misrepresent either or both requests
  entirely.
DISCONFIRMING_OBSERVATION: >
  Sending two unrelated messages to be captured at nearly the same time results in content from one
  appearing on the task created for the other.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Send two unrelated messages for capture at nearly the same time and inspect whether their content
  stays correctly separated in the resulting tasks.
```

## G12-PROJECT_MAIL_PLUGIN-Q037

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q037
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An attachment captured from an external message is stored in the project's own document space under
  the same access-permission rules as an internally uploaded document, not a separate, less-governed
  storage location.
WHY_IT_MATTERS: >
  A separate, less-governed storage path for captured attachments creates an inconsistent, easily
  overlooked gap in document access control.
DISCONFIRMING_OBSERVATION: >
  An attachment captured from an external message is accessible to someone who would be denied access
  to an equivalent internally uploaded document on the same project.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Capture a message with an attachment and compare the access permissions on it to those on an
  equivalent, internally uploaded document on the same project.
```

## G12-PROJECT_MAIL_PLUGIN-Q038

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q038
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A follow-up message that only quotes an earlier captured message, but is sent by a different,
  unrelated sender, is not silently merged into the original sender's task thread as though it came
  from that original sender.
WHY_IT_MATTERS: >
  Merging content by a different sender into another sender's thread misattributes who actually said
  what, which matters whenever the content carries any weight or accountability.
DISCONFIRMING_OBSERVATION: >
  A message from a different, unrelated sender that merely quotes an earlier captured message is
  merged into the original sender's task thread as though it came from them.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message from a different sender that quotes an already-captured message and inspect how it
  is attributed on the resulting task thread.
```

## G12-PROJECT_MAIL_PLUGIN-Q039

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q039
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where the capture channel is configured per company in a multi-company environment, a message
  captured under one company's channel is not attributed to a project belonging to a different company
  without an explicit cross-company step.
WHY_IT_MATTERS: >
  Company-scoped incoming communication crossing into an unrelated company's project is the same
  boundary failure any other cross-company data leak would be.
DISCONFIRMING_OBSERVATION: >
  A message captured through one company's capture channel is attributed to a project belonging to a
  different company with no explicit cross-company authorization.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure separate per-company capture channels and attempt to have a message captured under one
  company attributed to a project in a different company.
```

## G12-PROJECT_MAIL_PLUGIN-Q040

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q040
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A captured task's association with the message that created it survives a later change to how the
  project itself is categorized or restructured, rather than losing that link.
WHY_IT_MATTERS: >
  Losing the link between a task and its originating message during a routine reorganization removes
  the ability to later explain that task's origin.
DISCONFIRMING_OBSERVATION: >
  After a project is restructured or recategorized, a previously captured task's link to its
  originating message can no longer be found.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Capture a message into a task, restructure or recategorize the project, and inspect whether the
  task's link to its originating message survives.
```

## G12-PROJECT_MAIL_PLUGIN-Q041

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q041
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an external message source itself edits or recalls a message after it was already captured,
  the resulting task is not silently and retroactively altered to match the edited version without a
  visible record that a change occurred.
WHY_IT_MATTERS: >
  A task that silently changes to match a later edit could quietly rewrite what was actually
  requested, with no trace that the original differed.
DISCONFIRMING_OBSERVATION: >
  A captured task's content changes to match a subsequently edited or recalled version of the source
  message with no visible record that a change occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Capture a message into a task, then edit or recall that message at its source, and inspect whether
  the task changes and whether any record of the change exists.
```

## G12-PROJECT_MAIL_PLUGIN-Q042

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q042
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A message captured outside a project's normal operating hours or business calendar is timestamped
  with its actual receipt time, not shifted to appear as if received during business hours.
WHY_IT_MATTERS: >
  A shifted timestamp misrepresents exactly when a piece of communication actually arrived, which
  matters for any later timing-based investigation.
DISCONFIRMING_OBSERVATION: >
  A message received outside normal operating hours is timestamped as if received during business
  hours instead of its actual receipt time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message outside the project's normal operating hours and inspect the timestamp recorded on
  the resulting task.
```

## G12-PROJECT_MAIL_PLUGIN-Q043

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q043
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where multiple project capture addresses exist for closely related projects, a message sent to a
  similar but wrong address is not silently redirected to a different project without any indication
  that redirection occurred.
WHY_IT_MATTERS: >
  A silent redirection based on address similarity could route sensitive or urgent communication to a
  project the sender never actually intended.
DISCONFIRMING_OBSERVATION: >
  A message sent to a wrong but similarly patterned capture address is captured into a different
  project with no indication that a redirection took place.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Set up two closely related projects with similarly patterned capture addresses and send a message to
  the wrong one.
```

## G12-PROJECT_MAIL_PLUGIN-Q044

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q044
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The permission to disable or reconfigure a project's message-capture channel is distinct from
  ordinary project-editing permission.
WHY_IT_MATTERS: >
  Bundling channel reconfiguration into ordinary editing rights lets anyone who can edit a project
  also silently redirect or shut off its entire incoming-communication channel.
DISCONFIRMING_OBSERVATION: >
  An account with ordinary project-editing rights, but no distinct capture-channel permission, is able
  to disable or reconfigure that project's capture channel.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  From an account with ordinary project-editing rights but no distinct capture-channel grant, attempt
  to disable or reconfigure the project's message-capture channel.
```

## G12-PROJECT_MAIL_PLUGIN-Q045

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q045
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A message captured into a task whose project is later merged with another project preserves its
  original-project provenance in the merged history, rather than appearing as if it always belonged to
  the merged destination.
WHY_IT_MATTERS: >
  Losing original provenance after a merge makes it impossible to later tell which of the two merged
  projects a piece of communication actually first belonged to.
DISCONFIRMING_OBSERVATION: >
  After a project merge, a captured task's history shows no trace of which of the two original
  projects it actually came from.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Capture a message into a task on one project, merge that project into another, and inspect the
  resulting task for original-project provenance.
```

## G12-PROJECT_MAIL_PLUGIN-Q046

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q046
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an external sender's reply arrives after the task it would have updated has already been
  permanently deleted, the reply is preserved in some recoverable form rather than discarded with its
  content unrecoverable.
WHY_IT_MATTERS: >
  A reply silently discarded because its target task no longer exists loses potentially important
  communication with no trace it ever arrived.
DISCONFIRMING_OBSERVATION: >
  A reply arriving after its target task's permanent deletion is discarded entirely with no
  recoverable trace anywhere.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Permanently delete a task that originated from a captured message, then send a reply to that
  original message and check whether it is preserved anywhere.
```

## G12-PROJECT_MAIL_PLUGIN-Q047

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q047
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A message with no plausible meaningful content, such as an empty body containing only a signature
  block, is still captured with a defined minimal task representation, not silently discarded as
  though it were spam with no distinguishing log.
WHY_IT_MATTERS: >
  Silently discarding a near-empty message without any log makes it impossible to later distinguish a
  deliberate filter decision from a capture failure.
DISCONFIRMING_OBSERVATION: >
  A message with no meaningful body content beyond a signature block produces no task and no log entry
  of any kind.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message with an empty body containing only a signature block and inspect what, if anything,
  results.
```

## G12-PROJECT_MAIL_PLUGIN-Q048

```yaml
QID: G12-PROJECT_MAIL_PLUGIN-Q048
MODULE: project_mail_plugin
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The complete lifecycle of a captured message — receipt, project attribution, task creation, and any
  subsequent linked reply — can be reconstructed end to end from stored evidence alone.
WHY_IT_MATTERS: >
  If this chain cannot be reconstructed, no later dispute about what an external party actually sent,
  and when, can be resolved from the record.
DISCONFIRMING_OBSERVATION: >
  Attempting to reconstruct the full lifecycle of a captured message and its subsequent linked reply
  from stored records alone leaves a gap.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Capture a message into a task, exchange at least one linked reply, and attempt to reconstruct the
  full lifecycle from stored records alone.
```
