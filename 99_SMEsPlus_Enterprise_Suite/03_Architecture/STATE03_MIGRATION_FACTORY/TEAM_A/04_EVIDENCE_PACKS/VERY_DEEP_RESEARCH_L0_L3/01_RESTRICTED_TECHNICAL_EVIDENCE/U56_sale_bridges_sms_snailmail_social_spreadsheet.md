# U56 — sale bridges, SMS, snailmail, social media, spreadsheet family (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U56
- Modules: sale (remaining delta), sale_expense_margin, sale_gelato_stock, sale_mrp_margin, sale_project_stock_account, sale_purchase_project, sale_service, sale_sms, sale_timesheet_margin, sms, sms_twilio, snailmail_account, social_media, spreadsheet, spreadsheet_account, spreadsheet_dashboard, spreadsheet_dashboard_account, spreadsheet_dashboard_event_sale, spreadsheet_dashboard_hr_expense, spreadsheet_dashboard_hr_timesheet, spreadsheet_dashboard_im_livechat, spreadsheet_dashboard_sale, spreadsheet_dashboard_sale_timesheet, spreadsheet_dashboard_stock_account
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: DELTA-FIRST for sale (U04/U05 did core); full study for sms, snailmail, social, spreadsheet. Source evidence only; RT flags for runtime unknowns.

---

## CAP-U56-01 — Sale Expense Margin Bridge

### D1: expense_id link on sale.order.line
The bridge module adds a `Many2one` field `expense_id` pointing at `hr.expense` on `sale.order.line`, enabling an expense record to be associated with a sale line for cost tracking purposes.

### D2: Purchase price computation override for expenses
When a sale order line has an `expense_id`, the `_compute_purchase_price` method derives the purchase price by dividing `expense.untaxed_amount_currency` by `expense.quantity`, then converting to the sale-order-line currency. Lines without an expense fall back to `super()._compute_purchase_price()`.

### D3: Expense propagation from invoice line to sale line
When an invoice line (with an attached expense) is used to prepare sale line values, the `expense_id` is injected into the sale line creation dict, preserving the expense linkage chain.

---

## CAP-U56-02 — Sale MRP Margin Bridge

### D1: Phantom BOM cost calculation
The bridge extends MRP tests only; no new model code is present. Tests verify that BOM phantom kit purchase prices are computed correctly, including normalisation by `bom.product_qty` (so a BOM producing 12 units correctly divides total component cost by 12).

### D2: AVCO manufacturing move exclusion
Tests confirm that for AVCO-costed products, manufacturing moves are excluded from the delivery-cost computation so only the outgoing delivery move's unit value is used as `purchase_price`.

