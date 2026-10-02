# U62 — PEPPOL, IoT, lunch, mass mailing, payment providers (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U62
- Modules: account_peppol, account_peppol_advanced_fields, account_qr_code_sepa, data_recycle, iot_base, l10n_account_edi_ubl_cii_tests, l10n_account_withholding_tax_pos, lunch, marketing_card, mass_mailing, mass_mailing_crm, mass_mailing_event, mass_mailing_event_sms, mass_mailing_event_track_sms, mass_mailing_sale, mass_mailing_slides, mass_mailing_sms, payment_adyen, payment_aps, payment_asiapay, payment_authorize, payment_buckaroo, payment_demo
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: C-priority (dependency of CURRENT modules). l10n_account_withholding_tax_pos is CRITICAL for Thai scope. Source evidence only; RT flags for runtime unknowns.

---

## CAP-U62-01 PEPPOL Registration and Proxy State Management

### D1 Proxy state lifecycle
The company field `account_peppol_proxy_state` tracks five states: `not_registered`, `sender`, `smp_registration`, `receiver`, `rejected`. These are defined in `res_company.py:70-79`. Transition from `sender` to `receiver` involves a call to the IAP endpoint `1/register_sender_as_receiver` (line 553) after checking that no existing participant is already registered at the given EAS:endpoint.

### D2 EAS / endpoint validation
`res_company.py:29-51` defines `PEPPOL_ENDPOINT_RULES` (hard validation) and `PEPPOL_ENDPOINT_WARNINGS` (soft validation). Rules exist for EAS codes `0007` (Sweden), `0088` (EAN), `0184` (Denmark), `0192` (Norway), `0208` (Belgium). Sanitizers strip to numeric-only forms for `0007`, `0184`, `0192`, `0208`. There is no EAS rule specific to Thailand in this module; Thai EAS codes (if any) would be handled by country defaults or custom addition.

### D3 IAP connector URLs
`tools/peppol_iap_connector.py:12-15` declares `PEPPOL_PROXY_URLS = {'prod': 'https://peppol.api.odoo.com', 'test': 'https://peppol.test.odoo.com'}`. The edi mode is resolved via `_get_peppol_edi_mode()` which checks `ir.config_parameter` key `account_peppol.edi.mode` first (line 398-402, res_company.py).

### D4 Webhook token generation
`account_edi_proxy_user.py:648-652` — webhook token is generated via `tools.hash_sign(self.sudo().env, 'account_peppol_webhook', msg, expiration_hours=expiration)` where `expiration = 30 * 24` hours (30 days). The webhook endpoint on company is `urljoin(self.get_base_url(), '/peppol/webhook')`.

### D5 Out-of-sync handling
`account_edi_proxy_user.py:111-132` — on `invalid_signature` error from IAP, `_mark_connection_out_of_sync()` sets `is_token_out_of_sync=True`, `refresh_token=None`, then calls `/api/peppol/1/mark_connection_out_of_sync`. If the response is `connection_superseded`, the method `_peppol_out_of_sync_disconnect_this_database()` unlinks the proxy user and resets the company configuration.

### Ten-dimension table — CAP-U62-01

| Dimension | Finding |
|---|---|
| Data model | `account_edi_proxy_client.user` (extended), `res.company` (extended) |
| State machine | 5 states: not_registered → sender → smp_registration → receiver; rejected terminal |
| IAP dependency | Hard dependency on `https://peppol.api.odoo.com` / `https://peppol.test.odoo.com` |
| Config param | `account_peppol.edi.mode` in `ir.config_parameter` |
| Cron jobs | 4 crons: get_new_documents, get_message_status, get_participant_status, webhook_keepalive |
| Validation | Hard rules for 4 EAS codes (SE, EAN, DK, NO, BE); sanitizers for 4; warnings for AU, IT |
| Thailand relevance | No Thailand-specific EAS rule; Thai registration uses generic EAS path — RT |
| Token security | HMAC-signed webhook token, 30-day TTL |
| Self-billing | Type codes 389/527 (self-billing invoice) and 261 (self-billing credit note) auto-route to sale journal |
| Deregistration | Full flush of pending documents before IAP deregistration |

---

## CAP-U62-02 PEPPOL Document Sending and Receiving

### D1 Incoming document processing
`account_edi_proxy_user.py:292-372` — `_peppol_get_new_documents()` fetches up to `BATCH_SIZE=50` (line 17) messages per invocation from IAP endpoint `1/get_all_documents`. Duplicate detection is based on `peppol_message_uuid` in `account.move`. After processing, acknowledgement is sent to `1/ack`.

### D2 Outgoing document state
`account_move.py:16-28` (account_peppol) — `peppol_move_state` selection: `ready`, `to_send`, `skipped`, `processing`, `done`, `error`. The field `peppol_is_sent` (line 29) is True when state is not in `{False, 'ready', 'to_send', 'error', 'skipped'}`.

### D3 UBL BIS3 constraint
`account_edi_xml_ubl_bis3.py:7-29` — when context `from_peppol` is set, two additional constraints are enforced: `PEPPOL-EN16931-R010` (customer must have EAS endpoint ID) and `PEPPOL-EN16931-R020` (supplier must have EAS endpoint ID).

### D4 Default sending methods
`account_move_send.py:20-29` — PEPPOL is added as default sending method if `_is_applicable_to_move('peppol', move)` and any partner country is in `PEPPOL_DEFAULT_COUNTRIES`.

### D5 Embedded document handling
`account_edi_proxy_user.py:19-23` — regex `REMOVE_EMBEDDED_DOCUMENT_BINARY_OBJECT_RE` strips `EmbeddedDocumentBinaryObject` elements from XML before parsing when `xml_tree` is None (fallback for large files).

### Ten-dimension table — CAP-U62-02

| Dimension | Finding |
|---|---|
| Batch size | 50 documents per cron run (configurable via `peppol_crons_job_count` context key) |
| Dedup logic | UUID-based dedup via `account.move.peppol_message_uuid` |
| Self-billed routing | Type codes 389/527/261 → `out_invoice` in sale journal with `is_self_billing=True` flag |
| Constraint enforcement | EN16931-R010/R020 EAS endpoint constraints on both parties |
| Retry trigger | Cron re-triggered immediately if more than `job_count` messages found |
| Cancel restriction | Cannot cancel after `peppol_is_sent=True`; `show_reset_to_draft_button` hidden |
| Default countries | PEPPOL_DEFAULT_COUNTRIES drives auto-selection of PEPPOL as send method |
| Encryption | Documents decrypted via `_decrypt_data(document_content, enc_key)` |
| Journal flag | `is_peppol_journal` on `account.journal` marks the designated purchase journal |
| Partner verify | Post-processing triggers `button_account_peppol_check_partner_endpoint()` for unverified partners |

---

## CAP-U62-03 PEPPOL Partner Verification

### D1 NAPTR DNS lookup
`res_partner.py:150-183` — `_peppol_lookup_participant()` calls Odoo's PEPPOL proxy endpoint `1/lookup` with `peppol_identifier` query parameter. In demo mode, the call is skipped. Returns JSON result or None on error/not-found.

### D2 Verification state
`res_partner.py:29-38` — `peppol_verification_state` is a `company_dependent` selection field with states: `not_verified`, `not_valid`, `not_valid_format`, `valid`.

### D3 Document type check
`res_partner.py:185-198` — `_check_document_type_support()` checks that `expected_customization_id` (from `_get_customization_id()`) appears in the participant's services list. Deprecated fallback parses XML SMP response.

### D4 Belgian pre-registration exclusion
`res_partner.py:144-147` — Belgian companies are pre-registered on hermes-belgium; `_check_peppol_participant_exists()` excludes them by checking `'hermes-belgium' not in service_href`.

### Ten-dimension table — CAP-U62-03

| Dimension | Finding |
|---|---|
| Lookup method | NAPTR DNS via Odoo proxy `/api/peppol/1/lookup` |
| State field type | `company_dependent` — state varies per company |
| Demo mode | No lookup in demo mode (returns None) |
| Belgian exception | `hermes-belgium` pre-registration excluded from valid participants |
| Format validation | Checks customization ID in services array |
| Frontend writable | `peppol_eas` and `peppol_endpoint` exposed as frontend-writable fields |
| Auto-check | `create()` override calls `_update_peppol_state_per_company()` for all new partners |
| Write trigger | EAS/endpoint/edi_format changes trigger re-verification |
| Company scope | Verification per-company if partner has `company_id`; otherwise all PEPPOL-active companies checked |
| Tracking | State changes logged via `_log_verification_state_update()` using custom HTML body |

---

## CAP-U62-04 PEPPOL Advanced Fields (account_peppol_advanced_fields)

### D1 Deprecated fields
`account_peppol_advanced_fields/models/account_move.py:7-34` — all seven fields are marked `[DEPRECATED]` in their string labels: `peppol_contract_document_reference`, `peppol_project_reference`, `peppol_originator_document_reference`, `peppol_despatch_document_reference`, `peppol_additional_document_reference`, `peppol_accounting_cost`, `peppol_delivery_location_id`.

### Ten-dimension table — CAP-U62-04

| Dimension | Finding |
|---|---|
| Status | All 7 extended fields marked deprecated in label string |
| Model | `account.move` (inherited) |
| Purpose | PEPPOL business term extensions (contract ref, project ref, originator doc, despatch doc, additional doc, accounting cost, GLN) |
| GLN field | `peppol_delivery_location_id` stores Global Location Number (GLN) |
| Migration risk | Deprecated fields remain in DB schema; data migration may be needed to remove |
| No logic | Module contains only field definitions, no methods |

---

## CAP-U62-05 SEPA QR Code (account_qr_code_sepa)

### D1 QR method registration
`res_bank.py:76-80` — `_get_available_qr_methods()` appends `('sct_qr', _("SEPA Credit Transfer QR"), 20)` to available QR methods. Priority 20.

### D2 QR payload format
`res_bank.py:11-36` — `_get_qr_vals()` constructs a 12-line EPC QR code payload: Service Tag `BCD`, Version `002`, Character Set `1`, Identification `SCT`, BIC, beneficiary name (max 71 chars), IBAN, `currency+amount`, empty purpose, structured communication, unstructured comment (max 141 chars), empty beneficiary-to-originator. Amount formatted via `float_repr(currency.round(amount), currency.decimal_places)`.

