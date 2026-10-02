# U208 — mail_template: ir.mail.template Render Chain, Dynamic Expression Evaluation, Send Context

**Research Unit:** U208  
**Module:** mail (Odoo Community 19.0.post20260921)  
**Primary Source:** `odoo/addons/mail/models/mail_template.py`  
**Secondary Source:** `odoo/addons/mail/models/mail_render_mixin.py`  
**Tertiary Source:** `odoo/addons/mail/models/mail_mail.py`  
**SHA256 (mail_template.py):** `919991db70691f4e0d2a529502428fc2a33bb60b15b7e33c209fcd98cc5a8d95`  
**Lines (mail_template.py):** 828  
**Gate:** GREEN  

---

## 1. Model Declaration

**File:** `mail/models/mail_template.py:17–24`

```python
class MailTemplate(models.Model):
    "Templates for sending email"
    _name = 'mail.template'
    _inherit = ['mail.render.mixin', 'template.reset.mixin']
    _description = 'Email Templates'
    _order = 'user_id, name, id'
    _unrestricted_rendering = True
```

- `_unrestricted_rendering = True` signals that template editor group check is enforced on create/write when unsafe expressions are present (see `_check_access_right_dynamic_template()` in `mail_render_mixin.py:299`).
- Inherits `mail.render.mixin` (rendering machinery) and `template.reset.mixin`.

---

## 2. Key Fields

**File:** `mail/models/mail_template.py:39–102`

| Field | Type | Key Detail |
|---|---|---|
| `name` | Char | translate=True |
| `model_id` | Many2one('ir.model') | ondelete='cascade'; domain excludes abstract models |
| `model` | Char | related='model_id.model'; stored, indexed |
| `subject` | Char | Dynamic (inline_template); translate=True |
| `email_from` | Char | Dynamic (inline_template); placeholder for sender |
| `use_default_to` | Boolean | default=True; uses `_message_get_default_recipients()` when True |
| `email_to` | Char | Dynamic (inline_template); comma-separated |
| `partner_to` | Char | Dynamic; IDs resolved via `_parse_partner_to()` |
| `email_cc` | Char | Dynamic (inline_template) |
| `reply_to` | Char | Dynamic (inline_template) |
| `body_html` | Html | render_engine='qweb'; render_options={'post_process': True}; sanitize='email_outgoing' |
| `attachment_ids` | Many2many('ir.attachment') | Static attachment IDs linked to template |
| `report_template_ids` | Many2many('ir.actions.report') | Dynamic PDF/HTML reports per record; domain='[("model", "=", model)]' |
| `email_layout_xmlid` | Char | Optional notification layout xmlid for encapsulation |
| `mail_server_id` | Many2one('ir.mail_server') | Optional preferred outgoing server; index='btree_not_null' |
| `scheduled_date` | Char | Dynamic expression (inline_template); parsed to UTC datetime |
| `auto_delete` | Boolean | default=True; deletes mail.mail after send |
| `lang` | Char | From mail.render.mixin; dynamic expression for per-record language |

---

## 3. Dynamic Field Names

**File:** `mail/models/mail_template.py:233–244`

```python
def _get_dynamic_field_names(self):
    return {
        'body_html', 'email_cc', 'email_from', 'email_to',
        'lang', 'partner_to', 'reply_to', 'scheduled_date', 'subject',
    }
```

These are the fields subject to render-time evaluation. `attachment_ids`, `report_template_ids`, `auto_delete`, `mail_server_id`, `model` are NOT in this set—they are handled as static or as attachment/recipient special cases.

---

## 4. Rendering Chain: `_generate_template()`

**File:** `mail/models/mail_template.py:567–652`

The main orchestrator method. Called from `send_mail_batch()`.

