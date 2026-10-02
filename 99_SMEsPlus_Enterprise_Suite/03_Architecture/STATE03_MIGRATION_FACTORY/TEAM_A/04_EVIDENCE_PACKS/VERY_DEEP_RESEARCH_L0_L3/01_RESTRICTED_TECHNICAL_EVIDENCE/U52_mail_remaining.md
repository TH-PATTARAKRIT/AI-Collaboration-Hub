# U52 — mail remaining: templates, render mixin, compose wizard, aliases, followers, notifications (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U52
- Modules: mail (remaining Python areas)
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: DELTA-FIRST — covers mail Python areas not in U03/U42. JS/OWL static files not studied (out of source-study scope). Source evidence only; RT flags for runtime unknowns.

---

## CAP-U52-01 Mail Template Model

### D1 — Model identity and inheritance
`mail.template` (class `MailTemplate`) inherits `['mail.render.mixin', 'template.reset.mixin']` and sets `_unrestricted_rendering = True` at class level, meaning its rendering is not gated by the Template Editor group.

### D2 — Core fields
- `name`, `description`, `active`: basic metadata.
- `model_id` (Many2one to `ir.model`), `model` (related, stored): the target model that the template applies to.
- `subject`, `email_from`, `email_to`, `email_cc`, `partner_to`, `reply_to`: address/subject fields that accept dynamic placeholder expressions.
- `body_html` (Html field with `render_engine='qweb'` and `render_options={'post_process': True}`): the main HTML body rendered via QWeb.
- `attachment_ids`, `report_template_ids` (Many2many to `ir.actions.report`): static and dynamic attachment handling.
- `email_layout_xmlid`: optional notification wrapper layout.
- `mail_server_id`: preferred outgoing mail server.
- `scheduled_date`: dynamic char field for deferred sending.
- `auto_delete` (default True): removes sent email records to save space.
- `ref_ir_act_window`: sidebar action binding.
- `can_write`, `is_template_editor`: ACL-related computed fields.
- `template_category` (computed selection: `base_template`, `hidden_template`, `custom_template`).

### D3 — Template category classification
`_compute_template_category` classifies: archived → `hidden_template`; active with XML ID and description → `base_template`; active with XML ID but no description → `hidden_template`; active without XML ID → `custom_template`.

### D4 — Dynamic fields set
`_get_dynamic_field_names` returns the set `{'body_html', 'email_cc', 'email_from', 'email_to', 'lang', 'partner_to', 'reply_to', 'scheduled_date', 'subject'}` — these are checked during save/write.

### D5 — Save-time validation
On `create` and `write`, `_check_can_be_rendered` is called, which attempts a trial render of all dynamic fields against a sample record of the target model. A `ValidationError` is raised if rendering fails.

### D6 — Attachment generation
`_generate_template_attachments` iterates `report_template_ids` to generate reports per-record using `ir.actions.report._render_qweb_pdf` or `_render`, base64-encodes them, and resolves the name via `safe_eval(report.print_report_name, ...)`. Static `attachment_ids` are linked directly.

### D7 — Recipient generation
`_generate_template_recipients` either calls `_message_get_default_recipients()` / `_message_get_suggested_recipients_batch()` (when `use_default_to=True`) or renders `email_cc`/`email_to`/`partner_to` fields dynamically. When `find_or_create_partners=True`, emails are resolved to partners via `_partner_find_from_emails`.

### D8 — `send_mail` and `send_mail_batch`
`send_mail(res_id, ...)` delegates to `send_mail_batch([res_id], ...)`. `send_mail_batch` calls `_generate_template` in chunks (default 50 from `mail.batch_size` parameter), creates `mail.mail` records in sudo, optionally encapsulates body in layout via `_render_encapsulate`, and optionally calls `mail.mail.send()` for immediate delivery.

### D9 — Action binding
`create_action` creates an `ir.actions.act_window` with `default_composition_mode='mass_mail'` and binds it to the model via `ref_ir_act_window`. `unlink_action` removes it on template deletion.

### D10 — Abstract model constraint
`_check_abstract_models` raises `ValidationError` if the chosen `model_id` resolves to an abstract model.

---

## CAP-U52-02 Mail Render Mixin

### D1 — Abstract model and flag
`mail.render.mixin` is an `AbstractModel`. `_unrestricted_rendering = False` by default; subclasses override it to True (as `mail.template` does).

### D2 — Security sentinel
`BYPASS_RESTRICTED_RENDERING = object()` at module level is a sentinel used in `_is_restricted()`: restricted mode is active when `_unrestricted_rendering` is False, the user is not admin, does not have `mail.group_mail_template_editor`, and the context key `bypass_restricted_rendering` does not hold the sentinel object.

### D3 — Expression safety checks
`_has_unsafe_expression_template_qweb` parses the HTML fragment and calls `ir.qweb._generate_code` with `raise_on_forbidden_code_for_model=model`, catching `PermissionError`. `_has_unsafe_expression_template_inline_template` parses the inline template and checks each expression via `ir.qweb._is_expression_allowed(e, model)`.

### D4 — Dynamic template ACL check on save
`_check_access_right_dynamic_template` raises `AccessError` if `_has_unsafe_expression()` is True and the user is not superuser and not in `mail.group_mail_template_editor`.

### D5 — Evaluation context
`_render_eval_context` provides `user`, `ctx`, `format_date`, `format_datetime`, `format_time`, `format_amount`, `format_duration`, `is_html_empty`, `slug`, `env`, plus `template_env_globals` (from `odoo.tools.rendering_tools`).

### D6 — QWeb rendering engine
`_render_template_qweb` checks if the template has unsafe expressions; if safe, falls through to `_render_template_qweb_regex` (no eval). If unsafe and `_is_restricted()`, sets `raise_on_forbidden_code_for_model`. Calls `ir.qweb._render(fragment, variables, **options)` per record, stripping the wrapping `<div>` added to handle multi-root fragments.

### D7 — Inline template rendering
`_render_template_inline_template` similarly checks for unsafe expressions: if safe, uses `_render_template_inline_template_regex` (no eval); if unsafe and restricted, raises `AccessError`. Otherwise calls `render_inline_template(parse_inline_template(str(template_txt)), variables)`.

### D8 — QWeb view engine
`_render_template_qweb_view` renders using `ir.qweb._render(view_ref, variables, minimal_qcontext=True, raise_if_not_found=False)` per record, where `view_ref` may be an XML ID or integer view ID.

### D9 — Language resolution and per-lang template classification
`_render_lang` renders the `lang` field expression against each `res_id`. If no `lang` expression is set, falls back to the first partner's `lang` from `_mail_get_partners()`. `_classify_per_lang` groups `res_ids` by computed language and returns `{lang: (self.with_context(lang=lang), [res_ids])}`.

### D10 — Post-processing and encapsulation
`_render_template_postprocess` calls `_replace_local_links` per record. `_render_encapsulate` calls `ir.qweb._render(layout_xmlid, template_ctx, minimal_qcontext=True)` to wrap HTML in a notification layout, then calls `_replace_local_links`. `_replace_local_links` uses four regex substitutions to make relative URLs absolute using `web.base.url`.

### D11 — Preview text prepending
`_prepend_preview` adds a hidden `<div>` with zero font-size before the HTML body, so email clients show preview text below the subject line.

### D12 — `_render_field` dispatcher
`_render_field` reads `render_engine` and `render_options` from the field metadata, resolves language context, and dispatches to `_render_template(...)`.

### D13 — Placeholder builder
`_build_expression` constructs an inline template expression like `{{ object.<field_name>[.<sub_field_name>] [||| null_value] }}`.

### D14 — Template render options validation
`_render_template_get_valid_options` returns `{'post_process', 'preserve_comments'}`. Invalid option keys raise `ValueError`.

---

## CAP-U52-03 Mail Compose Message Wizard