### D3 Error conditions
`res_bank.py:50-66` — SEPA QR requires: EUR currency only; IBAN account type only; account IBAN prefix in SEPA zone. Non-IBAN country codes excluded: `AX, NC, YT, TF, BL, RE, MF, GP, PM, PF, GF, MQ, JE, GG, IM`.

### D4 Generation parameters
`res_bank.py:38-48` — QR generation uses `barcode_type='QR'`, `quiet=0`, `width=128`, `height=128`, `humanreadable=1`. Values joined by `\n`.

### D5 Thailand relevance
Thailand does not use SEPA (SEPA is a European payment scheme). This module has limited direct Thailand scope. QR code payment in Thailand uses PromptPay standards, not SEPA Credit Transfer. However, if a Thai company has European bank accounts (e.g., subsidiary), this module may apply. RT — actual usage in Thai context depends on runtime configuration.

### Ten-dimension table — CAP-U62-05

| Dimension | Finding |
|---|---|
| QR standard | EPC QR Code (European Payments Council) v002 |
| Currency | EUR only |
| Account type | IBAN only |
| SEPA zone | Checked against `base.sepa_zone` country group |
| Format | 12-line newline-separated text payload |
| Beneficiary name | Truncated to 71 characters |
| Unstructured ref | Truncated to 141 characters; mutually exclusive with structured ref |
| Priority | 20 (lower = higher priority in QR method list) |
| Thailand relevance | Low — SEPA is European; PromptPay is the Thai QR standard |
| QR size | 128×128 pixels |

---

## CAP-U62-06 Data Recycle (data_recycle)

### D1 Recycle model configuration
`data_recycle_model.py:20-70` — `data_recycle.model` stores recycling rules: target model, domain filter, time field with delta (days/weeks/months/years), recycle mode (manual/automatic), recycle action (archive/unlink), notification users, notification frequency.

### D2 Batch size constants
`data_recycle_model.py:15-16` — `DR_CREATE_STEP_AUTO = 5000`, `DR_CREATE_STEP_MANUAL = 50000`. Automatic mode uses smaller batches because `action_validate()` is called per batch, which is slower.

### D3 Automatic vs manual mode
`data_recycle_model.py:136-148` — automatic mode immediately calls `action_validate()` on each created `data_recycle.record` batch. Manual mode creates records for user review without acting.

### D4 Validate action
`data_recycle_record.py:66-84` — `action_validate()` separates records into archive-list and unlink-list, then calls `action_archive()` or `unlink()` on the originals via `sudo()`. The recycle record itself is unlinked after action.

### D5 Notification
`data_recycle_model.py:150-167` — `_notify_records_to_recycle()` sends notifications only to users in `base.group_system`. Frequency controlled by `notify_frequency` + `notify_frequency_period`. `last_notification` datetime prevents duplicate sends.

### D6 Batch commits
`data_recycle_model.py:139-142` — `batch_commits=True` triggers `env.cr.commit()` after each batch iteration (except in test mode) to prevent full rollback on timeout.

### Ten-dimension table — CAP-U62-06

| Dimension | Finding |
|---|---|
| Model | `data_recycle.model` (rule) + `data_recycle.record` (matched record) |
| Batch sizes | Auto: 5,000 records; Manual: 50,000 records |
| Actions | archive (requires active field on model) or unlink |
| Modes | manual (user reviews) or automatic (immediate action) |
| Constraint | `archive` action fails if model has no `active` field |
| Archive guard | Deactivating a recycle model triggers unlink of its records |
| Notify scope | Only `base.group_system` users receive notifications |
| Time-based filter | Supports date/datetime fields with configurable delta |
| Commit strategy | Periodic commit during cron to survive timeout |
| Discard | `action_discard()` sets `active=False` on record (soft delete) |

---

## CAP-U62-07 IoT Base (iot_base)

### D1 Module composition
`iot_base/__manifest__.py:1-23` — module is categorized `Hidden`, depends only on `web`. No Python models defined (`__init__.py` is empty). All functionality is JavaScript-based: `iot_base/static/src/network_utils/*` and `iot_base/static/src/device_controller.js`, loaded in `web.assets_backend`.

### D2 No Python model
The module provides no Python-side ORM model. IoT device management and proxy connectivity are implemented entirely in JavaScript frontend assets. No server-side evidence available from Python source. RT — actual device communication protocol and proxy discovery are JavaScript runtime behaviors.

### Ten-dimension table — CAP-U62-07

| Dimension | Finding |
|---|---|
| Python models | None — empty `__init__.py` |
| Assets | `network_utils/*` JS + `device_controller.js` in backend |
| Dependencies | `web` only |
| Category | Hidden (infrastructure dependency) |
| Runtime behavior | RT — all logic in JS; cannot read from Python source |
| License | LGPL-3 |

---

## CAP-U62-08 UBL/CII Test Helpers (l10n_account_edi_ubl_cii_tests)

### D1 Test scope
`l10n_account_edi_ubl_cii_tests` contains only test files. Test modules found: BE, DE, NL, attached document, AU, US (CII), FR (CII), SG. No Thailand-specific UBL test file found in this module.

### D2 Common test base
`tests/common.py` provides shared test setup. Individual test files (`test_xml_ubl_be.py`, `test_xml_ubl_de.py`, etc.) test format-specific UBL/CII generation.

### D3 Thailand relevance
No `test_xml_ubl_th*.py` file exists in this module. UBL tests for Thailand would need to be in `l10n_th` or a Thailand-specific EDI test module. This module provides generic UBL/CII testing infrastructure for use by localization modules.

### Ten-dimension table — CAP-U62-08

| Dimension | Finding |
|---|---|
| Purpose | Test helpers/suites for UBL and CII format validation |
| Countries covered | BE, DE, NL, AU, US, FR, SG (no TH) |
| Python-only | All content is test code, no production models |
| Thailand relevance | Indirect — provides test patterns; TH tests absent |
| License | via manifest only |

---

## CAP-U62-09 Withholding Tax at POS — Thailand CRITICAL (l10n_account_withholding_tax_pos)

### D1 Module purpose
`__manifest__.py:3-16` — "Add support for the withholding tax module in the PoS." Depends on `l10n_account_withholding_tax` and `point_of_sale`. `auto_install=True`. Category `Accounting/Localizations`. License LGPL-3.

### D2 Python model
`models/account_tax.py:5-13` — `AccountTax` inherits `account.tax` and overrides `_load_pos_data_fields()`. It appends `is_withholding_tax_on_payment` to the fields list. This ensures the field is available in the POS `batch_for_taxes_computation` operation.

### D3 JavaScript assets
`__manifest__.py:9-11` — the POS asset bundle `point_of_sale._assets_pos` loads `l10n_account_withholding_tax/static/src/helpers/*.js`. This JavaScript code provides withholding tax computation helpers for POS sessions.

### D4 Thailand relevance
Withholding tax (WHT) at Point of Sale is critical for Thailand operations. Thai businesses must deduct WHT at source for services. This module bridges the `l10n_account_withholding_tax` accounting module with POS operations. The `is_withholding_tax_on_payment` field allows the POS to identify and apply WHT when processing payments.

### Ten-dimension table — CAP-U62-09

| Dimension | Finding |
|---|---|
| CRITICAL TAG | Thailand WHT at POS — critical for Thai scope |
| Depends | `l10n_account_withholding_tax` + `point_of_sale` |
| Auto-install | True — installs automatically when both dependencies are present |
| Field extended | `is_withholding_tax_on_payment` added to `_load_pos_data_fields()` |
| JS assets | WHT computation helpers loaded in POS asset bundle |
| Python logic | Minimal — single model override, single method override |
| Configuration RT | RT — actual WHT rates, tax codes, and POS payment flow are runtime configured |
| Thai compliance | Enables Thai WHT deduction at POS checkout |
| License | LGPL-3 |
| Integration point | `batch_for_taxes_computation` in POS — RT |

---

## CAP-U62-10 Lunch Module

### D1 Core models
Lunch module provides: `lunch.order`, `lunch.cashmove`, `lunch.supplier`, `lunch.product`, `lunch.product.category`, `lunch.topping`, `lunch.location`, `lunch.alert`, and a report model `lunch.cashmove.report`.

### D2 Order state machine
`lunch_order.py:35-40` — order states: `new` (To Order), `ordered` (Ordered), `sent` (Sent to supplier), `confirmed` (Received), `cancelled`.

### D3 Cash move wallet
`lunch_cashmove.py:26-31` — `get_wallet_balance()` reads from `lunch.cashmove.report` search_read, sums `amount`, rounds to 2 decimal places, and adds `company_id.lunch_minimum_threshold`.

### D4 Topping categories
`lunch_order.py:16-18` — three topping category M2M relations: `topping_ids_1`, `topping_ids_2`, `topping_ids_3`, with domain `[('topping_category', '=', 1/2/3)]` respectively.

### D5 Supplier scheduling
`lunch_supplier.py:18-28` — `WEEKDAY_TO_NAME` maps 0-6 to mon-sun. `float_to_time()` converts fractional hour to `time` object. `CRON_DEPENDS` = `{'name', 'active', 'send_by', 'automatic_email_time', 'moment', 'tz'}` triggers cron update.

### Ten-dimension table — CAP-U62-10

| Dimension | Finding |
|---|---|
| Models | order, cashmove, supplier, product, product.category, topping, location, alert |
| Order lifecycle | new → ordered → sent → confirmed / cancelled |
| Wallet | Sum of cashmove.report amounts + company minimum threshold |
| Toppings | 3 independent category groups per order |
| Supplier contact | send_by: phone or email |
| Scheduling | Timezone-aware automatic order email via cron |
| Index | `(user_id, product_id, date)` composite index on `lunch.order` |
| Thailand relevance | Generic employee benefit — no localization dependency |
| Images | `image_1920` falls back to category image if product has none |
| Currency | Company currency via related field |

---

## CAP-U62-11 Marketing Card (marketing_card)