```
_generate_template(res_ids, render_fields, ...)
  └── _classify_per_lang(res_ids)   [groups res_ids by computed language]
        ├── for each (template_with_lang, lang_res_ids):
        │     ├── _render_field(field, lang_res_ids)     [subject, email_from, reply_to, body_html]
        │     ├── _generate_template_recipients(...)     [email_cc, email_to, partner_to]
        │     ├── _generate_template_scheduled_date(...) [scheduled_date]
        │     ├── _generate_template_static_values(...)  [auto_delete, mail_server_id, model, res_id]
        │     └── _generate_template_attachments(...)    [attachment_ids, report_template_ids]
```

**`_classify_per_lang()`** (`mail_render_mixin.py:750`): Renders `self.lang` expression per record (or falls back to primary partner's lang) to group res_ids by language. Returns `{lang: (template.with_context(lang=lang), lang_res_ids)}`.

---

## 5. `_render_field()` — Per-Field Rendering

**File:** `mail/models/mail_render_mixin.py:775–853`

- Determines engine from field metadata (`f.render_engine`).
- `body_html` field has `render_engine='qweb'`, so calls `_render_template_qweb()`.
- Other dynamic fields (subject, email_from, etc.) use default `inline_template` engine.
- Merges `render_options` from field definition with caller-supplied options.
- Delegates to `_render_template(template_src, model, res_ids, engine=...)`.

---

## 6. `_render_template()` and Engines

**File:** `mail/models/mail_render_mixin.py:657–719`

Three rendering engines:
1. **`inline_template`** (default): `{{ object.field }}` syntax. Calls `parse_inline_template()` + `render_inline_template()` from `odoo.tools.rendering_tools`. Falls back to regex-based evaluation if no unsafe expressions detected.
2. **`qweb`**: Raw QWeb HTML template. Calls `ir.qweb._render()`. Falls back to regex if no unsafe expressions.
3. **`qweb_view`**: QWeb from an `ir.ui.view` XmlID/record. Always calls `ir.qweb._render()`.

**Optimization (security & performance):** Before calling the eval-based engine, both QWeb and inline_template check `_has_unsafe_expression_*()`. If only `object.field.subfield` expressions are present (no Python calls), a regex-based renderer is used without invoking `safe_eval`. This is the "safe path" for most standard templates.

---

## 7. `_render_eval_context()` — Rendering Variables

**File:** `mail/models/mail_render_mixin.py:312–333`

```python
render_context = {
    'ctx': self.env.context,
    'format_addr': tools.formataddr,
    'format_date': lambda date, ...: format_date(self.env, date, ...),
    'format_datetime': lambda dt, ...: format_datetime(self.env, dt, ...),
    'format_time': lambda time, ...: format_time(self.env, time, ...),
    'format_amount': lambda amount, currency, ...: tools.format_amount(self.env, amount, currency, ...),
    'format_duration': tools.format_duration,
    'is_html_empty': is_html_empty,
    'slug': self.env['ir.http']._slug,
    'user': self.env.user,
    'env': self.env,
}
render_context.update(copy.copy(template_env_globals))
```

When rendering a specific record, `'object': record` is added immediately before render. There is NO explicit `'time'` variable in the eval context (it is available via `template_env_globals` from `odoo.tools.rendering_tools`).

---

## 8. `_generate_template_recipients()`

**File:** `mail/models/mail_template.py:407–510`

Two code paths:
1. **`use_default_to=True`** (default): Calls `Model._message_get_default_recipients()` on all res_ids (or `_message_get_suggested_recipients_batch()` if `allow_suggested=True`). Returns `email_to`, `email_cc`, `partner_ids`.
2. **`use_default_to=False`**: Renders `email_cc`, `email_to`, `partner_to` fields dynamically via `_render_field()`.

After both paths, if `find_or_create_partners=True`:
- Emails from `email_to`/`email_cc` are extracted.
- `_partner_find_from_emails()` is called on the model (or on `mail.thread`).
- Found/created partners added to `partner_ids`.

`partner_to` field (comma-separated IDs or Python list): parsed by `_parse_partner_to()` (`mail_template.py:654–665`) using `literal_eval` first, then comma-split fallback. Resolved to existing partner IDs via `res.partner.sudo().browse().exists()`.

---

## 9. `_generate_template_attachments()`

**File:** `mail/models/mail_template.py:332–405`

Two sources:
1. **Static attachments** (`attachment_ids`): IDs are copied directly — no render-time computation.
2. **Dynamic reports** (`report_template_ids`): For each `ir.actions.report`:
   - `qweb-html`/`qweb-pdf`: calls `ir.actions.report._render_qweb_pdf()`.
   - Other: calls `ir.actions.report._render()`.
   - Report name: evaluated via `safe_eval(report.print_report_name, {'object': record, 'time': time})`.
   - Returns `(report_name, base64_content)` tuples as `'attachments'` key.
3. Hook: `_process_attachments_for_template_post()` on the model (e.g., accounting).

---

## 10. `scheduled_date` Rendering

**File:** `mail/models/mail_template.py:512–532` + `mail_render_mixin.py:644–650`

```
_generate_template_scheduled_date()
  └── _render_field('scheduled_date', res_ids)   [inline_template rendering]
  └── _process_scheduled_date(rendered_value)
        └── mail.mail._parse_scheduled_datetime()
              → parses string/date/datetime → UTC-normalized naive datetime
```

`scheduled_date` on `mail.template` is a **Char** field (not Datetime). The rendered string is parsed to a naive UTC datetime via `_parse_scheduled_datetime()` in `mail_mail.py:292–328`. If no timezone info in the string, UTC is assumed.

---

## 11. `lang` Field — Per-Record Language Resolution

**File:** `mail/models/mail_render_mixin.py:721–748`

`_render_lang()`: If `self.lang` is set, renders it as inline_template per record (typical value: `{{ object.partner_id.lang }}`). If not set, reads `_mail_get_partners()` for the primary partner's lang.

`_classify_per_lang()` (`mail_render_mixin.py:750`): Groups res_ids by lang, returns `{lang: (template.with_context(lang=lang), res_ids)}`. Each language group gets a separate rendering pass, enabling proper translation of `translate=True` fields (`subject`, `body_html`, etc.).

If `template_preview_lang` in context, forces all res_ids to that single language.

---

## 12. `send_mail()` / `send_mail_batch()`

**File:** `mail/models/mail_template.py:675–807`

```
send_mail(res_id, force_send=False, ...) → mail.mail.id
  └── send_mail_batch([res_id], ...)
        ├── _send_check_access(res_ids)         [check read access on target records]
        ├── batch_size = ir.config_parameter 'mail.batch_size' (default 50)
        ├── for res_ids_chunk in split_every(batch_size, res_ids):
        │     ├── _generate_template(chunk, render_fields=(attachment_ids, auto_delete,
        │     │       body_html, email_cc, email_from, email_to, mail_server_id,
        │     │       model, partner_to, reply_to, report_template_ids,
        │     │       res_id, scheduled_date, subject))
        │     ├── Optional: _render_encapsulate() for email_layout_xmlid
        │     └── mail.mail.sudo().create(values_list)
        └── if force_send: mails_sudo.send()
```

`email_layout_xmlid`: if set, `_render_encapsulate()` wraps `body_html` in a QWeb notification layout (e.g., `mail_notification_layout`). Language/company for encapsulation resolved per record.

`email_values` parameter: merged into per-record values dict after template rendering (overrides template values).

---

## 13. `mail.mail` State Machine

**File:** `mail/models/mail_mail.py:69–75`, `_send()` lines 769–956`

```
States: outgoing (default) → sent
                           → exception → outgoing (via action_retry / mark_outgoing)
                                       → cancel (via cancel())
        outgoing → cancel
```

`_send()` mechanism (mail_mail.py:769):
1. Pre-emptively writes `state='exception'` to prevent duplicate sends on rollback.
2. Builds `_prepare_outgoing_list()` — per-recipient email data dicts.
3. Calls `IrMailServer._build_email__()` + `send_email()` per entry.
4. On success: writes `state='sent'`, clears `failure_type`/`failure_reason`.
5. Calls `_postprocess_sent_message()`:
   - Updates `mail.notification` records to `'sent'`/`'exception'`.
   - If `auto_delete=True` and no non-email-invalid failure: `unlink()` the `mail.mail` record.

`process_email_queue()` (mail_mail.py:194): Scheduled action. Fetches `outgoing` mails with `scheduled_date=False OR scheduled_date <= utcnow()`. Default batch: 1000 (configurable via `mail.mail.queue.batch.size`).

---

## 14. Security: Template Editor Group

**File:** `mail/models/mail_render_mixin.py:299–305`

```python
def _check_access_right_dynamic_template(self):
    if not self.env.su and not self.env.user.has_group('mail.group_mail_template_editor') \
            and self._has_unsafe_expression():
        raise AccessError(...)
```

Called in `MailRenderMixin.create()` and `MailRenderMixin.write()` when `_unrestricted_rendering=True`. An "unsafe expression" is any expression not limited to `object.field.subfield` traversal (e.g., Python method calls, filter expressions).

At render time, `_is_restricted()` (mail_render_mixin.py:260) checks the same group + `bypass_restricted_rendering` context key to decide whether to pass `raise_on_forbidden_code_for_model` to QWeb.

---

## 15. `template_category` Computed Field (v19 New)

**File:** `mail/models/mail_template.py:140–181`

```python
template_category = fields.Selection(
    [('base_template', 'Base Template'),
     ('hidden_template', 'Hidden Template'),
     ('custom_template', 'Custom Template')],
    compute="_compute_template_category", search="_search_template_category")
```

- `base_template`: active + has XML ID + has description
- `hidden_template`: inactive, or active + XML ID + no description
- `custom_template`: active + no XML ID

This field did not exist in v16/v17 in this form. Migration scripts targeting template categorization must account for this.

---

## 16. `send_mail_batch()` (v19 New API)

**File:** `mail/models/mail_template.py:699–807`

Batched version of `send_mail()`. Added in v19. In v16/v17 there was no public batch API on `mail.template`—callers looped over `send_mail()`. v19 introduces:
- Explicit batch chunking via `mail.batch_size` config parameter.
- Single `mail.mail.sudo().create(values_list)` call per chunk (bulk insert).
- Per-record layout encapsulation within the same batch loop.

---

## 17. Migration Flags (v16/v17 → v19)

### Fields PRESENT in v19 (confirm NOT removed):
- `use_default_to` — confirmed present (`mail_template.py:57`)
- `mail_server_id` — confirmed present (`mail_template.py:87`)
- `attachment_ids` — confirmed present (`mail_template.py:73`)
- `report_template_ids` — confirmed present as Many2many (`mail_template.py:79`)
- `auto_delete` — confirmed present (`mail_template.py:91`)
- `lang` — confirmed present via `mail.render.mixin` (`mail_render_mixin.py:55`)

### Field name change confirmed:
- `report_template_ids` is a **Many2many** in v19 (relation: `mail_template_ir_actions_report_rel`). In older versions this was `report_template_id` (Many2one). Migration must handle FK → M2M conversion.

### New fields in v19:
- `template_category` (computed Selection) — new
- `user_id` (Many2one res.users, 'Owner') — new
- `has_dynamic_reports` (computed Boolean) — new
- `has_mail_server` (computed Boolean) — new
- `is_template_editor` (computed Boolean) — new

### `scheduled_date` remains Char (not Datetime):
On `mail.template`, `scheduled_date` is `fields.Char` (dynamic expression). On `mail.mail`, it is `fields.Datetime`. The conversion from rendered string to datetime happens in `_process_scheduled_date()` / `_parse_scheduled_datetime()`. This is unchanged from v16/v17 pattern.

### `email_layout_xmlid` (Char) present:
Used to wrap body in a notification layout. Was `email_layout_xmlid` in v16 too, confirmed present.

### Removed: no evidence of removed significant fields from v16/v17 scope in v19:
- No `use_default_to` removal (it is present)
- No `mail_server_id` removal (it is present)
- `copy_attachments` logic changed (now in `copy()` method)
