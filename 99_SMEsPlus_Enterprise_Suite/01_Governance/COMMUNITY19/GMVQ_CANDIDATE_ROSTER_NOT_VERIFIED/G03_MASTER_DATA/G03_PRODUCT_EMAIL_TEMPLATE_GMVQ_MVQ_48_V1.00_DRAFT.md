# SMEsPlus ENTERPRISE SUITE
## GMVQ — G03 MASTER_DATA / product_email_template Module MVQ Bank

**Document ID:** GMVQ-G03-PRODUCT_EMAIL_TEMPLATE-MVQ48-V1.00
**Group:** G03 MASTER_DATA
**Module Metadata:** `product_email_template`
**Wave:** W1
**Author Cell:** TEAM 17 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This bank supplies the module-specific MVQ set for `product_email_template`, outbound message templates bound to a master item record. The material ground is entitlement and fidelity of what is actually sent: whether a template can surface data the recipient is not entitled to see, whether it renders under the sender's rights instead of the recipient's, per-company and per-language template selection and its fallback, what a changed template shows for messages already sent, a template's behaviour when its referenced item record is later archived or renamed, attachments and pricing resolved at send time versus at queue time, and auditability of what was actually delivered. Coverage is spread across business capability, business rule, state transition, configuration dependency, role and permission, exception path, cancellation, reversal, negative case, cross-module dependency, optional behaviour, auditability, tenant/company boundary, concurrency and ordering, runtime reachability, configuration reachability, and source/runtime contradiction potential. This bank supplements the 35-question Standard bank; combined research depth for this module is 35 + 48 = 83.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses; none was trimmed or stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table, field, method, XML ID, API path), and the module's own metadata name never appears outside the `MODULE:` field — the generic terms "item record" and "outbound message" / "template" stand in for it throughout.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready. Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G03-PRODUCT_EMAIL_TEMPLATE-Q001

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q001
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An outbound message template does not surface data fields to a recipient that the recipient would not otherwise be entitled to view directly.
WHY_IT_MATTERS: >
  A template can become a side channel that leaks internally sensitive figures to an external party who has no direct access to see them.
DISCONFIRMING_OBSERVATION: >
  A rendered outbound message to an external recipient includes a data value that the recipient has no permission to view through any direct-access path.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Identify a data field the recipient has no direct viewing permission for, reference it in a template, and inspect the rendered message sent to that recipient.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q002

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q002
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An outbound message template renders its content using the recipient's entitlement to the referenced data, not the sending user's broader access rights.
WHY_IT_MATTERS: >
  Rendering under the sender's rights turns every privileged sender into an unintentional channel for exposing data the recipient was never meant to see.
DISCONFIRMING_OBSERVATION: >
  The same template sent by two different senders with different access levels produces different rendered content for the same recipient, reflecting the sender's access rather than the recipient's.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Send the same template to the same recipient from two sending users with different access levels to the referenced data, and compare the rendered content.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q003

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q003
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When more than one company can send under a shared template configuration, the specific variant that resolves for a given message is chosen according to the sending company, and one company's variant never resolves for another company's send.
WHY_IT_MATTERS: >
  The wrong company's variant resolving would put another company's branding, contact details, or legal wording into a message it did not send.
DISCONFIRMING_OBSERVATION: >
  A message sent under one company resolves to a template variant configured for a different company.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure distinct per-company template variants for the same purpose, then trigger a send under each company and compare which variant is used.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q004

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q004
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The language variant of an outbound message is derived from the recipient's own stored language preference, not from the sending user's active session language.
WHY_IT_MATTERS: >
  Deriving the language from the sender rather than the recipient would send messages in a language the actual recipient may not read.
DISCONFIRMING_OBSERVATION: >
  The same recipient with a stored language preference receives a message in a different language purely because the sender's session language differed.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set a recipient's stored language preference, then trigger the same template from sending sessions in two different languages and compare the recipient's rendered message.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q005

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q005
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When no per-company template variant exists for a sending company, a defined default variant is used consistently, rather than the send failing or resolving to an arbitrary variant.
WHY_IT_MATTERS: >
  An undefined fallback for a missing company variant means some companies' messages either fail silently or go out with unpredictable content.