### D1 — Model identity and inheritance
`mail.compose.message` (class `MailComposeMessage`) inherits `['mail.composer.mixin']`, is transient (`_log_access = True`), with `_batch_size = 50`.

### D2 — Composition modes
`composition_mode` selection: `'comment'` (post on a record) or `'mass_mail'` (email mass mailing).

### D3 — Key fields
- `subject`, `body` (with `render_engine='qweb'`), `parent_id`, `template_id`, `attachment_ids`, `email_layout_xmlid`, `email_add_signature`.
- `email_from`, `author_id`: authorship fields.
- `model`, `res_ids` (Text), `res_domain` (Text), `res_domain_user_id`: record targeting.
- `composition_batch` (Boolean, computed): True when more than 1 record targeted.
- `message_type` (selection: `auto_comment`, `comment`, `notification`).
- `subtype_id`, `subtype_is_log`: controls chatter subtype.
- `reply_to`, `reply_to_force_new`, `reply_to_mode` (selection: `update`/`new`).
- `partner_ids`: explicit additional contacts.
- `auto_delete`, `auto_delete_keep_log`, `force_send`, `mail_server_id`.
- `notify_author`, `notify_author_mention`, `notify_skip_followers`: notification control parameters.
- `scheduled_date`: deferred sending date.
- `use_exclusion_list` (default True): excludes blacklisted contacts.

### D4 — Body and subject compute chain
`_compute_body` and `_compute_subject` check `template_id`: in monorecord comment mode they render the template field; in batch mode they copy the raw template value. When no template, body is reset to False.

### D5 — force_send logic
`_compute_force_send`: single record → `force_send=True`; batch comment or domain-based → `force_send=False`; batch mass_mail → `force_send = (len(res_ids) <= mail.mail.force.send.limit)`.

### D6 — Mass mail send flow
`_action_send_mail_mass_mail` iterates `res_ids` in `batch_size` chunks, calls `_prepare_mail_values` + `_manage_mail_values`, creates `mail.mail` records in sudo, creates `mail.notification` records via `_generate_mail_notification_values`, calls `_message_mail_after_hook`, and conditionally calls `mail.send()`.

### D7 — Comment send flow
`_action_send_mail_comment` calls `message_post` on the active model (or `message_notify` if model has no `message_post`). In batch comment mode sets `mail_post_autofollow_author_skip=True`.

### D8 — Notification values generation
`_generate_mail_notification_values`: if `auto_delete` and not `auto_delete_keep_log`, returns empty list (no notification records). Otherwise creates notification rows for each partner in `recipient_ids` and each address in `email_to`/`email_cc`.

### D9 — Schedule message action
`action_schedule_message` calls `_action_schedule_message`, which creates a `mail.scheduled.message` record. Only allowed in mono-comment mode; requires `scheduled_date` to be set.

### D10 — Template save
`create_mail_template` creates a new `mail.template` from the current composer body. Transfers attachments that belong to the composer.

### D11 — Garbage collection
`_gc_lost_attachments` (decorated `@api.autovacuum`) deletes attachments linked to `mail.compose.message` with `res_id=0` older than 1 day.

### D12 — auto_delete defaults
In comment mode without template, `auto_delete=True` (removes notification emails). In mass_mail mode without template, `auto_delete=False` (preserves emails for tracking).

---

## CAP-U52-04 Mail Alias

### D1 — Model identity
`mail.alias` (`_name = 'mail.alias'`, `_order = 'alias_model_id, alias_name'`). Unique index: `(alias_name, COALESCE(alias_domain_id, 0))`.

