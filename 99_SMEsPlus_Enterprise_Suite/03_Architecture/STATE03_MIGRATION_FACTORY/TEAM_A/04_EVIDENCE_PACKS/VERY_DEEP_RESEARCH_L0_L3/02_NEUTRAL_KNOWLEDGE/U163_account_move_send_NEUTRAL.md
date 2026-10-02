# U163 Neutral Knowledge — Invoice Email and PDF Dispatch in Odoo 19 Community

## Overview

In Odoo 19 Community, the capability that generates invoice PDF documents and dispatches
them to customers by email is not a separate installable module. It is built directly into
the core accounting module. This knowledge record describes what the system does,
how it is organised, and what constraints govern its behaviour — without referencing
internal code identifiers, file names, or technical object names.

---

## VDR Claims Table

| # | Claim | Confidence | Evidence Type | Location (L/R) | Counter-evidence | Risk | Migration Impact | Notes |
|---|---|---|---|---|---|---|---|---|
| C1 | The invoice sending capability exists as a built-in part of the accounting module, not as a separate installable component | High | Direct source read | L | None found | Low | Must be treated as core accounting behaviour, not an optional addon | No standalone module directory exists |
| C2 | A shared orchestration layer handles both single and batch invoice sending; two separate interactive forms are used depending on whether one or multiple documents are selected | High | Direct source read | L | None | Low | Custom workflows must account for both entry points | Single form is synchronous; batch form is asynchronous |
| C3 | The entry point for the send-and-print action on an invoice checks that the document is in a valid state before opening the appropriate form | High | Direct source read | L | None | Low | Validation logic must be preserved in any migration | Documents not in the confirmed state cannot be sent |
| C4 | PDF generation calls a QWeb rendering engine, collects per-invoice binary content, stores it as a binary attachment linked to the invoice record, and marks the record as sent | High | Direct source read | L | None | Low | Binary attachment handling must be tested after migration | The attachment is stored in a dedicated binary field |
| C5 | The default PDF template for invoice sending is the invoice-with-payments variant; a second template without the payments section is also available and both can be selected per-partner | High | Direct source read | L | None | Low | Template selection per partner must be preserved | Template is resolved from partner preference, then journal preference, then system default |
| C6 | The filename given to the generated PDF is derived from the invoice display name at the time of generation | High | Direct source read | L | None | Low | Filename logic may need review if display name format changes | Method delegates to the move display name method |
| C7 | Email sending uses the platform messaging system's post mechanism directly; no separate email composition wizard is invoked | High | Direct source read | L | None | Low | Downstream email delivery depends on mail server configuration | After posting, attachment ownership is re-assigned from the invoice to the message record |
| C8 | Four distinct email templates exist for different document types: standard invoice, credit note, self-billing invoice, and self-billing credit note | High | Direct source read | L | None | Low | All four templates must be present after migration | Template selection is determined by the move type field |
| C9 | Attachment management exposes a widget that distinguishes between placeholder entries (PDF not yet generated), protected entries (invoice PDF already generated), and user-added manual entries | High | Direct source read | L | None | Medium | Attachment widget behaviour is client-side and may need UI testing | Dynamic report attachments from the template are also listed |
| C10 | Electronic document format support is designed as an extension point; the base Community system provides no built-in electronic document formats, so only PDF email is dispatched by default | High | Direct source read | L | None | Low | Any EDI requirements need separate module installation | Hooks for pre- and post-render web service calls exist but are no-ops in base |
| C11 | Multiple invoices can be queued for background sending; the system stores pending send configuration on each invoice record and a scheduled job processes the queue periodically | High | Direct source read | L | None | Medium | The scheduled job must be active for batch sending to function; migration must verify cron status | Default job capacity is ten invoices per run |
| C12 | The batch sending form shows a preview of how many invoices will be sent by each method before the user confirms; if the scheduled job is inactive, a blocking error prevents batch dispatch | High | Direct source read | L | None | Medium | Post-migration activation of the scheduled job is a prerequisite for batch sending | System administrators see a redirect to the cron configuration; regular users see an error message |
| C13 | When an invoice email is sent, a portal access link is automatically embedded in the notification; this link uses a per-invoice access token generated on demand | High | Direct source read | L | None | Medium | Portal module must be installed; access token field must survive migration | The token is generated only if not already present |
| C14 | The sending method preference (email, download, or other) is stored on the customer partner record and drives the default selection in the send form | High | Direct source read | L | None | Low | Partner preferences must be preserved during migration | The manual download method triggers a file download action instead of sending an email |
| C15 | Alert detection runs before sending and can block the action entirely if a danger-level condition is detected, such as missing recipient email address on a single invoice | High | Direct source read | L | None | Low | Alert conditions must be tested post-migration | Batch sending issues a warning rather than a blocking error for missing emails |
| C16 | PDF generation supports a configurable batch size to avoid memory exhaustion when processing large numbers of invoices; the default batch size is eighty invoices per rendering pass | High | Direct source read | L | None | Low | System parameter must be configured appropriately for production volume | The batch size is an integer-valued system configuration parameter |
| C17 | A fallback proforma PDF can be generated when electronic document generation fails, allowing the email to still be sent with a non-final PDF attachment | High | Direct source read | L | None | Medium | Fallback behaviour must be tested for any EDI-enabled move types | The fallback is triggered by an allow-fallback flag passed by the caller |
| C18 | Two extension hooks execute immediately before and immediately after PDF rendering, allowing other modules to inject custom logic without modifying the core rendering path | High | Direct source read | L | None | Low | Any custom modules using these hooks must be verified post-migration | Both hooks are no-ops in the base Community installation |
| C19 | After successful sending, a real-time notification is sent to the author user via the bus system; errors during cron processing are also notified via the bus and posted to the invoice chatter | High | Direct source read | L | None | Low | Bus notification depends on the web worker / longpolling service being active | Notifications include a direct link to the affected invoices |
| C20 | Journal subscribers receive a separate notification after successful invoice sending; this supports downstream automation such as accounting integrations that monitor journal activity | High | Direct source read | L | None | Low | Journal subscriber notification may need testing if custom journal listeners are present | Exceptions during subscriber notification are caught and logged rather than propagated |
| C21 | No Thai-specific override of the invoice sending or PDF generation chain exists in the Community source tree; Thai localisation uses the same generic PDF template as all other localisations | High | Direct source read | L | None | Low | Thai deployments requiring tax-invoice-specific PDF formats must use additional localisation modules | The l10n_th module was confirmed present but contains no send-chain overrides |
| C22 | The send form inherits from the mail composition mixin and supports saving the current email body and subject as a reusable mail template | High | Direct source read | L | None | Low | Saved templates must be preserved during migration | A dedicated save-as-template sub-dialog is provided |

---

## Summary for Migration Planning

The invoice dispatch chain is a tightly integrated part of the accounting module.
Migration must preserve:

1. The scheduled job for batch processing (verify it is active after migration).
2. Partner-level preferences for sending method and PDF template.
3. All four email templates and the logic that selects among them by move type.
4. The portal access token field on the invoice model.
5. The binary field that stores the generated PDF.
6. The system configuration parameter controlling PDF batch size.
7. Any custom modules that override the pre/post render hooks or the web service hooks.

No Thai-specific customisation exists in the base Community dispatch chain.
EDI formats require additional modules not present in base Community.