DISCONFIRMING_OBSERVATION: >
  A sending company with no configured variant of its own produces a send that fails, or resolves to a variant that differs from one attempt to the next with no configuration change between them.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Remove or never configure a per-company variant for a sending company, trigger a send more than once, and compare the resolved content each time.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q006

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q006
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When no per-language variant exists for a recipient's stored language, the message falls back to a defined default language rather than failing to send or producing an untranslated mixture.
WHY_IT_MATTERS: >
  A failed or malformed fallback for a missing language variant means recipients in less-common languages are silently underserved.
DISCONFIRMING_OBSERVATION: >
  A recipient whose stored language has no authored variant either receives no message at all or receives one mixing content from more than one language with no coherent fallback.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set a recipient's language to one with no authored template variant, trigger a send, and inspect the outcome.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q007

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q007
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Editing a template's content after a message using an earlier version was already sent does not change what that already-sent message shows when it is later reopened or reviewed.
WHY_IT_MATTERS: >
  A sent message that silently changes its displayed content after the fact would make it impossible to know what a recipient actually originally received.
DISCONFIRMING_OBSERVATION: >
  Reopening a record of a previously sent message shows content reflecting the template as it exists now, rather than as it existed at the moment the message was sent.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message using a template, edit the template's content afterward, then reopen the record of the earlier sent message.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q008

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q008
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Each sent message is preserved with an actual snapshot of what was rendered and delivered at send time, not merely a reference back to the current state of the template.
WHY_IT_MATTERS: >
  Without a true snapshot, there is no way to reconstruct what a recipient actually received once the template has moved on.
DISCONFIRMING_OBSERVATION: >
  The record of a sent message contains only a reference to the template rather than the actual rendered content, and that reference now resolves to different content than what was originally sent.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message, materially change the underlying template afterward, and inspect whether the sent-message record still shows the original rendered content.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q009

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q009
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A template referencing an item record that is later archived still renders without error for any subsequent trigger, either by using the archived record's last known values or by a defined, visible fallback.
WHY_IT_MATTERS: >
  An unhandled error from an archived reference could block an entire category of outbound messages with no clear cause.
DISCONFIRMING_OBSERVATION: >
  A send attempt referencing a now-archived item record fails outright with an unhandled error rather than rendering with the archived record's values or a defined fallback.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Archive an item record referenced by a template, then trigger a new send that would reference it.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q010

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q010
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an item record referenced by a template is renamed, previously sent messages continue to display the name as it was at the time they were sent, not the current name.
WHY_IT_MATTERS: >
  A historical message that silently updates to a new name misrepresents what the recipient was actually told at the time.
DISCONFIRMING_OBSERVATION: >
  A previously sent message's stored record displays the item's current name rather than the name in effect when the message was sent.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message referencing an item record by name, rename that item record afterward, then reopen the record of the earlier sent message.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q011

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q011
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Any attachment generated for an outbound message reflects the data as it existed at the moment of actual dispatch, not the data as it existed when the message was first queued.
WHY_IT_MATTERS: >
  An attachment frozen at queue time can go stale if the underlying data changes before a delayed dispatch actually occurs, misinforming the recipient.
DISCONFIRMING_OBSERVATION: >
  A generated attachment on a delayed send reflects data from the moment of queuing rather than data current at the moment of actual dispatch, after the underlying data changed in between.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Queue a message with a generated attachment, change the underlying referenced data before dispatch actually occurs, and inspect the attachment content at dispatch.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q012

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q012
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A pricing figure referenced in an outbound message reflects the price current at actual dispatch time, not a price captured earlier when the message was queued, unless the message is explicitly defined to lock the price at queue time.
WHY_IT_MATTERS: >
  A recipient quoted a stale price that no longer matches what will actually be charged creates a customer-facing discrepancy and potential dispute.
