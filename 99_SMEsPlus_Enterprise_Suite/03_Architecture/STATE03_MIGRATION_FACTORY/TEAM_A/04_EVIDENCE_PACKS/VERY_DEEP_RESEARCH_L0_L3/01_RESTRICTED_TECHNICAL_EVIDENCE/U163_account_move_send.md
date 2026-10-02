# U163 — account_move_send: Invoice Email/PDF Dispatch Chain (BUILT-IN)

**Unit:** U163 | **Group:** G01/G13 | **Priority:** P1
**Source tree:** Odoo Community 19.0.post20260921
**Module status:** BUILT-IN to `account` addon (no separate `account_move_send` module directory)
**Research depth:** L3

---

## 1. Module / Built-In Nature

`account_move_send` does **not** exist as a standalone addon directory under
`odoo/addons/`. The entire dispatch chain lives inside the `account` addon:

| File | Role |
|---|---|
| `account/models/account_move_send.py` | Abstract model `account.move.send` (863 lines) — shared orchestration logic |
| `account/wizard/account_move_send_wizard.py` | TransientModel `account.move.send.wizard` — single-invoice, synchronous |
| `account/wizard/account_move_send_batch_wizard.py` | TransientModel `account.move.send.batch.wizard` — multi-invoice, asynchronous |
| `account/models/account_move.py` | `action_send_and_print()`, `_get_mail_template()`, `_get_report_base_filename()`, cron handler |
| `account/views/account_report.xml` | QWeb report action `account.account_invoices` |

Manifest reference: `account/__manifest__.py` lines 73–74 declare
`wizard/account_move_send_wizard.xml` and `wizard/account_move_send_batch_wizard.xml` as view data files.
Security access: `account/security/ir.model.access.csv` line 124–125 grant invoice group access to both wizard models.

---

## 2. Abstract Model `account.move.send`

**Path:** `account/models/account_move_send.py:13`

```python
class AccountMoveSend(models.AbstractModel):
    _name = 'account.move.send'
    _description = "Account Move Send"
```

This is an **abstract** model — not instantiated directly. Both wizards inherit it
via `_inherit = ['account.move.send']`.

**Key fields / methods in the abstract model:**

| Method | Line | Purpose |
|---|---|---|
| `_get_default_sending_methods(move)` | 26 | Reads `commercial_partner_id.invoice_sending_method`; defaults to `{'email'}` |
| `_get_default_sending_settings(move, from_cron, **custom)` | 68 | Assembles full settings dict (methods, EDI, PDF report, mail template, lang, body, subject, partners, attachments) |
| `_get_alerts(moves, moves_data)` | 111 | Returns blocking/informational alerts (e.g. missing email, archived cron) |
| `_get_mail_template_id(move)` | 64 | Delegates to `move._get_mail_template()` |
| `_get_default_mail_attachments_widget(move, mail_template, ...)` | 228 | Combines placeholder PDF, dynamic template reports, existing PDF, and template static attachments |
| `_prepare_invoice_pdf_report(invoices_data)` | 407 | Calls `ir.actions.report._pre_render_qweb_pdf()` then `_get_splitted_report()` per-invoice; stores binary in `pdf_attachment_values` |
| `_link_invoice_documents(invoices_data)` | 464 | Creates `ir.attachment` records for the PDF, sets `invoice_pdf_report_file`, `message_main_attachment_id`, `is_move_sent = True` |
| `_hook_invoice_document_before_pdf_report_render(invoice, invoice_data)` | 398 | Extension hook (no-op in base) |
| `_hook_invoice_document_after_pdf_report_render(invoice, invoice_data)` | 455 | Extension hook (no-op in base) |
| `_call_web_service_before_invoice_pdf_render(invoices_data)` | 704 | Web-service hook before PDF render (no-op in base) |
| `_call_web_service_after_invoice_pdf_render(invoices_data)` | 710 | Web-service hook after PDF render (no-op in base) |
| `_generate_invoice_documents(invoices_data, allow_fallback_pdf)` | 716 | Master PDF pipeline: hooks → web service → batch render → link |
| `_send_mail(move, mail_template, **kwargs)` | 555 | Calls `move.message_post(message_type='comment', ...)` with email layout |
| `_send_mails(moves_data)` | 657 | Generates dynamic report attachments, then calls `_send_mail()` for each move |
| `_hook_if_success(moves_data, from_cron)` | 497 | Sends emails, sends bus notifications, notifies journal subscribers |
| `_hook_if_errors(moves_data, allow_raising)` | 485 | Raises UserError (sync) or posts error to chatter and sends bus notification (cron) |
| `_generate_and_send_invoices(moves, from_cron, allow_raising, allow_fallback_pdf, **custom)` | 816 | **Top-level orchestrator**: validate → build settings dict → generate PDFs → handle errors → send → clear `sending_data` → return attachments |