### D1 Campaign model
`card_campaign.py:10-62` — `card.campaign` inherits `mail.thread`, `mail.activity.mixin`, `mail.render.mixin`. Supported models are hardcoded: `res.partner`, `event.track`, `event.booth`, `event.registration`.

### D2 Card stats
`card_campaign.py:30-33` — computed fields: `card_count`, `card_click_count`, `card_share_count`. Link tracker integration via `link_tracker_id` on campaign.

### D3 Template dimensions
`card_template.py` imported at line 7 — `TEMPLATE_DIMENSIONS` constant used. Preview generation uses computed `image_preview` field stored as attachment.

### D4 Social sharing
`card_campaign.py:46-57` — `post_suggestion` for X (Twitter), `target_url` and `reward_target_url` for redirect destinations. `request_title` defaults to "Help us share the news".

### Ten-dimension table — CAP-U62-11

| Dimension | Finding |
|---|---|
| Models | `card.campaign`, `card.card`, `card.template`, `card.campaign.tag` |
| Allowed source models | res.partner, event.track, event.booth, event.registration (hardcoded) |
| Mixins | mail.thread, mail.activity.mixin, mail.render.mixin |
| Link tracking | Via `link.tracker` with click count |
| Rendering | Unrestricted QWeb rendering (`_unrestricted_rendering = True`) |
| Image | Background image + preview generation stored as attachment |
| Social | Post suggestion text + target URL for social sharing |
| Thailand | Generic — no localization dependency |
| Reward mechanism | Thank-you message + reward link after sharing |

---

## CAP-U62-12 Mass Mailing Core (mass_mailing)

### D1 Mailing model
`mailing.py:36-246` — `mailing.mailing` inherits `mail.thread`, `mail.activity.mixin`, `mail.render.mixin`, `utm.source.mixin`. States: `draft`, `in_queue`, `sending`, `done`.

### D2 A/B testing
`mailing.py:189-209` — A/B testing controlled by `ab_testing_enabled` (Boolean), `ab_testing_pc` (percentage 0-100), `ab_testing_winner_selection` (default `opened_ratio`), `ab_testing_schedule_datetime`. Campaign-level `ab_testing_completed` flag.

### D3 Statistics fields
`mailing.py:213-231` — statistics tracked per mailing: `scheduled`, `expected`, `canceled`, `sent`, `process`, `pending`, `delivered`, `opened`, `clicked`, `replied`, `bounced`, `failed`. Ratio fields: `received_ratio`, `opened_ratio`, `replied_ratio`, `bounced_ratio`, `clicks_ratio`.

### D4 Mailing trace states
`mailing_trace.py:87-96` — `trace_status` selection: `outgoing`, `process`, `pending`, `sent`, `open`, `reply`, `bounce`, `error`, `cancel`.

### D5 Blacklist integration
`mail_blacklist.py:10-20` — `mail.blacklist` extended with `opt_out_reason_id` Many2one to `mailing.subscription.optout` (with tracking=10). Reason logged as comment when set.

### D6 Mailing list opt-out
`mailing_list.py:270-365` — `_update_subscription_from_email()` handles opt-in and opt-out. Opt-out switches existing opt-in subscriptions. Opt-in switches opt-out and creates new subscriptions for public lists.

### D7 List merge
`mailing_list.py:227-264` — `action_merge()` uses a single SQL INSERT with row_number() window function to merge contact subscriptions from multiple lists while deduplicating by email and respecting opt-out and blacklist.

### D8 Exclusion list
`mailing.py:178-181` — `use_exclusion_list` field (default True). When disabled, blacklisted contacts may still receive emails — field help warns "Disable only when absolutely necessary."

### Ten-dimension table — CAP-U62-12

| Dimension | Finding |
|---|---|
| Model | `mailing.mailing` (mailing), `mailing.list`, `mailing.contact`, `mailing.trace`, `mailing.subscription` |
| States | draft → in_queue → sending → done |
| Trace states | 9 states including process/pending (SMS-specific) |
| Failure types | 11 mail failure types + SMS failure types via sms extension |
| A/B testing | Campaign-level, percentage-based recipient sampling |
| Blacklist | Extended with opt-out reason tracking |
| Scheduling | `now` or `scheduled` with datetime |
| UTM | UTM source via mixin, UTM medium computed |
| Mail server | Specific outgoing server selectable per mailing |
| QWeb rendering | Body uses QWeb with `post_process=True` |

---

## CAP-U62-13 Mass Mailing Bridge Modules

### D1 mass_mailing_sms
`mass_mailing_sms/models/mailing_mailing.py:27-50` — adds `sms` mailing type to `mailing_type` selection. Adds `body_plaintext` (Text, store=True), `sms_template_id`, `sms_has_insufficient_credit`, `sms_has_unregistered_account`, `sms_force_send`. `keep_archives` defaults True for SMS.

### D2 SMS trace extension
`mass_mailing_sms/models/mailing_trace.py` — extends `mailing.trace` with SMS-specific trace types and failure codes (`sms_number_missing`, `sms_number_format`, `sms_credit`, `sms_server`, `sms_acc`, `sms_country_not_supported`, `sms_registration_needed`, `sms_blacklist`, `sms_duplicate`, `sms_optout`).

### D3 Bridge module summary
- `mass_mailing_crm`: bridges mailings to CRM leads
- `mass_mailing_event`: bridges mailings to event registrations
- `mass_mailing_event_sms`: SMS variant for event mailing
- `mass_mailing_event_track_sms`: SMS for event tracks
- `mass_mailing_sale`: bridges mailings to sale orders
- `mass_mailing_slides`: bridges mailings to slide channel users

### Ten-dimension table — CAP-U62-13

| Dimension | Finding |
|---|---|
| SMS type | `sms` added to `mailing_type` selection |
| SMS body | `body_plaintext` stored text field |
| IAP | IAP credit check for SMS (`sms_has_insufficient_credit`, `sms_has_unregistered_account`) |
| Force send | `sms_force_send` bypasses opt-out (use cautiously) |
| Archive default | SMS mailings archive by default |
| CRM bridge | Links mailing to leads via mass_mailing_crm |
| Event bridge | Links mailing to registrations and event tracks |
| Sale bridge | Links mailing to sale order customers |
| Slides bridge | Links mailing to eLearning channel subscribers |

---

## CAP-U62-14 Payment Provider — Adyen

### D1 Provider fields
`payment_adyen/models/payment_provider.py:19-53` — custom fields: `adyen_merchant_account` (groups=system), `adyen_api_key` (groups=system), `adyen_client_key`, `adyen_hmac_key` (groups=system), `adyen_api_url_prefix`. All `copy=False`.

### D2 Feature support
`payment_adyen/models/payment_provider.py:88-95` — `support_manual_capture='partial'`, `support_refund='partial'`, `support_tokenization=True`.

### D3 URL construction
`payment_adyen/models/payment_provider.py:152-166` — URL pattern: `https://{prefix}.adyen.com/checkout/V{version}/{endpoint}` (test) or `https://{prefix}-checkout-live.adyenpayments.com/checkout/V{version}/{endpoint}` (prod). Version per endpoint from `const.API_ENDPOINT_VERSIONS`.

### D4 Request headers
`payment_adyen/models/payment_provider.py:168-178` — API key in `X-API-Key` header. POST requests with `idempotency_key` include `idempotency-key` header.

### D5 S2S payment request
`payment_adyen/models/payment_transaction.py:45-109` — token payment uses `recurringProcessingModel='Subscription'`, `shopperInteraction='ContAuth'`. Includes `applicationInfo` with Odoo platform name and version. `captureDelayHours=0` forced if provider not configured for manual capture.

### D6 Webhook event handling
`payment_adyen/models/payment_transaction.py:213-286` — event codes: `AUTHORISATION`, `CANCELLATION`, `CAPTURE`, `CAPTURE_FAILED`, `REFUND`. Child transactions auto-created for capture/void/refund initiated from Adyen dashboard.

### D7 Token extraction
`payment_adyen/models/payment_transaction.py:441-455` — token values from `additionalData`: `recurring.recurringDetailReference` (provider_ref), `cardSummary` (payment_details), `recurring.shopperReference`.

### D8 Amount formatting
`payment_adyen/models/payment_provider.py:119-136` — amounts converted to minor currency units via `payment_utils.to_minor_currency_units()`, using `const.CURRENCY_DECIMALS` override where applicable.

### Ten-dimension table — CAP-U62-14

| Dimension | Finding |
|---|---|
| Auth | `X-API-Key` header |
| Capture | Partial manual capture supported |
| Refund | Partial refund supported |
| Tokenization | Supported, shopper reference = `ODOO_PARTNER_{partner_id}` |
| URL scheme | Version-specific per endpoint from const |
| Idempotency | POST requests can carry idempotency key |
| 3DS | `threeDS2` action type skips amount validation |
| Webhook | HMAC-signed; event-code-based routing |
| S2S model | Subscription model for stored cards |
| Test/prod | URL prefix differs by state |

---

## CAP-U62-15 Payment Provider — Amazon Payment Services (payment_aps)

### D1 Provider fields
`payment_aps/models/payment_provider.py:17-44` — fields: `aps_merchant_identifier`, `aps_access_code` (groups=system), `aps_sha_request` (groups=system), `aps_sha_response` (groups=system).

### D2 API URLs
`payment_aps/models/payment_provider.py:57-61` — production: `https://checkout.payfort.com/FortAPI/paymentPage`; test: `https://sbcheckout.payfort.com/FortAPI/paymentPage`.

### D3 Signature calculation
`payment_aps/models/payment_provider.py:63-75` — signature is SHA-256 of `key + sorted_concatenated_kv_pairs + key` where key is `aps_sha_response` (incoming) or `aps_sha_request` (outgoing). Key excluded from signed data.

### D4 Reference requirements
`payment_aps/models/payment_transaction.py:19-38` — APS references must contain only alphanumeric chars and `-`/`_`. Prefix forced to singularized reference (avoids INV/2020/... format).

### D5 Rendering values
`payment_aps/models/payment_transaction.py:40-74` — renders `command='PURCHASE'`, `access_code`, `merchant_identifier`, `merchant_reference`, `amount` (minor units), `currency`, `language` (2-char), `customer_email`, `return_url`, optional `payment_option`. Signature appended.