DISCONFIRMING_OBSERVATION: >
  A recipient receives a message quoting a price that differs from the price actually in effect at dispatch, with no documented rule stating the price is meant to be locked at queue time.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Queue a message referencing a priced item, change the price before dispatch, and compare the price shown in the delivered message against the price in effect at dispatch.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q013

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q013
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  For any given sent message, the exact content and any attachments actually delivered to a specific recipient at a specific time can be fully reconstructed after the fact.
WHY_IT_MATTERS: >
  The inability to reconstruct exactly what was sent to whom and when defeats any later investigation of a customer complaint or compliance question.
DISCONFIRMING_OBSERVATION: >
  A request to reconstruct exactly what content and attachments a specific recipient received at a specific past time cannot be fully satisfied from the retained records.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message with content and an attachment to a specific recipient, then attempt to reconstruct exactly what was delivered from the retained records alone.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q014

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q014
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A user without permission to view an item record's internal cost figure cannot trigger a template send that would cause that figure to be included in the rendered message, whether to themselves or to a third party.
WHY_IT_MATTERS: >
  Triggering a template is a supported action separate from direct viewing, and if it bypasses the same permission it becomes an unguarded path to the same sensitive data.
DISCONFIRMING_OBSERVATION: >
  A user without cost-viewing permission successfully triggers a send whose rendered content includes the cost figure.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Assign a role with template-trigger rights but no cost-viewing permission, and have that role trigger a send referencing an item record's cost figure.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q015

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q015
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When rendering fails partway through because required data is missing, the send is blocked entirely rather than delivering a partially rendered message to the recipient.
WHY_IT_MATTERS: >
  A partially rendered message reaching a recipient can expose broken placeholders, error text, or worse, an incomplete but plausible-looking figure.
DISCONFIRMING_OBSERVATION: >
  A recipient receives a message with missing or broken content where required data was unavailable, rather than the send being blocked before dispatch.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Remove or block access to a data field the template requires, trigger a send, and observe whether the recipient receives a partial message or the send is blocked.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q016

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q016
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A template containing a reference to a value that cannot resolve is caught and flagged before any send is attempted, rather than reaching the recipient as a visible error string or broken placeholder.
WHY_IT_MATTERS: >
  A recipient seeing an error string or broken placeholder in a real business communication damages professionalism and can also leak internal implementation detail.
DISCONFIRMING_OBSERVATION: >
  A message is delivered to a recipient containing a visible error string, broken placeholder, or unresolved reference marker.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Author a template with a reference to a value known not to resolve for a test case, and trigger a send to see what the recipient receives.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q017

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q017
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two send triggers for the same template, same recipient, and same triggering event occurring close together in time do not both result in the recipient receiving a duplicate message.
WHY_IT_MATTERS: >
  Unintended duplicate messages to the same recipient look unprofessional at best and can cause real confusion when the content includes time-sensitive figures.
DISCONFIRMING_OBSERVATION: >
  The same recipient receives two identical messages for what was a single triggering event, sent within a short time of each other.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger the same template send twice in rapid succession for the same recipient and event, and check whether both are delivered.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q018

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q018
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A template scoped to one company cannot be used to send a message that appears to originate from a different company's identity.
WHY_IT_MATTERS: >
  A message misrepresenting its sending company would confuse the recipient about who they are actually dealing with and could carry legal or branding consequences.
DISCONFIRMING_OBSERVATION: >
  A send using a template scoped to one company produces a message whose sender identity, contact details, or branding belong to a different company.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Scope a template to one company and attempt to trigger a send under a different company's context.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q019

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q019
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Enabling a multi-language configuration at the tenant level does not silently cause every existing template, previously authored for a single language, to be treated as fully multi-language without an explicit authoring step for the new languages.
WHY_IT_MATTERS: >
  Assuming existing single-language content magically covers new languages would send recipients content in a language they did not choose, under the appearance of proper localization.