### D2 — Core fields
- `alias_name`: local part of email (ASCII dot-atom only, validated by regex).
- `alias_full_name` (stored computed): `alias_name@domain_name` when both set.
- `alias_domain_id` (Many2one to `mail.alias.domain`, default = company's domain).
- `alias_model_id` (Many2one to `ir.model`, required): the model for new record creation.
- `alias_defaults` (Text, default `'{}'`): Python literal dict evaluated for new record defaults.
- `alias_force_thread_id` (Integer): if set, disables new record creation, routes to existing thread.
- `alias_parent_model_id`, `alias_parent_thread_id`: owner record (e.g. a project owning a task-creation alias).
- `alias_contact` (selection: `everyone`, `partners`, `followers`): security policy for inbound messages.
- `alias_incoming_local` (Boolean): local-part based detection mode.
- `alias_bounced_content` (Html): custom bounce message for unauthorized senders.
- `alias_status` (selection: `not_tested`, `valid`, `invalid`): recomputed to `not_tested` when routing fields change.

### D3 — ASCII constraint
`_check_alias_is_ascii` validates `alias_name` against `dot_atom_text` regex (RFC 5322 section 3.2.3). Rejects internationalized or quoted-string addresses.

### D4 — Defaults constraint
`_check_alias_defaults` validates that `alias_defaults` is a valid Python literal dictionary via `ast.literal_eval`.

### D5 — Domain clash constraint
`_check_alias_domain_clash` prevents alias names that conflict with the domain's `bounce_alias` or `catchall_alias`.

### D6 — Multi-company domain constraint
`_check_alias_domain_id_mc` checks that when an alias domain belongs to specific companies, the owner record (via `alias_parent_model_id`/`alias_parent_thread_id`) and target record (via `alias_model_id`/`alias_force_thread_id`) belong to those companies.

### D7 — Create-time sanitization
On `create`, `alias_name` is sanitized via `_sanitize_alias_name`, the company's `alias_domain_id` is defaulted if not given, and uniqueness is validated via `_check_unique` before the ORM call.

### D8 — Display name
`_compute_display_name` produces `alias_name@domain` if both set, `alias_name` if only name set, or `"Inactive Alias"` string if neither.

### D9 — Full name stored field
`alias_full_name` is stored and indexed (btree_not_null) to enable efficient search.

### D10 — Model domain restriction
`alias_model_id` domain is `[('field_id.name', '=', 'message_ids')]` — restricts selection to models that have a `message_ids` field (i.e., mail.thread inheritors).

---

## CAP-U52-05 Mail Alias Domain

### D1 — Model identity
`mail.alias.domain` (`_name = 'mail.alias.domain'`, `_order = 'sequence ASC, id ASC'`). Replaces `mail.alias.domain` config parameter used until v16.

### D2 — Core fields
- `name`: email domain string (e.g. `'example.com'`).
- `company_ids` (One2many to `res.company`): companies using this domain.
- `sequence`: ordering.
- `bounce_alias` (default `'bounce'`), `catchall_alias` (default `'catchall'`), `default_from` (default `'notifications'`): local-part aliases.
- `bounce_email`, `catchall_email`, `default_from_email`: computed full addresses.

### D3 — Constraints
Unique constraints on `(bounce_alias, name)` and `(catchall_alias, name)`. `_check_bounce_catchall_uniqueness` raises `ValidationError` if aliases clash within the same domain name.

### D4 — Default from email computation
`_compute_default_from_email` only appends `@domain` when `default_from` does not already contain `@`.

---

## CAP-U52-06 Mail Alias Mixin (and Optional Variant)

### D1 — Two mixin variants
`mail.alias.mixin.optional` (light, `alias_id` optional, no `_inherits`) and `mail.alias.mixin` (strict, uses `_inherits = {'mail.alias': 'alias_id'}`, `alias_id` required).

### D2 — Optional mixin ALIAS_WRITEABLE_FIELDS
`ALIAS_WRITEABLE_FIELDS = ['alias_domain_id', 'alias_name', 'alias_contact', 'alias_defaults', 'alias_bounced_content']` — only these fields from alias are written through the mixin.

### D3 — Optional mixin create
On create, if a `alias_name` is given and `_require_new_alias(vals)` is True, an alias record is created in sudo with values from `_alias_get_creation_values()` under the record's company domain. The created alias ID is written back into the record's `alias_id`.

### D4 — Optional mixin alias_email field
`alias_email` (computed, searchable via `alias_id.alias_full_name`) is `alias_name@domain` when both set, Falsy otherwise.

### D5 — Strict mixin _inherits
`mail.alias.mixin` uses `_inherits = {'mail.alias': 'alias_id'}` so all alias fields are available directly on the model. `alias_id` is required.

### D6 — Column init
`_init_column_alias_id` creates missing aliases for existing rows post-install, logging each creation.

---

## CAP-U52-07 Mail Followers

### D1 — Model identity
`mail.followers` (`_log_access = False`, `_description = 'Document Followers'`). Unique constraint: `unique(res_model, res_id, partner_id)`.

### D2 — Core fields
- `res_model` (Char, required, indexed): model name of followed object.
- `res_id` (Many2oneReference, indexed): ID of followed record.
- `partner_id` (Many2one to `res.partner`, required, cascade): the follower.
- `subtype_ids` (Many2many to `mail.message.subtype`): which subtypes this follower tracks.
- `name`, `email`, `is_active`: related from `partner_id`.

### D3 — Cache invalidation on CRUD
`_invalidate_documents` is called on create/write/unlink to invalidate cached data for affected documents, since follower changes affect access rights computation.

### D4 — `_get_mail_doc_to_followers`
Returns a dict mapping `(model, doc_id)` → list of partner IDs that are followers for a given set of `mail_mail` IDs. Uses a direct SQL join across `mail_mail`, `mail_mail_res_partner_rel`, `mail_message`, and `mail_followers`.

### D5 — `_get_recipient_data` — main query
Fetches recipient data using a CTE-based SQL query. The main query uses `mail_followers` joined with `mail_followers_mail_message_subtype_rel` and `mail_message_subtype` to check subtype subscription. Joins `res_users` laterally to get `notification_type`, `share` flag, and `groups`. Returns one row per (partner, document), classified as `portal`, `customer`, or `user`.

### D6 — Three query paths in `_get_recipient_data`
1. Records + subtype → CTE with `sub_followers` UNION for direct `pids`.
2. Records + `pids` only → simplified LEFT JOIN to check follower status.
3. `pids` only → simple partner data fetch without follower context.

### D7 — `_get_subscription_data`
Fetches follower data for multiple documents at once. Uses WHERE clauses generated from `doc_data` list of `(res_model, res_ids)` pairs. Optionally includes `partner_share` and `active` flags.

### D8 — Recipient type classification
After SQL fetch, each partner is classified: `ushare=True` → `'portal'`; `share=True` (no user) → `'customer'`; otherwise → `'user'`.

### D9 — Group implied transitive closure
After fetching groups, `self.env['res.groups'].browse(set(groups or [])).all_implied_ids.ids` is used to expand to the transitive closure of implied groups.

---

## CAP-U52-08 Mail Notification

### D1 — Model identity
`mail.notification` (`_table = 'mail_notification'`, `_rec_name = 'res_partner_id'`, `_log_access = False`).

### D2 — Core fields
- `author_id` (Many2one to `res.partner`, set null on delete).
- `mail_message_id` (Many2one to `mail.message`, cascade, required, indexed).
- `mail_mail_id` (Many2one to `mail.mail`, indexed): optional optimization reference.
- `res_partner_id` (Many2one to `res.partner`, cascade, indexed): recipient partner.
- `mail_email_address` (Char): recipient email when no matching partner (mass mail).
- `notification_type` (selection: `inbox`, `email`; default `inbox`).
- `notification_status` (selection: `ready`, `process`, `pending`, `sent`, `bounce`, `exception`, `canceled`; default `ready`).
- `is_read` (Boolean, indexed), `read_date` (Datetime).
- `failure_type` (selection): `unknown`, `mail_bounce`, `mail_spam`, `mail_email_invalid`, `mail_email_missing`, `mail_from_invalid`, `mail_from_missing`, `mail_smtp`, `mail_bl`, `mail_optout`, `mail_dup`.
- `failure_reason` (Text).

### D3 — DB constraints
`CHECK(notification_type != 'inbox' OR res_partner_id IS NOT NULL)` — inbox requires a partner. `CHECK(notification_type != 'email' OR failure_type IS NOT NULL OR res_partner_id IS NOT NULL OR COALESCE(mail_email_address, '') != '')` — email requires either partner or email address (unless failed).

### D4 — DB indexes
Composite index on `(res_partner_id, is_read, notification_status, mail_message_id)`. Partial index on `(author_id, notification_status) WHERE notification_status IN ('bounce', 'exception')`. Unique index on `(mail_message_id, res_partner_id) WHERE res_partner_id IS NOT NULL`.

### D5 — create/write guards
On `create`, `mail_message_id` records have `check_access('read')` called. If `is_read` is set, `read_date` is auto-stamped. On `write`, changing `mail_message_id` or `res_partner_id` is blocked for non-admins.

### D6 — Garbage collection
`_gc_notifications` removes read notifications older than 180 days where the partner is internal (`partner_share=False`) and status is `sent` or `canceled`. Uses `GC_UNLINK_LIMIT` constant. Returns `(done, remaining)` tuple.

### D7 — Web client filter
`_filtered_for_web_client` keeps notifications where status is `bounce`/`exception`/`canceled`, recipient is a share partner, or has a non-partner email, or the message subtype has `track_recipients=True`.

### D8 — `_to_store_defaults`
Returns store projection including `mail_email_address`, `failure_type`, `mail_message_id`, `notification_status`, `notification_type`, and `res_partner_id` (with `name`, `email`, `display_name` when `name` is falsy).

### D9 — `format_failure_reason`
Returns human-readable failure reason: for `failure_type != 'unknown'` uses the selection description; for `unknown` appends `failure_reason` text or returns generic message.

---

## CAP-U52-09 Mail Controller (mail.py)

### D1 — `MailController` class
`class MailController(http.Controller)` with `_cp_path = '/mail'`.

### D2 — `/mail/view` route
`@http.route('/mail/view', type='http', auth='public')` — generic access point from notification emails. Accepts `model`, `res_id`, `access_token`, plus optional `message_id` for backward compatibility. Calls `_redirect_to_record`.

### D3 — Record redirect logic
`_redirect_to_record` checks whether the record exists and whether the user has read access (using `check_access`). Handles `allowed_company_ids` cookies, falling back to `_get_redirect_suggested_company`. Builds backend URL as `/odoo/{model_in_url}/{res_id}?{params}` (dots in model name → used as-is; otherwise prefixed `m-`).

### D4 — Token validation
`_check_token` recomputes the expected token from the request path and params using `mail.thread._encode_link`, then compares with `consteq`. Used by unfollow and similar routes.

### D5 — `/mail/unfollow` route
`@http.route('/mail/unfollow', type='http', auth='public', csrf=False)`. Validates token and record, calls `record.sudo().message_unsubscribe([pid])`. Renders `mail.message_document_unfollowed` template.

### D6 — Login redirect helper
`_redirect_to_login_with_mail_view` builds `/mail/view` URL and redirects to `/web/login?redirect=<mail_view_url>`.

---

## CAP-U52-10 Mail Compose Wizard Rendering

### D1 — `_prepare_mail_values` field classification
Fields classified as MAIL (body_html, recipient_ids, res_id, auto_delete, model, is_notification), MESSAGE (body, email_add_signature, email_layout_xmlid, force_email_lang, record_alias_domain_id, record_company_id), or BOTH (attachment_ids, author_id, email_from, mail_activity_type_id, mail_server_id, message_type, parent_id, partner_ids, reply_to, reply_to_force_new, scheduled_date, subject, subtype_id).

### D2 — `_generate_template_for_composer`
Delegates to the template's `_generate_template` if a template is selected, otherwise uses the composer's own rendering.

### D3 — Reply-to mode
`reply_to_mode='update'` (default) → store replies in document chatter. `reply_to_mode='new'` → route replies to a separate address. Setting `reply_to_mode='update'` clears `reply_to` field.

### D4 — BCC warning
`notified_bcc_contains_share` computed in mono-comment mode: calls `mail.followers._get_recipient_data` to find if any follower who will receive a silent copy is a share (portal/customer) partner.

### D5 — `use_exclusion_list`
Default True. When True, prevents sending to blacklisted email addresses. Can be disabled only for specific use cases.

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U52-C001 | CAP-U52-01 | mail/models/mail_template.py:17 | `class MailTemplate(models.Model):` | FACT | Always | — | `mail.template` is a concrete Model class | N-U52-001 |
| VDR-U52-C002 | CAP-U52-01 | mail/models/mail_template.py:19 | `_name = 'mail.template'` | FACT | Always | — | Model technical name is `mail.template` | N-U52-001 |
| VDR-U52-C003 | CAP-U52-01 | mail/models/mail_template.py:20 | `_inherit = ['mail.render.mixin', 'template.reset.mixin']` | FACT | Always | — | Template inherits render mixin and reset mixin | N-U52-001 |
| VDR-U52-C004 | CAP-U52-01 | mail/models/mail_template.py:24 | `_unrestricted_rendering = True` | FACT | Always | — | mail.template disables rendering group gate | N-U52-002 |
| VDR-U52-C005 | CAP-U52-01 | mail/models/mail_template.py:51 | `subject = fields.Char('Subject', translate=True, prefetch=True` | FACT | Always | — | Subject field supports translation and accepts placeholders | N-U52-003 |
| VDR-U52-C006 | CAP-U52-01 | mail/models/mail_template.py:69 | body_html = fields.Html | FACT | Always | — | Body uses QWeb engine with post-processing (absolute URL rewrite) | N-U52-004 |
| VDR-U52-C007 | CAP-U52-01 | mail/models/mail_template.py:85 | `email_layout_xmlid = fields.Char('Email Notification Layout', copy=False)` | FACT | Always | — | Layout xmlid field controls wrapping layout; not copied | N-U52-005 |
| VDR-U52-C008 | CAP-U52-01 | mail/models/mail_template.py:91 | auto_delete = fields.Boolean | FACT | Always | — | Auto-delete defaults to True; removes sent email records | N-U52-006 |
| VDR-U52-C009 | CAP-U52-01 | mail/models/mail_template.py:138 | `self.is_template_editor = self.env.user.has_group('mail.group_mail_template_editor')` | FACT | Always | — | Template editor flag uses security group `mail.group_mail_template_editor` | N-U52-002 |
| VDR-U52-C010 | CAP-U52-01 | mail/models/mail_template.py:143 | a description and | FACT | Always | — | Base templates require both active flag, description, and XML ID | N-U52-007 |
| VDR-U52-C011 | CAP-U52-01 | mail/models/mail_template.py:233 | def _get_dynamic_field_names(self) | FACT | Always | — | These 9 fields are the full set of dynamic (rendered) template fields | N-U52-003 |
| VDR-U52-C012 | CAP-U52-01 | mail/models/mail_template.py:208 | `def _check_can_be_rendered(self, fnames=None, render_options=None):` | FACT | On create/write | — | Template save triggers trial render validation | N-U52-008 |
| VDR-U52-C013 | CAP-U52-01 | mail/models/mail_template.py:247 | def create(self, vals_list) | FACT | On create | — | Abstract model is rejected with ValidationError at create time | N-U52-009 |
| VDR-U52-C014 | CAP-U52-01 | mail/models/mail_template.py:367 | # generate content | FACT | When report_template_ids set | — | QWeb PDF/HTML reports are rendered per-record during attachment generation | N-U52-010 |
| VDR-U52-C015 | CAP-U52-01 | mail/models/mail_template.py:378 | report_name = safe_eval | FACT | When print_report_name set | — | Report name is computed via safe_eval with object and time variables | N-U52-010 |
| VDR-U52-C016 | CAP-U52-01 | mail/models/mail_template.py:450 | `if self.use_default_to and self.model:` | FACT | Always | — | `use_default_to` flag routes to default recipients vs explicit template fields | N-U52-011 |
| VDR-U52-C017 | CAP-U52-01 | mail/models/mail_template.py:567 | `def _generate_template(self, res_ids, render_fields,` | FACT | Always | — | `_generate_template` is the central orchestration method for rendering all template fields | N-U52-012 |
| VDR-U52-C018 | CAP-U52-01 | mail/models/mail_template.py:608 | `for (template, template_res_ids) in self._classify_per_lang(res_ids).values():` | FACT | Always | — | `_generate_template` iterates per language group using `_classify_per_lang` | N-U52-013 |
| VDR-U52-C019 | CAP-U52-01 | mail/models/mail_template.py:675 | def send_mail(self | FACT | Always | — | `send_mail` is the public single-record sending API | N-U52-014 |
| VDR-U52-C020 | CAP-U52-01 | mail/models/mail_template.py:691 | return self.send_mail_batch | FACT | Always | — | `send_mail` delegates to `send_mail_batch` | N-U52-014 |
| VDR-U52-C021 | CAP-U52-01 | mail/models/mail_template.py:714 | self.env['ir.config_parameter'].sudo | FACT | On send | — | Batch size for mass send is configurable via `mail.batch_size` parameter, defaulting to 50 | N-U52-015 |
| VDR-U52-C022 | CAP-U52-01 | mail/models/mail_template.py:300 | ActWindow = self.env['ir.actions.act_window'] | FACT | On create_action | — | Sidebar action opens composer in mass_mail mode | N-U52-016 |
| VDR-U52-C023 | CAP-U52-02 | mail/models/mail_render_mixin.py:23 | `BYPASS_RESTRICTED_RENDERING = object()` | FACT | Always | — | Module-level sentinel object for bypassing rendering restriction | N-U52-017 |
| VDR-U52-C024 | CAP-U52-02 | mail/models/mail_render_mixin.py:46 | `class MailRenderMixin(models.AbstractModel):` | FACT | Always | — | Render mixin is abstract; never instantiated directly | N-U52-017 |
| VDR-U52-C025 | CAP-U52-02 | mail/models/mail_render_mixin.py:52 | `_unrestricted_rendering = False` | FACT | Always | — | Default is restricted; subclasses must explicitly opt out | N-U52-002 |
| VDR-U52-C026 | CAP-U52-02 | mail/models/mail_render_mixin.py:260 | def _is_restricted(self) | FACT | On render call | — | Restricted mode requires all four conditions simultaneously | N-U52-002 |
| VDR-U52-C027 | CAP-U52-02 | mail/models/mail_render_mixin.py:281 | def _has_unsafe_expression_template_qweb | FACT | On unsafe check | — | QWeb expression safety uses `raise_on_forbidden_code_for_model` context key | N-U52-018 |
| VDR-U52-C028 | CAP-U52-02 | mail/models/mail_render_mixin.py:295 | `if not all(self.env["ir.qweb"]._is_expression_allowed(e, model) for e in expressions if e):` | FACT | On unsafe check | — | Inline template expressions each checked via `ir.qweb._is_expression_allowed` | N-U52-018 |
| VDR-U52-C029 | CAP-U52-02 | mail/models/mail_render_mixin.py:299 | `def _check_access_right_dynamic_template(self):` | FACT | On create/write of unrestricted template | — | Raises AccessError if template has unsafe expressions and user not in editor group | N-U52-002 |
| VDR-U52-C030 | CAP-U52-02 | mail/models/mail_render_mixin.py:319 | render_context = | FACT | On render | — | Render context always includes ctx, user, env and formatting helpers | N-U52-019 |
| VDR-U52-C031 | CAP-U52-02 | mail/models/mail_render_mixin.py:361 | if not self._has_unsafe_expression_template_qweb | FACT | On QWeb render | — | Safe templates bypass eval and use regex-based rendering | N-U52-020 |
| VDR-U52-C032 | CAP-U52-02 | mail/models/mail_render_mixin.py:376 | render_result = self.env['ir.qweb']._render | FACT | On QWeb render with unsafe expressions | — | QWeb renders HTML fragment wrapped in div; result stripped of div tags | N-U52-020 |
| VDR-U52-C033 | CAP-U52-02 | mail/models/mail_render_mixin.py:451 | `def _render_template_qweb_regex(self, template_src, model, res_ids):` | FACT | Safe QWeb only | — | Regex mode renders `t-out` attributes without calling Python eval | N-U52-020 |
| VDR-U52-C034 | CAP-U52-02 | mail/models/mail_render_mixin.py:541 | `def _render_template_inline_template(self, template_txt, model, res_ids,` | FACT | Always | — | Inline template is the default rendering engine | N-U52-021 |
| VDR-U52-C035 | CAP-U52-02 | mail/models/mail_render_mixin.py:568 | if not self._has_unsafe_expression_templ | FACT | On restricted render with unsafe inline expressions | — | Unsafe inline expression + restricted mode raises AccessError with group name | N-U52-002 |
| VDR-U52-C036 | CAP-U52-02 | mail/models/mail_render_mixin.py:586 | try | FACT | On unrestricted or safe inline render | — | Inline template uses `render_inline_template` from `odoo.tools.rendering_tools` | N-U52-021 |
| VDR-U52-C037 | CAP-U52-02 | mail/models/mail_render_mixin.py:489 | `def _render_template_qweb_view(self, view_ref, model, res_ids,` | FACT | On qweb_view engine | — | QWeb view engine renders via `ir.qweb._render(view_ref, ...)` supporting xmlid or integer view ID | N-U52-022 |
| VDR-U52-C038 | CAP-U52-02 | mail/models/mail_render_mixin.py:657 | def _render_template | FACT | Always | — | Only three rendering engines are supported | N-U52-020 |
| VDR-U52-C039 | CAP-U52-02 | mail/models/mail_render_mixin.py:716 | if options.get('post_process') | FACT | When post_process option set | — | post_process option triggers absolute URL rewrite on all rendered results | N-U52-023 |
| VDR-U52-C040 | CAP-U52-02 | mail/models/mail_render_mixin.py:721 | `def _render_lang(self, res_ids, engine='inline_template'):` | FACT | Always | — | Language is determined per-record by rendering the `lang` field expression | N-U52-013 |
| VDR-U52-C041 | CAP-U52-02 | mail/models/mail_render_mixin.py:740 | customers = records._mail_get_partners() | FACT | When no lang expression set | — | Falls back to partner's lang when no lang expression is set on template | N-U52-013 |
| VDR-U52-C042 | CAP-U52-02 | mail/models/mail_render_mixin.py:763 | if self.env.context.get('template_preview_lang') | FACT | In preview mode | — | Template preview mode forces all records to a single specified language | N-U52-013 |
| VDR-U52-C043 | CAP-U52-02 | mail/models/mail_render_mixin.py:168 | `def _render_encapsulate(self, layout_xmlid, html, add_context=None, context_record=None):` | FACT | When layout_xmlid is set | — | `_render_encapsulate` builds a context dict and calls `ir.qweb._render(layout_xmlid, template_ctx)` | N-U52-024 |
| VDR-U52-C044 | CAP-U52-02 | mail/models/mail_render_mixin.py:209 | `template_ctx['company'] = context_record._mail_get_companies(default=self.env.company)[context_record.id] if context_record else self.env.company` | FACT | In encapsulate | — | Company is resolved per-record via `_mail_get_companies` | N-U52-024 |
| VDR-U52-C045 | CAP-U52-02 | mail/models/mail_render_mixin.py:126 | `def _replace_local_links(self, html, base_url=None):` | FACT | On post-process | — | Converts relative URLs to absolute in img src, a href, background, and CSS url() | N-U52-023 |
| VDR-U52-C046 | CAP-U52-02 | mail/models/mail_render_mixin.py:232 | `def _prepend_preview(self, html, preview):` | FACT | When preview text set | — | Preview text injected as hidden div at start of HTML body | N-U52-025 |
| VDR-U52-C047 | CAP-U52-02 | mail/models/mail_render_mixin.py:80 | field_name | FACT | Always | — | Placeholder format is object.field_name optionally sub_field_name with null_value fallback | N-U52-026 |
| VDR-U52-C048 | CAP-U52-03 | mail/wizard/mail_compose_message.py:31 | `class MailComposeMessage(models.TransientModel):` | FACT | Always | — | Compose wizard is a transient model | N-U52-027 |
| VDR-U52-C049 | CAP-U52-03 | mail/wizard/mail_compose_message.py:45 | `_batch_size = 50` | FACT | Always | — | Default batch size for compose wizard is 50 | N-U52-015 |
| VDR-U52-C050 | CAP-U52-03 | mail/wizard/mail_compose_message.py:123 | composition_mode = fields.Selection | FACT | Always | — | Two composition modes: comment (chatter) and mass_mail | N-U52-027 |
| VDR-U52-C051 | CAP-U52-03 | mail/wizard/mail_compose_message.py:93 | 'Contents | FACT | Always | — | Composer body also uses QWeb engine with post-processing | N-U52-028 |
| VDR-U52-C052 | CAP-U52-03 | mail/wizard/mail_compose_message.py:204 | use_exclusion_list = fields.Boolean | FACT | Always | — | Blacklist exclusion is on by default | N-U52-029 |
| VDR-U52-C053 | CAP-U52-03 | mail/wizard/mail_compose_message.py:581 | email mode we keep | FACT | Without template | — | In comment mode without template, auto_delete defaults True | N-U52-006 |
| VDR-U52-C054 | CAP-U52-03 | mail/wizard/mail_compose_message.py:601 | @api.depends('composition_mode | FACT | In batch mass_mail | — | Force-send limit configurable via `mail.mail.force.send.limit`, default 100 | N-U52-030 |
| VDR-U52-C055 | CAP-U52-03 | mail/wizard/mail_compose_message.py:780 | `def _action_send_mail(self, auto_commit=False):` | FACT | Always | — | `_action_send_mail` dispatches between `_action_send_mail_mass_mail` and `_action_send_mail_comment` | N-U52-031 |
| VDR-U52-C056 | CAP-U52-03 | mail/wizard/mail_compose_message.py:804 | if wizard.composition_mode == 'mass_mail | FACT | In mass_mail mode | — | Mass mail creates `mail.mail` records; comment mode calls `message_post` | N-U52-031 |
| VDR-U52-C057 | CAP-U52-03 | mail/wizard/mail_compose_message.py:816 | `ActiveModel = self.env[self.model] if self.model and hasattr(self.env[self.model], 'message_post') else self.env['mail.thread']` | FACT | In comment mode | — | Falls back to `mail.thread.message_notify` when model lacks `message_post` | N-U52-032 |
| VDR-U52-C058 | CAP-U52-03 | mail/wizard/mail_compose_message.py:854 | `iter_mails_sudo = self.env['mail.mail'].sudo().create(list(prepared_mail_values_filtered.values()))` | FACT | In mass_mail | — | Mass mail creates `mail.mail` records in sudo | N-U52-031 |
| VDR-U52-C059 | CAP-U52-03 | mail/wizard/mail_compose_message.py:854 | `self.env['mail.notification'].create(self._generate_mail_notification_values(iter_mails_sudo))` | FACT | In mass_mail | — | Notification records created alongside mail records in mass mode | N-U52-033 |
| VDR-U52-C060 | CAP-U52-03 | mail/wizard/mail_compose_message.py:884 | def _generate_mail_notification_values | FACT | In mass_mail | — | When auto_delete=True and keep_log=False, no notification records are created | N-U52-033 |
| VDR-U52-C061 | CAP-U52-03 | mail/wizard/mail_compose_message.py:747 | def _action_schedule_message(self) | FACT | On schedule | — | Message scheduling only supported in mono-comment mode | N-U52-034 |
| VDR-U52-C062 | CAP-U52-03 | mail/wizard/mail_compose_message.py:917 | `def create_mail_template(self):` | FACT | On save-as-template | — | Composer can save current body as a new `mail.template` record | N-U52-035 |
| VDR-U52-C063 | CAP-U52-03 | mail/wizard/mail_compose_message.py:700 | `def _gc_lost_attachments(self):` | FACT | Via autovacuum | — | Orphaned composer attachments (res_id=0, >1 day old) are garbage-collected | N-U52-036 |
| VDR-U52-C064 | CAP-U52-04 | mail/models/mail_alias.py:19 | `class MailAlias(models.Model):` | FACT | Always | — | `mail.alias` is a concrete model mapping email addresses to Odoo models | N-U52-037 |
| VDR-U52-C065 | CAP-U52-04 | mail/models/mail_alias.py:39 | alias_name = fields.Char | FACT | Always | — | Alias name is the local-part of the email address | N-U52-037 |
| VDR-U52-C066 | CAP-U52-04 | mail/models/mail_alias.py:48 | alias_model_id | FACT | Always | — | Aliased model must have a `message_ids` field (mail.thread inheritor) | N-U52-037 |
| VDR-U52-C067 | CAP-U52-04 | mail/models/mail_alias.py:56 | `alias_defaults = fields.Text('Default Values', required=True, default='{}'` | FACT | Always | — | Alias defaults is a required Python literal dict, defaulting to empty dict | N-U52-038 |
| VDR-U52-C068 | CAP-U52-04 | mail/models/mail_alias.py:59 | alias_force_thread_id = fields.Integer | FACT | When set | — | Setting force_thread_id routes all inbound mail to one record and disables new record creation | N-U52-039 |
| VDR-U52-C069 | CAP-U52-04 | mail/models/mail_alias.py:73 | alias_contact = fields.Selection | FACT | Always | — | Three-level contact policy: everyone, partners only, followers only | N-U52-040 |
| VDR-U52-C070 | CAP-U52-04 | mail/models/mail_alias.py:96 | `_name_domain_unique = models.UniqueIndex('(alias_name, COALESCE(alias_domain_id, 0))')` | FACT | Always | — | Database unique index ensures no duplicate aliases per domain | N-U52-037 |
| VDR-U52-C071 | CAP-U52-04 | mail/models/mail_alias.py:179 | def _check_alias_is_ascii(self) | FACT | On create/write | — | Non-ASCII or quoted-string alias names are rejected | N-U52-041 |
| VDR-U52-C072 | CAP-U52-04 | mail/models/mail_alias.py:196 | `dict(ast.literal_eval(alias.alias_defaults))` | FACT | On create/write | — | Alias defaults validated as literal Python dict via ast.literal_eval | N-U52-038 |
| VDR-U52-C073 | CAP-U52-04 | mail/models/mail_alias.py:207 | failing = self.filtered | FACT | On create/write | — | Alias name must not conflict with domain's bounce or catchall aliases | N-U52-042 |
| VDR-U52-C074 | CAP-U52-04 | mail/models/mail_alias.py:241 | @api.depends('alias_contact | FACT | On alias_contact/alias_defaults/alias_model_id change | — | Alias status resets to not_tested when routing configuration changes | N-U52-043 |
| VDR-U52-C075 | CAP-U52-04 | mail/models/mail_alias.py:257 | `vals['alias_name'] = self._sanitize_alias_name(vals.get('alias_name'))` | FACT | On create | — | Alias name is sanitized before ORM create call | N-U52-041 |
| VDR-U52-C076 | CAP-U52-04 | mail/models/mail_alias.py:259 | `vals['alias_domain_id'] = vals.get('alias_domain_id', self.env.company.alias_domain_id.id)` | FACT | On create | — | Alias domain defaults to current company's domain if not specified | N-U52-037 |
| VDR-U52-C077 | CAP-U52-05 | mail/models/mail_alias_domain.py:9 | `class MailAliasDomain(models.Model):` | FACT | Always | — | `mail.alias.domain` is a concrete model, new in v17+, replaces config parameter | N-U52-044 |
| VDR-U52-C078 | CAP-U52-05 | mail/models/mail_alias_domain.py:27 | bounce_alias = fields.Char | FACT | Always | — | Bounce alias defaults to 'bounce'; used for Return-Path | N-U52-045 |
| VDR-U52-C079 | CAP-U52-05 | mail/models/mail_alias_domain.py:34 | help="Local-part | FACT | Always | — | Catchall alias defaults to 'catchall'; used for Reply-To | N-U52-045 |
| VDR-U52-C080 | CAP-U52-05 | mail/models/mail_alias_domain.py:37 | default_from = fields.Char | FACT | Always | — | Default from alias used when no outgoing server filter matches | N-U52-046 |
| VDR-U52-C081 | CAP-U52-05 | mail/models/mail_alias_domain.py:70 | self.default_from_email = | FACT | Always | — | default_from can be a full email or just a local-part | N-U52-046 |
| VDR-U52-C082 | CAP-U52-05 | mail/models/mail_alias_domain.py:44 | _bounce_email_uniques = models.Constraint | FACT | Always | — | Bounce alias must be unique per domain name | N-U52-045 |
| VDR-U52-C083 | CAP-U52-06 | mail/models/mail_alias_mixin.py:11 | class MailAliasMixin(models.AbstractModel) | FACT | Always | — | Strict mixin uses `_inherits` to expose all alias fields directly on the model | N-U52-047 |
| VDR-U52-C084 | CAP-U52-06 | mail/models/mail_alias_mixin.py:19 | `alias_id = fields.Many2one(required=True)` | FACT | Always | — | In strict mixin, alias_id is always required | N-U52-047 |
| VDR-U52-C085 | CAP-U52-06 | mail/models/mail_alias_mixin_optional.py:11 | class MailAliasMixinOptional | FACT | Always | — | Optional mixin allows alias to be absent; alias_id not required | N-U52-047 |
| VDR-U52-C086 | CAP-U52-06 | mail/models/mail_alias_mixin_optional.py:19 | `ALIAS_WRITEABLE_FIELDS = ['alias_domain_id', 'alias_name', 'alias_contact', 'alias_defaults', 'alias_bounced_content']` | FACT | Always | — | Only these 5 fields from alias are writeable through the optional mixin | N-U52-047 |
| VDR-U52-C087 | CAP-U52-06 | mail/models/mail_alias_mixin_optional.py:63 | if vals.get('alias_name') | FACT | On record create when alias_name given | — | Alias record created in sudo, using record's company for domain selection | N-U52-048 |
| VDR-U52-C088 | CAP-U52-06 | mail/models/mail_alias_mixin.py:36 | # aliases after the reflection of models | FACT | On module install | — | Alias column initialization for existing rows deferred to post-init hook | N-U52-048 |
| VDR-U52-C089 | CAP-U52-07 | mail/models/mail_followers.py:11 | class MailFollowers(models.Model) | FACT | Always | — | Followers model has no access logging (no create_uid/write_uid columns) | N-U52-049 |
| VDR-U52-C090 | CAP-U52-07 | mail/models/mail_followers.py:27 | res_model = fields.Char | FACT | Always | — | Model name stored as char (not FK to ir.model) for performance | N-U52-049 |
| VDR-U52-C091 | CAP-U52-07 | mail/models/mail_followers.py:29 | res_id = fields.Many2oneReference | FACT | Always | — | res_id is a Many2oneReference (generic ID) indexed for fast lookup | N-U52-049 |
| VDR-U52-C092 | CAP-U52-07 | mail/models/mail_followers.py:33 | subtype_ids = fields.Many2many | FACT | Always | — | Each follower record stores which message subtypes are subscribed | N-U52-050 |
| VDR-U52-C093 | CAP-U52-07 | mail/models/mail_followers.py:69 | _mail_followers_res_partner_res_model_id_uniq | FACT | Always | — | A partner can follow a given record only once | N-U52-049 |
| VDR-U52-C094 | CAP-U52-07 | mail/models/mail_followers.py:40 | `def _invalidate_documents(self, vals_list=None):` | FACT | On create/write/unlink | — | Document cache is invalidated when follower records change | N-U52-051 |
| VDR-U52-C095 | CAP-U52-07 | mail/models/mail_followers.py:115 | `def _get_recipient_data(self, records, message_type, subtype_id, pids=None):` | FACT | Always | — | Central method for recipient data fetch; used by notification system | N-U52-052 |
| VDR-U52-C096 | CAP-U52-07 | mail/models/mail_followers.py:162 | `if message_type != 'user_notification' and records and subtype_id:` | FACT | Always | — | Follower query skipped for `user_notification` message type | N-U52-052 |
| VDR-U52-C097 | CAP-U52-07 | mail/models/mail_followers.py:163 | query = | FACT | In main query path | — | CTE uses lateral join to check per-follower subtype subscription | N-U52-052 |
| VDR-U52-C098 | CAP-U52-07 | mail/models/mail_followers.py:199 | `COALESCE(sub_user.notification_type, 'email') as notif,` | FACT | In SQL query | — | Notification type defaults to 'email' when user has no explicit preference | N-U52-053 |
| VDR-U52-C099 | CAP-U52-07 | mail/models/mail_followers.py:356 | if follower_data['ushare'] | FACT | Always | — | Recipient classification: ushare → portal, share-no-user → customer, has-internal-user → user | N-U52-054 |
| VDR-U52-C100 | CAP-U52-07 | mail/models/mail_followers.py:337 | `groups = self.env['res.groups'].browse(set(groups or [])).all_implied_ids.ids` | FACT | Always | — | Group list expanded to transitive implied groups using ormcache-backed `all_implied_ids` | N-U52-054 |
| VDR-U52-C101 | CAP-U52-08 | mail/models/mail_notification.py:13 | _name = 'mail.notification | FACT | Always | — | Notification model uses explicit table name `mail_notification` | N-U52-055 |
| VDR-U52-C102 | mail/models/mail_notification.py:29 | mail/models/mail_notification.py:29 | notification_type = fields.Selection | FACT | Always | — | Two notification delivery channels: inbox (Discuss) and email | N-U52-055 |
| VDR-U52-C103 | CAP-U52-08 | mail/models/mail_notification.py:32 | notification_status = fields.Selection | FACT | Always | — | Seven notification statuses covering lifecycle from ready to delivered or failed | N-U52-056 |
| VDR-U52-C104 | CAP-U52-08 | mail/models/mail_notification.py:43 | failure_type = fields.Selection(selection= | FACT | On failure | — | 11 specific failure types covering address issues, SMTP, blacklist, opt-out, and dedup | N-U52-057 |
| VDR-U52-C105 | CAP-U52-08 | mail/models/mail_notification.py:60 | _notification_partner_required | FACT | Always | — | Inbox notification requires a partner; enforced at DB level | N-U52-058 |
| VDR-U52-C106 | CAP-U52-08 | mail/models/mail_notification.py:68 | `_res_partner_id_is_read_notification_status_mail_message_id = models.Index("(res_partner_id, is_read, notification_status, mail_message_id)")` | FACT | Always | — | Composite index optimizes inbox unread lookups | N-U52-058 |
| VDR-U52-C107 | CAP-U52-08 | mail/models/mail_notification.py:69 | `_author_id_notification_status_failure = models.Index("(author_id, notification_status) WHERE notification_status IN ('bounce', 'exception')")` | FACT | Always | — | Partial index for failure lookups by author | N-U52-058 |
| VDR-U52-C108 | CAP-U52-08 | mail/models/mail_notification.py:78 | `messages.check_access('read')` | FACT | On create | — | Creating notification records requires read access on the linked message | N-U52-059 |
| VDR-U52-C109 | CAP-U52-08 | mail/models/mail_notification.py:86 | if ('mail_message_id | FACT | On write | — | Non-admin users cannot change message or recipient on existing notifications | N-U52-059 |
| VDR-U52-C110 | CAP-U52-08 | mail/models/mail_notification.py:93 | `def _gc_notifications(self, max_age_days=180):` | FACT | Via GC | — | GC purges read notifications older than 180 days for internal partners | N-U52-060 |
| VDR-U52-C111 | CAP-U52-08 | mail/models/mail_notification.py:121 | `def _filtered_for_web_client(self):` | FACT | Always | — | Web client only shows bounce/exception/canceled or share-partner or track_recipients notifications | N-U52-060 |
| VDR-U52-C112 | CAP-U52-09 | mail/controllers/mail.py:26 | class MailController(http.Controller) | FACT | Always | — | Mail controller serves HTTP routes under /mail prefix | N-U52-061 |
| VDR-U52-C113 | CAP-U52-09 | mail/controllers/mail.py:190 | `@http.route('/mail/view', type='http', auth='public')` | FACT | Always | — | /mail/view is publicly accessible; handles redirect from notification email links | N-U52-061 |
| VDR-U52-C114 | CAP-U52-09 | mail/controllers/mail.py:225 | `@http.route('/mail/unfollow', type='http', auth='public', csrf=False)` | FACT | Always | — | Unfollow route is public (one-click unsubscribe) and CSRF-exempt | N-U52-062 |
| VDR-U52-C115 | CAP-U52-09 | mail/controllers/mail.py:57 | def _check_token(cls, token) | FACT | Always | — | Token validation uses constant-time comparison to prevent timing attacks | N-U52-063 |
| VDR-U52-C116 | CAP-U52-09 | mail/controllers/mail.py:186 | model_in_url = model | FACT | On redirect | — | Backend redirect URL uses model name directly if contains dot, otherwise prefixes 'm-' | N-U52-064 |
| VDR-U52-C117 | CAP-U52-09 | mail/controllers/mail.py:233 | `record_sudo.message_unsubscribe([pid])` | FACT | On unfollow | — | Unfollow uses sudo to call message_unsubscribe | N-U52-062 |
| VDR-U52-C118 | CAP-U52-04 | mail/models/mail_alias.py:84 | `alias_incoming_local = fields.Boolean('Local-part based incoming detection', default=False)` | FACT | Always | — | Local-part only detection mode available but off by default | N-U52-039 |
| VDR-U52-C119 | CAP-U52-04 | mail/models/mail_alias.py:85 | alias_bounced_content = fields.Html | FACT | Always | — | Alias can define a custom HTML bounce message for unauthorized senders | N-U52-040 |
| VDR-U52-C120 | CAP-U52-01 | mail/models/mail_template.py:79 | report_template_ids = fields.Many2many | FACT | Always | — | Dynamic reports are many2many to ir.actions.report, domain-filtered to template's model | N-U52-010 |
| VDR-U52-C121 | CAP-U52-02 | mail/models/mail_render_mixin.py:55 | lang = fields.Char | FACT | Always | — | Lang is a Char field that may contain a dynamic expression resolved per-record | N-U52-013 |
| VDR-U52-C122 | CAP-U52-02 | mail/models/mail_render_mixin.py:96 | @api.model_create_multi | FACT | On create of unrestricted template | — | Dynamic template access check runs after create for unrestricted models | N-U52-002 |
| VDR-U52-C123 | CAP-U52-02 | mail/models/mail_render_mixin.py:113 | def _update_field_translations | FACT | On translation update | — | Access check also enforced when updating field translations | N-U52-002 |
| VDR-U52-C124 | CAP-U52-03 | mail/wizard/mail_compose_message.py:135 | `res_domain = fields.Text('Active domain')` | FACT | Always | — | Composer can target records via domain expression rather than explicit IDs | N-U52-031 |
| VDR-U52-C125 | CAP-U52-03 | mail/wizard/mail_compose_message.py:196 | notify_author_mention | FACT | Always | — | Skip followers flag controlled by composition_comment_option (forward mode sets it True) | N-U52-032 |
| VDR-U52-C126 | CAP-U52-03 | mail/wizard/mail_compose_message.py:643 | def _compute_notify_skip_followers(self) | FACT | In forward mode | — | Forward mode sets notify_skip_followers=True automatically | N-U52-032 |
| VDR-U52-C127 | CAP-U52-07 | mail/models/mail_followers.py:155 | self.env['mail.followers'].flush_model | FACT | Before SQL query | — | Multiple model flushes performed before raw SQL to ensure data consistency | N-U52-052 |
| VDR-U52-C128 | CAP-U52-07 | mail/models/mail_followers.py:207 | `AND (sub_followers.internal IS NOT TRUE OR partner.partner_share IS NOT TRUE)` | FACT | In SQL query | — | Internal subtypes are not shown to share (portal/customer) partners | N-U52-052 |
| VDR-U52-C129 | CAP-U52-08 | mail/models/mail_notification.py:34 | ('process', 'Processing') | FACT | Always | — | 'pending' status means sent for SMS; email uses 'sent' for delivered | N-U52-056 |
| VDR-U52-C130 | CAP-U52-03 | mail/wizard/mail_compose_message.py:878 | self.env['ir.cron']._commit_progress | FACT | In mass_mail with auto_commit | — | Cron progress tracking called during mass mail send for long-running jobs | N-U52-065 |
| VDR-U52-C131 | CAP-U52-01 | mail/models/mail_template.py:271 | def copy(self, default=None) | FACT | On template copy | — | Template copy creates independent copies of attachments (filestore dedup) | N-U52-066 |
| VDR-U52-C132 | CAP-U52-06 | mail/models/mail_alias_mixin_optional.py:28 | `alias_email = fields.Char('Email Alias', compute='_compute_alias_email', search='_search_alias_email')` | FACT | Always | — | alias_email is a computed, searchable field (not stored) | N-U52-047 |
| VDR-U52-C133 | CAP-U52-04 | mail/models/mail_alias.py:100 | `def _check_alias_domain_id_mc(self):` | FACT | On create/write | — | Multi-company constraint verifies alias domain matches owner and target record companies | N-U52-042 |
| VDR-U52-C134 | CAP-U52-02 | mail/models/mail_render_mixin.py:653 | def _render_template_get_valid_options(self) | FACT | Always | — | Only two valid render options: post_process and preserve_comments | N-U52-067 |
| VDR-U52-C135 | CAP-U52-09 | mail/controllers/mail.py:208 | if kwargs.get('message_id') | FACT | Legacy path | — | Backward-compatible message_id parameter resolves old-format notification links | N-U52-068 |
| VDR-U52-C136 | CAP-U52-03 | mail/wizard/mail_compose_message.py:550 | `def _compute_notified_bcc_contains_share(self):` | FACT | In mono-comment mode | — | BCC warning computed by calling `_get_recipient_data` against the target record | N-U52-069 |
| VDR-U52-C137 | CAP-U52-01 | mail/models/mail_template.py:512 | `def _generate_template_scheduled_date(self, res_ids, render_results=None):` | FACT | When scheduled_date field in render_fields | — | Scheduled date rendered per-record and parsed to UTC datetime without timezone | N-U52-070 |
| VDR-U52-C138 | CAP-U52-07 | mail/models/mail_followers.py:366 | `def _get_subscription_data(self, doc_data, pids, include_pshare=False, include_active=False):` | FACT | Always | — | Subscription data can be fetched for multiple documents in a single query | N-U52-071 |
| VDR-U52-C139 | CAP-U52-03 | mail/wizard/mail_compose_message.py:185 | auto_delete_keep_log = fields.Boolean | FACT | In mass_mail | — | `auto_delete_keep_log` keeps message trace in chatter when mail records are deleted | N-U52-072 |
| VDR-U52-C140 | CAP-U52-02 | mail/models/mail_render_mixin.py:399 | template_label = _("Template name not identified") | FACT | On QWeb render error | — | Template source stripped from error message before presenting to user | N-U52-073 |
| VDR-U52-C141 | CAP-U52-01 | mail/models/mail_template.py:187 | if hasattr(target | FACT | On model change in UI | — | Models can define `_mail_template_default_values()` to populate template fields on model selection | N-U52-008 |
| VDR-U52-C142 | CAP-U52-04 | mail/models/mail_alias.py:43 | alias_domain_id = fields.Many2one | FACT | Always | — | Alias domain defaults to current company's domain | N-U52-037 |
| VDR-U52-C143 | CAP-U52-08 | mail/models/mail_notification.py:95 | ('is_read', '=', True) | FACT | In GC | — | GC targets only read, old, internal-partner, successfully-sent/cancelled notifications | N-U52-060 |
| VDR-U52-C144 | CAP-U52-09 | mail/controllers/mail.py:113 | cids_str = request.cookies.get | FACT | On redirect | — | Company context read from 'cids' cookie for multi-company access check | N-U52-064 |
| VDR-U52-C145 | CAP-U52-09 | mail/controllers/mail.py:129 | cids = cids + [suggested_company.id] | FACT | On access retry | — | Suggested company added to cids cookie to enable access to cross-company records | N-U52-064 |
| VDR-U52-C146 | CAP-U52-03 | mail/wizard/mail_compose_message.py:819 | ActiveModel = ActiveModel.with_context | FACT | In batch comment mode | — | Author auto-follow suppressed in batch comment mode | N-U52-069 |
| VDR-U52-C147 | CAP-U52-01 | mail/models/mail_template.py:395 | if hasattr(self.env[self.model] | FACT | On attachment generation | — | Models can define `_process_attachments_for_template_post` to add model-specific attachments | N-U52-010 |
| VDR-U52-C148 | CAP-U52-03 | mail/wizard/mail_compose_message.py:960 | def _prepare_mail_values(self, res_ids) | FACT | On invalid email | — | Invalid email state is 'cancel' (silent) when no log kept, 'exception' when log is kept | N-U52-073 |
| VDR-U52-C149 | CAP-U52-02 | mail/models/mail_render_mixin.py:92 | def _valid_field_parameter(self, field, name) | FACT | Always | — | `render_engine` and `render_options` are valid field parameters when using render mixin | N-U52-020 |
| VDR-U52-C150 | CAP-U52-07 | mail/models/mail_followers.py:96 | self.env['mail.mail'].flush_model | FACT | In `_get_mail_doc_to_followers` | — | Three model flushes before raw SQL for follower-mail join | N-U52-052 |
| VDR-U52-C151 | CAP-U52-03 | mail/wizard/mail_compose_message.py:736 | 'composition_comment_option | FACT | On schedule message | — | Environment context cleaned before storing with scheduled message | N-U52-034 |
| VDR-U52-C152 | CAP-U52-08 | mail/models/mail_notification.py:132 | def _to_store_defaults(self, target) | FACT | Always | — | Store projection includes conditional display_name (only when name is falsy) | N-U52-074 |
| VDR-U52-C153 | CAP-U52-01 | mail/models/mail_template.py:57 | use_default_to = fields.Boolean | FACT | Always | — | Default recipients flag is True by default — uses record's partner/email fields | N-U52-011 |
| VDR-U52-C154 | CAP-U52-04 | mail/models/mail_alias.py:88 | alias_status = fields.Selection | FACT | Always | — | Alias status is stored/computed; resets to not_tested on config changes | N-U52-043 |
| VDR-U52-C155 | CAP-U52-06 | mail/models/mail_alias_mixin_optional.py:21 | `alias_id = fields.Many2one('mail.alias', string='Alias', ondelete="restrict", required=False, copy=False)` | FACT | Always | — | Optional mixin's alias_id has `ondelete="restrict"` and `copy=False` | N-U52-047 |