---

## 3. Entry Point on `account.move`

**Path:** `account/models/account_move.py:6121`

```python
def action_send_and_print(self):
    self.env['account.move.send']._check_move_constraints(self)
    return {
        'name': _("Send"),
        'type': 'ir.actions.act_window',
        'view_mode': 'form',
        'res_model': 'account.move.send.wizard' if len(self) == 1 else 'account.move.send.batch.wizard',
        'target': 'new',
        'context': {'active_model': 'account.move', 'active_ids': self.ids},
    }
```

For single invoice → `account.move.send.wizard` (synchronous).
For multiple invoices (list view selection) → `account.move.send.batch.wizard` (asynchronous via cron).

A second entry point `_generate_and_send()` at line 6851 bypasses the UI wizard and calls
`_generate_and_send_invoices()` directly (used by programmatic flows).

---

## 4. PDF Generation Chain

**Report action XML ID:** `account.account_invoices`
**Defined:** `account/views/account_report.xml:5`
**QWeb report name:** `account.report_invoice_with_payments`
**Model:** `account.move`
**Field:** `is_invoice_report = True`
**Filename expression:** `(object._get_report_base_filename())`

`_get_report_base_filename()` at `account/models/account_move.py:6453`:
```python
def _get_report_base_filename(self):
    return self._get_move_display_name()
```
This returns the move's display name (e.g. `INV/2024/00001`).

**Batch size control:** IR config param `account.pdf_generation_batch`, default 80
(line 743 of `account_move_send.py`). Large invoice sets are processed in batches to
avoid memory errors.

A second report `account_invoices_without_payment` uses report name
`account.report_invoice` (without payment reconciliation section).

---

## 5. Email Composition

No separate `mail.compose.message` wizard is used. The abstract model calls
`move.message_post()` directly via `_send_mail()` at line 555:

```python
new_message = move.with_context(
    email_notification_allow_footer=True,
    disable_attachment_import=True,
    no_document=True,
).message_post(
    message_type='comment',
    email_layout_xmlid='mail.mail_notification_layout_with_responsible_signature',
    ...
)
```

Mail template selection (`_get_mail_template()` at `account_move.py:6415`):

| Move type | Template XML ID |
|---|---|
| `out_invoice` (default) | `account.email_template_edi_invoice` |
| `out_refund` | `account.email_template_edi_credit_note` |
| `in_invoice` + self-billing | `account.email_template_edi_self_billing_invoice` |
| `in_refund` + self-billing | `account.email_template_edi_self_billing_credit_note` |

The wizard's `template_id` field inherits `mail.composer.mixin` and supports
save-as-template, body/subject rendering, and language resolution.

---

## 6. Attachment Management

After `message_post()`, attachment ownership is explicitly re-pointed away from
`account.move` to `mail.message` (lines 574–580 of `account_move_send.py`):

```python
# Prevent duplicated attachments linked to the invoice.
new_message.attachment_ids.invalidate_recordset(['res_id', 'res_model'], flush=False)
if new_message.attachment_ids.ids:
    self.env.cr.execute("UPDATE ir_attachment SET res_id = NULL WHERE id IN %s", ...)
new_message.attachment_ids.write({'res_model': new_message._name, 'res_id': new_message.id})
```

The PDF attachment itself is stored in `invoice_pdf_report_file` (binary field, line 729 of
`account_move.py`) and is guarded by `protect_from_deletion: True` in the attachments widget.

---

## 7. EDI Integration

The abstract model exposes two hooks for EDI dispatch:

- `_get_all_extra_edis()` (line 31): returns `{}` in Community base — no built-in EDI formats.
- `_get_default_extra_edis(move)` (line 38): returns set of applicable EDI keys.

EDI modules (e.g. `account_edi_ubl_cii`) override these methods to inject their
formats. The `invoice_edi_format` selection field (driven by `res.partner.invoice_edi_format`)
controls the electronic document format embedded alongside the PDF.
The `_call_web_service_before/after_invoice_pdf_render()` hooks are the integration points
for EDI web-service calls.