DISCONFIRMING_OBSERVATION: >
  After enabling multi-language configuration, a recipient with a different stored language than the original template still receives content in the original language with no indication it is a fallback.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Author a template in a single language, enable multi-language configuration afterward, and trigger a send to a recipient with a different stored language.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q020

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q020
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling a queued send before it dispatches fully retracts the message; no message is delivered to the recipient after a successful cancellation.
WHY_IT_MATTERS: >
  A cancellation that only appears to succeed while the message still dispatches undermines the entire purpose of having a cancel action.
DISCONFIRMING_OBSERVATION: >
  A recipient receives a message whose send was reported as successfully cancelled before dispatch.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Queue a send with a delay, cancel it before dispatch, and confirm afterward whether the recipient received anything.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q021

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q021
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a defective message is corrected by re-sending, the record retains both the original defective send and the corrected send as distinct events, rather than the correction overwriting the record of the original.
WHY_IT_MATTERS: >
  Losing the record of an originally defective send erases the evidence needed to understand what a recipient may have seen before the correction went out.
DISCONFIRMING_OBSERVATION: >
  After a corrected re-send, only the corrected message's record remains retrievable, with no trace that a defective version was ever sent.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message with a known defect, then correct and resend it, and check whether both the original and corrected sends remain separately retrievable.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q022

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q022
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Messages queued while a template was in a draft or inactive state either do not dispatch until the template is active, or are clearly blocked, rather than dispatching using incomplete draft content.
WHY_IT_MATTERS: >
  Dispatching content that was never finished being authored risks sending recipients incomplete or placeholder material.
DISCONFIRMING_OBSERVATION: >
  A message queued against a draft or inactive template dispatches to a recipient before the template is made active.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Set a template to draft or inactive, attempt to queue a send referencing it, and observe whether dispatch occurs before activation.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q023

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q023
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A template is prevented from referencing a data field that policy currently marks as forbidden for outbound communication, and this restriction is enforced at authoring time, not discovered only after a message has already gone out.
WHY_IT_MATTERS: >
  Discovering a policy violation only after a message is delivered means the exposure has already occurred and cannot be undone.
DISCONFIRMING_OBSERVATION: >
  A template referencing a currently forbidden data field is saved and later used to send a message before the restriction is caught.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Mark a data field as forbidden for outbound communication, then attempt to author and save a template referencing that field.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q024

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q024
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether an attachment is generated for a given send is a configurable choice on the template rather than unconditionally hardwired into every send regardless of context.
WHY_IT_MATTERS: >
  An unconditionally hardwired attachment forces every recipient to receive a document that may not be relevant or wanted for a particular trigger.
DISCONFIRMING_OBSERVATION: >
  An attachment intended to be optional is generated and delivered on every send with no configuration able to suppress it for a specific case.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Configure a template with an attachment marked as optional, and attempt to trigger a send where the attachment should be suppressed.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q025

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q025
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A background or automated trigger for a template send enforces the same permission and approval requirements as a manually initiated send of the same template.
WHY_IT_MATTERS: >
  An automated path with weaker enforcement than the manual path is an unguarded back door around a control that exists specifically to gate that message.
DISCONFIRMING_OBSERVATION: >
  An automated trigger successfully sends a message that a manual attempt by the same effective actor would have been blocked from sending.
EXPECTED_SURFACE: S1,S4,S8
PRECONDITIONS: >
  Identify a permission or approval requirement enforced on manual sends, then trigger the same template through an automated or background path and compare enforcement.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q026

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q026
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Any override allowing a specific user to bypass normal per-company or per-language template resolution is itself gated by a distinct, auditable permission rather than reachable through ordinary send actions.
WHY_IT_MATTERS: >
  An unguarded resolution override would let an ordinary user quietly send content intended only for a different company or language audience.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary send rights can override the normal per-company or per-language resolution with no distinct permission check or audit trace.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Locate any override path for template resolution and check what permission and audit trace it requires.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q027

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q027
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to the classification or category of the item record a template references does not silently change what data fields that template is permitted to display without an explicit re-authoring step.
WHY_IT_MATTERS: >
  An automatic widening of what a template may display, triggered only by a classification change elsewhere, could expose new data with no one having reviewed the template for it.
