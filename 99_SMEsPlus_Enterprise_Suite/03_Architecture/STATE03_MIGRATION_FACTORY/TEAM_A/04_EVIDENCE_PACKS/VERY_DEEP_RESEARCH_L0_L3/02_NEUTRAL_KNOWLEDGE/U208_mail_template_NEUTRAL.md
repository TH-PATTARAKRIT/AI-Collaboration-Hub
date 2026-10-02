# U208 — Neutral Knowledge: Email Template Render Chain and Send Context

**Research Unit:** U208  
**Module:** mail (Odoo Community 19.0.post20260921)  
**Gate:** GREEN  
**Claim count:** 20  

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U208-C01 | MODEL-DECL | mail/models/mail_template.py:17–24 | class MailTemplate | STRUCTURE | Always | CONFIRMED | The email template model inherits from both a rendering mixin and a reset mixin, and declares unrestricted rendering enabled | Email template model inherits two mixins and permits unrestricted dynamic rendering |
| U208-C02 | FIELD-BODY | mail/models/mail_template.py:69–72 | body_html field | FIELD | Always | CONFIRMED | The body HTML field declares the QWeb rendering engine and sets post-process true in its render options, with email outgoing sanitization | Email body uses the QWeb rendering engine with automatic post-processing and email-safe sanitization |
| U208-C03 | FIELD-SCHED | mail/models/mail_template.py:90 | scheduled_date field | FIELD | Always | CONFIRMED | The scheduled send date is stored as a character field (not a datetime field) on the template, allowing dynamic expressions that are later parsed to UTC | Template stores scheduled date as text to support dynamic expressions; parsing to UTC occurs at send time |
| U208-C04 | FIELD-USETO | mail/models/mail_template.py:57–62 | use_default_to field | FIELD | Always | CONFIRMED | A boolean field named use default to, defaulting true, controls whether recipient resolution uses the record default recipients method instead of rendered email fields | A boolean field (default true) switches recipient resolution between the record default and explicit rendered fields |
| U208-C05 | FIELD-RPTIDS | mail/models/mail_template.py:79–84 | report_template_ids field | FIELD | Always | MIGRATION-FLAG | Report templates are stored as a many-to-many relation to report actions (not a single many-to-one), domain-restricted to the same model as the template | Dynamic report attachment is a many-to-many relation to report actions, filtered to the same model |
| U208-C06 | DYNFIELDS | mail/models/mail_template.py:233–244 | _get_dynamic_field_names | BEHAVIOR | Always | CONFIRMED | Nine fields are designated as dynamic: body HTML, email CC, email FROM, email TO, language, partner TO, reply TO, scheduled date, and subject; attachment and server fields are not in this set | Nine specific fields receive dynamic expression rendering; attachment and server configuration fields are excluded |
| U208-C07 | EVAL-CTX | mail/models/mail_render_mixin.py:312–333 | _render_eval_context | BEHAVIOR | Always | CONFIRMED | The rendering evaluation context includes the current user record, the environment context, the environment object, formatting helpers for date, datetime, time, amount, duration, address, and a slug helper | Rendering context provides user, environment, and a set of formatting helpers including date, currency amount, address, and slug |
| U208-C08 | EVAL-OBJ | mail/models/mail_render_mixin.py:370–371 | _render_template_qweb | BEHAVIOR | Per record | CONFIRMED | The variable named object referring to the current record being rendered is injected into the evaluation context immediately before each record is rendered | The record being rendered is available as a variable named object during template evaluation |
| U208-C09 | SAFE-PATH | mail/models/mail_render_mixin.py:361–363 | _render_template_qweb | BEHAVIOR | No unsafe expressions present | CONFIRMED | When no unsafe expressions are detected, QWeb rendering falls through to a regex-based renderer that does not invoke the evaluation engine, improving performance and security | Templates containing only safe field traversal expressions use a regex renderer without invoking the evaluation engine |
| U208-C10 | LANG-RESOLVE | mail/models/mail_render_mixin.py:721–748 | _render_lang | BEHAVIOR | lang field set | CONFIRMED | When the language field on the template contains an expression, it is rendered per record to determine each record language; when not set, the primary partner language of the record is used | Per-record language is resolved by rendering the language expression, or by reading the primary partner language when the expression is absent |
| U208-C11 | LANG-CLASSIFY | mail/models/mail_render_mixin.py:750–773 | _classify_per_lang | BEHAVIOR | Multiple records | CONFIRMED | Records are grouped by their resolved language and each group is rendered against a language-contextualized copy of the template, enabling translated subject and body output | Records are batched by resolved language and each batch renders against a language-contextualized template for correct translation |
| U208-C12 | RECIP-DEFAULT | mail/models/mail_template.py:450–468 | _generate_template_recipients | BEHAVIOR | use_default_to=True | CONFIRMED | When use default to is true, the record default recipients method is called to produce recipient partner IDs plus email addresses, bypassing the template email fields | With use default to enabled, recipient resolution delegates entirely to the record default recipients method |
| U208-C13 | RECIP-PARTNER | mail/models/mail_template.py:495–509 | _generate_template_recipients | BEHAVIOR | partner_to rendered | CONFIRMED | The rendered partner to value is parsed as a Python literal or comma-split integer list; only IDs of existing partners pass the existence check and are appended to partner IDs | Rendered partner IDs from the partner to field are validated against existing records before inclusion as recipients |
| U208-C14 | ATTACH-REPORT | mail/models/mail_template.py:365–390 | _generate_template_attachments | BEHAVIOR | report_template_ids present | CONFIRMED | Each linked report action is rendered against the record; QWeb PDF and HTML reports use the QWeb PDF renderer; other types use the generic render call; output is base64-encoded and returned as name-data tuples | Each linked report action is rendered per record, base64-encoded, and returned as a named attachment tuple |
| U208-C15 | SCHED-UTC | mail/models/mail_template.py:512–532 | _generate_template_scheduled_date | BEHAVIOR | scheduled_date expressed | CONFIRMED | The rendered scheduled date string is passed through a parser that converts it to a naive UTC datetime; if no timezone is present in the string, UTC is assumed | Rendered scheduled date strings are normalized to naive UTC datetimes, assuming UTC when no timezone is specified |
| U208-C16 | SEND-BATCH | mail/models/mail_template.py:699–807 | send_mail_batch | BEHAVIOR | Always | CONFIRMED | The batch send method reads a batch size from a configuration parameter (defaulting to 50), chunks the record ID list, calls the template generator per chunk, creates mail records in bulk, and optionally forces immediate send | Batch send uses a configurable chunk size, generates template values per chunk, bulk-creates mail records, and optionally sends immediately |
| U208-C17 | SEND-LAYOUT | mail/models/mail_template.py:765–784 | send_mail_batch | BEHAVIOR | email_layout_xmlid set | CONFIRMED | When an email layout XML ID is provided, the rendered body is re-wrapped by a QWeb notification layout renderer that adds company, model description, record, and layout context variables per record | When a layout XML ID is set, the rendered body is encapsulated in a QWeb notification layout with per-record company and model context |
| U208-C18 | MAIL-STATE | mail/models/mail_mail.py:69–75 | state field | STRUCTURE | Always | CONFIRMED | The outgoing mail model carries five states: outgoing, sent, received, exception, and cancel; the default is outgoing | The outgoing mail record has five lifecycle states: outgoing, sent, received, exception, and cancel |
| U208-C19 | SEND-PREEMPT | mail/models/mail_mail.py:800–804 | _send | BEHAVIOR | Per send attempt | CONFIRMED | Before attempting SMTP delivery, the send method writes the exception state to the record; on successful delivery it overwrites with the sent state; this prevents duplicate sends after a database rollback | Send preemptively sets the exception state before delivery and writes sent only on confirmed success to prevent duplicate delivery |
| U208-C20 | AUTODEL | mail/models/mail_mail.py:287–288 | _postprocess_sent_message | BEHAVIOR | auto_delete=True, no non-address failure | CONFIRMED | After a successful send, records with auto delete true are permanently deleted unless the failure type is a non-email-address error; this is the default behavior as auto delete defaults to true on both the template and the mail record | Mail records with auto delete enabled are permanently removed after successful send unless a non-address delivery failure occurred |

---

## Summary

U208 covers the complete rendering and send lifecycle of `ir.mail.template` in Odoo 19 Community:

- **Model structure:** 17+ fields, 9 dynamic, inherits rendering mixin
- **Rendering:** Three engines (inline template, QWeb, QWeb view); safe regex optimization path for simple field expressions
- **Eval context:** user, env, ctx, format helpers, object injected per record
- **Recipient resolution:** Two paths (default recipients vs. explicit template fields); partner creation optional
- **Attachments:** Static IDs plus per-record rendered reports (Many2many in v19)
- **Language:** Per-record language expression drives translation-contextualized rendering
- **Send path:** Batch creation of mail records, optional layout encapsulation, optional immediate send
- **Mail state machine:** Five states with preemptive exception write
- **Auto-delete:** Default behavior permanently removes mail records after successful send

**Key migration flag:** `report_template_ids` is Many2many in v19 (was `report_template_id` Many2one in earlier versions).