### Ten-dimension table — CAP-U62-15

| Dimension | Finding |
|---|---|
| Provider | Amazon Payment Services (formerly PayFort) |
| Auth | SHA-256 HMAC with dual-key prefix+suffix pattern |
| Reference | Alphanumeric + `-` + `_` only; max 40 chars enforced via singularize |
| Environment | payfort.com (prod) / sbcheckout.payfort.com (test) |
| Amount | Minor currency units |
| Language | 2-char language code from partner lang |
| Feature support | No tokenization, capture, refund advertised in compute method |
| Signature | Sorted key=value concatenation wrapped with secret keys |

---

## CAP-U62-16 Payment Provider — AsiaPay

### D1 Provider fields
`payment_asiapay/models/payment_provider.py:17-45` — `asiapay_brand` selection: paydollar, pesopay, siampay, bimopay. `asiapay_merchant_id`, `asiapay_secure_hash_secret` (groups=system), `asiapay_secure_hash_function` (sha1/sha256/sha512, default sha1).

### D2 SiamPay brand
`payment_asiapay/models/payment_provider.py:22` — `siampay` is an AsiaPay brand. SiamPay is used in Thailand. This brand selection directly supports Thai payment processing via AsiaPay infrastructure.

### D3 Currency constraint
`payment_asiapay/models/payment_provider.py:49-65` — only one currency allowed per account; unsupported currencies raise ValidationError. Currency support defined in `const.CURRENCY_MAPPING`.

### D4 API URL resolution
`payment_asiapay/models/payment_provider.py:78-88` — URL from `const.API_URLS[environment][brand]`, defaulting to `paydollar` URL if brand not found.

### D5 Signature calculation
`payment_asiapay/models/payment_provider.py:90-104` — signature keys defined in `const.SIGNATURE_KEYS['incoming'/'outgoing']`. Data concatenated with `|` separator, appended with `secure_hash_secret`. Hash computed via `hashlib.new(asiapay_secure_hash_function)`.

### D6 Reference requirements
`payment_asiapay/models/payment_transaction.py:20-47` — references max 35 characters. Uses `payment_utils.singularize_reference_prefix(prefix=prefix, max_length=35)`.

### D7 Thailand relevance
SiamPay brand directly supports Thai payment processing. THB (Thai Baht) currency support depends on `const.CURRENCY_MAPPING` — RT for exact currency codes.

### Ten-dimension table — CAP-U62-16

| Dimension | Finding |
|---|---|
| Provider | AsiaPay (PayDollar, PesoPay, SiamPay, BimoPay) |
| Thailand brand | SiamPay — direct Thai payment processing support |
| Hash algorithms | SHA1, SHA256, SHA512 selectable |
| Currency | Single currency per account; validated against const.CURRENCY_MAPPING |
| Reference limit | 35 characters maximum |
| Signature | Pipe-delimited ordered fields + secret |
| Rendering | MPS mode SCP, payment_type N (new), language mapped |
| Feature support | No tokenization/capture/refund in compute_feature_support_fields |
| Environment | production/test URLs per brand from const |

---

## CAP-U62-17 Payment Provider — Authorize.Net

### D1 Provider fields
`payment_authorize/models/payment_provider.py:23-45` — `authorize_login` (API Login ID), `authorize_transaction_key` (groups=system), `authorize_signature_key` (groups=system), `authorize_client_key` (public).

### D2 Currency constraint
`payment_authorize/models/payment_provider.py:51-57` — only one currency per account (Authorize.Net is single-currency per gateway). ValidationError if more than one currency when provider is enabled.

### D3 Feature support
`payment_authorize/models/payment_provider.py:61-68` — `support_manual_capture='full_only'`, `support_refund='full_only'`, `support_tokenization=True`. Note: full-only (not partial) capture and refund.

### D4 Validation amount
`payment_authorize/models/payment_provider.py:108-118` — validation amount is `0.01`.

### D5 AuthorizeAPI class
`authorize_request.py:16-75` — `AuthorizeAPI` is a plain Python class (not ORM model). Production URL: `https://api.authorize.net/xml/v1/request.api`; test: `https://apitest.authorize.net/xml/v1/request.api`. Requests use JSON with `merchantAuthentication` wrapper.

### D6 Auth vs auth_and_capture
`payment_authorize/models/payment_transaction.py:48-51` — uses `authorize()` (auth only) when `capture_manually=True` or `operation == 'validation'`; otherwise uses `auth_and_capture()`.

### Ten-dimension table — CAP-U62-17

| Dimension | Finding |
|---|---|
| Provider | Authorize.Net |
| Auth | API Login ID + Transaction Key in request body |
| Signature | Signature key for webhook verification |
| Capture | Full-only manual capture |
| Refund | Full-only refund |
| Tokenization | Supported via customer profile/payment profile |
| Currency | Single currency per gateway account |
| Validation | $0.01 test charge |
| API class | Plain Python class AuthorizeAPI, not ORM model |
| Error format | `messages.resultCode == 'Error'` check + `transactionResponse.errors` |

---

## CAP-U62-18 Payment Provider — Buckaroo

### D1 Provider fields
`payment_buckaroo/models/payment_provider.py:17-28` — `buckaroo_website_key`, `buckaroo_secret_key` (groups=system).

### D2 Currency support
`payment_buckaroo/models/payment_provider.py:32-39` — overrides `_get_supported_currencies()` to filter to `const.SUPPORTED_CURRENCIES`.

### D3 API URLs
`payment_buckaroo/models/payment_provider.py:52-64` — production: `https://checkout.buckaroo.nl/html/`; test: `https://testcheckout.buckaroo.nl/html/`.

### D4 Signature generation
`payment_buckaroo/models/payment_provider.py:66-96` — for incoming: URL-decode values (except `brq_signature`). Filter to keys starting with `add_`, `brq_`, or `cust_` (case-insensitive). Sort by lower-cased key. Concatenate `k=v` pairs. Append secret key. SHA-1 hash.

### D5 Reference extraction
`payment_buckaroo/models/payment_transaction.py:50-54` — reference from `brq_invoicenumber` in payment data.

### D6 Rendering
`payment_buckaroo/models/payment_transaction.py:17-47` — rendering values include `Brq_websitekey`, `Brq_amount`, `Brq_currency`, `Brq_invoicenumber`, four return URLs (all same value but all included for signature), optional `Brq_culture` (lang with `_` replaced by `-`).

### Ten-dimension table — CAP-U62-18

| Dimension | Finding |
|---|---|
| Provider | Buckaroo |
| Auth | Website key + SHA-1 HMAC |
| Signature keys | Prefixes: add_, brq_, cust_ (case-insensitive) |
| Sort order | Lower-cased key alphabetical sort |
| Reference field | `brq_invoicenumber` |
| Return URLs | 4 distinct URL keys (return/cancel/error/reject) — all same value |
| Currency | Filtered to const.SUPPORTED_CURRENCIES |
| Culture | `partner_lang.replace('_', '-')` |

---

## CAP-U62-19 Payment Provider — Demo (payment_demo)

### D1 State constraint
`payment_demo/models/payment_provider.py:28-31` — demo providers constrained to `test` or `disabled` state only. `UserError` raised if state is `enabled`.

### D2 Feature support
`payment_demo/models/payment_provider.py:16-24` — `support_express_checkout=True`, `support_manual_capture='partial'`, `support_refund='partial'`, `support_tokenization=True`. Most complete feature set.

### D3 Simulated states
`payment_demo/models/payment_transaction.py:19-59` — action methods: `action_demo_set_done()`, `action_demo_set_canceled()`, `action_demo_set_error()`. Each calls `_process('demo', {'reference': ..., 'simulated_state': ...})`.

### D4 Apply updates
`payment_demo/models/payment_transaction.py:106-142` — `_apply_updates()` sets `provider_reference = f'demo-{self.reference}'`. Handles `capture_manually` flag correctly (authorized vs done state).

### D5 Token simulation
`payment_demo/models/payment_transaction.py:144-158` — token extraction returns empty if already done/authorized (to avoid double-tokenize). Otherwise returns `provider_ref='fake provider reference'` + `demo_simulated_state`.

### D6 Amount validation skip
`payment_demo/models/payment_transaction.py:100-104` — `_extract_amount_data()` returns None for demo, skipping amount validation entirely.

### Ten-dimension table — CAP-U62-19