DISCONFIRMING_OBSERVATION: >
  A template begins rendering a data field it did not render before, purely because the referenced item record's classification changed, with no edit made to the template itself.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Author a template referencing a field gated by the item record's classification, then change that classification and observe the rendered output without editing the template.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q028

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q028
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The actual resolved recipient list used for a specific sent message — including any addresses added beyond the template's default rule — is captured and retrievable per message, distinct from the template's general default configuration.
WHY_IT_MATTERS: >
  Without a per-message record of who actually received it, an investigation into an over-broad or misdirected send has nothing concrete to examine.
DISCONFIRMING_OBSERVATION: >
  The record of a sent message shows only the template's default recipient rule, not the actual list of addresses the message was delivered to for that specific send.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message with a recipient list that differs from the template's plain default, then check whether the sent-message record captures the actual list used.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q029

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q029
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A manual, user-initiated send of a template and an automated trigger of the same template produce equivalent rendered content when given equivalent input data.
WHY_IT_MATTERS: >
  A divergence between the two paths means the same nominal template can produce two different customer experiences depending purely on how it was triggered.
DISCONFIRMING_OBSERVATION: >
  The same template rendered manually and rendered through an automated trigger, with equivalent underlying data, produces materially different content.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Trigger the same template once manually and once through an automated path with equivalent underlying data, and compare the rendered content.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q030

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q030
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dispatch failure such as an invalid or bouncing recipient address is surfaced to the sender or an accountable party rather than silently disappearing as if the message succeeded.
WHY_IT_MATTERS: >
  A silently failed send that appears successful means a recipient who should have been informed of something never was, with no one aware of the gap.
DISCONFIRMING_OBSERVATION: >
  A send to an invalid address fails without any surfaced notice, and the sender's record of the event shows it as having succeeded.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Trigger a send to a known-invalid recipient address and check whether the failure is surfaced anywhere the sender or an accountable party would see it.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q031

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q031
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A recipient who has opted out or unsubscribed between the time a message was queued and the time it would dispatch does not receive that message.
WHY_IT_MATTERS: >
  Delivering to an opted-out recipient after their opt-out was recorded is both a broken promise to the recipient and a potential compliance exposure.
DISCONFIRMING_OBSERVATION: >
  A recipient who opted out after a message was queued but before dispatch still receives that message.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Queue a delayed send to a recipient, have that recipient opt out before dispatch, and check whether the message is still delivered.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q032

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q032
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Data belonging to an item record scoped to one tenant is never rendered into a message sent under a different tenant's context, even when both tenants happen to use templates with the same name or structure.
WHY_IT_MATTERS: >
  Cross-tenant data appearing in an outbound message would be a severe isolation breach visible directly to an external recipient.
DISCONFIRMING_OBSERVATION: >
  A message sent under one tenant's context renders data belonging to an item record scoped to a different tenant.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create similarly named or structured templates and item records under two distinct tenants, then trigger a send under one tenant and inspect for any leakage of the other tenant's data.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q033

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q033
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Archiving a template while messages referencing it are still queued either completes those queued sends using the content as it stood at queue time, or explicitly blocks them — it does not leave them in an indeterminate state.
WHY_IT_MATTERS: >
  An indeterminate outcome for queued sends after their template is archived means no one can predict or verify whether recipients will actually receive anything.
DISCONFIRMING_OBSERVATION: >
  A message queued before its template was archived remains pending indefinitely with no dispatch and no failure notice after the archiving.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Queue a delayed send referencing a template, archive that template before dispatch, and observe the outcome.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q034

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q034
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The same triggering event does not cause the same templated message to be sent to the same recipient more than once, even if the triggering condition is evaluated repeatedly.
WHY_IT_MATTERS: >
  Repeated sends for a single real-world event erode recipient trust and can misrepresent that something happened more than once when it did not.
DISCONFIRMING_OBSERVATION: >
  A single triggering event results in the same recipient receiving the same templated message more than once.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Construct a triggering condition that could plausibly be evaluated more than once for the same event, and check whether the recipient receives duplicate messages.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q035

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q035
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A company-level branding or signature configuration is applied on top of the template's own content in a defined, documented way — either merging or overriding a specific section — rather than in a way that varies unpredictably by template.
WHY_IT_MATTERS: >
  Unpredictable interaction between company branding and template content could produce a message with a garbled or contradictory identity.