### D3: Dropshipped kit cost
For dropshipped kits, supplier `price_unit` from purchase order lines (not the kit's `standard_price`) is aggregated as the sale line's purchase price after receipt validation.

---

## CAP-U56-03 — Sale Timesheet Margin Bridge

### D1: Timesheet-based cost computation
For sale order lines where `qty_delivered_method == 'timesheet'` and `product_id.standard_price == 0`, the purchase price is computed as the negation of the summed analytic line `amount` divided by summed `unit_amount` (average hourly cost from actual timesheet entries).

### D2: Service-non-timesheet lines excluded from recomputation
Lines that are services with policies `ordered_prepaid`, `delivered_manual`, or `delivered_milestones` — confirmed as in state `sale` with a non-zero `purchase_price` — are filtered out of recomputation by `super()`, preventing cost overwrite.

### D3: Unit-of-measure conversion for time cost
If the product UoM differs from the company's `project_time_mode_id`, the per-unit cost is converted via `_compute_quantity` before being stored.

---

## CAP-U56-04 — Sale Gelato Stock Bridge

### D1: Gelato product stock-rule bypass
`_action_launch_stock_rule` is overridden to filter out lines where `product_id.gelato_product_uid` is truthy; those lines skip stock rule launch (no picking is created).

---

## CAP-U56-05 — Sale Project Stock Account Bridge

### D1: Expense-policy exclusion from analytic move lines
In `stock.move._get_valid_moves_domain`, when `company.anglo_saxon_accounting` is enabled, moves whose `product_id.expense_policy` is `'sales_price'` or `'cost'` are excluded from the domain of valid moves, preventing the creation of duplicate analytic accounting lines for re-invoiced products.

---

## CAP-U56-06 — Sale Purchase Project Bridge

### D1: Analytic distribution propagation to purchase lines
When a service sale line generates a purchase order line via `_purchase_service_prepare_line_values`, the project analytic distribution is injected into the PO line values if the sale line has no explicit `analytic_distribution` but its order's project does.

### D2: Project ID on purchase order
`_purchase_service_prepare_order_values` adds `project_id` from the sale order's project to the purchase order creation values.

---

## CAP-U56-07 — Sale Service Module

### D1: is_service stored computed field
A stored Boolean `is_service` is computed on `sale.order.line` based on `product_id.type == 'service'`, with a partial index `_name_search_services_index` on `(order_id DESC, sequence, id) WHERE is_service IS TRUE` for query performance.

### D2: Auto-init column backfill
`_auto_init` creates the `is_service` column via `create_column` and bulk-updates it via raw SQL if not existing, avoiding ORM overhead on large tables.

### D3: Service domain helper
`_domain_sale_line_service` provides a configurable domain that always requires `is_service = True` and optionally checks `is_expense = False` and `state = 'sale'`.

### D4: Specialised name_search optimisation
When the domain includes `('is_service', '=', True)` and the operator is `like/ilike`, `name_search` uses `search_fetch` with explicit `order` to avoid joining on `sale_order` with many lines.

---

## CAP-U56-08 — Sale SMS Module

### D1: Module structure
`sale_sms` contains only `__init__.py` and `__manifest__.py`; it carries no Python model code. Its contribution is XML data (views/templates) linking the sms module to sale.

---

## CAP-U56-09 — SMS Core — sms.sms Model

### D1: Outgoing SMS record structure
`sms.sms` stores: `uuid` (Char, unique, auto-generated via `uuid4().hex`), `number`, `body`, `partner_id`, `mail_message_id`, `state`, `failure_type`, `to_delete`, `sms_tracker_id`.

### D2: SMS state machine
Seven states: `outgoing` (In Queue), `process` (Processing), `pending` (Sent to carrier), `sent` (Delivered), `error`, `canceled`. IAP success states map: `processing→process`, `success→pending`, `sent→pending`, `delivered→sent`.

### D3: CRON-triggered send on create
`create` calls `self.env.ref('sms.ir_cron_sms_scheduler_action')._trigger()` to wake the scheduler immediately when new SMS records are created.

### D4: Batch send via _split_by_api
`send()` calls `_split_by_api()` (yielding `SmsApi` by default) then iterates `_split_batch()` to send in configurable batches (default 500, from `sms.session.batch.size` config param).

### D5: CRON queue processing
`_process_queue` searches for `state = 'outgoing'` and `to_delete != True` records, locks them with `try_lock_for_update()`, sends in batches, and reports progress via `ir.cron._commit_progress`.

### D6: Autovacuum garbage collection
`_gc_device` executes `DELETE FROM sms_sms WHERE to_delete = TRUE` via raw SQL to purge processed messages.

### D7: Failure type vocabulary
Defined failure types: `unknown`, `sms_number_missing`, `sms_number_format`, `sms_country_not_supported`, `sms_registration_needed`, `sms_credit`, `sms_server`, `sms_acc`, `sms_blacklist`, `sms_duplicate`, `sms_optout`.

### D8: Delivery error sets
`BOUNCE_DELIVERY_ERRORS = {'sms_invalid_destination', 'sms_not_allowed', 'sms_rejected'}` and `DELIVERY_ERRORS = {'sms_expired', 'sms_not_delivered', *BOUNCE_DELIVERY_ERRORS}`.

---

## CAP-U56-10 — SMS Core — SmsApi (IAP)

### D1: IAP endpoint constant
`SmsApi.DEFAULT_ENDPOINT = 'https://sms.api.odoo.com'` (overridable via `sms.endpoint` config param).

### D2: Batch send endpoint
`_send_sms_batch` posts to `/api/sms/3/send` with `messages` (grouped by content), `webhook_url` (delivery reports URL), and `dbuuid`.

### D3: Message format
Each message element: `{'content': str, 'numbers': [{'uuid': str, 'number': str}, ...]}`.

### D4: Provider failure mapping
`PROVIDER_TO_SMS_FAILURE_TYPE`: `server_error→sms_server`, `sms_number_missing→sms_number_missing`, `wrong_number_format→sms_number_format`, plus IAP-specific: `country_not_supported→sms_country_not_supported`, `insufficient_credit→sms_credit`, `unregistered→sms_acc`.

### D5: SmsApiBase interface
`SmsApiBase` defines the interface with `_send_sms_batch` (raises `NotImplementedError`) and `_get_sms_api_error_messages`. `SmsApi` is the IAP concrete implementation.

### D6: Account verification flow
`_send_verification_sms` POSTs to `/api/sms/1/account/create`; `_verify_account` to `/api/sms/2/account/verify`; `_set_sender_name` to `/api/sms/1/account/update_sender`.

---

## CAP-U56-11 — SMS Core — sms.template

### D1: Template model
`sms.template` inherits `mail.render.mixin` and `template.reset.mixin`, with `_unrestricted_rendering = True`. Fields: `name`, `model_id` (restricted to SMS-capable, non-transient models), `model`, `body` (translatable Char), `sidebar_action_id`.

### D2: Sidebar action creation
`action_create_sidebar_action` creates an `ir.actions.act_window` for `sms.composer` with context including `sms_composition_mode: 'guess'` and `default_template_id`, bound to the template's model.

---

## CAP-U56-12 — SMS Core — sms.tracker

### D1: Tracker model purpose
`sms.tracker` links an SMS (by UUID) to `mail.notification` or mailing traces. Stores `sms_uuid` (Char, unique) and `mail_notification_id` (Many2one to `mail.notification`, cascade-delete).

### D2: State→notification status mapping
`SMS_STATE_TO_NOTIFICATION_STATUS`: `canceled→canceled`, `process→process`, `error→exception`, `outgoing→ready`, `sent→sent`, `pending→pending`.

### D3: Forward-only notification updates
`_update_sms_notifications` applies an "ignore list" per status to prevent backward state transitions (e.g., a `sent` notification will not be reset to `canceled`).

### D4: Bounce detection
`_action_update_from_provider_error` checks if `failure_type` is in `BOUNCE_DELIVERY_ERRORS`; if so, sets notification status to `bounce`.

---

## CAP-U56-13 — SMS Core — mail.thread SMS extension

### D1: message_has_sms_error computed field
SQL query aggregates SMS `exception`-status notifications per `res_id` filtered by `author_id = current user partner`; stored as Boolean on `mail.thread`.

### D2: message_post SMS override
When `message_type == 'sms'`, the body is stored as `sms_content` (plain text) and `sms_content_to_rendered_html` is applied to the body for the mail.message record.

### D3: _message_sms_schedule_mass shortcut
Instantiates `sms.composer` in `mass` mode with `mass_force_send: False` and `mass_keep_log: True`.

### D4: _message_sms core method
Resolves recipients from `number_field` or `_sms_get_recipients_info`, then calls `message_post` with `message_type='sms'`, passing `sms_numbers` and `sms_pid_to_number`.

### D5: _notify_thread_by_sms
Iterates partner recipients from `recipients_data` where `notif == 'sms'`, formats numbers from `sms_pid_to_number` or `partner.phone`, creates `sms.sms` records and linked `mail.notification` records. SMS trackers are created via `Command.create({'sms_uuid': sms.uuid})` only for `outgoing` state.

### D6: Scheduled notification support
`_notify_thread` checks `scheduled_date` and skips `_notify_thread_by_sms` if notification is scheduled.

---

## CAP-U56-14 — SMS Core — _sms_get_recipients_info (base)

### D1: Recipient resolution logic
Priority: (1) check record's own phone fields (`_phone_get_number_fields`), sanitize; (2) if not found and `partner_fallback=True`, check linked partner's phone fields; (3) if no valid number, store the raw value with `sanitized=False`.

### D2: Return structure
Returns `{record_id: {'partner': res.partner, 'sanitized': str|False, 'number': str, 'partner_store': bool, 'field_store': str}}`.

---

## CAP-U56-15 — SMS Core — sms.composer wizard

### D1: Composition modes
Three modes: `numbers` (arbitrary number list), `comment` (post on a document), `mass` (batch over multiple records).

### D2: Mass mode blacklist/optout/duplicate handling
`_prepare_mass_sms_values` checks blacklist numbers, optout IDs, and duplicate sanitized numbers; assigns state `canceled` with appropriate failure types (`sms_blacklist`, `sms_optout`, `sms_duplicate`) for excluded records.

### D3: Blacklist lookup
`_get_blacklist_record_ids` searches `phone.blacklist` for all blacklisted numbers when `use_exclusion_list = True`.

### D4: Template rendering
When `template_id` is set and `composition_mode == 'comment'`, the body renders via `template._render_field('body', [res_id], compute_lang=True)`. For mass mode, all IDs are rendered in batch.

### D5: Mass force send vs queue
If `mass_force_send` is True, `sms_all.filtered(lambda sms: sms.state == 'outgoing').send()` is called immediately; otherwise records remain in queue.

---

## CAP-U56-16 — SMS Core — IrActionsServer SMS state

### D1: SMS server action state
`ir.actions.server` gains a new `state = 'sms'` that sets available models to mail-thread non-transient models only.

### D2: SMS server action execution
`_run_action_sms_multi` creates an `sms.composer` in `comment` or `mass` mode (controlled by `sms_method` field), calling `action_send_sms()`.

### D3: Warning validation
If model is transient or not a `mail.thread`, a warning is produced; also warns if template model mismatches action model.

---

## CAP-U56-17 — SMS Core — IrModel is_mail_thread_sms

### D1: is_mail_thread_sms detection
A non-stored computed field on `ir.model`; a model qualifies if it is `is_mail_thread = True` AND has any field in `_phone_get_number_fields() + _mail_get_partner_fields()`.

---

## CAP-U56-18 — SMS Core — MailNotification SMS extension

### D1: SMS notification type
`notification_type` selection gains `sms` (with `ondelete='cascade'`).

### D2: SMS-specific fields
`sms_id_int` (Integer, btree-not-null index), `sms_id` (non-stored Many2one computed from `sms_id_int` excluding `to_delete` SMS), `sms_tracker_ids` (One2many), `sms_number` (Char, group restricted), and SMS failure types (`sms_number_missing`, `sms_number_format`, `sms_credit`, `sms_country_not_supported`, `sms_registration_needed`, `sms_server`, `sms_acc`, `sms_expired`, `sms_invalid_destination`, `sms_not_allowed`, `sms_not_delivered`, `sms_rejected`).

---

## CAP-U56-19 — SMS Core — IAP Delivery Webhook

### D1: Delivery report controller
`SmsController` at `/sms/status` (jsonrpc, public auth) receives batch delivery reports from IAP: `[{'sms_status': str, 'uuids': [str]}]`. For success states, `sms_trackers._action_update_from_sms_state`. For errors, `_action_update_from_provider_error`. Processed UUIDs are marked `to_delete = True`.

---

## CAP-U56-20 — SMS Twilio — SmsApiTwilio

### D1: Twilio REST API integration
`SmsApiTwilio._sms_twilio_send_request` POSTs to `https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json` with `From`, `To`, `Body`, `StatusCallback` params, authenticated via HTTP Basic with `account_sid:auth_token`.

### D2: From-number selection
`get_twilio_from_number` selects a Twilio number from `company.sms_twilio_number_ids` sorted by country code match with the destination `to_number`, falling back to first available.

### D3: StatusCallback URL format
`get_twilio_status_callback_url` constructs `/sms_twilio/status/{uuid}` relative to `company.get_base_url()`.

### D4: HMAC-SHA1 signature verification
`generate_twilio_sms_callback_signature` computes HMAC-SHA1 of URL + sorted POST params, base64-encoded, as the Twilio webhook signature.

### D5: Error code mapping
Twilio error codes mapped: 21211/21614/21265→`wrong_number_format`; 21604→`sms_number_missing`; 21266→`twilio_from_to`; 21603→`twilio_from_missing`; 21608→`twilio_acc_unverified`; 21609→`twilio_callback`.

### D6: Additional failure types
Four Twilio-specific failure types added to `sms.sms.failure_type`: `twilio_authentication`, `twilio_callback`, `twilio_from_missing`, `twilio_from_to`.

---

## CAP-U56-21 — SMS Twilio — Company Configuration

### D1: sms_provider field
`res.company` gains `sms_provider` selection (`iap` default, `twilio`). `_get_sms_api_class()` returns `SmsApiTwilio` when `sms_provider == 'twilio'`.

### D2: Twilio credentials
`sms_twilio_account_sid` (Char, system group) and `sms_twilio_auth_token` (Char, system group) stored on company; `_assert_twilio_sid` validates format (starts 'AC', 34 chars, alphanumeric).

### D3: Twilio number pool
`sms_twilio_number_ids` (One2many to `sms.twilio.number`) groups per-country Twilio numbers. Each `sms.twilio.number` stores: `company_id`, `sequence`, `number`, `country_id`, `country_code` (related).

---

## CAP-U56-22 — SMS Twilio — sms.sms API routing

### D1: _split_by_api override
Groups SMS records by company (`_get_sms_company()`); if company's `sms_provider == 'twilio'`, creates `SmsApiTwilio` with `_set_company`; otherwise falls back to `super()._split_by_api()` (IAP).

### D2: Twilio batch size
Twilio batch size is `int(ir.config_parameter.sms_twilio.session.batch.size, 10)` — ten SMS per API call — vs the IAP default of 500.

### D3: Twilio SID storage hook
`_handle_call_result_hook` writes `sms_twilio_sid` from Twilio's response onto the SMS tracker record (since the SMS itself is deleted after send).

---

## CAP-U56-23 — SMS Twilio — Status Webhook Controller

### D1: Twilio status callback route
`/sms_twilio/status/<string:uuid>` (public POST, no CSRF) validates UUID format, Twilio status value, and Twilio HMAC signature before processing.

### D2: State mapping from Twilio
`TWILIO_TO_SMS_STATE`: `queued→outgoing`, `sending→process`, `sent→pending`, `delivered→sent`, `canceled→canceled`, `failed/undelivered→error`.

### D3: Error code to failure type (sms.tracker)
Twilio error codes: `30002→expired`, `30003→invalid_destination`, `30004→rejected`, `30005→invalid_destination`, `30006→not_allowed`, `30007→rejected`, `30008→not_delivered`.

---

## CAP-U56-24 — Snailmail Account — Invoice Integration

### D1: snailmail.letter creation on invoice send
`account_move_send._hook_if_success` creates `snailmail.letter` records for moves where `sending_methods` includes `snailmail` and partner has a valid address. The report template used is `account.account_invoices`.

### D2: Invalid-address alert
`_get_alerts` generates a `danger` level alert (single invoice) or `warning` (batch) when any invoice in a snailmail batch has a partner without a valid address.

### D3: snailmail applicability check
`_is_applicable_to_move('snailmail', ...)` delegates to `snailmail.letter._is_valid_address(move.partner_id)`.

### D4: Invoice deletion cleanup
`@api.ondelete(at_uninstall=False)` on `account.move` searches and unlinks `snailmail.letter` records linked to the deleted invoices.

### D5: Sending method on partner
`res.partner.invoice_sending_method` gains `snailmail` → `'by Post'` option.

### D6: Stamp count in batch wizard
`account_move_send_batch_wizard.send_by_post_stamps` counts partners with valid addresses across all move partners, displaying as `(Stamps: N)` in summary data.

### D7: Portal method label
`snailmail_account/controllers/portal.py` injects `{'snailmail': _("by Post")}` into the portal invoice sending methods rendering dict.

---

## CAP-U56-25 — Social Media — Company Fields

### D1: Eight social media URL fields
`res.company` gains eight Char fields: `social_twitter` ('X Account'), `social_facebook`, `social_github`, `social_linkedin`, `social_youtube`, `social_instagram`, `social_tiktok`, `social_discord` ('Discord Account').

---

## CAP-U56-26 — Spreadsheet Core — SpreadsheetMixin

### D1: Abstract mixin
`spreadsheet.mixin` is an `AbstractModel` (`_auto = False`) providing: `spreadsheet_binary_data` (Binary, default empty workbook), `spreadsheet_data` (Text computed from attachment), `spreadsheet_file_name` (Char computed as `display_name + '.osheet.json'`), `thumbnail` (Binary).

### D2: JSON storage format
Data is stored as base64-encoded JSON (verified in `_check_spreadsheet_data`). A valid XLSX file (`[Content_Types].xml` key present) is also accepted without field/menu validation.

### D3: Test-time field/menu validation
In test mode, `_check_spreadsheet_data` iterates `fields_in_spreadsheet(data)` and validates each model and field chain exists; also validates `menus_xml_ids_in_spreadsheet(data)` — checks XML ID exists and menu has an action.

### D4: Empty workbook structure
`_empty_spreadsheet_data` creates `{"sheets": [{"id": "sheet1", "name": _("Sheet1")}], "settings": {"locale": ...}, "revisionId": "START_REVISION"}` with user lang-derived locale.

### D5: XLSX export support
`_zip_xslx_files` assembles a ZIP of XLSX component files, resolving `imageSrc` paths from `ir.attachment` binary store.

### D6: Display name batch resolution
`get_display_names_for_spreadsheet(args)` accepts `[{"model": str, "id": int}]`, searches each model with `active_test=False`, returns display names in same order as input.

---

## CAP-U56-27 — Spreadsheet Core — Currency and Locale

### D1: Company currency for spreadsheet
`res.currency.get_company_currency_for_spreadsheet(company_id)` returns `{"code", "symbol", "decimalPlaces", "position"}` for the company's currency.

### D2: Currency rate for spreadsheet
`res.currency_rate.get_rates_for_spreadsheet(requests)` returns conversion rates per `[{"from": code, "to": code, "date": str?, "company_id": int?}]` using `Currency._get_conversion_rate`.

### D3: Locale conversion
`res.lang._odoo_lang_to_spreadsheet_locale()` returns `{name, code, thousandsSeparator, decimalSeparator, dateFormat, timeFormat, formulaArgSeparator, weekStart}`. `formulaArgSeparator` is `";"` when `decimalSeparator == ","`.

### D4: Date format conversion
`strftime_format_to_spreadsheet_date_format` and `strftime_format_to_spreadsheet_time_format` translate Python `strftime` tokens to spreadsheet format tokens (e.g., `%Y→yyyy`, `%m→mm`, `%d→dd`).

### D5: IR model searchable parent
`ir.model.has_searchable_parent_relation(model_names)` returns `{model_name: bool}` where `True` iff model has `_parent_store=True` and `_parent_name` in fields.

---

## CAP-U56-28 — Spreadsheet Core — Export Logging

### D1: Export audit log
`/spreadsheet/log` (jsonrpc POST, auth=user) logs spreadsheet export actions (`download`, `copy`, `freeze`, `print`) with user ID, action type, and datasource summary (model + fields + groupby + domain) to Python logger at INFO level.

---

## CAP-U56-29 — Spreadsheet Account — Accounting Formulas Backend

### D1: Debit/credit fetch
`account.account.spreadsheet_fetch_debit_credit(args_list)` computes `{'debit': sum, 'credit': sum}` from `account.move.line` using `_build_spreadsheet_formula_domain`. Powers the `ODOO.DEBIT`, `ODOO.CREDIT`, `ODOO.BALANCE` spreadsheet formulas.

### D2: Residual amount fetch
`spreadsheet_fetch_residual_amount(args_list)` aggregates `amount_residual:sum` from `account.move.line`. Powers `ODOO.RESIDUAL`.

### D3: Partner balance fetch
`spreadsheet_fetch_partner_balance(args_list)` aggregates `balance:sum` filtered by `partner_ids` and account domain. Powers `ODOO.PARTNER.BALANCE`.

### D4: Balance tag fetch
`spreadsheet_fetch_balance_tag(args_list)` aggregates `balance:sum` by `account_tag_ids`. Powers `ODOO.BALANCE.TAG`.

### D5: Domain builder logic
`_build_spreadsheet_formula_domain` handles `year`, `month`, `quarter`, `day` period types; balance-sheet accounts use `date <= end` (cumulative); P&L accounts use `date >= start AND date <= end`. Respects `include_unposted` flag.

### D6: Fiscal year boundary
`_get_date_period_boundaries` uses `company.fiscalyear_last_day` and `company.fiscalyear_last_month` for `year` and `day` period types, delegating to `date_utils.get_fiscal_year`.

### D7: Account group lookup
`get_account_group(account_types)` returns an array of code arrays for each `account_type`, ordered matching the input list.

### D8: Fiscal dates for company
`res.company.get_fiscal_dates(payload)` processes `[{"company_id": int|None, "date": str}]` returning `[{"start": date, "end": date}|False]`.

---

## CAP-U56-30 — Spreadsheet Dashboard — Core Model

### D1: spreadsheet.dashboard model
Inherits `spreadsheet.mixin`. Fields: `name` (Char, translatable), `dashboard_group_id` (Many2one, indexed), `sequence` (Integer), `sample_dashboard_file_path` (Char), `is_published` (Boolean, default True), `company_ids` (Many2many `res.company`), `group_ids` (Many2many `res.groups`, default `base.group_user`), `favorite_user_ids` (Many2many `res.users`, domain restricts to current user for write), `is_favorite` (computed, depends_context `uid`), `main_data_model_ids` (Many2many `ir.model`, no copy).

### D2: Sample dashboard fallback
`_dashboard_is_empty` checks if any `main_data_model_ids` model returns 0 records (using `sudo` for access bypass if needed). If empty and `sample_dashboard_file_path` is set, the HTTP controller returns JSON-loaded sample data with `is_sample: True`.

### D3: Serialized readonly dashboard
`_get_serialized_readonly_dashboard` injects user locale and company default currency into the spreadsheet snapshot JSON, wrapping in `{snapshot, revisions: [], default_currency, translation_namespace}`.

### D4: Translation namespace
`_get_dashboard_translation_namespace` finds the `ir.model.data` external ID module for the dashboard record, used for i18n in the frontend.

---

## CAP-U56-31 — Spreadsheet Dashboard — Group Model

### D1: spreadsheet.dashboard.group
Fields: `name` (translatable), `dashboard_ids` (One2many), `published_dashboard_ids` (One2many filtered `is_published=True`), `sequence`. On delete, raises `UserError` if the group has a non-export external ID (prevents deleting module-defined groups).

---

## CAP-U56-32 — Spreadsheet Dashboard — Share Model

### D1: spreadsheet.dashboard.share
Inherits `spreadsheet.mixin`. Fields: `dashboard_id` (Many2one cascade), `excel_export` (Binary), `access_token` (Char, UUID-generated), `full_url` (computed as `{base_url}/dashboard/share/{id}/{access_token}`), `name` (related to dashboard).

### D2: Share URL generation
`action_get_share_url(vals)` optionally zips XLSX files into `excel_export`, creates the share record, and returns its `full_url`.

### D3: Access validation
`_check_dashboard_access` verifies token via `consteq` and checks that the dashboard is readable by the share record's `create_uid`. Raises `Forbidden` on any failure.

---

## CAP-U56-33 — Spreadsheet Dashboard — Controllers

### D1: Dashboard data route
`GET /spreadsheet/dashboard/data/{dashboard}` (auth=user, readonly) returns the serialized snapshot JSON with locale and currency, or sample data if the dashboard is empty and has a sample path.

### D2: Company context from cookie
`cids` cookie is parsed to set `allowed_company_ids` context for multi-company data filtering.

### D3: Public share portal
`GET /dashboard/share/{share_id}/{token}` (auth=public) renders `spreadsheet.public_spreadsheet_layout` with props including `dataUrl`, `downloadExcelUrl` (if user has `base.group_allow_export`), and `mode: "dashboard"`.

### D4: Shared dashboard data
`GET /dashboard/data/{share_id}/{token}` streams `spreadsheet_binary_data` from the share record directly.

### D5: Export download
`GET /dashboard/download/{share_id}/{token}` (auth=user) streams `excel_export` binary; raises `UserError` if user lacks `base.group_allow_export`.

---

## CAP-U56-34 — Spreadsheet Dashboard Sub-modules (data-only)

### D1: No Python models in sub-modules
All eight sub-modules (`spreadsheet_dashboard_account`, `spreadsheet_dashboard_event_sale`, `spreadsheet_dashboard_hr_expense`, `spreadsheet_dashboard_hr_timesheet`, `spreadsheet_dashboard_im_livechat`, `spreadsheet_dashboard_sale`, `spreadsheet_dashboard_sale_timesheet`, `spreadsheet_dashboard_stock_account`) contain only `__init__.py` and `__manifest__.py` (plus XML data). They install dashboard records by XML. RT: exact dashboard configuration content is in XML, not Python.

### D2: Auto-install behaviour
All sub-modules declare `auto_install: [<dependent_module>]`, meaning they install automatically when both `spreadsheet_dashboard` and the specific domain module (e.g., `sale`, `hr_timesheet`, `stock_account`) are present.

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U56-C001 | CAP-U56-01 | sale_expense_margin/models/sale_order_line.py:9 | `expense_id = fields.Many2one('hr.expense', string='Expense')` | FACT | — | — | `sale.order.line` gains a `Many2one` field `expense_id` pointing at `hr.expense` | N-U56-001 |
| VDR-U56-C002 | CAP-U56-01 | sale_expense_margin/models/sale_order_line.py:16 | `product_cost = expense.untaxed_amount_currency / (expense.quantity or 1.0)` | FACT | — | — | Purchase price = `untaxed_amount_currency / quantity` when expense_id is set | N-U56-001 |
| VDR-U56-C003 | CAP-U56-01 | sale_expense_margin/models/account_move_line.py:12 | if self.expense_id | FACT | — | — | When invoice line has `expense_id`, it is propagated to the prepared sale line values | N-U56-001 |
| VDR-U56-C004 | CAP-U56-01 | sale_expense_margin/models/sale_order_line.py:17 | `line.purchase_price = line._convert_to_sol_currency(product_cost, expense.currency_id)` | FACT | — | — | The expense currency is converted to the sale order line's currency | N-U56-001 |
| VDR-U56-C005 | CAP-U56-03 | sale_timesheet_margin/models/sale_order_line.py:9 | `@api.depends('analytic_line_ids.amount', 'qty_delivered_method')` | FACT | — | — | `_compute_purchase_price` depends on analytic line amounts for timesheet lines | N-U56-002 |
| VDR-U56-C006 | CAP-U56-03 | sale_timesheet_margin/models/sale_order_line.py:19 | `lambda sol: sol.qty_delivered_method == 'timesheet' and not sol.product_id.standard_price` | FACT | — | — | Timesheet cost is computed only when `qty_delivered_method == 'timesheet'` and `standard_price == 0` | N-U56-002 |
| VDR-U56-C007 | CAP-U56-03 | sale_timesheet_margin/models/sale_order_line.py:24 | group_amount = self.env['account.analyti | FACT | — | — | Aggregates analytic line amounts and unit amounts per sale line via `_read_group` | N-U56-002 |
| VDR-U56-C008 | CAP-U56-03 | sale_timesheet_margin/models/sale_order_line.py:29 | `- amount_sum / unit_amount_sum if unit_amount_sum else 0.0` | FACT | — | — | Cost per time unit is the negative of amount sum divided by unit amount sum | N-U56-002 |
| VDR-U56-C009 | CAP-U56-03 | sale_timesheet_margin/models/sale_order_line.py:13 | `service_non_timesheet_sols = self.filtered(` | FACT | — | — | Lines that are services with ordered/manual/milestone policies and non-zero purchase_price are excluded from recomputation | N-U56-002 |
| VDR-U56-C010 | CAP-U56-04 | sale_gelato_stock/models/sale_order_line.py:12 | `gelato_lines = self.filtered(lambda l: l.product_id.gelato_product_uid)` | FACT | — | — | Lines with a non-falsy `gelato_product_uid` on the product are filtered out before calling `super()._action_launch_stock_rule` | N-U56-003 |
| VDR-U56-C011 | CAP-U56-05 | sale_project_stock_account/models/stock_move.py:13 | `if self.env.user.company_id.anglo_saxon_accounting:` | FACT | — | — | Expense-policy product exclusion from AAL domain is conditioned on `anglo_saxon_accounting = True` | N-U56-004 |
| VDR-U56-C012 | CAP-U56-05 | sale_project_stock_account/models/stock_move.py:14 | `Domain.AND([domain, [('product_id.expense_policy', 'not in', ('sales_price', 'cost'))]])` | FACT | — | — | Products with `expense_policy` of `sales_price` or `cost` are excluded from valid move domain | N-U56-004 |
| VDR-U56-C013 | CAP-U56-06 | sale_purchase_project/models/sale_order_line.py:11 | `analytic_distribution = self.order_id.project_id._get_analytic_distribution()` | FACT | — | — | Project analytic distribution is fetched from the sale order's linked project | N-U56-005 |
| VDR-U56-C014 | CAP-U56-06 | sale_purchase_project/models/sale_order_line.py:12 | `if not self.analytic_distribution and analytic_distribution:` | FACT | — | — | Project distribution is only applied if the line itself has no explicit `analytic_distribution` | N-U56-005 |
| VDR-U56-C015 | CAP-U56-06 | sale_purchase_project/models/sale_order_line.py:19 | `'project_id': self.order_id.project_id.id,` | FACT | — | — | The `project_id` from the sale order is passed to the purchase order creation values | N-U56-005 |
| VDR-U56-C016 | CAP-U56-07 | sale_service/models/sale_order_line.py:14 | `_name_search_services_index = models.Index("(order_id DESC, sequence, id) WHERE is_service IS TRUE")` | FACT | — | — | A partial index on `(order_id DESC, sequence, id)` is defined for rows where `is_service IS TRUE` | N-U56-006 |
| VDR-U56-C017 | CAP-U56-07 | sale_service/models/sale_order_line.py:17 | `is_service = fields.Boolean("Is a Service", compute='_compute_is_service', store=True, compute_sudo=True` | FACT | — | — | `is_service` is a stored Boolean computed from `product_id.type == 'service'` | N-U56-006 |
| VDR-U56-C018 | CAP-U56-07 | sale_service/models/sale_order_line.py:42-54 | def _auto_init(self) | FACT | — | — | `_auto_init` uses raw SQL to backfill `is_service` column if it doesn't exist, avoiding ORM compute | N-U56-006 |
| VDR-U56-C019 | CAP-U56-09 | sms/models/sms_sms.py:38-40 | `uuid = fields.Char('UUID', copy=False, readonly=True, default=lambda self: uuid4().hex` | FACT | — | — | Each SMS record is assigned a unique UUID on creation via `uuid4().hex` | N-U56-007 |
| VDR-U56-C020 | CAP-U56-09 | sms/models/sms_sms.py:44-51 | state = fields.Selection | FACT | — | — | SMS state machine has six states: outgoing, process, pending, sent, error, canceled | N-U56-007 |
| VDR-U56-C021 | CAP-U56-09 | sms/models/sms_sms.py:79 | `self.env.ref('sms.ir_cron_sms_scheduler_action')._trigger()` | FACT | — | — | Creating an SMS record triggers the scheduler CRON immediately | N-U56-007 |
| VDR-U56-C022 | CAP-U56-09 | sms/models/sms_sms.py:163 | `return int(self.env['ir.config_parameter'].sudo().get_param('sms.session.batch.size', 500))` | FACT | — | — | IAP SMS batch size defaults to 500, configurable via `sms.session.batch.size` | N-U56-007 |
| VDR-U56-C023 | CAP-U56-09 | sms/models/sms_sms.py:237-239 | @api.autovacuum | FACT | — | — | Autovacuum job deletes all SMS records marked `to_delete = TRUE` via direct SQL | N-U56-007 |
| VDR-U56-C024 | CAP-U56-09 | sms/models/sms_sms.py:35-36 | `BOUNCE_DELIVERY_ERRORS = {'sms_invalid_destination', 'sms_not_allowed', 'sms_rejected'}` | FACT | — | — | Three error types are classified as bounce errors (invalid destination, not allowed, rejected) | N-U56-007 |
| VDR-U56-C025 | CAP-U56-09 | sms/models/sms_sms.py:109-118 | `for sms_api, sms in to_send._split_by_api():` | FACT | — | — | `send()` iterates API instances from `_split_by_api()` and sends each batch via `_send()` | N-U56-007 |
| VDR-U56-C026 | CAP-U56-10 | sms/tools/sms_api.py:59 | `DEFAULT_ENDPOINT = 'https://sms.api.odoo.com'` | FACT | — | — | IAP SMS endpoint is `https://sms.api.odoo.com` by default | N-U56-008 |
| VDR-U56-C027 | CAP-U56-10 | sms/tools/sms_api.py:106 | `return self._contact_iap('/api/sms/3/send', {` | FACT | — | — | SMS batch send uses IAP endpoint path `/api/sms/3/send` | N-U56-008 |
| VDR-U56-C028 | CAP-U56-10 | sms/tools/sms_api.py:72 | `if not self.env.registry.ready:` | FACT | — | — | IAP contact is blocked during module installation | N-U56-008 |
| VDR-U56-C029 | CAP-U56-10 | sms/tools/sms_api.py:131 | `def _send_verification_sms(self, phone_number):` | FACT | — | — | Account verification SMS posted to `/api/sms/1/account/create` | N-U56-008 |
| VDR-U56-C030 | CAP-U56-10 | sms/tools/sms_api.py:136 | `def _verify_account(self, verification_code):` | FACT | — | — | Account verification code confirmed via `/api/sms/2/account/verify` | N-U56-008 |
| VDR-U56-C031 | CAP-U56-11 | sms/models/sms_template.py:8 | `_inherit = ['mail.render.mixin', 'template.reset.mixin']` | FACT | — | — | `sms.template` inherits `mail.render.mixin` and `template.reset.mixin` | N-U56-009 |
| VDR-U56-C032 | CAP-U56-11 | sms/models/sms_template.py:13 | `_unrestricted_rendering = True` | FACT | — | — | SMS template rendering is unrestricted (any field accessible) | N-U56-009 |
| VDR-U56-C033 | CAP-U56-11 | sms/models/sms_template.py:24 | `domain=['&', ('is_mail_thread_sms', '=', True), ('transient', '=', False)]` | FACT | — | — | SMS templates can only be applied to non-transient models with SMS capability | N-U56-009 |
| VDR-U56-C034 | CAP-U56-11 | sms/models/sms_template.py:63 | 'context': "{'default_template_id | FACT | — | — | Sidebar action context uses `sms_composition_mode: 'guess'` to auto-determine single vs mass mode | N-U56-009 |
| VDR-U56-C035 | CAP-U56-12 | sms/models/sms_tracker.py:19 | `_name = 'sms.tracker'` | FACT | — | — | `sms.tracker` model links SMS UUID to `mail.notification` | N-U56-010 |
| VDR-U56-C036 | CAP-U56-12 | sms/models/sms_tracker.py:31 | `sms_uuid = fields.Char('SMS uuid', required=True)` | FACT | — | — | Tracker is keyed on `sms_uuid` (unique constraint `sms_uuid_unique`) | N-U56-010 |
| VDR-U56-C037 | CAP-U56-12 | sms/models/sms_tracker.py:32 | `mail_notification_id = fields.Many2one('mail.notification', ondelete='cascade', index='btree_not_null')` | FACT | — | — | Tracker cascades on notification deletion and has a btree_not_null index | N-U56-010 |
| VDR-U56-C038 | CAP-U56-12 | sms/models/sms_tracker.py:46 | `failure_type = f'sms_{provider_error}'` | FACT | — | — | Provider error strings are prefixed with `sms_` to form failure type codes | N-U56-010 |
| VDR-U56-C039 | CAP-U56-13 | sms/models/mail_thread.py:16 | `message_has_sms_error = fields.Boolean(` | FACT | — | — | `mail.thread` gains `message_has_sms_error` computed Boolean for SMS delivery errors | N-U56-011 |
| VDR-U56-C040 | CAP-U56-13 | sms/models/mail_thread.py:47-52 | def message_post | FACT | — | — | For SMS message_type, original body stored as `sms_content`; body converted to HTML with clickable URLs | N-U56-011 |
| VDR-U56-C041 | CAP-U56-13 | sms/models/mail_thread.py:96 | `def _message_sms(self, body, subtype_id=False, partner_ids=False, number_field=False,` | FACT | — | — | `_message_sms` is the core SMS posting method on `mail.thread` | N-U56-011 |
| VDR-U56-C042 | CAP-U56-13 | sms/models/mail_thread.py:129 | subtype_id = self.env['ir.model.data']._ | FACT | — | — | Default subtype for SMS messages is `mail.mt_note` | N-U56-011 |
| VDR-U56-C043 | CAP-U56-13 | sms/models/mail_thread.py:222 | `'sms_tracker_ids': [Command.create({'sms_uuid': sms.uuid})] if sms.state == 'outgoing' else False,` | FACT | — | — | SMS tracker is created only for outgoing SMS, not for already-errored ones | N-U56-011 |
| VDR-U56-C044 | CAP-U56-13 | sms/models/mail_thread.py:230 | if sms_all and not put_in_queue | FACT | — | — | SMS is sent immediately unless `put_in_queue=True` | N-U56-011 |
| VDR-U56-C045 | CAP-U56-14 | sms/models/models.py:8 | `def _sms_get_recipients_info(self, force_field=False, partner_fallback=True):` | FACT | — | — | `_sms_get_recipients_info` is defined on `base` (AbstractModel) and available on all records | N-U56-012 |
| VDR-U56-C046 | CAP-U56-15 | sms/wizard/sms_composer.py:32-36 | composition_mode = fields.Selection | FACT | — | — | Three composition modes: numbers, comment, mass | N-U56-013 |
| VDR-U56-C047 | CAP-U56-15 | sms/wizard/sms_composer.py:280-286 | def _get_blacklist_record_ids | FACT | — | — | Blacklist is loaded from `phone.blacklist` model when `use_exclusion_list = True` | N-U56-013 |
| VDR-U56-C048 | CAP-U56-15 | sms/wizard/sms_composer.py:328-340 | if sanitized and record.id in blacklist_ids | FACT | — | — | Duplicate sanitized numbers in mass send result in `canceled` state with `sms_duplicate` failure | N-U56-013 |
| VDR-U56-C049 | CAP-U56-15 | sms/wizard/sms_composer.py:261-264 | if sms_all and self.mass_force_send | FACT | — | — | `mass_force_send = True` causes immediate send; otherwise SMS remain in queue | N-U56-013 |
| VDR-U56-C050 | CAP-U56-16 | sms/models/ir_actions_server.py:11-12 | state = fields.Selection(selection_add= | FACT | — | — | Server action state gains `sms` option before `followers` | N-U56-014 |
| VDR-U56-C051 | CAP-U56-16 | sms/models/ir_actions_server.py:88 | `def _run_action_sms_multi(self, eval_context=None):` | FACT | — | — | SMS server action runs via `_run_action_sms_multi` creating `sms.composer` | N-U56-014 |
| VDR-U56-C052 | CAP-U56-17 | sms/models/ir_model.py:10 | is_mail_thread_sms = fields.Boolean | FACT | — | — | `is_mail_thread_sms` is a non-stored computed field on `ir.model` | N-U56-015 |
| VDR-U56-C053 | CAP-U56-18 | sms/models/mail_notification.py:10 | notification_type | FACT | — | — | SMS notification type cascades on deletion | N-U56-016 |
| VDR-U56-C054 | CAP-U56-18 | sms/models/mail_notification.py:13 | `sms_id_int = fields.Integer('SMS ID', index='btree_not_null')` | FACT | — | — | `sms_id_int` stores the SMS ID as integer with btree_not_null index (persists after SMS deletion) | N-U56-016 |
| VDR-U56-C055 | CAP-U56-19 | sms/controllers/main.py:15 | `@route('/sms/status', type='jsonrpc', auth='public')` | FACT | — | — | IAP delivery reports webhook at `/sms/status` (public jsonrpc POST) | N-U56-017 |
| VDR-U56-C056 | CAP-U56-19 | sms/controllers/main.py:40 | `request.env['sms.sms'].sudo().search([('uuid', 'in', all_uuids), ('to_delete', '=', False)]).to_delete = True` | FACT | — | — | All processed UUIDs are marked `to_delete = True` after delivery report processing | N-U56-017 |
| VDR-U56-C057 | CAP-U56-20 | sms_twilio/tools/sms_api.py:11 | `class SmsApiTwilio(SmsApiBase):` | FACT | — | — | `SmsApiTwilio` extends `SmsApiBase` (not `SmsApi`), overriding the IAP implementation | N-U56-018 |
| VDR-U56-C058 | CAP-U56-20 | sms_twilio/tools/sms_api.py:30 | try | FACT | — | — | Twilio Messages API endpoint: `https://api.twilio.com/2010-04-01/Accounts/{sid}/Messages.json` | N-U56-018 |
| VDR-U56-C059 | CAP-U56-20 | sms_twilio/tools/sms_api.py:41 | `def _send_sms_batch(self, messages, delivery_reports_url=False):` | FACT | — | — | Twilio sends sequentially (not in batch): one API call per SMS number | N-U56-018 |
| VDR-U56-C060 | CAP-U56-20 | sms_twilio/tools/sms_twilio.py:30 | url = get_twilio_status_callback_url | FACT | — | — | Twilio webhook signature: HMAC-SHA1 of URL + sorted POST params, base64-encoded | N-U56-018 |
| VDR-U56-C061 | CAP-U56-20 | sms_twilio/tools/sms_api.py:83-98 | if error_code in | FACT | — | — | Twilio error codes 21211, 21614, 21265 map to `wrong_number_format` | N-U56-018 |
| VDR-U56-C062 | CAP-U56-21 | sms_twilio/models/res_company.py:12-18 | sms_provider = fields.Selection | FACT | — | — | Company `sms_provider` field selects between IAP (default) and Twilio | N-U56-018 |
| VDR-U56-C063 | CAP-U56-21 | sms_twilio/models/res_company.py:30-34 | `if not account_sid or len(account_sid) != 34 or not account_sid.startswith('AC'):` | FACT | — | — | Twilio Account SID validation: must start 'AC', length 34 | N-U56-018 |
| VDR-U56-C064 | CAP-U56-21 | sms_twilio/models/sms_twilio_number.py:8 | `_name = 'sms.twilio.number'` | FACT | — | — | `sms.twilio.number` model stores one Twilio number per company per country | N-U56-018 |
| VDR-U56-C065 | CAP-U56-22 | sms_twilio/models/sms_sms.py:65 | if company.sms_provider == "twilio | FACT | — | — | Routing to Twilio is per-company: each company can independently use IAP or Twilio | N-U56-019 |
| VDR-U56-C066 | CAP-U56-22 | sms_twilio/models/sms_sms.py:80 | `return int(self.env['ir.config_parameter'].sudo().get_param('sms_twilio.session.batch.size', 10))` | FACT | — | — | Twilio batch size defaults to 10 (vs IAP 500) | N-U56-019 |
| VDR-U56-C067 | CAP-U56-22 | sms_twilio/models/sms_sms.py:96 | `if sms and sms.sms_tracker_id and result.get('sms_twilio_sid'):` | FACT | — | — | Twilio SID stored on tracker (not SMS record which is deleted) | N-U56-019 |
| VDR-U56-C068 | CAP-U56-23 | sms_twilio/controllers/controllers.py:33 | `@route('/sms_twilio/status/<string:uuid>', type='http', auth='public', methods=['POST'], csrf=False)` | FACT | — | — | Twilio status callback at `/sms_twilio/status/{uuid}` (public HTTP POST, no CSRF) | N-U56-019 |
| VDR-U56-C069 | CAP-U56-23 | sms_twilio/controllers/controllers.py:14-26 | TWILIO_TO_SMS_STATE = | FACT | — | — | Full Twilio status → Odoo SMS state mapping defined in controller | N-U56-019 |
| VDR-U56-C070 | CAP-U56-23 | sms_twilio/models/sms_tracker.py:5-12 | '30002': "expired",  # Account suspended | FACT | — | — | Eight Twilio delivery error codes mapped to Odoo failure type strings | N-U56-019 |
| VDR-U56-C071 | CAP-U56-24 | snailmail_account/models/account_move_send.py:37 | `'report_template': self.env['ir.actions.report']._get_report('account.account_invoices').id` | FACT | — | — | Snailmail letters use the `account.account_invoices` report template | N-U56-020 |
| VDR-U56-C072 | CAP-U56-24 | snailmail_account/models/account_move_send.py:47 | `def _is_applicable_to_move(self, method, move, **move_data):` | FACT | — | — | `snailmail` sending method is applicable only when partner has a valid address | N-U56-020 |
| VDR-U56-C073 | CAP-U56-24 | snailmail_account/models/account_move_send.py:65 | ._snailmail_print(immediate=False) | FACT | — | — | Snailmail letters are created and printed with `immediate=False` (queued, not instant) | N-U56-020 |
| VDR-U56-C074 | CAP-U56-24 | snailmail_account/models/account_move.py:7-13 | @api.ondelete(at_uninstall=False) | FACT | — | — | On invoice delete, snailmail letters linked via `res_id` are also deleted | N-U56-020 |
| VDR-U56-C075 | CAP-U56-24 | snailmail_account/models/res_partner.py:7-8 | invoice_sending_method = fields.Selection | FACT | — | — | Partner's invoice_sending_method gains `snailmail` → `by Post` option | N-U56-020 |
| VDR-U56-C076 | CAP-U56-24 | snailmail_account/wizard/account_move_send_batch_wizard.py:8 | `send_by_post_stamps = fields.Integer(compute='_compute_send_by_post_stamps')` | FACT | — | — | Batch wizard computes stamp count as number of partners with valid snailmail addresses | N-U56-020 |
| VDR-U56-C077 | CAP-U56-24 | snailmail_account/controllers/portal.py:12 | `rendering_values['invoice_sending_methods'].update({'snailmail': _("by Post")})` | FACT | — | — | Portal invoice sending methods displays snailmail as "by Post" | N-U56-020 |
| VDR-U56-C078 | CAP-U56-25 | social_media/models/res_company.py:10-17 | social_twitter = fields.Char('X Account') | FACT | — | — | `res.company` gains eight social network URL/handle fields: Twitter/X, Facebook, GitHub, LinkedIn, YouTube, Instagram, TikTok, Discord | N-U56-021 |
| VDR-U56-C079 | CAP-U56-26 | spreadsheet/models/spreadsheet_mixin.py:17 | class SpreadsheetMixin(models.AbstractModel) | FACT | — | — | `spreadsheet.mixin` is an AbstractModel with `_auto = False` (no database table) | N-U56-022 |
| VDR-U56-C080 | CAP-U56-26 | spreadsheet/models/spreadsheet_mixin.py:22-25 | spreadsheet_binary_data = fields.Binary | FACT | — | — | Default spreadsheet content is set from `_empty_spreadsheet_data_base64()` | N-U56-022 |
| VDR-U56-C081 | CAP-U56-26 | spreadsheet/models/spreadsheet_mixin.py:38-39 | `if data.get("[Content_Types].xml"):` | FACT | — | — | XLSX files are identified by presence of `[Content_Types].xml` key and skip Odoo-specific field validation | N-U56-022 |
| VDR-U56-C082 | CAP-U56-26 | spreadsheet/models/spreadsheet_mixin.py:96-99 | `spreadsheet.spreadsheet_file_name = f"{spreadsheet.display_name}.osheet.json"` | FACT | — | — | Download filename is `{display_name}.osheet.json` | N-U56-022 |
| VDR-U56-C083 | CAP-U56-26 | spreadsheet/models/spreadsheet_mixin.py:136-148 | locale = lang._odoo_lang_to_spreadsheet_locale() | FACT | — | — | Empty workbook JSON structure includes `revisionId: "START_REVISION"` | N-U56-022 |
| VDR-U56-C084 | CAP-U56-26 | spreadsheet/models/spreadsheet_mixin.py:107-121 | `def get_display_names_for_spreadsheet(self, args):` | FACT | — | — | `get_display_names_for_spreadsheet` uses `active_test=False` to include archived records | N-U56-022 |
| VDR-U56-C085 | CAP-U56-27 | spreadsheet/models/res_currency.py:9 | `def get_company_currency_for_spreadsheet(self, company_id=None):` | FACT | — | — | Returns `{code, symbol, decimalPlaces, position}` for company currency | N-U56-023 |
| VDR-U56-C086 | CAP-U56-27 | spreadsheet/models/res_currency_rate.py:8 | `def _get_rate_for_spreadsheet(self, currency_from_code, currency_to_code, date=None, company_id=None):` | FACT | — | — | Currency conversion uses `Currency._get_conversion_rate` with optional date and company context | N-U56-023 |
| VDR-U56-C087 | CAP-U56-27 | spreadsheet/models/res_lang.py:37 | `"formulaArgSeparator": ";" if self.decimal_point == "," else ","` | FACT | — | — | Formula argument separator is `;` when decimal separator is `,`, else `,` | N-U56-023 |
| VDR-U56-C088 | CAP-U56-27 | spreadsheet/utils/formatting.py:61 | `INITIAL_1900_DAY = datetime(1899, 12, 30)` | FACT | — | — | Spreadsheet date serial baseline is 1899-12-30 (Excel/Lotus epoch) | N-U56-023 |
| VDR-U56-C089 | CAP-U56-28 | spreadsheet/controllers/main.py:13 | `@http.route("/spreadsheet/log", type="jsonrpc", auth="user", methods=["POST"])` | FACT | — | — | Spreadsheet export actions are logged via `/spreadsheet/log` endpoint (auth=user) | N-U56-024 |
| VDR-U56-C090 | CAP-U56-28 | spreadsheet/controllers/main.py:18 | if action_type not | FACT | — | — | Only download, copy, freeze, and print actions are logged | N-U56-024 |
| VDR-U56-C091 | CAP-U56-29 | spreadsheet_account/models/account.py:108 | `def spreadsheet_fetch_debit_credit(self, args_list):` | FACT | — | — | `spreadsheet_fetch_debit_credit` aggregates `debit:sum` and `credit:sum` from `account.move.line` | N-U56-025 |
| VDR-U56-C092 | CAP-U56-29 | spreadsheet_account/models/account.py:134 | `def spreadsheet_fetch_residual_amount(self, args_list):` | FACT | — | — | `spreadsheet_fetch_residual_amount` aggregates `amount_residual:sum` | N-U56-025 |
| VDR-U56-C093 | CAP-U56-29 | spreadsheet_account/models/account.py:23-25 | fiscal_day = company.fiscalyear_last_day | FACT | — | — | Fiscal year period uses company's `fiscalyear_last_day` and `fiscalyear_last_month` | N-U56-025 |
| VDR-U56-C094 | CAP-U56-29 | spreadsheet_account/models/account.py:49-56 | balance_domain = Domain | FACT | — | — | Balance-sheet accounts accumulate from inception (`date <= end`); P&L accounts use period bounds | N-U56-025 |
| VDR-U56-C095 | CAP-U56-29 | spreadsheet_account/models/account.py:83 | `posted_domain = [("move_id.state", "!=", "cancel")] if formula_params.get("include_unposted") else [("move_id.state", "=", "posted")]` | FACT | — | — | `include_unposted` flag controls whether to include draft journal entries | N-U56-025 |
| VDR-U56-C096 | CAP-U56-29 | spreadsheet_account/models/account.py:191 | `def get_account_group(self, account_types):` | FACT | — | — | `get_account_group` returns arrays of account codes grouped by `account_type` | N-U56-025 |
| VDR-U56-C097 | CAP-U56-29 | spreadsheet_account/models/account.py:95 | `def spreadsheet_move_line_action(self, args):` | FACT | — | — | `spreadsheet_move_line_action` returns an `ir.actions.act_window` on `account.move.line` for audit drill-down | N-U56-025 |
| VDR-U56-C098 | CAP-U56-29 | spreadsheet_account/models/res_company.py:12 | `def get_fiscal_dates(self, payload):` | FACT | — | — | `get_fiscal_dates` returns `{start, end}` fiscal year boundaries for a list of company/date pairs | N-U56-025 |
| VDR-U56-C099 | CAP-U56-30 | spreadsheet_dashboard/models/spreadsheet_dashboard.py:7 | class SpreadsheetDashboard(models.Model) | FACT | — | — | `spreadsheet.dashboard` inherits `spreadsheet.mixin`, ordered by `sequence` | N-U56-026 |
| VDR-U56-C100 | CAP-U56-30 | spreadsheet_dashboard/models/spreadsheet_dashboard.py:18 | `company_ids = fields.Many2many('res.company', string="Companies")` | FACT | — | — | Dashboards can be restricted to specific companies via `company_ids` | N-U56-026 |
| VDR-U56-C101 | CAP-U56-30 | spreadsheet_dashboard/models/spreadsheet_dashboard.py:19 | `group_ids = fields.Many2many('res.groups', default=lambda self: self.env.ref('base.group_user'))` | FACT | — | — | Default access group is `base.group_user` (all internal users) | N-U56-026 |
| VDR-U56-C102 | CAP-U56-30 | spreadsheet_dashboard/models/spreadsheet_dashboard.py:31 | `main_data_model_ids = fields.Many2many('ir.model', copy=False)` | FACT | — | — | `main_data_model_ids` links to the models whose data populates the dashboard (for empty-check) | N-U56-026 |
| VDR-U56-C103 | CAP-U56-30 | spreadsheet_dashboard/models/spreadsheet_dashboard.py:67 | for model_name in | FACT | — | — | Dashboard is considered empty if any main data model has zero records | N-U56-026 |
| VDR-U56-C104 | CAP-U56-30 | spreadsheet_dashboard/models/spreadsheet_dashboard.py:50 | `default_currency = self.env['res.currency'].get_company_currency_for_spreadsheet()` | FACT | — | — | Serialized dashboard JSON includes company default currency | N-U56-026 |
| VDR-U56-C105 | CAP-U56-31 | spreadsheet_dashboard/models/spreadsheet_dashboard_group.py:5 | `_name = 'spreadsheet.dashboard.group'` | FACT | — | — | Dashboard groups cannot be deleted if they have a non-`__export__` external ID | N-U56-027 |
| VDR-U56-C106 | CAP-U56-32 | spreadsheet_dashboard/models/spreadsheet_dashboard_share.py:16 | `access_token = fields.Char(required=True, default=lambda _x: str(uuid.uuid4()))` | FACT | — | — | Share access token is a UUID4 string generated on creation | N-U56-028 |
| VDR-U56-C107 | CAP-U56-32 | spreadsheet_dashboard/models/spreadsheet_dashboard_share.py:22 | `share.full_url = "%s/dashboard/share/%s/%s" % (share.get_base_url(), share.id, share.access_token)` | FACT | — | — | Share URL pattern: `{base_url}/dashboard/share/{id}/{access_token}` | N-U56-028 |
| VDR-U56-C108 | CAP-U56-32 | spreadsheet_dashboard/models/spreadsheet_dashboard_share.py:44 | user_access = dashboard.has_access("read") | FACT | — | — | Dashboard access check uses the share creator's user ID for `has_access` check | N-U56-028 |
| VDR-U56-C109 | CAP-U56-33 | spreadsheet_dashboard/controllers/dashboards_controllers.py:8 | @http.route | FACT | — | — | Dashboard data route uses model converter `model("spreadsheet.dashboard")` with user auth | N-U56-029 |
| VDR-U56-C110 | CAP-U56-33 | spreadsheet_dashboard/controllers/dashboards_controllers.py:18 | `cids_str = request.cookies.get('cids', str(request.env.user.company_id.id))` | FACT | — | — | Company IDs are read from the `cids` cookie for multi-company context | N-U56-029 |
| VDR-U56-C111 | CAP-U56-33 | spreadsheet_dashboard/controllers/dashboards_controllers.py:20-27 | `if dashboard.sample_dashboard_file_path and dashboard._dashboard_is_empty():` | FACT | — | — | Sample data (from file) replaces live data when dashboard is empty and has a sample path | N-U56-029 |
| VDR-U56-C112 | CAP-U56-33 | spreadsheet_dashboard/controllers/share.py:6 | `@http.route(['/dashboard/share/<int:share_id>/<token>'], type='http', auth='public')` | FACT | — | — | Dashboard share portal is public (no login required) | N-U56-029 |
| VDR-U56-C113 | CAP-U56-33 | spreadsheet_dashboard/controllers/share.py:13 | if request.env.user.has_group | FACT | — | — | Download URL on shared dashboard is only provided to users with `base.group_allow_export` | N-U56-029 |
| VDR-U56-C114 | CAP-U56-34 | spreadsheet_dashboard_sale/__manifest__.py:9 | `'depends': ['spreadsheet_dashboard', 'sale']` | FACT | — | — | `spreadsheet_dashboard_sale` depends on both `spreadsheet_dashboard` and `sale` | N-U56-030 |
| VDR-U56-C115 | CAP-U56-34 | spreadsheet_dashboard_account/__manifest__.py:9 | 'depends': ['spreadsheet_dashboard', 'account'] | FACT | — | — | All dashboard sub-modules use `auto_install` keyed on their domain module | N-U56-030 |
| VDR-U56-C116 | CAP-U56-34 | spreadsheet_dashboard_hr_expense/__manifest__.py:8 | `'depends': ['spreadsheet_dashboard', 'sale_expense']` | FACT | — | — | HR expense dashboard depends on `sale_expense` (not `hr_expense` directly) | N-U56-030 |
| VDR-U56-C117 | CAP-U56-09 | sms/models/sms_sms.py:188 | def _send_with_api | FACT | — | — | IAP batch messages are grouped by body content before sending | N-U56-007 |
| VDR-U56-C118 | CAP-U56-10 | sms/tools/sms_api.py:74-77 | params['account_token'] | FACT | — | — | IAP contact uses `account_token` from `iap.account` and custom endpoint from config | N-U56-008 |
| VDR-U56-C119 | CAP-U56-29 | spreadsheet_account/models/account.py:203 | `def spreadsheet_fetch_balance_tag(self, args_list):` | FACT | — | — | Balance tag formula backend uses `account_tag_ids` as integer filter on move lines | N-U56-025 |
| VDR-U56-C120 | CAP-U56-27 | spreadsheet/models/ir_model.py:10 | @api.model | FACT | — | — | `has_searchable_parent_relation` requires both `_parent_store=True` AND `_parent_name` present in fields | N-U56-023 |
| VDR-U56-C121 | CAP-U56-26 | spreadsheet/utils/validate_data.py:186 | def fields_in_spreadsheet | INFERENCE | test mode only | — | Field and menu validation in `_check_spreadsheet_data` runs only in test mode (`tools.config['test_enable']` or `test_file`) | N-U56-022 |
| VDR-U56-C122 | CAP-U56-08 | sale_sms/__manifest__.py:5 | Sale - SMS | FACT | — | — | `sale_sms` module contains no Python model code; contributes only XML data/views | N-U56-031 |
| VDR-U56-C123 | CAP-U56-02 | sale_mrp_margin/tests/test_sale_mrp_flow.py:51 | `self.assertEqual(so.order_line.purchase_price, 60)` | FACT | — | — | Test verifies nested phantom BOM cost = 2 * 3 * $10 = $60 per super kit unit | N-U56-032 |
| VDR-U56-C124 | CAP-U56-02 | sale_mrp_margin/tests/test_sale_mrp_flow.py:194 | Without normalization | FACT | — | — | Test confirms BOM qty normalisation: 12-unit BOM with $360 total cost gives $30/unit purchase price | N-U56-032 |
| VDR-U56-C125 | CAP-U56-02 | sale_mrp_margin/tests/test_sale_mrp_flow.py:325 | `self.assertEqual(so.order_line.purchase_price, 7.5)` | FACT | — | — | Test verifies manufacturing move is excluded from AVCO delivery cost: only outgoing delivery $7.5 used, not average of MO + delivery | N-U56-032 |