| Dimension | Finding |
|---|---|
| Provider | Demo (test/disabled only) |
| Simulated states | pending, done, cancel, error |
| Manual capture | Simulated correctly — sets authorized then done |
| Refund | Simulated — always succeeds |
| Tokenization | Simulated with fake provider reference |
| Express checkout | Supported |
| Amount validation | Skipped entirely |
| Provider reference | `demo-{reference}` |
| Use case | Development and testing only |

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U62-C001 | PEPPOL-proxy-state | `account_peppol/models/res_company.py:70-79` | account_peppol_proxy_state = fields.Selection | FACT | — | — | Company proxy state has 5 values: not_registered, sender, smp_registration, receiver, rejected | N-U62-001 |
| VDR-U62-C002 | PEPPOL-proxy-url | `account_peppol/tools/peppol_iap_connector.py:12-15` | PEPPOL_PROXY_URLS = | FACT | — | — | Proxy production URL is peppol.api.odoo.com; test URL is peppol.test.odoo.com | N-U62-002 |
| VDR-U62-C003 | PEPPOL-batch-size | `account_peppol/models/account_edi_proxy_user.py:17` | `BATCH_SIZE = 50` | FACT | — | — | Module-level constant BATCH_SIZE=50 limits incoming document retrieval per cron run | N-U62-003 |
| VDR-U62-C004 | PEPPOL-EAS-rules | `account_peppol/models/res_company.py:29-35` | PEPPOL_ENDPOINT_RULES = | FACT | — | — | Hard validation rules for EAS codes 0007 (SE), 0088 (EAN), 0184 (DK), 0192 (NO), 0208 (BE) | N-U62-004 |
| VDR-U62-C005 | PEPPOL-EAS-sanitize | `account_peppol/models/res_company.py:46-51` | PEPPOL_ENDPOINT_SANITIZERS = | FACT | — | — | Sanitizers strip non-numeric chars for EAS 0007, 0184, 0192, 0208 | N-U62-004 |
| VDR-U62-C006 | PEPPOL-edi-mode | `account_peppol/models/res_company.py:397-402` | `config_param = self.env['ir.config_parameter'].sudo().get_param('account_peppol.edi.mode')` | FACT | — | — | EDI mode resolved from ir.config_parameter key account_peppol.edi.mode; fallback to peppol_user.edi_mode or 'prod' | N-U62-005 |
| VDR-U62-C007 | PEPPOL-webhook-endpoint | `account_peppol/models/res_company.py:404-406` | `return urljoin(self.get_base_url(), '/peppol/webhook')` | FACT | — | — | Webhook URL is base_url + /peppol/webhook | N-U62-006 |
| VDR-U62-C008 | PEPPOL-webhook-ttl | `account_peppol/models/account_edi_proxy_user.py:649` | `expiration = 30 * 24  # in 30 days` | FACT | — | — | Webhook token TTL is 30 days (30*24 hours) | N-U62-006 |
| VDR-U62-C009 | PEPPOL-out-of-sync | `account_peppol/models/account_edi_proxy_user.py:98-103` | elif e.code == 'invalid_signature | FACT | — | — | invalid_signature error triggers mark_connection_out_of_sync; clears refresh_token | N-U62-007 |
| VDR-U62-C010 | PEPPOL-self-billed-codes | `account_peppol/models/account_edi_proxy_user.py:235-236` | `is_self_billed = type_code in ['389', '527', '261']` | FACT | — | — | Type codes 389/527 (self-billing invoice) and 261 (self-billing credit note) trigger self-billed routing | N-U62-008 |
| VDR-U62-C011 | PEPPOL-move-state | `account_peppol/models/account_move.py:17-27` | selection= | FACT | — | — | peppol_move_state has 6 values: ready, to_send, skipped, processing, done, error | N-U62-009 |
| VDR-U62-C012 | PEPPOL-is-sent | `account_peppol/models/account_move.py:73-74` | `move.peppol_is_sent = move.peppol_move_state not in {False, 'ready', 'to_send', 'error', 'skipped'}` | FACT | — | — | peppol_is_sent is True only for processing and done states | N-U62-009 |
| VDR-U62-C013 | PEPPOL-cancel-guard | `account_peppol/models/account_move.py:36-41` | def action_cancel_peppol_documents(self) | FACT | — | — | Cannot cancel document if peppol_is_sent is True | N-U62-010 |
| VDR-U62-C014 | PEPPOL-R010-constraint | `account_peppol/models/account_edi_xml_ubl_bis3.py:14-21` | if self.env.context.get('from_peppol') | FACT | context=from_peppol | — | PEPPOL-EN16931-R010: customer EAS endpoint required when sending via PEPPOL | N-U62-011 |
| VDR-U62-C015 | PEPPOL-R020-constraint | `account_peppol/models/account_edi_xml_ubl_bis3.py:22-27` | # [PEPPOL-EN16931-R020] | FACT | context=from_peppol | — | PEPPOL-EN16931-R020: supplier EAS endpoint required when sending via PEPPOL | N-U62-011 |
| VDR-U62-C016 | PEPPOL-default-countries | `account_peppol/models/account_move_send.py:24-29` | self._is_applicable_to_move('peppol', move) | FACT | — | — | PEPPOL auto-selected as sending method when partner country in PEPPOL_DEFAULT_COUNTRIES | N-U62-012 |
| VDR-U62-C017 | PEPPOL-journal-flag | `account_peppol/models/account_journal.py:9` | `is_peppol_journal = fields.Boolean(string="Account used for Peppol", default=False)` | FACT | — | — | is_peppol_journal boolean marks the designated PEPPOL purchase journal | N-U62-013 |
| VDR-U62-C018 | PEPPOL-journal-type-constraint | `account_peppol/models/account_journal.py:11-17` | @api.constrains('type') | FACT | — | — | PEPPOL journal must remain type 'purchase'; type change raises ValidationError | N-U62-013 |
| VDR-U62-C019 | PEPPOL-verify-state | `account_peppol/models/res_partner.py:29-38` | peppol_verification_state = fields.Selection | FACT | — | — | Partner PEPPOL verification has 4 states: not_verified, not_valid, not_valid_format, valid | N-U62-014 |
| VDR-U62-C020 | PEPPOL-verify-company-dep | `account_peppol/models/res_partner.py:37` | `company_dependent=True` | FACT | — | — | peppol_verification_state is company_dependent — each company has independent verification | N-U62-014 |
| VDR-U62-C021 | PEPPOL-lookup-endpoint | `account_peppol/models/res_partner.py:158-159` | `api_endpoint = self.env['account_edi_proxy_client.user']._get_peppol_proxy_endpoint('1/lookup', proxy_type=proxy_type)` | FACT | — | — | Participant lookup via IAP endpoint /api/peppol/1/lookup with peppol_identifier query param | N-U62-014 |
| VDR-U62-C022 | PEPPOL-belgian-exclude | `account_peppol/models/res_partner.py:144-147` | `return edi_identification.lower() == participant_identifier.lower() and 'hermes-belgium' not in service_href` | FACT | — | — | Belgian hermes-belgium pre-registration excluded from valid PEPPOL participants | N-U62-015 |
| VDR-U62-C023 | PEPPOL-adv-fields-deprecated | `account_peppol_advanced_fields/models/account_move.py:7-34` | peppol_contract_document_reference = fields.Char | FACT | — | — | All 7 advanced fields in account_peppol_advanced_fields are marked deprecated in their string labels | N-U62-016 |
| VDR-U62-C024 | PEPPOL-adv-GLN | `account_peppol_advanced_fields/models/account_move.py:31-34` | peppol_delivery_location_id = fields.Char | FACT | — | — | Delivery Location GLN (Global Location Number) field exists but is deprecated | N-U62-016 |
| VDR-U62-C025 | SEPA-QR-method-reg | `account_qr_code_sepa/models/res_bank.py:77-80` | `rslt.append(('sct_qr', _("SEPA Credit Transfer QR"), 20))` | FACT | — | — | SEPA QR method registered as 'sct_qr' with priority 20 | N-U62-017 |
| VDR-U62-C026 | SEPA-QR-payload | `account_qr_code_sepa/models/res_bank.py:22-34` | 'BCD | FACT | — | — | EPC QR payload: ServiceTag=BCD, Version=002, CharSet=1, IdentCode=SCT | N-U62-017 |
| VDR-U62-C027 | SEPA-QR-currency | `account_qr_code_sepa/models/res_bank.py:58-59` | if currency.name != 'EUR | FACT | — | — | SEPA QR requires EUR currency | N-U62-017 |
| VDR-U62-C028 | SEPA-QR-account-type | `account_qr_code_sepa/models/res_bank.py:60-61` | if self.acc_type != 'iban | FACT | — | — | SEPA QR requires IBAN account type | N-U62-017 |
| VDR-U62-C029 | SEPA-QR-size | `account_qr_code_sepa/models/res_bank.py:41-47` | 'barcode_type': 'QR | FACT | — | — | QR code generated at 128x128 pixels | N-U62-017 |
| VDR-U62-C030 | DR-batch-auto | `data_recycle/models/data_recycle_model.py:15` | `DR_CREATE_STEP_AUTO = 5000` | FACT | — | — | Auto recycle batch size is 5,000 records | N-U62-018 |
| VDR-U62-C031 | DR-batch-manual | `data_recycle/models/data_recycle_model.py:16` | `DR_CREATE_STEP_MANUAL = 50000` | FACT | — | — | Manual recycle batch size is 50,000 records | N-U62-018 |
| VDR-U62-C032 | DR-modes | `data_recycle/models/data_recycle_model.py:33-36` | recycle_mode = fields.Selection | FACT | — | — | Recycle model supports manual and automatic modes | N-U62-018 |
| VDR-U62-C033 | DR-actions | `data_recycle/models/data_recycle_model.py:37-40` | recycle_action = fields.Selection | FACT | — | — | Recycle action is either archive or unlink (delete) | N-U62-019 |
| VDR-U62-C034 | DR-archive-guard | `data_recycle/models/data_recycle_model.py:77-81` | @api.constrains('recycle_action') | FACT | — | — | Archive action requires model to have active field; UserError if not | N-U62-019 |
| VDR-U62-C035 | DR-validate | `data_recycle/models/data_recycle_record.py:66-84` | def action_validate(self) | FACT | — | — | action_validate calls action_archive() or unlink() via sudo() on original records | N-U62-020 |
| VDR-U62-C036 | DR-commit | `data_recycle/models/data_recycle_model.py:139-142` | if batch_commits and not is_test | FACT | not test mode | — | Database commit after each batch when batch_commits=True and not in test mode | N-U62-020 |
| VDR-U62-C037 | DR-notify-group | `data_recycle/models/data_recycle_model.py:62-64` | `domain=lambda self: [('all_group_ids', 'in', self.env.ref('base.group_system').id)]` | FACT | — | — | Notification users restricted to base.group_system (system administrators) | N-U62-021 |
| VDR-U62-C038 | IOT-no-python | iot_base/__manifest__.py:1-23 | Part of Odoo | FACT | — | — | iot_base module has no Python models; all logic in JavaScript assets | N-U62-022 |
| VDR-U62-C039 | IOT-assets | `iot_base/__manifest__.py:17-22` | 'assets': | FACT | — | — | IoT base provides network_utils/* and device_controller.js in backend asset bundle | N-U62-022 |
| VDR-U62-C040 | WHT-POS-field | `l10n_account_withholding_tax_pos/models/account_tax.py:12` | `fields.append('is_withholding_tax_on_payment')` | FACT | — | — | is_withholding_tax_on_payment added to POS data fields via _load_pos_data_fields override | N-U62-023 |
| VDR-U62-C041 | WHT-POS-auto-install | `l10n_account_withholding_tax_pos/__manifest__.py:10` | `'auto_install': True` | FACT | — | — | Module auto-installs when both l10n_account_withholding_tax and point_of_sale are present | N-U62-023 |
| VDR-U62-C042 | WHT-POS-depends | `l10n_account_withholding_tax_pos/__manifest__.py:7` | `'depends': ['l10n_account_withholding_tax', 'point_of_sale']` | FACT | — | — | Module depends on l10n_account_withholding_tax and point_of_sale | N-U62-023 |
| VDR-U62-C043 | WHT-POS-js-assets | `l10n_account_withholding_tax_pos/__manifest__.py:9-11` | `'l10n_account_withholding_tax/static/src/helpers/*.js'` | FACT | — | — | WHT helper JS from l10n_account_withholding_tax loaded into POS asset bundle | N-U62-023 |
| VDR-U62-C044 | LUNCH-order-states | `lunch/models/lunch_order.py:35-40` | state = fields.Selection([('new', 'To Order') | FACT | — | — | Lunch order has 5 states: new, ordered, sent, confirmed, cancelled | N-U62-024 |
| VDR-U62-C045 | LUNCH-wallet | `lunch/models/lunch_cashmove.py:26-31` | def get_wallet_balance | FACT | — | — | Wallet balance is sum of cashmove.report amounts (precision 2) + company minimum threshold | N-U62-025 |
| VDR-U62-C046 | LUNCH-toppings | `lunch/models/lunch_order.py:16-18` | topping_ids_1 = | FACT | — | — | Three independent topping category groups (1/2/3) on each order | N-U62-026 |
| VDR-U62-C047 | LUNCH-supplier-send-cron | `lunch/models/lunch_supplier.py:19` | `CRON_DEPENDS = {'name', 'active', 'send_by', 'automatic_email_time', 'moment', 'tz'}` | FACT | — | — | Cron depends on 6 supplier fields; changes to these fields trigger cron update | N-U62-026 |
| VDR-U62-C048 | LUNCH-index | `lunch/models/lunch_order.py:64` | `_user_product_date = models.Index("(user_id, product_id, date)")` | FACT | — | — | Composite database index on (user_id, product_id, date) for performance | N-U62-024 |
| VDR-U62-C049 | MKTCARD-models | `marketing_card/models/card_campaign.py:21-24` | `allowed_models = ['res.partner', 'event.track', 'event.booth', 'event.registration']` | FACT | — | — | Marketing card campaigns can only target 4 hardcoded models | N-U62-027 |
| VDR-U62-C050 | MKTCARD-unrestricted | `marketing_card/models/card_campaign.py:15` | `_unrestricted_rendering = True` | FACT | — | — | Marketing card uses unrestricted QWeb rendering | N-U62-027 |
| VDR-U62-C051 | MAILING-states | `mass_mailing/models/mailing.py:129-135` | state = fields.Selection | FACT | — | — | Mailing has 4 states: draft, in_queue, sending, done | N-U62-028 |
| VDR-U62-C052 | MAILING-ab-test | `mass_mailing/models/mailing.py:191-208` | ab_testing_enabled = fields.Boolean | FACT | — | — | A/B testing uses percentage-based sampling (default 10%); winner selection default is opened_ratio | N-U62-029 |
| VDR-U62-C053 | MAILING-trace-states | `mass_mailing/models/mailing_trace.py:87-96` | trace_status = fields.Selection(selection= | FACT | — | — | mailing.trace has 9 trace_status values: outgoing, process, pending, sent, open, reply, bounce, error, cancel | N-U62-030 |
| VDR-U62-C054 | MAILING-failure-types | `mass_mailing/models/mailing_trace.py:97-112` | failure_type = fields.Selection(selection= | FACT | — | — | 11 mail failure types defined on mailing.trace | N-U62-030 |
| VDR-U62-C055 | MAILING-blacklist | `mass_mailing/models/mail_blacklist.py:11-14` | opt_out_reason_id = fields.Many2one | FACT | — | — | mail.blacklist extended with opt_out_reason_id with tracking | N-U62-031 |
| VDR-U62-C056 | MAILING-exclusion | `mass_mailing/models/mailing.py:178-181` | use_exclusion_list = fields.Boolean | FACT | — | — | use_exclusion_list defaults True; disabling allows emailing blacklisted contacts | N-U62-031 |
| VDR-U62-C057 | MAILING-list-merge-sql | `mass_mailing/models/mailing_list.py:231-261` | self.env.cr.execute | FACT | — | — | List merge uses window function (row_number) to deduplicate by email | N-U62-032 |
| VDR-U62-C058 | MAILING-opt-out | `mass_mailing/models/mailing_list.py:356-365` | def _mailing_get_opt_out_list(self, mailing) | FACT | — | — | Opt-out logic: email opted-out only if not also opted-in in another list | N-U62-032 |
| VDR-U62-C059 | MAILING-sms-type | `mass_mailing_sms/models/mailing_mailing.py:27-29` | mailing_type = fields.Selection(selection_add= | FACT | — | — | mass_mailing_sms adds 'sms' mailing type | N-U62-033 |
| VDR-U62-C060 | MAILING-sms-iap | `mass_mailing_sms/models/mailing_mailing.py:46-49` | sms_has_insufficient_credit = fields.Boolean | FACT | — | — | IAP credit check exposes sms_has_insufficient_credit and sms_has_unregistered_account flags | N-U62-033 |
| VDR-U62-C061 | ADYEN-fields | `payment_adyen/models/payment_provider.py:21-53` | adyen_merchant_account = fields.Char | FACT | — | — | Adyen requires 5 configuration fields; merchant_account, api_key, hmac_key restricted to system group | N-U62-034 |
| VDR-U62-C062 | ADYEN-features | `payment_adyen/models/payment_provider.py:88-95` | def _compute_feature_support_fields(self) | FACT | — | — | Adyen supports partial manual capture, partial refund, tokenization | N-U62-034 |
| VDR-U62-C063 | ADYEN-url-prod | `payment_adyen/models/payment_provider.py:163-166` | endpoint = endpoint.lstrip | FACT | state=enabled | — | Adyen production URL pattern: {prefix}-checkout-live.adyenpayments.com | N-U62-034 |
| VDR-U62-C064 | ADYEN-auth-header | `payment_adyen/models/payment_provider.py:175` | `headers = {'X-API-Key': self.adyen_api_key}` | FACT | — | — | Adyen authentication uses X-API-Key request header | N-U62-034 |
| VDR-U62-C065 | ADYEN-idempotency | `payment_adyen/models/payment_provider.py:176-178` | if method == 'POST' and idempotency_key | FACT | POST + idempotency_key provided | — | Idempotency key added to POST request headers when provided | N-U62-034 |
| VDR-U62-C066 | ADYEN-s2s-recurring | `payment_adyen/models/payment_transaction.py:70-72` | 'countryCode': partner_country_code | FACT | — | — | S2S token payments use Subscription processing model and ContAuth shopper interaction | N-U62-035 |
| VDR-U62-C067 | ADYEN-shopper-ref | `payment_adyen/models/payment_provider.py:148` | `return f'ODOO_PARTNER_{partner_id}'` | FACT | — | — | Adyen shopper reference computed as ODOO_PARTNER_{partner_id} | N-U62-035 |
| VDR-U62-C068 | ADYEN-capture-force | `payment_adyen/models/payment_transaction.py:97-98` | if not self.provider_id.capture_manually | FACT | capture_manually=False | — | captureDelayHours=0 forced in S2S request when provider not set for manual capture | N-U62-035 |
| VDR-U62-C069 | ADYEN-event-codes | `payment_adyen/models/payment_transaction.py:230-231` | `elif event_code in ['CANCELLATION', 'CAPTURE', 'CAPTURE_FAILED']:` | FACT | — | — | Webhook handles event codes: AUTHORISATION, CANCELLATION, CAPTURE, CAPTURE_FAILED, REFUND | N-U62-036 |
| VDR-U62-C070 | ADYEN-token-data | `payment_adyen/models/payment_transaction.py:448-454` | if 'recurring.recurringDetailReference | FACT | — | — | Token extracts recurringDetailReference (provider_ref), cardSummary, shopperReference from additionalData | N-U62-036 |
| VDR-U62-C071 | APS-provider | `payment_aps/models/payment_provider.py:18` | selection_add= | FACT | — | — | APS provider code is 'aps'; Amazon Payment Services (formerly PayFort) | N-U62-037 |
| VDR-U62-C072 | APS-urls | `payment_aps/models/payment_provider.py:57-61` | def _aps_get_api_url(self) | FACT | — | — | APS production URL is checkout.payfort.com; test is sbcheckout.payfort.com | N-U62-037 |
| VDR-U62-C073 | APS-signature | `payment_aps/models/payment_provider.py:72-75` | sign_data = ''.join | FACT | — | — | APS signature: SHA-256 of (key + sorted_kv_string + key) | N-U62-037 |
| VDR-U62-C074 | APS-ref-format | `payment_aps/models/payment_transaction.py:35-36` | if provider_code == 'aps | FACT | — | — | APS reference prefix singularized (avoids slash-containing doc refs) | N-U62-037 |
| VDR-U62-C075 | ASIAPAY-brand | `payment_asiapay/models/payment_provider.py:18-25` | string="Asiapay Brand | FACT | — | — | AsiaPay supports 4 brands: paydollar, pesopay, siampay (Thailand), bimopay | N-U62-038 |
| VDR-U62-C076 | ASIAPAY-siampay | `payment_asiapay/models/payment_provider.py:22` | `("siampay", "SiamPay")` | FACT | — | — | SiamPay brand directly supports Thai payment processing via AsiaPay | N-U62-038 |
| VDR-U62-C077 | ASIAPAY-hash | `payment_asiapay/models/payment_provider.py:38-44` | asiapay_secure_hash_function = fields.Selection | FACT | — | — | AsiaPay supports SHA1, SHA256, SHA512 hash functions | N-U62-038 |
| VDR-U62-C078 | ASIAPAY-currency-limit | `payment_asiapay/models/payment_provider.py:53-54` | if len(provider.available_currency_ids) | FACT | — | — | AsiaPay allows only one currency per account | N-U62-038 |
| VDR-U62-C079 | ASIAPAY-signature | `payment_asiapay/models/payment_provider.py:99-103` | signing_string = | FACT | — | — | AsiaPay signature: pipe-delimited field values + secret, hashed with selected algorithm | N-U62-039 |
| VDR-U62-C080 | ASIAPAY-ref-max | `payment_asiapay/models/payment_transaction.py:46` | `prefix = payment_utils.singularize_reference_prefix(prefix=prefix, max_length=35)` | FACT | — | — | AsiaPay reference limited to 35 characters | N-U62-039 |
| VDR-U62-C081 | AUTHORIZE-login | `payment_authorize/models/payment_provider.py:23-34` | authorize_login = fields.Char | FACT | — | — | Authorize.Net requires API Login ID, Transaction Key (system group), Signature Key (system group) | N-U62-040 |
| VDR-U62-C082 | AUTHORIZE-currency | `payment_authorize/models/payment_provider.py:53-57` | for provider in | FACT | — | — | Authorize.Net allows only one currency per gateway account | N-U62-040 |
| VDR-U62-C083 | AUTHORIZE-features | `payment_authorize/models/payment_provider.py:64-68` | self.filtered(lambda | FACT | — | — | Authorize.Net supports full-only manual capture, full-only refund, tokenization | N-U62-040 |
| VDR-U62-C084 | AUTHORIZE-validation | `payment_authorize/models/payment_provider.py:115-118` | `return 0.01` | FACT | — | — | Authorize.Net validation charge amount is $0.01 | N-U62-041 |
| VDR-U62-C085 | AUTHORIZE-urls | `payment_authorize/models/authorize_request.py:33-36` | if provider.state == 'enabled | FACT | — | — | Authorize.Net prod URL: api.authorize.net; test URL: apitest.authorize.net | N-U62-041 |
| VDR-U62-C086 | AUTHORIZE-auth-capture | `payment_authorize/models/payment_transaction.py:48-51` | if self.provider_id.capture_manually | FACT | — | — | Manual capture mode uses authorize-only; auto mode uses auth_and_capture | N-U62-041 |
| VDR-U62-C087 | BUCKAROO-fields | `payment_buckaroo/models/payment_provider.py:17-28` | buckaroo_website_key = fields.Char | FACT | — | — | Buckaroo requires website key and secret key (system-restricted) | N-U62-042 |
| VDR-U62-C088 | BUCKAROO-urls | `payment_buckaroo/models/payment_provider.py:62-64` | return 'https://checkout.buckaroo.nl/html/ | FACT | — | — | Buckaroo prod URL: checkout.buckaroo.nl; test URL: testcheckout.buckaroo.nl | N-U62-042 |
| VDR-U62-C089 | BUCKAROO-sig-prefix | `payment_buckaroo/models/payment_provider.py:85-88` | `if any(k.lower().startswith(key_prefix) for key_prefix in ('add_', 'brq_', 'cust_'))` | FACT | — | — | Signature only includes keys starting with add_, brq_, cust_ | N-U62-042 |
| VDR-U62-C090 | BUCKAROO-sha1 | `payment_buckaroo/models/payment_provider.py:95-96` | # Calculate the SHA-1 hash over the signing string | FACT | — | — | Buckaroo signature uses SHA-1 | N-U62-043 |
| VDR-U62-C091 | BUCKAROO-four-urls | `payment_buckaroo/models/payment_transaction.py:33-40` | 'Brq_amount': self.amount | FACT | — | — | 4 return URL keys used (all same value) — required for Buckaroo signature | N-U62-043 |
| VDR-U62-C092 | DEMO-constraint | `payment_demo/models/payment_provider.py:28-31` | @api.constrains('state', 'code') | FACT | — | — | Demo provider cannot be enabled in production; test/disabled states only | N-U62-044 |
| VDR-U62-C093 | DEMO-features | `payment_demo/models/payment_provider.py:16-24` | def _compute_feature_support_fields(self) | FACT | — | — | Demo supports all features: express checkout, partial manual capture, partial refund, tokenization | N-U62-044 |
| VDR-U62-C094 | DEMO-provider-ref | `payment_demo/models/payment_transaction.py:112` | `self.provider_reference = f'demo-{self.reference}'` | FACT | — | — | Demo provider reference is demo-{transaction_reference} | N-U62-044 |
| VDR-U62-C095 | DEMO-amount-skip | `payment_demo/models/payment_transaction.py:100-104` | def _extract_amount_data(self, payment_data) | FACT | — | — | Demo provider skips amount validation (returns None) | N-U62-044 |
| VDR-U62-C096 | PEPPOL-doc-types | `account_peppol/models/res_company.py:373-386` | return | FACT | — | — | Default supported document types include BIS Billing 3.0 Invoice, CreditNote, Self-billing variants, and SI-UBL 2.0 | N-U62-011 |
| VDR-U62-C097 | PEPPOL-registration-key | `account_peppol/models/res_company.py:64` | `account_peppol_migration_key = fields.Char(string="Migration Key", groups="base.group_system")` | FACT | — | — | Migration key stored system-restricted; cleared after sending to IAP (line 562) | N-U62-001 |
| VDR-U62-C098 | PEPPOL-phone-validation | `account_peppol/models/res_company.py:168-191` | def _sanitize_peppol_phone_number | FACT | — | — | Phone number must be in international format; validated via phonenumbers library | N-U62-001 |
| VDR-U62-C099 | PEPPOL-metadata | `account_peppol/models/res_company.py:99-100` | peppol_metadata | FACT | — | — | IAP-driven peppol_metadata stored as JSON on company | N-U62-001 |
| VDR-U62-C100 | PEPPOL-can-send | `account_peppol/models/res_company.py:324-327` | def _compute_peppol_can_send(self) | FACT | — | — | peppol_can_send computed from _get_can_send_domain() = ('sender', 'smp_registration', 'receiver') | N-U62-002 |
| VDR-U62-C101 | PEPPOL-purchase-journal | `account_peppol/models/res_company.py:86-94` | peppol_purchase_journal_id = fields.Many2one | FACT | — | — | Company has dedicated PEPPOL purchase journal (purchase type required) | N-U62-013 |
| VDR-U62-C102 | PEPPOL-iap-connect | `account_peppol/tools/peppol_iap_connector.py:44-52` | `def can_connect(self, *, peppol_identifier, db_uuid, callback_url, connect_token, contact_email=None, webhook_url=None)` | FACT | — | — | New connection flow requires: peppol_identifier, db_uuid, callback_url, connect_token, optional contact_email, webhook_url | N-U62-002 |
| VDR-U62-C103 | PEPPOL-iap-create | `account_peppol/tools/peppol_iap_connector.py:54-64` | `def create_connection(self, *, peppol_identifier, db_uuid, public_key, auth_token=None, **company_details)` | FACT | — | — | create_connection sends POST to /api/peppol/2/connect with public key and optional auth token | N-U62-002 |
| VDR-U62-C104 | PEPPOL-resync | `account_peppol/models/account_edi_proxy_user.py:134-160` | def _peppol_out_of_sync_reconnect_this_database | FACT | is_token_out_of_sync=True | — | Resync increments token_sync_version, calls /api/peppol/1/resync_connection, triggers participant status cron | N-U62-007 |
| VDR-U62-C105 | PEPPOL-embedded-strip | `account_peppol/models/account_edi_proxy_user.py:19-24` | REMOVE_EMBEDDED_DOCUMENT_BINARY_OBJECT_RE | FACT | — | — | Regex strips EmbeddedDocumentBinaryObject elements from XML when xml_tree cannot be parsed | N-U62-008 |
| VDR-U62-C106 | PEPPOL-french-detect | `account_peppol/models/res_company.py:198-203` | def _peppol_is_french_company(self) | FACT | — | — | French company detection includes overseas territories GP/MQ/RE and EAS-based detection | N-U62-016 |
| VDR-U62-C107 | ADYEN-prefix-extract | `payment_adyen/models/payment_provider.py:75-84` | def _adyen_extract_prefix_from_api_url | FACT | — | — | API URL prefix extracted from full URL using regex; stores only the prefix portion | N-U62-034 |
| VDR-U62-C108 | ADYEN-child-tx | `payment_adyen/models/payment_transaction.py:288-310` | `def _adyen_create_child_tx(self, source_tx, payment_data, is_refund=False):` | FACT | — | — | Child transactions auto-created for captures/voids/refunds initiated externally from Adyen dashboard | N-U62-036 |
| VDR-U62-C109 | AUTHORIZE-api-class | `payment_authorize/models/authorize_request.py:16-75` | class AuthorizeAPI | FACT | — | — | AuthorizeAPI is a standalone Python class (not ORM model) wrapping Authorize.Net XML API | N-U62-041 |
| VDR-U62-C110 | AUTHORIZE-timeout | `payment_authorize/models/authorize_request.py:55` | `response = requests.post(self.url, json.dumps(request), timeout=60)` | FACT | — | — | Authorize.Net API calls have 60-second timeout | N-U62-041 |
| VDR-U62-C111 | MAILING-mail-constraint | `mass_mailing/models/mailing.py:243-246` | _email_from = models.Constraint | FACT | — | — | Database constraint: email_from required when mailing_type is 'mail' | N-U62-028 |
| VDR-U62-C112 | MAILING-ab-constraint | `mass_mailing/models/mailing.py:239-242` | _percentage_valid = models.Constraint | FACT | — | — | Database constraint: A/B testing percentage must be 0-100 | N-U62-029 |
| VDR-U62-C113 | MAILING-body-arch | `mass_mailing/models/mailing.py:114` | `body_arch = fields.Html(string='Body', translate=False, sanitize='email_outgoing'` | FACT | — | — | body_arch is the design-time body (not translated); body_html is QWeb-rendered send-time body | N-U62-028 |
| VDR-U62-C114 | MAILING-reply-modes | `mass_mailing/models/mailing.py:144-148` | reply_to_mode = fields.Selection | FACT | — | — | Reply-To mode: 'update' = replies go to target document thread; 'new' = replies to specified address | N-U62-028 |
| VDR-U62-C115 | MAILING-trace-mail-id | `mass_mailing/models/mailing_trace.py:62-69` | mail_mail_id = fields.Many2one | FACT | — | — | mail_mail_id_int stores mail ID as integer to survive deletion of original mail.mail record | N-U62-030 |
| VDR-U62-C116 | MAILING-set-sent | `mass_mailing/models/mailing_trace.py:145-148` | def set_sent(self, domain=None) | FACT | — | — | set_sent() clears failure_type when marking trace as sent | N-U62-030 |
| VDR-U62-C117 | MAILING-set-opened | `mass_mailing/models/mailing_trace.py:150-155` | def set_opened(self, domain=None) | FACT | — | — | set_opened() skips traces already in 'open' or 'reply' state to prevent status downgrade | N-U62-030 |
| VDR-U62-C118 | MAILING-list-is-public | `mass_mailing/models/mailing_list.py:40-43` | is_public = fields.Boolean | FACT | — | — | Mailing lists can optionally be shown in subscriber preference page (is_public default False) | N-U62-032 |
| VDR-U62-C119 | MAILING-list-archive-guard | `mass_mailing/models/mailing_list.py:112-122` | def write(self, vals) | FACT | — | — | Archiving a mailing list blocked if used in any ongoing (not-done) mailing campaign | N-U62-032 |
| VDR-U62-C120 | MAILING-image-re | `mass_mailing/models/mailing.py:30` | `image_re = re.compile(r"data:(image/[A-Za-z]+);base64,(.*)")` | FACT | — | — | Module-level regex for detecting inline base64-encoded data URL images in HTML body | N-U62-028 |
| VDR-U62-C121 | LUNCH-image-fallback | `lunch/models/lunch_order.py:67-70` | `line.image_1920 = line.product_id.image_1920 or line.category_id.image_1920` | FACT | — | — | Order image falls back to category image when product has no image | N-U62-026 |
| VDR-U62-C122 | LUNCH-deadline | `lunch/models/lunch_order.py:28-29` | available_on_date | FACT | — | — | Order availability and deadline checks are computed fields | N-U62-024 |
| VDR-U62-C123 | LUNCH-quantity | `lunch/models/lunch_order.py:44` | `quantity = fields.Float('Quantity', required=True, default=1)` | FACT | — | — | Lunch orders support floating-point quantity (not integer) | N-U62-024 |
| VDR-U62-C124 | DR-discard | `data_recycle/models/data_recycle_record.py:86-87` | def action_discard(self) | FACT | — | — | action_discard() soft-deletes recycle record by setting active=False | N-U62-019 |
| VDR-U62-C125 | IOT-js-only | iot_base/__manifest__.py:1 | Part of Odoo | OBSERVATION | — | RT | iot_base is a pure JS module; no Python server-side behavior; all IoT device/proxy logic is RT | N-U62-022 |
| VDR-U62-C126 | WHT-POS-rt | `l10n_account_withholding_tax_pos/models/account_tax.py:12` | `fields.append('is_withholding_tax_on_payment')` | OBSERVATION | — | RT | Actual WHT computation, POS payment UI, and journal entries are RT JavaScript/cron behavior | N-U62-023 |
| VDR-U62-C127 | PEPPOL-participant-status | `account_peppol/models/account_edi_proxy_user.py:479-495` | `def _peppol_process_participant_status(self, proxy_user):` | FACT | — | — | Participant status mapping: draft→not_registered, sender/smp_registration/receiver/rejected→same. not_registered triggers soft-reset and archive | N-U62-001 |
| VDR-U62-C128 | PEPPOL-deregister | `account_peppol/models/account_edi_proxy_user.py:568-594` | @handle_demo | FACT | — | — | Deregistration: fetch pending docs/statuses → call cancel_peppol_registration → reset company config → unlink edi user | N-U62-007 |
| VDR-U62-C129 | PEPPOL-services-get | `account_peppol/models/account_edi_proxy_user.py:642-645` | def _peppol_get_services(self) | FACT | — | — | IAP endpoint 2/get_services retrieves registered PEPPOL services for participant | N-U62-002 |
| VDR-U62-C130 | PEPPOL-auto-deregister | `account_peppol/models/account_edi_proxy_user.py:616-641` | def _peppol_auto_deregister_services | FACT | — | — | Module uninstall hook calls _peppol_auto_deregister_services to remove document type registrations | N-U62-002 |
| VDR-U62-C131 | ADYEN-3ds-skip | `payment_adyen/models/payment_transaction.py:318-324` | # payment_data | FACT | — | — | Amount validation skipped for redirect/3DS2 actions and refused payments | N-U62-035 |
| VDR-U62-C132 | MAILING-mso | `mass_mailing/models/mailing.py:33` | `mso_re = re.compile(r"\[if mso\]>[\s\S]*<!\[endif\]")` | FACT | — | — | Regex for stripping MSO (Microsoft Office) conditional comments from mailing HTML | N-U62-028 |
| VDR-U62-C133 | MAILING-image-chunk | `mass_mailing/models/mailing.py:31` | `DEFAULT_IMAGE_CHUNK_SIZE = 32768` | FACT | — | — | Default image upload chunk size is 32768 bytes (32 KB) | N-U62-028 |
| VDR-U62-C134 | AUTHORIZE-refund-flow | `payment_authorize/models/payment_transaction.py:73-99` | def _send_refund_request(self) | FACT | — | — | Authorize.Net refund checks current transaction status: voided→cancel, refunded→done, authorized/captured→proceed with refund | N-U62-041 |
| VDR-U62-C135 | PEPPOL-webhook-keepalive | `account_peppol/models/account_edi_proxy_user.py:193-195` | def _cron_peppol_webhook_keepalive(self) | FACT | — | — | Webhook keepalive cron runs only for sender/receiver state companies | N-U62-006 |
| VDR-U62-C136 | PEPPOL-proxy-ident | `account_peppol/models/account_edi_proxy_user.py:202-207` | if proxy_type == 'peppol | FACT | — | — | PEPPOL proxy identification is peppol_eas:peppol_endpoint concatenated with colon | N-U62-001 |
| VDR-U62-C137 | PEPPOL-ack | `account_peppol/models/account_edi_proxy_user.py:364-366` | if processed_uuids | FACT | — | — | Processed messages are acknowledged to IAP via endpoint 1/ack with list of UUIDs | N-U62-008 |
| VDR-U62-C138 | PEPPOL-retrigger | `account_peppol/models/account_edi_proxy_user.py:371-372` | if need_retrigger | FACT | — | — | Cron re-triggered immediately if more messages remain (more than job_count unprocessed) | N-U62-003 |
| VDR-U62-C139 | LUNCH-cashmove-order | `lunch/models/lunch_cashmove.py:8-9` | class LunchCashmove(models.Model) | FACT | — | — | Cashmoves ordered by date descending | N-U62-025 |
| VDR-U62-C140 | MAILING-notify-einvoices | `account_peppol/models/account_edi_proxy_user.py:406-409` | self.ensure_one() | FACT | — | — | Post-processing notifies PEPPOL purchase journal of newly received e-invoices | N-U62-013 |
| VDR-U62-C141 | PEPPOL-status-1hr | `account_peppol/models/account_edi_proxy_user.py:190-191` | if self.search_count | FACT | state=smp_registration | — | During smp_registration state, participant status cron retriggers every hour | N-U62-001 |
| VDR-U62-C142 | PEPPOL-msg-status-5min | `account_peppol/models/account_edi_proxy_user.py:435-438` | if need_retrigger | FACT | — | — | Message status cron retriggers after 5 minutes when more messages need status update | N-U62-009 |
| VDR-U62-C143 | PEPPOL-dup-self-address | `account_peppol/models/account_edi_proxy_user.py:326-331` | # duplicate check | FACT | — | — | Self-addressed messages (sender==receiver) excluded from duplicate check to allow self-invoicing | N-U62-008 |
| VDR-U62-C144 | MAILING-mail-server-default | `mass_mailing/models/mailing.py:73-79` | `server_id = self.env['ir.config_parameter'].sudo().get_param('mass_mailing.mail_server_id')` | FACT | — | — | Default mail server ID sourced from ir.config_parameter key mass_mailing.mail_server_id | N-U62-028 |
| VDR-U62-C145 | MAILING-link-tracker | `mass_mailing/models/mailing_trace.py:115-116` | links_click_ids | FACT | — | — | mailing.trace tracks link clicks via link.tracker.click relationship; last click datetime stored | N-U62-030 |
| VDR-U62-C146 | MAILING-trace-constraint | `mass_mailing/models/mailing_trace.py:118-121` | _check_res_id_is_set = models.Constraint | FACT | — | — | Database constraint: res_id must be not null and not zero on mailing traces | N-U62-030 |
| VDR-U62-C147 | MAILING-sms-archive | `mass_mailing_sms/models/mailing_mailing.py:22-23` | if fields is not | FACT | — | — | SMS mailings default keep_archives=True | N-U62-033 |
| VDR-U62-C148 | DR-time-field | `data_recycle/models/data_recycle_model.py:44-47` | time_field_id = fields.Many2one | FACT | — | — | Time field for recycle must be a stored date or datetime field on the target model | N-U62-018 |
| VDR-U62-C149 | PEPPOL-deregister-to-sender | `account_peppol/models/account_edi_proxy_user.py:596-608` | def _peppol_deregister_participant_to_sender | FACT | — | — | Partial deregistration (receiver→sender) calls endpoint 1/unregister_to_sender | N-U62-007 |
| VDR-U62-C150 | ADYEN-appinfo | `payment_adyen/models/payment_transaction.py:62-69` | 'applicationInfo': | FACT | — | — | Adyen payment requests include applicationInfo identifying Odoo version as external platform | N-U62-034 |
| VDR-U62-C151 | MAILING-calendar | `mass_mailing/models/mailing.py:108-112` | calendar_date = fields.Datetime | FACT | — | — | calendar_date stored computed field used for calendar view; different from schedule_date | N-U62-028 |
| VDR-U62-C152 | PEPPOL-new-conn-flow | `account_peppol/tools/peppol_iap_connector.py:19-64` | def __init__(self, company) | FACT | — | — | New registration uses 2-step public HTTP flow: can_connect check then create_connection | N-U62-002 |