DISCONFIRMING_OBSERVATION: >
  The same company-level branding configuration produces a materially different placement or override outcome across two otherwise-comparable templates with no configuration difference between them.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply the same company-level branding configuration across two comparable templates and compare how each renders it.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q036

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q036
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Previewing a template with real data before sending renders under the same recipient-entitlement rules that would apply at actual send time, not under a neutral or unrestricted preview context.
WHY_IT_MATTERS: >
  A preview that shows more than the real send would let the previewer see data that the actual recipient is not entitled to, defeating the purpose of a faithful preview.
DISCONFIRMING_OBSERVATION: >
  A preview of a template shows a data field to the previewer that would not have been included in the actual message delivered to the real recipient.
EXPECTED_SURFACE: S1,S4,S5
PRECONDITIONS: >
  Configure a data field to be included only for certain recipient entitlements, then preview the template with a recipient who would not qualify and compare against an actual send.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q037

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q037
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to a template's content is captured with who made the change and when, distinguishable from an earlier version of the same template.
WHY_IT_MATTERS: >
  Without a change history, there is no way to determine when a template began producing a particular piece of content or who introduced it.
DISCONFIRMING_OBSERVATION: >
  A template's content differs from an earlier known state with no retrievable record of who changed it or when.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Edit a template's content, then attempt to retrieve who made the change and when from the system's own records.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q038

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q038
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Removing support for a language that a template was authored in is surfaced as a flagged condition on that template rather than silently leaving it to fail or fall back at the next send with no warning beforehand.
WHY_IT_MATTERS: >
  A silent failure discovered only at send time means the gap is found by an actual recipient not receiving something, rather than by proactive review.
DISCONFIRMING_OBSERVATION: >
  Language support for a template's authored language is removed, and no flag or warning appears on that template before its next send attempt.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Author a template in a specific language, remove support for that language at the configuration level, and check whether the template is flagged before its next use.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q039

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q039
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Currency and price formatting in a rendered message follow a documented, consistent rule for whether they reflect the sending company's convention or the recipient's, and that rule does not vary unpredictably between otherwise similar sends.
WHY_IT_MATTERS: >
  Inconsistent currency or format resolution could misrepresent an amount in a way that leads to a real pricing misunderstanding with the recipient.
DISCONFIRMING_OBSERVATION: >
  Two otherwise comparable sends to recipients in different regions show currency or number formatting resolved by two different rules with no configuration explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Send comparable messages to recipients associated with different regions and compare which formatting convention each uses.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q040

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q040
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A template variable that resolves to an empty or null value renders as a defined, graceful placeholder or is omitted, rather than as a raw error token or a broken-looking gap in the message.
WHY_IT_MATTERS: >
  A raw error token or obviously broken gap reaching a recipient undermines the professionalism of the communication and may confuse them about what was intended.
DISCONFIRMING_OBSERVATION: >
  A message delivered to a recipient shows a raw error token, a literal null marker, or an obviously broken gap where a variable failed to resolve.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct a scenario where a template variable resolves to empty or null, trigger a send, and inspect the delivered content.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q041

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q041
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A background or scheduled digest process that reuses a template renders against data that is as fresh as what a manual send at the same moment would use, not against a stale snapshot from an earlier point.
WHY_IT_MATTERS: >
  A digest process silently using stale data would tell recipients something was true at send time when it had actually already changed.
DISCONFIRMING_OBSERVATION: >
  A scheduled digest message shows data that differs from the actual current state at the moment the digest was sent, in a way a manual send at the same moment would not have.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Change underlying data shortly before a scheduled digest is due, then compare the digest's rendered content against the actual current state at send time.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q042

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q042
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Editing a template that is actively used by production sends does not allow a mid-edit, incomplete version of that template to be used by a send that happens to be triggered during the edit.
WHY_IT_MATTERS: >
  A send capturing a half-edited template could deliver malformed or contradictory content to a real recipient purely due to timing.