**In Community base, `_get_all_extra_edis()` returns `{}` — no EDI dispatch occurs out of the box.**

---

## 8. Batch Sending

**Wizard:** `account/wizard/account_move_send_batch_wizard.py`
**Model name:** `account.move.send.batch.wizard`

`action_send_and_print(force_synchronous=False)` at line 80:

1. If `force_synchronous=True`: calls `_generate_and_send_invoices()` immediately (used in tests).
2. Otherwise: sets `sending_data = {'author_user_id': ..., 'author_partner_id': ...}` on all moves,
   then triggers cron `account.ir_cron_account_move_send`.

**Cron handler** `_cron_account_move_send(job_count=10)` at `account_move.py:6496`:
- Queries moves with `sending_data != False` and `state = 'posted'`
- Processes up to `job_count` (default 10) per run, ordered by date/sequence
- Calls `_generate_and_send_invoices(to_process, from_cron=True)`

A UI summary view computes how many invoices will be sent by which method.
Cron must be active for async batch sending; if archived, a blocking alert is raised for
system administrators or an error is shown to regular users (line 90–103 of batch wizard).

---

## 9. Portal Access

**Path:** `account/models/account_move.py:6428`

`_notify_get_recipients_groups()` overrides the base mail method. For any non-journal-entry
move, it:
1. Calls `_portal_ensure_token()` to generate `access_token` if not yet set.
2. Builds an `access_link` via `_notify_get_action_link('view', access_token=...)`.
3. Adds an `additional_intended_recipient` group that receives a "View" button in the email.

This means every customer who receives an invoice email gets a portal access link
embedded in the notification — no separate step required.

---

## 10. Thai Context (l10n_th)

`l10n_th` module exists at `odoo/addons/l10n_th/` but contains **no override** of
`account_move_send`, `AccountMoveSend`, or `action_send_and_print`. There is no
Thai-specific PDF print template in the Community dispatch chain. Thai tax invoices use
the same generic `account.report_invoice_with_payments` template.

---

## 11. Single-Wizard Fields Detail

**Path:** `account/wizard/account_move_send_wizard.py`
**Model:** `account.move.send.wizard`
**Inheritance:** `['account.move.send', 'mail.composer.mixin']`

Key fields:

| Field | Type | Purpose |
|---|---|---|
| `move_id` | Many2one | The single invoice being sent |
| `sending_method_checkboxes` | Json | Checkbox state for each applicable sending method |
| `sending_methods` | Json (computed) | Derived from checked boxes |
| `invoice_edi_format` | Selection | EDI format for the move |
| `pdf_report_id` | Many2one `ir.actions.report` | Selected PDF template |
| `template_id` | Many2one `mail.template` | Email template |
| `mail_partner_ids` | Many2many `res.partner` | Recipients |
| `mail_attachments_widget` | Json | Widget data for attachment management |
| `extra_edi_checkboxes` | Json | Additional EDI formats to include |

`available_pdf_report_ids` is computed from `_get_available_action_reports()` —
if only one template applies, the template selection is hidden (`display_pdf_report_id = False`).

---

## 12. Sending Method Selection

`res.partner.invoice_sending_method` selection field drives default behavior.
Methods (excluding `manual`) are shown in the single wizard's checkbox panel.
The `manual` method triggers PDF download instead of email sending (`action_send_and_print`
returns `_action_download(attachments)` at wizard line 391–405).

---

## 13. `is_move_sent` Flag and Status

`is_move_sent = fields.Boolean(...)` at `account_move.py:665` is set to `True` in
`_link_invoice_documents()` at `account_move_send.py:482`.

The `move_sent_values` computed field at line 833 derives the send status string
(`sent` / `not_sent`) used in list/kanban views.

`sending_data` JSON field at line 722 holds the async send configuration while the move
is queued for cron processing; cleared to `False` after processing.

---

## 14. Proforma Fallback

If EDI generation fails and `allow_fallback_pdf=True`, a proforma PDF is generated
via `_prepare_invoice_proforma_pdf_report()` at line 437. This uses report name
`account.account_invoices` with `data={'proforma': True}`.

---

## Sources

All line numbers refer to:
- `odoo/addons/account/models/account_move_send.py` (863 lines)
- `odoo/addons/account/models/account_move.py`
- `odoo/addons/account/wizard/account_move_send_wizard.py`
- `odoo/addons/account/wizard/account_move_send_batch_wizard.py`
- `odoo/addons/account/views/account_report.xml`