DISCONFIRMING_OBSERVATION: >
  A send triggered while a template is being actively edited delivers content reflecting an incomplete, in-progress edit rather than either the prior saved version or the fully saved new version.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Begin editing a template without saving, trigger a send referencing it during the edit, and inspect which version of the content the send used.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q043

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q043
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a template is edited mid-way through dispatching a batch of queued messages, every recipient in that batch receives content from a single, consistent version of the template rather than a mix of pre-edit and post-edit content across the batch.
WHY_IT_MATTERS: >
  A mixed-version batch means some recipients receive materially different content than others for what was meant to be one uniform communication.
DISCONFIRMING_OBSERVATION: >
  Recipients within the same dispatched batch receive content from two different versions of the same template, split by when their individual message happened to render relative to the edit.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Queue a large batch of sends from one template, edit the template mid-dispatch, and compare the content received across different recipients in the batch.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q044

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q044
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A test send to an internal address is distinguishable in the retained records from a genuine send to a real external recipient, so it does not inflate or contaminate metrics or audit trails meant to reflect actual customer communication.
WHY_IT_MATTERS: >
  An indistinguishable test send would corrupt any later analysis of actual customer communication volume or content history.
DISCONFIRMING_OBSERVATION: >
  A test send to an internal address is recorded identically to a genuine customer send, with no marker distinguishing the two in the retained history.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger a test send to an internal address and compare its retained record against that of a genuine send to an external recipient.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q045

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q045
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the item record referenced by a template is deleted outright rather than archived, an attempt to send using that template fails in a controlled, clearly reported way rather than an unhandled error or a message with entirely missing referenced content.
WHY_IT_MATTERS: >
  An uncontrolled failure from a deleted reference could crash a wider dispatch process or produce a message that is nonsensical to the recipient.
DISCONFIRMING_OBSERVATION: >
  A send referencing a deleted item record either crashes the broader dispatch process or delivers a message with the referenced content entirely missing and no indication of a problem.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Delete an item record referenced by a template, then attempt to trigger a send that would reference it.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q046

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q046
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the sender operates across multiple companies, the contact and signature data pulled into a message correctly reflects the specific company the message is being sent under, not a default or another company's data.
WHY_IT_MATTERS: >
  The wrong company's contact details on an outbound message misdirects any reply and misrepresents which entity the recipient is dealing with.
DISCONFIRMING_OBSERVATION: >
  A message sent under a specific company shows contact or signature data belonging to a different company the sender also has access to.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Give a sending user access to more than one company with distinct contact and signature configurations, then trigger sends under each company and compare the resulting content.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q047

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q047
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The specific version of the template used to render a given sent message is recorded against that message, not merely the template's name or identifier which could refer to many versions over time.
WHY_IT_MATTERS: >
  Recording only the template's name gives no way to know which actual version of the content was used once the template has been edited multiple times since.
DISCONFIRMING_OBSERVATION: >
  The record of a sent message identifies only the template's name, and cannot be used to determine which specific version of that template's content was rendered.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message, edit the template more than once afterward, and check whether the sent-message record can still identify the exact version used originally.
```

## G03-PRODUCT_EMAIL_TEMPLATE-Q048

```yaml
QID: G03-PRODUCT_EMAIL_TEMPLATE-Q048
MODULE: product_email_template
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If generating an expected attachment fails because the underlying document is not available, the send is either blocked or clearly flagged as missing its attachment, rather than silently delivered as if the attachment had been included.
WHY_IT_MATTERS: >
  A recipient expecting a supporting document that silently never arrives, with the message appearing otherwise complete, may act on incomplete information without realizing anything is missing.
DISCONFIRMING_OBSERVATION: >
  A message is delivered with no attachment and no indication that an expected attachment failed to generate, so it appears to the recipient as if none was ever intended.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Make the underlying document unavailable for attachment generation, trigger a send, and inspect whether the recipient's message indicates the missing attachment.
```
