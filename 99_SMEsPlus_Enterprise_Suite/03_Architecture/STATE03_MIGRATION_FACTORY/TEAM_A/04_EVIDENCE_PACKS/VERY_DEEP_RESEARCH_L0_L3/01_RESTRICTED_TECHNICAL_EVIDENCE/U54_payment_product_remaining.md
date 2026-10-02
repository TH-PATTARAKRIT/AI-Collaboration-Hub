# U54 — payment provider/token/capture and product catalog/labels/packaging (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U54
- Modules: payment (remaining), product (remaining)
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: DELTA-FIRST — payment U12/U20/U45 done; this unit adds provider config, tokens, capture, refunds. Product U02/U45 done; this unit adds labels, catalog mixin, combo products, pricelist items, supplier info, documents. Source evidence only; RT flags for runtime unknowns.

---

## CAP-U54-01 — Payment Provider Configuration

### D1 — Provider state and publication
The `payment.provider` model (`payment/models/payment_provider.py`) has a `state` field with three values: `disabled`, `enabled`, and `test`. A separate `is_published` Boolean controls website visibility independently of state. An `_onchange_state_switch_is_published` handler automatically sets `is_published = True` when state is set to `enabled` and `False` otherwise.

### D2 — Form templates for payment flows
Four separate `ir.ui.view` Many2one fields distinguish the payment UI path: `redirect_form_view_id` (redirect flow), `inline_form_view_id` (direct inline payment), `token_inline_form_view_id` (token-based inline), and `express_checkout_form_view_id` (Apple/Google Pay express). All carry `ondelete='restrict'`.

### D3 — Availability filters
`available_country_ids` (Many2many to `res.country`) and `available_currency_ids` (Many2many to `res.currency`, computed and stored) restrict availability. An empty `available_country_ids` means the provider is available in all countries. `maximum_amount` is a Monetary field that caps payment size (empty = unlimited). The `_get_compatible_providers` class method applies all three filters, plus tokenization and express-checkout filters, returning a filtered recordset.

### D4 — Feature support computed fields
`support_tokenization`, `support_manual_capture` (selection: `full_only` / `partial`), `support_express_checkout`, and `support_refund` (selection: `none` / `full_only` / `partial`) are all computed by `_compute_feature_support_fields`. The base implementation sets all to `None`/`none`; individual provider modules must override this method to advertise their capabilities.

### D5 — Provider write() lifecycle
`write()` detects state transitions: on any change away from `disabled`/`test`/`enabled`, it calls `_archive_linked_tokens()` to set related `payment.token.active = False`. It then conditionally calls `_deactivate_unsupported_payment_methods()` or `_activate_default_pms()`, and toggles the post-processing cron via `_toggle_post_processing_cron()`.

### D6 — Required-if-provider validation
The `_check_required_if_provider` method reads the `required_if_provider` field attribute (a custom parameter declared via `_valid_field_parameter`) on each field; for enabled/test providers whose `code` matches, it raises `ValidationError` if the field is empty.

### D7 — API request helpers
`_send_api_request` sends HTTP requests with `timeout=10` seconds, logs both request and response, and raises `ValidationError` on HTTP errors after calling `_parse_response_error`. Proxy requests use JSON-RPC 2.0 format with a UUID `id` field.

### Ten-dimension table (CAP-U54-01)
| Dimension | Finding |
|---|---|
| Model | `payment.provider` |
| Key fields | `state`, `is_published`, `code`, `capture_manually`, `allow_tokenization`, `allow_express_checkout` |
| Availability gates | country, currency, maximum_amount, tokenization, express_checkout |
| Form flow markers | `redirect_form_view_id`, `inline_form_view_id`, `token_inline_form_view_id`, `express_checkout_form_view_id` |
| Feature support | `support_tokenization`, `support_manual_capture`, `support_refund`, `support_express_checkout` (all computed) |
| State transitions | write() archives tokens, activates/deactivates PMs, toggles cron |
| Multi-company | `_setup_provider` copies provider record per top-level company |
| Deletion protection | `_unlink_except_master_data` raises UserError if external XML id present |
| API transport | `_send_api_request` with 10s timeout, JSON-RPC 2.0 proxy support |
| Message fields | `pre_msg`, `pending_msg`, `auth_msg`, `done_msg`, `cancel_msg` (all Html, translated) |

---

## CAP-U54-02 — Payment Token Lifecycle

### D1 — Token structure
`payment.token` (`payment/models/payment_token.py`) links to a `payment.provider`, a `payment.method`, and a `res.partner`. `provider_ref` stores the opaque reference from the gateway (required, not the same as the transaction's provider reference). `active` defaults to `True`.

### D2 — Archiving protection
`write()` blocks reactivation of tokens linked to an inactive payment method or a disabled provider, raising `UserError`. When archiving (`active=False`), it calls `sudo()._handle_archiving()` on the previously active tokens — an empty hook for modules to extend.

### D3 — Partner constraint
`_check_partner_is_never_public` raises `ValidationError` if the partner is the public/portal user (checked via `partner_id.is_public`).

### D4 — Display name
`_build_display_name` pads payment details with bullet characters (`•`) to a maximum of 34 characters. If no `payment_details` is available it falls back to the creation date.

### D5 — Available tokens query
`_get_available_tokens` searches tokens by provider and partner. For validation operations it broadens the search to include the commercial partner's tokens.

### Ten-dimension table (CAP-U54-02)
| Dimension | Finding |
|---|---|
| Model | `payment.token` |
| Core constraint | `provider_ref` required; partner must not be public |
| Archive guard | Cannot re-activate if provider disabled or PM inactive |
| Hook | `_handle_archiving()` empty extensible hook |
| Display | `_build_display_name` with bullet padding up to 34 chars |
| Linked docs | `get_linked_records_info()` returns empty list by default; overridden by modules |
| Order | `partner_id, id desc` |
| Create hook | `_get_specific_create_values` hook for provider-specific values |
| Validation tokens | `_get_available_tokens` broadens to commercial partner for validation |
| Token reference | `provider_ref` is NOT the same as transaction `provider_reference` |

---

## CAP-U54-03 — Manual Capture, Void, and Refund Flows

### D1 — Capture wizard
`payment.capture.wizard` (`payment/wizards/payment_capture_wizard.py`) is a transient model. It computes `authorized_amount`, `captured_amount` (from `done` child transactions with no further children), `voided_amount` (from `cancel` child transactions), and `available_amount = authorized - captured - voided`. `support_partial_capture` requires both the provider (`support_manual_capture == 'partial'`) and the payment method to support partial capture. The constraint `_check_amount_to_capture_within_boundaries` raises `ValidationError` if the requested amount is outside `(0, available_amount]` or if partial capture is unsupported and the amount is not the full available amount.

### D2 — _capture / _void / _refund pattern
All three methods on `payment.transaction` follow the same child-transaction pattern:
1. Call `_ensure_provider_is_not_disabled()`
2. Call `_create_child_transaction(amount)` to create a linked child transaction with `source_transaction_id` set to `self.id`
3. Log via `_log_sent_message()`
4. Call the provider hook (`_send_capture_request`, `_send_void_request`, `_send_refund_request`) — each is an empty stub that providers must override
5. On `ValidationError`, call `_set_error()`

### D3 — Child transaction reference prefixes
`_create_child_transaction` uses `R-{reference}` for refunds (with negated amount) and `P-{reference}` for partial capture/void. The `operation` for refunds is `'refund'`; for capture/void it inherits the parent's operation.

### D4 — State-setting methods
`_set_pending`: allowed source states `('draft',)`.
`_set_authorized`: allowed source states `('draft', 'pending')`.
`_set_done`: allowed source states `('draft', 'pending', 'authorized', 'error')`. After updating state, calls `_update_source_transaction_state()`.
`_set_canceled`: allowed source states `('draft', 'pending', 'authorized')`. Also calls `_update_source_transaction_state()`.
`_set_error`: allowed source states `('draft', 'pending', 'authorized')`.

### D5 — Source transaction state propagation
`_update_source_transaction_state` sums all sibling child transactions that share the same `operation` and are in `done` or `cancel` state. When the total equals the source transaction's amount, it transitions the source to `done` (if any child is `done`) or `cancel` (if all children are `cancel`), by calling `_update_state` directly to avoid recursion.

### D6 — Post-processing cron
`_cron_post_process` uses a retry window of 4 days (`retry_limit_date = datetime.now() - relativedelta(days=4)`), searches for transactions with `is_post_processed=False` since that date, and commits per-transaction. On `psycopg2.OperationalError` it rolls back and continues.

### D7 — action_capture and action_void
`action_capture` on `payment.transaction` opens the `payment.capture.wizard` when any transaction's provider supports `partial` capture; otherwise calls `_capture()` directly in a loop. `action_void` requires all selected transactions to be in `authorized` state.

### D8 — action_refund
`action_refund` requires all transactions to be in `done` state, then calls `_refund(amount_to_refund=amount_to_refund)` per transaction in sudo mode.

### Ten-dimension table (CAP-U54-03)
| Dimension | Finding |
|---|---|
| Capture wizard | `payment.capture.wizard` — transient, multi-source-tx support |
| Partial capture gate | Both provider AND PM must report `support_manual_capture == 'partial'` |
| Child tx prefix | `R-` for refunds, `P-` for capture/void |
| Refund negation | `amount = -amount` at `_create_child_transaction` for `is_refund=True` |
| State guards | `_set_pending`→draft; `_set_authorized`→draft/pending; `_set_done`→draft/pending/authorized/error |
| Source propagation | `_update_source_transaction_state` rolls up child results to parent |
| Cron retry window | 4 days, per-transaction commit, rollback on DB error |
| Void guard | `action_void` raises ValidationError if any tx not `authorized` |
| Refund guard | `action_refund` raises ValidationError if any tx not `done` |
| Provider hooks | `_send_capture_request`, `_send_void_request`, `_send_refund_request` — all empty stubs |

---

## CAP-U54-04 — Payment Link Wizard

### D1 — Wizard structure
`payment.link.wizard` (`payment/wizards/payment_link_wizard.py`) is a transient model. `default_get` loads `res_model` and `res_id` from context and calls `_get_default_payment_link_values()` on the related document. `_compute_link` builds the URL using `_prepare_url`, `_prepare_query_params`, and `_prepare_anchor`.

### D2 — URL construction
`_prepare_url` returns `{base_url}/payment/pay` by default. `_prepare_query_params` includes `amount`, `access_token` (via `payment_utils.generate_access_token`), `currency_id`, `partner_id`, and `company_id`. The access token signs the partner, amount, and currency.

### D3 — Warning messages
`_compute_warning_message` warns if `amount_max <= 0` ("nothing to pay"), `amount <= 0` ("set positive amount"), or `amount > amount_max` ("set lower amount").

### Ten-dimension table (CAP-U54-04)
| Dimension | Finding |
|---|---|
| Model | `payment.link.wizard` (transient) |
| URL base | `/payment/pay` |
| Security | Access token signed on partner_id + amount + currency_id |
| Warning logic | Three distinct warning conditions on amounts |
| Company | Computed from related document's `company_id` if present |
| Extension points | `_prepare_url`, `_prepare_query_params`, `_prepare_anchor` all overrideable |

---

## CAP-U54-05 — Product Catalog Mixin

### D1 — Abstract mixin
`product.catalog.mixin` (`product/models/product_catalog_mixin.py`) is an `AbstractModel`. It assumes the inheriting model has an O2M field for product lines whose co-model implements `_get_product_catalog_lines_data`.

### D2 — Catalog action
`action_add_from_catalog` opens a kanban window action on `product.product` using view refs `product.product_view_kanban_catalog` and `product.product_view_search_catalog`. It calls `_get_product_catalog_domain()` and strips `form_view_ref` from context.

### D3 — Domain filtering
`_get_product_catalog_domain` returns a domain combining company restriction (company_id is False OR parent_of the current company) and excludes combo products (`type != 'combo'`).

### D4 — Order line info aggregation
`_get_product_catalog_order_line_info` merges data from `_get_product_catalog_record_lines` (existing lines) and `_get_product_catalog_order_data` (new products), resulting in a dict keyed by `product.product` id with fields: `productType`, `uomDisplayName`, `code`, `quantity`, `readOnly`, `price`.

### D5 — Extra context
`_get_action_add_from_catalog_extra_context` injects `display_uom` (based on `uom.group_uom` group), `product_catalog_order_id`, and `product_catalog_order_model` into the action context.

### Ten-dimension table (CAP-U54-05)
| Dimension | Finding |
|---|---|
| Model type | `AbstractModel` — no direct records, inherited by sale/purchase order models |
| Catalog view | Kanban `product.product_view_kanban_catalog`, search `product.product_view_search_catalog` |
| Domain | Excludes combo products; restricts by company (parent_of) |
| Data merge | Line info + product data merged; line data takes precedence |
| Required override | `_get_product_catalog_record_lines`, `_update_order_line_info`, `_is_readonly` |
| UoM display | Controlled by `uom.group_uom` feature group |

---

## CAP-U54-06 — Product Label Layout Wizard

### D1 — Wizard structure
`product.label.layout` (`product/wizard/product_label_layout.py`) is a transient model with `print_format` selection, `custom_quantity` integer, `product_ids` and `product_tmpl_ids` Many2many fields, `extra_html` Html field, and `pricelist_id` Many2one.

### D2 — Print formats
Five format options: `dymo`, `2x7xprice`, `4x7xprice`, `4x12`, `4x12xprice`. `_compute_dimensions` parses the `XxY` pattern from the format string to set `rows` and `columns`.

### D3 — Report data preparation
`_prepare_report_data` maps the format to a report XML id (`product.report_product_template_label_dymo` or `product.report_product_template_label_{columns}x{rows}[_noprice]`). It determines the `active_model` from whether `product_tmpl_ids` or `product_ids` are set. The data dict includes `quantity_by_product`, `layout_wizard`, and `price_included`.

### D4 — Processing
`process()` resolves the report action via `self.env.ref(xml_id).report_action(None, data=data, config=False)` and sets `close_on_report_download=True`.

### Ten-dimension table (CAP-U54-06)
| Dimension | Finding |
|---|---|
| Model | `product.label.layout` (transient) |
| Formats | dymo, 2x7xprice, 4x7xprice, 4x12, 4x12xprice |
| Price inclusion | `'xprice' in print_format` flag drives `price_included` in report data |
| Active model | Determined by whether product_tmpl_ids or product_ids are populated |
| Pricelist | `pricelist_id` field available but passed to report for rendering (RT: how report uses it) |
| Error guard | Raises UserError if quantity <= 0 or no products selected or format unrecognized |

---

## CAP-U54-07 — Combo Products

### D1 — product.combo model
`product.combo` (`product/models/product_combo.py`) is ordered by `sequence, id`. It has a `name` (required), `company_id` (optional), `combo_item_ids` (O2M to `product.combo.item`), `combo_item_count` (computed via `_read_group`), `currency_id` (computed from company or main company), and `base_price` (computed as the minimum price across all combo items after currency conversion).

### D2 — Base price computation
`_compute_base_price` converts each combo item's `lst_price` to the combo's currency using the company's exchange rate at database `now()` time, then takes the minimum. This minimum is used to prorate the combo's price contribution relative to other combos in a combo product.

### D3 — Constraints
Two constraints enforce: (a) at least one item per combo (`_check_combo_item_ids_not_empty`); (b) no duplicate products in a combo (`_check_combo_item_ids_no_duplicates` compares `len(combo_item_ids.mapped('product_id'))` against `len(combo_item_ids)`).

### D4 — product.combo.item model
`product.combo.item` (`product/models/product_combo_item.py`) has `company_id` (stored, from combo), `combo_id` (required, cascade delete), `product_id` (restricted to non-combo type via domain), `lst_price` (related from product), and `extra_price` (float, default 0.0). Constraint `_check_product_id_no_combo` raises `ValidationError` if the selected product type is `'combo'`.

### Ten-dimension table (CAP-U54-07)
| Dimension | Finding |
|---|---|
| Models | `product.combo`, `product.combo.item` |
| Combo ordering | `sequence, id` |
| Base price | Min of all item prices (currency-converted) at current exchange rate |
| Constraints | Min 1 item; no duplicates; items cannot be combo-type products |
| Extra price | `extra_price` on item for optional upsell amount |
| Company | Optional on combo; items inherit via `related` |

---

## CAP-U54-08 — Pricelist (Residual)

### D1 — Pricelist structure
`product.pricelist` (`product/models/product_pricelist.py`) inherits `mail.thread` and `mail.activity.mixin`. Ordered `sequence, id, name`. `display_name` computed as `{name} ({currency_id.name})`. Deletion is blocked by `_unlink_except_used_as_rule_base` if any other pricelist's item references this pricelist as `base`.

### D2 — Country group association
`country_group_ids` (Many2many to `res.country.group`) ties the pricelist to geographic regions. `_get_partner_pricelist_multi` resolves the pricelist per partner: first checks a specific property, then country group, then falls back to the config parameter `res.partner.property_product_pricelist_{company_id}`, then the first available pricelist.

### D3 — Price rule computation
`_compute_price_rule` iterates applicable rules (from `_get_applicable_rules`) per product, finds the first matching rule via `_is_applicable_for`, and calls `rule._compute_price()`. Returns `{product_id: (price, rule_id)}`.

### D4 — Applicable rules domain
`_get_applicable_rules_domain` filters by pricelist, optional category (parent_of), optional product template, optional variant, and date range (start/end). Date is applied as `date_start <= date` and `date_end >= date`.

### D5 — pricelist.item compute_price modes
`product.pricelist.item` (`product/models/product_pricelist_item.py`): `compute_price` selection is `fixed`, `percentage`, or `formula`. Formula mode applies `price_discount` (or `-price_markup` for cost base), `price_round`, `price_surcharge`, `price_min_margin`, and `price_max_margin` in that order. Recursion in pricelist chains is detected via DFS in `_check_pricelist_recursion`.

### D6 — applied_on levels
Four levels: `3_global` (all products), `2_product_category` (category + children via `parent_path`), `1_product` (specific template), `0_product_variant` (specific variant). `create()` and `write()` enforce mutual exclusivity by clearing irrelevant fields.

### Ten-dimension table (CAP-U54-08)
| Dimension | Finding |
|---|---|
| Pricelist model | `product.pricelist` — mail.thread + mail.activity.mixin |
| Partner resolution | Specific property → country group → config param → first active |
| Rule matching | First applicable rule wins (ordered by applied_on, min_quantity desc) |
| Formula fields | price_discount/markup, price_round, price_surcharge, min/max margin |
| Recursion guard | DFS `_check_pricelist_recursion` raises ValidationError on cycle |
| Date filter | date_start/date_end on item (Datetime, timezone-aware note in help) |

---

## CAP-U54-09 — Supplier Pricelist (product.supplierinfo)

### D1 — Model structure
`product.supplierinfo` (`product/models/product_supplierinfo.py`), description "Supplier Pricelist", ordered `sequence, min_qty DESC, price, id`. Links to `res.partner` (vendor), optionally to a specific `product.product` variant (if None, applies to all variants of the template).

### D2 — Key fields
`min_qty` (float, threshold for price to apply), `price` (unit price), `delay` (integer, lead time in days), `discount` (float, percentage), `date_start`/`date_end` (validity dates), `product_uom_id` (computed from product or template UoM), `currency_id` (company currency default).

### D3 — Discounted price
`_compute_price_discounted` converts the unit price to the product's UoM via `product_uom_id._compute_price(price, product_uom)` and then applies `* (1 - discount / 100)`.

### D4 — Sanitize on create/write
`_sanitize_vals` auto-populates `product_tmpl_id` from `product_id.product_tmpl_id` when a variant is set without an explicit template.

### D5 — Filtering
`_get_filtered_supplier` filters by company (no company or matching) and by active partner; and by product variant match if set.

### Ten-dimension table (CAP-U54-09)
| Dimension | Finding |
|---|---|
| Model | `product.supplierinfo` |
| Order | sequence, min_qty DESC, price, id |
| Vendor-specific names | `product_name`, `product_code` fields |
| Lead time | `delay` integer in days |
| Discount | `discount` float field; `price_discounted` computed |
| Template sync | `_sanitize_vals` keeps product_tmpl_id in sync with product_id |

---

## CAP-U54-10 — Product Document

### D1 — Inherits ir.attachment
`product.document` (`product/models/product_document.py`) uses `_inherits` from `ir.attachment` via `ir_attachment_id` (required, `ondelete='cascade'`). This means all attachment fields (name, type, url, datas, etc.) are accessible directly on a `product.document` record.

### D2 — URL validation
`_onchange_url` raises `ValidationError` if the URL does not start with `https://`, `http://`, or `ftp://`.

### D3 — Unlink cascade
`unlink()` deletes the `ir.attachment` records after deleting the `product.document` records.

### D4 — Copy behavior
`copy_data` copies the underlying `ir.attachment` separately with context `no_document=True` and `disable_product_documents_creation=True`.

### Ten-dimension table (CAP-U54-10)
| Dimension | Finding |
|---|---|
| Model | `product.document` |
| Delegate | `_inherits` from `ir.attachment` via `ir_attachment_id` |
| Order | `sequence, name` |
| URL validation | Only https/http/ftp accepted |
| Unlink | Cascades to `ir.attachment` after document deletion |
| Copy | Attachment copied separately with no_document context flag |

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U54-C001 | PAY-PROVIDER-STATE | payment/models/payment_provider.py:41 | state = fields.Selection | FACT | Always | — | Provider state field has three values: disabled, enabled, test; defaults to disabled | N-U54-001 |
| VDR-U54-C002 | PAY-PROVIDER-PUBLISHED | payment/models/payment_provider.py:47 | is_published = fields.Boolean | FACT | Always | — | is_published controls visibility on website but tokens remain functional even when unpublished | N-U54-002 |
| VDR-U54-C003 | PAY-PROVIDER-COMPANY | payment/models/payment_provider.py:53 | company_id = fields.Many2one | FACT | Always | — | company_id is required and indexed for ir_rule ORM performance | N-U54-003 |
| VDR-U54-C004 | PAY-PROVIDER-PM | payment/models/payment_provider.py:60 | payment_method_ids = fields.Many2many | FACT | Always | — | Provider has Many2many to payment.method for supported methods | N-U54-004 |
| VDR-U54-C005 | PAY-PROVIDER-TOKENIZE | payment/models/payment_provider.py:63 | allow_tokenization = fields.Boolean | FACT | Always | — | allow_tokenization flag controls whether customers can save payment methods as tokens | N-U54-005 |
| VDR-U54-C006 | PAY-PROVIDER-CAPTURE | payment/models/payment_provider.py:68 | capture_manually = fields.Boolean | FACT | Always | — | capture_manually flag enables deferred capture at delivery time | N-U54-006 |
| VDR-U54-C007 | PAY-PROVIDER-EXPRESS | payment/models/payment_provider.py:73 | allow_express_checkout = fields.Boolean | FACT | Always | — | allow_express_checkout controls availability of Apple Pay / Google Pay flows | N-U54-007 |
| VDR-U54-C008 | PAY-PROVIDER-REDIRECT-VIEW | payment/models/payment_provider.py:79 | redirect_form_view_id = fields.Many2one | FACT | Always | — | redirect_form_view_id stores the QWeb template for redirect-flow payment forms | N-U54-008 |
| VDR-U54-C009 | PAY-PROVIDER-INLINE-VIEW | payment/models/payment_provider.py:85 | inline_form_view_id = fields.Many2one | FACT | Always | — | inline_form_view_id stores the QWeb template for direct inline payment forms | N-U54-008 |
| VDR-U54-C010 | PAY-PROVIDER-TOKEN-VIEW | payment/models/payment_provider.py:91 | token_inline_form_view_id = fields.Many2one | FACT | Always | — | token_inline_form_view_id stores QWeb template for token-based inline forms | N-U54-008 |
| VDR-U54-C011 | PAY-PROVIDER-EXPRESS-VIEW | payment/models/payment_provider.py:98 | express_checkout_form_view_id = fields.Many2one | FACT | Always | — | express_checkout_form_view_id stores QWeb template for Apple/Google Pay forms | N-U54-008 |
| VDR-U54-C012 | PAY-PROVIDER-COUNTRIES | payment/models/payment_provider.py:107 | available_country_ids = fields.Many2many | FACT | Always | — | available_country_ids M2M; empty list means available in all countries | N-U54-009 |
| VDR-U54-C013 | PAY-PROVIDER-CURRENCIES | payment/models/payment_provider.py:116 | available_currency_ids = fields.Many2many | FACT | Always | — | available_currency_ids is computed and stored; empty means no currency restriction | N-U54-009 |
| VDR-U54-C014 | PAY-PROVIDER-MAX-AMOUNT | payment/models/payment_provider.py:129 | maximum_amount = fields.Monetary | FACT | Always | — | maximum_amount caps the payment size; empty means unlimited | N-U54-009 |
| VDR-U54-C015 | PAY-PROVIDER-MESSAGES | payment/models/payment_provider.py:137 | pre_msg = fields.Html | FACT | Always | — | Five Html translated message fields (pre_msg, pending_msg, auth_msg, done_msg, cancel_msg) shown at payment stages | N-U54-010 |
| VDR-U54-C016 | PAY-PROVIDER-SUPPORT-TOKENIZE | payment/models/payment_provider.py:160 | support_tokenization = fields.Boolean | FACT | Always | — | support_tokenization is computed; base sets to None; providers must override | N-U54-011 |
| VDR-U54-C017 | PAY-PROVIDER-SUPPORT-CAPTURE | payment/models/payment_provider.py:163 | support_manual_capture = fields.Selection | FACT | Always | — | support_manual_capture selection: full_only or partial; base sets to None | N-U54-011 |
| VDR-U54-C018 | PAY-PROVIDER-SUPPORT-REFUND | payment/models/payment_provider.py:171 | support_refund = fields.Selection | FACT | Always | — | support_refund selection: none, full_only, or partial; base sets to 'none' | N-U54-011 |
| VDR-U54-C019 | PAY-PROVIDER-COMPUTE-FEATURE | payment/models/payment_provider.py:264 | self.update | FACT | Always | — | Base _compute_feature_support_fields sets all features to None/none by default | N-U54-011 |
| VDR-U54-C020 | PAY-PROVIDER-ONCHANGE-PUBLISH | payment/models/payment_provider.py:278 | `self.is_published = self.state == 'enabled'` | FACT | Always | — | State change to 'enabled' auto-publishes; any other state auto-unpublishes | N-U54-012 |
| VDR-U54-C021 | PAY-PROVIDER-WARN-TOKENS | payment/models/payment_provider.py:291 | `if self._origin.state in ('test', 'enabled') and self._origin.state != self.state:` | FACT | Onchange | — | Changing state from active (enabled/test) warns about archiving related tokens | N-U54-012 |
| VDR-U54-C022 | PAY-PROVIDER-WRITE-ARCHIVE | payment/models/payment_provider.py:352 | `state_changed_providers._archive_linked_tokens()` | FACT | write() state change | — | write() archives tokens when provider state changes away from enabled/test | N-U54-012 |
| VDR-U54-C023 | PAY-PROVIDER-CHECK-REQUIRED | payment/models/payment_provider.py:368 | def _check_required_if_provider(self) | FACT | Always | — | _check_required_if_provider inspects `required_if_provider` custom field attribute | N-U54-013 |
| VDR-U54-C024 | PAY-PROVIDER-CRON-TOGGLE | payment/models/payment_provider.py:396 | def _toggle_post_processing_cron(self) | FACT | Always | — | _toggle_post_processing_cron activates/deactivates 'payment.cron_post_process_payment_tx' based on any_active_provider | N-U54-014 |
| VDR-U54-C025 | PAY-PROVIDER-ARCHIVE-TOKENS | payment/models/payment_provider.py:417 | `self.env['payment.token'].search([('provider_id', 'in', self.ids)]).write({'active': False})` | FACT | Always | — | _archive_linked_tokens sets active=False on all tokens linked to the providers | N-U54-015 |
| VDR-U54-C026 | PAY-PROVIDER-DEACTIVATE-PMS | payment/models/payment_provider.py:424 | unsupported_pms | FACT | Always | — | _deactivate_unsupported_payment_methods deactivates PMs only linked to disabled providers | N-U54-015 |
| VDR-U54-C027 | PAY-PROVIDER-ACTIVATE-PMS | payment/models/payment_provider.py:429 | `def _activate_default_pms(self):` | FACT | Always | — | _activate_default_pms activates PMs listed as default; filters out PMs incompatible with manual capture | N-U54-015 |
| VDR-U54-C028 | PAY-PROVIDER-COMPATIBLE | payment/models/payment_provider.py:554 | @api.model | FACT | Always | — | _get_compatible_providers is a @api.model method applying 5 filters: company, country, max_amount, currency, tokenization/express | N-U54-016 |
| VDR-U54-C029 | PAY-PROVIDER-COMPAT-COUNTRY | payment/models/payment_provider.py:591 | partner = self.env['res.partner'].browse | FACT | Always | — | Country filter skipped if partner has no country; empty available_country_ids passes all partners | N-U54-016 |
| VDR-U54-C030 | PAY-PROVIDER-COMPAT-AMOUNT | payment/models/payment_provider.py:614 | providers = providers.filtered | FACT | Non-validation only | — | Amount filter converts to company currency before comparing; skipped for validation transactions | N-U54-016 |
| VDR-U54-C031 | PAY-PROVIDER-INLINE-FORM | payment/models/payment_provider.py:679 | def _should_build_inline_form | FACT | Always | — | _should_build_inline_form returns True by default; providers override for redirect-only flows | N-U54-017 |
| VDR-U54-C032 | PAY-PROVIDER-VALIDATION-AMOUNT | payment/models/payment_provider.py:703 | `return 0.0` | FACT | Always | — | _get_validation_amount returns 0.0 by default for tokenization validation | N-U54-017 |
| VDR-U54-C033 | PAY-PROVIDER-VALIDATION-CURR | payment/models/payment_provider.py:729 | `validation_currency = (provider_currencies & pm_currencies)[:1]` | FACT | Always | — | _get_validation_currency finds intersection of provider and PM supported currencies; falls back to company currency | N-U54-017 |
| VDR-U54-C034 | PAY-PROVIDER-API-TIMEOUT | payment/models/payment_provider.py:793 | timeout=10 | FACT | Always | — | All provider API requests use a 10-second timeout | N-U54-018 |
| VDR-U54-C035 | PAY-PROVIDER-SETUP | payment/models/payment_provider.py:969 | `def _setup_provider(self, provider_code, **kwargs):` | FACT | Post-install | — | _setup_provider creates a copy of the main provider for each top-level company that doesn't already have one | N-U54-019 |
| VDR-U54-C036 | PAY-PROVIDER-REMOVAL | payment/models/payment_provider.py:1010 | `def _get_removal_values(self):` | FACT | Module uninstall | — | _get_removal_values resets code to 'none', state to 'disabled', is_published to False, and clears all form view fields | N-U54-019 |
| VDR-U54-C037 | PAY-PROVIDER-STATUS-MSG | payment/models/payment_provider.py:1040 | def _get_status_message(self, status) | FACT | Always | — | _get_status_message uses Python match-case on status string; returns empty string if HTML is empty | N-U54-010 |
| VDR-U54-C038 | PAY-TOKEN-ACTIVE | payment/models/payment_token.py:37 | `active = fields.Boolean(string="Active", default=True)` | FACT | Always | — | Token active field defaults to True; archiving sets to False | N-U54-020 |
| VDR-U54-C039 | PAY-TOKEN-PROVREF | payment/models/payment_token.py:29 | provider_ref = fields.Char | FACT | Always | — | provider_ref is required; it is NOT the same as the transaction's provider_reference | N-U54-020 |
| VDR-U54-C040 | PAY-TOKEN-WRITE-GUARD | payment/models/payment_token.py:83 | if 'active' in vals | FACT | write() | — | write() raises UserError if any token being reactivated has an inactive PM or disabled provider | N-U54-021 |
| VDR-U54-C041 | PAY-TOKEN-ARCHIVING | payment/models/payment_token.py:96 | `self.filtered('active').sudo()._handle_archiving()` | FACT | write() active=False | — | _handle_archiving called in sudo on currently-active tokens being archived | N-U54-021 |
| VDR-U54-C042 | PAY-TOKEN-PARTNER-CHECK | payment/models/payment_token.py:100 | @api.constrains('partner_id') | FACT | Always | — | Constraint blocks assigning a public partner to a token | N-U54-022 |
| VDR-U54-C043 | PAY-TOKEN-AVAILABLE | payment/models/payment_token.py:119 | `def _get_available_tokens(self, providers_ids, partner_id, is_validation=False, **kwargs):` | FACT | Always | — | For non-validation returns tokens filtered by provider and partner; for validation broadens to commercial partner | N-U54-022 |
| VDR-U54-C044 | PAY-TOKEN-DISPLAY | payment/models/payment_token.py:144 | def _build_display_name | FACT | Always | — | _build_display_name pads with up to 4 bullet chars and a space; max 34 chars total | N-U54-023 |
| VDR-U54-C045 | PAY-TOKEN-LINKED-DOCS | payment/models/payment_token.py:183 | def get_linked_records_info(self) | FACT | Always | — | get_linked_records_info returns empty list by default; modules override to add linked record data | N-U54-023 |
| VDR-U54-C046 | PAY-TOKEN-CREATE-HOOK | payment/models/payment_token.py:62 | def _get_specific_create_values | FACT | create() | — | create() merges provider-specific values via _get_specific_create_values hook | N-U54-024 |
| VDR-U54-C047 | PAY-TX-OPERATION | payment/models/payment_transaction.py:77 | operation = fields.Selection | FACT | Always | — | Operation field has 6 values: online_redirect, online_direct, online_token, validation, offline, refund | N-U54-025 |
| VDR-U54-C048 | PAY-TX-SOURCE | payment/models/payment_transaction.py:95 | source_transaction_id = fields.Many2one | FACT | Always | — | source_transaction_id links a child tx (capture, void, refund) to its parent | N-U54-025 |
| VDR-U54-C049 | PAY-TX-CHILDREN | payment/models/payment_transaction.py:102 | child_transaction_ids = fields.One2many | FACT | Always | — | child_transaction_ids is read-only O2M of all child transactions | N-U54-025 |
| VDR-U54-C050 | PAY-TX-REFUNDS-COUNT | payment/models/payment_transaction.py:109 | `refunds_count = fields.Integer(string="Refunds Count", compute='_compute_refunds_count')` | FACT | Always | — | refunds_count computed via _read_group on child transactions with operation='refund' | N-U54-025 |
| VDR-U54-C051 | PAY-TX-AUTHORIZED-CHECK | payment/models/payment_transaction.py:158 | @api.constrains('state') | FACT | Always | — | Constraint blocks 'authorized' state on providers that don't support manual capture | N-U54-026 |
| VDR-U54-C052 | PAY-TX-TOKEN-ACTIVE-CHECK | payment/models/payment_transaction.py:170 | @api.constrains('token_id') | FACT | create() | — | Constraint blocks creating a transaction from an archived token | N-U54-026 |
| VDR-U54-C053 | PAY-TX-ACTION-CAPTURE-WIZARD | payment/models/payment_transaction.py:275 | `if any(tx.provider_id.sudo().support_manual_capture == 'partial' for tx in self):` | FACT | action_capture | — | action_capture opens the wizard only if any provider supports partial capture; otherwise captures directly | N-U54-027 |
| VDR-U54-C054 | PAY-TX-ACTION-VOID | payment/models/payment_transaction.py:300 | if any(tx.state != 'authorized' for tx in self) | FACT | action_void | — | action_void raises ValidationError if any selected tx is not in authorized state | N-U54-027 |
| VDR-U54-C055 | PAY-TX-ACTION-REFUND | payment/models/payment_transaction.py:321 | if any(tx.state != 'done' for tx in self) | FACT | action_refund | — | action_refund raises ValidationError if any selected tx is not in done state | N-U54-027 |
| VDR-U54-C056 | PAY-TX-CAPTURE-METHOD | payment/models/payment_transaction.py:591 | `def _capture(self, amount_to_capture=None):` | FACT | Always | — | _capture creates a child transaction then calls _send_capture_request; catches ValidationError to _set_error | N-U54-028 |
| VDR-U54-C057 | PAY-TX-VOID-METHOD | payment/models/payment_transaction.py:623 | `def _void(self, amount_to_void=None):` | FACT | Always | — | _void creates a child transaction then calls _send_void_request; same error handling as _capture | N-U54-028 |
| VDR-U54-C058 | PAY-TX-REFUND-METHOD | payment/models/payment_transaction.py:655 | `def _refund(self, amount_to_refund=None):` | FACT | Always | — | _refund creates a child transaction with is_refund=True then calls _send_refund_request | N-U54-028 |
| VDR-U54-C059 | PAY-TX-CREATE-CHILD-REFUND-NEG | payment/models/payment_transaction.py:715 | if is_refund | FACT | _create_child_transaction | — | Refund child gets R- prefix and negated amount; operation set to 'refund' | N-U54-028 |
| VDR-U54-C060 | PAY-TX-CREATE-CHILD-PARTIAL | payment/models/payment_transaction.py:719 | else:  # Partial capture or void. | FACT | _create_child_transaction | — | Partial capture/void child gets P- prefix and inherits parent's operation | N-U54-028 |
| VDR-U54-C061 | PAY-TX-SET-PENDING | payment/models/payment_transaction.py:924 | `allowed_states = ('draft',)` | FACT | _set_pending | — | _set_pending only accepts draft-state transactions; moves to pending | N-U54-029 |
| VDR-U54-C062 | PAY-TX-SET-AUTHORIZED | payment/models/payment_transaction.py:941 | `allowed_states = ('draft', 'pending')` | FACT | _set_authorized | — | _set_authorized accepts draft and pending transactions | N-U54-029 |
| VDR-U54-C063 | PAY-TX-SET-DONE | payment/models/payment_transaction.py:958 | `allowed_states = ('draft', 'pending', 'authorized', 'error')` | FACT | _set_done | — | _set_done accepts draft, pending, authorized, and error; calls _update_source_transaction_state | N-U54-029 |
| VDR-U54-C064 | PAY-TX-SET-CANCELED | payment/models/payment_transaction.py:976 | `allowed_states = ('draft', 'pending', 'authorized')` | FACT | _set_canceled | — | _set_canceled accepts draft, pending, and authorized; also calls _update_source_transaction_state | N-U54-029 |
| VDR-U54-C065 | PAY-TX-SET-ERROR | payment/models/payment_transaction.py:994 | `allowed_states = ('draft', 'pending', 'authorized')` | FACT | _set_error | — | _set_error accepts draft, pending, and authorized states | N-U54-029 |
| VDR-U54-C066 | PAY-TX-UPDATE-STATE | payment/models/payment_transaction.py:1052 | txs_to_process.write | FACT | _update_state | — | _update_state resets is_post_processed=False to allow re-post-processing after state change | N-U54-030 |
| VDR-U54-C067 | PAY-TX-SOURCE-PROPAGATE | payment/models/payment_transaction.py:1060 | `def _update_source_transaction_state(self):` | FACT | _set_done/_set_canceled | — | When all same-operation children reach final state summing to source amount, source is moved to done or cancel | N-U54-030 |
| VDR-U54-C068 | PAY-TX-CRON-4DAY | payment/models/payment_transaction.py:1092 | `retry_limit_date = datetime.now() - relativedelta.relativedelta(days=4)` | FACT | cron | — | Post-processing cron retries transactions for up to 4 days | N-U54-031 |
| VDR-U54-C069 | PAY-TX-TOKENIZE | payment/models/payment_transaction.py:876 | `def _tokenize(self, payment_data):` | FACT | _process | — | _tokenize creates payment.token then writes token_id to transaction and clears tokenize flag | N-U54-032 |
| VDR-U54-C070 | PAY-TX-IS-LIVE | payment/models/payment_transaction.py:186 | `values['is_live'] = provider.state == 'enabled'` | FACT | create() | — | is_live flag is True only when provider is in 'enabled' (not 'test') state at transaction creation | N-U54-033 |
| VDR-U54-C071 | PAY-CAPTURE-WIZ-MODEL | payment/wizards/payment_capture_wizard.py:8 | class PaymentCaptureWizard(models.TransientModel) | FACT | Always | — | payment.capture.wizard is a TransientModel for manual capture UI | N-U54-034 |
| VDR-U54-C072 | PAY-CAPTURE-WIZ-AMOUNTS | payment/wizards/payment_capture_wizard.py:67 | @api.depends('authorized_amount | FACT | Always | — | available_amount = authorized - captured - voided; drives maximum capture constraint | N-U54-034 |
| VDR-U54-C073 | PAY-CAPTURE-WIZ-PARTIAL-CHECK | payment/wizards/payment_capture_wizard.py:87 | def _compute_support_partial_capture(self) | FACT | Always | — | Both provider AND primary payment method must support partial capture | N-U54-034 |
| VDR-U54-C074 | PAY-CAPTURE-WIZ-CONSTRAINT | payment/wizards/payment_capture_wizard.py:122 | if not wizard.support_partial_capture | FACT | constrains | — | Constraint blocks partial amount when provider/PM supports only full capture | N-U54-034 |
| VDR-U54-C075 | PAY-CAPTURE-WIZ-ACTION | payment/wizards/payment_capture_wizard.py:131 | `def action_capture(self):` | FACT | UI action | — | action_capture loops authorized source txs, calls _capture per tx, optionally calls _void for remaining amount | N-U54-035 |
| VDR-U54-C076 | PAY-LINK-WIZ-URL | payment/wizards/payment_link_wizard.py:74 | `return f'{base_url}/payment/pay'` | FACT | Always | — | Payment link URL base is /payment/pay | N-U54-036 |
| VDR-U54-C077 | PAY-LINK-WIZ-TOKEN | payment/wizards/payment_link_wizard.py:96 | return payment_utils.generate_access_token | FACT | Always | — | Access token is generated by payment_utils.generate_access_token over partner, amount, currency | N-U54-036 |
| VDR-U54-C078 | PROD-CATALOG-MIXIN | product/models/product_catalog_mixin.py:7 | class ProductCatalogMixin(models.AbstractModel) | FACT | Always | — | product.catalog.mixin is an AbstractModel; no direct records | N-U54-037 |
| VDR-U54-C079 | PROD-CATALOG-DOMAIN | product/models/product_catalog_mixin.py:39 | def _get_product_catalog_domain(self) -> Domain | FACT | Always | — | _get_product_catalog_domain excludes combo-type products and applies company parent_of filter | N-U54-037 |
| VDR-U54-C080 | PROD-CATALOG-ACTION | product/models/product_catalog_mixin.py:18 | `kanban_view_id = self.env.ref('product.product_view_kanban_catalog').id` | FACT | Always | — | action_add_from_catalog uses product.product_view_kanban_catalog and product.product_view_search_catalog | N-U54-037 |
| VDR-U54-C081 | PROD-CATALOG-LINE-MERGE | product/models/product_catalog_mixin.py:107 | order_line_info = {} | FACT | Always | — | Existing line data merged with productType and code from product; line data takes precedence | N-U54-038 |
| VDR-U54-C082 | PROD-CATALOG-CONTEXT | product/models/product_catalog_mixin.py:130 | return | FACT | Always | — | Extra context includes product_catalog_order_id and product_catalog_order_model for JS to call back | N-U54-038 |
| VDR-U54-C083 | PROD-LABEL-MODEL | product/wizard/product_label_layout.py:9 | class ProductLabelLayout(models.TransientModel) | FACT | Always | — | product.label.layout is a TransientModel for configuring label print jobs | N-U54-039 |
| VDR-U54-C084 | PROD-LABEL-FORMATS | product/wizard/product_label_layout.py:13 | print_format = fields.Selection | FACT | Always | — | Five print format options; dymo and four grid formats with optional price column | N-U54-039 |
| VDR-U54-C085 | PROD-LABEL-DIMENSIONS | product/wizard/product_label_layout.py:28 | def _compute_dimensions(self) | FACT | Always | — | Dimensions parsed from format string by splitting on 'x' | N-U54-039 |
| VDR-U54-C086 | PROD-LABEL-PRICE-FLAG | product/wizard/product_label_layout.py:66 | `'price_included': 'xprice' in self.print_format,` | FACT | Always | — | price_included flag in report data is True when format name contains 'xprice' | N-U54-040 |
| VDR-U54-C087 | PROD-LABEL-PRICELIST | product/wizard/product_label_layout.py:25 | `pricelist_id = fields.Many2one('product.pricelist', string="Pricelist")` | FACT | Always | RT | pricelist_id is available on the wizard; how report templates use it is RT (not visible in wizard model) | N-U54-040 |
| VDR-U54-C088 | PROD-LABEL-XMLID | product/wizard/product_label_layout.py:44 | `xml_id = 'product.report_product_template_label_%sx%s' % (self.columns, self.rows)` | FACT | _prepare_report_data | — | Grid report XML id is dynamically constructed from columns and rows; '_noprice' suffix added for no-price formats | N-U54-040 |
| VDR-U54-C089 | PROD-LABEL-ACTIVE-MODEL | product/wizard/product_label_layout.py:52 | if self.product_tmpl_ids | FACT | _prepare_report_data | — | product_tmpl_ids takes precedence over product_ids for determining active_model | N-U54-040 |
| VDR-U54-C090 | PROD-COMBO-MODEL | product/models/product_combo.py:7 | class ProductCombo(models.Model) | FACT | Always | — | product.combo ordered by sequence then id | N-U54-041 |
| VDR-U54-C091 | PROD-COMBO-BASE-PRICE | product/models/product_combo.py:25 | " prorate the price | FACT | Always | — | base_price is the minimum item price (currency-converted) used for price proration | N-U54-041 |
| VDR-U54-C092 | PROD-COMBO-BASE-PRICE-COMPUTE | product/models/product_combo.py:55 | combo.base_price | FACT | _compute_base_price | — | base_price computed as min of lst_price of all items after currency conversion at current db time | N-U54-041 |
| VDR-U54-C093 | PROD-COMBO-NOT-EMPTY | product/models/product_combo.py:64 | @api.constrains('combo_item_ids') | FACT | Always | — | Constraint requires at least 1 item in each combo | N-U54-042 |
| VDR-U54-C094 | PROD-COMBO-NO-DUP | product/models/product_combo.py:69 | `if len(combo.combo_item_ids.mapped('product_id')) < len(combo.combo_item_ids):` | FACT | Always | — | Constraint blocks duplicate products within a combo | N-U54-042 |
| VDR-U54-C095 | PROD-COMBO-ITEM-MODEL | product/models/product_combo_item.py:7 | class ProductComboItem(models.Model) | FACT | Always | — | product.combo.item links a combo to individual product variants | N-U54-043 |
| VDR-U54-C096 | PROD-COMBO-ITEM-DOMAIN | product/models/product_combo_item.py:17 | `domain=[('type', '!=', 'combo')],` | FACT | Always | — | product_id on combo item restricted by domain to non-combo product types | N-U54-043 |
| VDR-U54-C097 | PROD-COMBO-ITEM-EXTRA | product/models/product_combo_item.py:28 | `extra_price = fields.Float(string="Extra Price", min_display_digits='Product Price', default=0.0)` | FACT | Always | — | extra_price float on combo item for optional upsell surcharge; defaults to 0 | N-U54-043 |
| VDR-U54-C098 | PROD-COMBO-ITEM-NO-COMBO | product/models/product_combo_item.py:30 | @api.constrains('product_id') | FACT | Always | — | Constraint blocks adding a combo-type product as a combo item | N-U54-043 |
| VDR-U54-C099 | PROD-PRICELIST-ORDER | product/models/product_pricelist.py:14 | `_order = "sequence, id, name"` | FACT | Always | — | Pricelist records ordered sequence, id, name | N-U54-044 |
| VDR-U54-C100 | PROD-PRICELIST-MAIL | product/models/product_pricelist.py:12 | `_inherit = ['mail.thread', 'mail.activity.mixin']` | FACT | Always | — | Pricelist inherits mail.thread and mail.activity.mixin for chatter and activities | N-U54-044 |
| VDR-U54-C101 | PROD-PRICELIST-COUNTRY-GROUP | product/models/product_pricelist.py:49 | country_group_ids = fields.Many2many | FACT | Always | — | Pricelist linked to country groups for geographic segmentation | N-U54-044 |
| VDR-U54-C102 | PROD-PRICELIST-DISPLAY-NAME | product/models/product_pricelist.py:68 | `pricelist.display_name = f'{pricelist_name} ({pricelist.currency_id.name})'` | FACT | Always | — | display_name shows pricelist name followed by currency code in parentheses | N-U54-044 |
| VDR-U54-C103 | PROD-PRICELIST-DELETE-GUARD | product/models/product_pricelist.py:393 | @api.ondelete(at_uninstall=False) | FACT | unlink | — | Cannot delete a pricelist that is used as base in another pricelist's rules | N-U54-045 |
| VDR-U54-C104 | PROD-PRICELIST-PARTNER-RESOLVE | product/models/product_pricelist.py:334 | def _get_partner_pricelist_multi | FACT | Always | — | Resolution order: specific property → country group → config param pricelist_{company_id} → first active | N-U54-045 |
| VDR-U54-C105 | PROD-PRICELIST-PRICE-RULE | product/models/product_pricelist.py:169 | def _compute_price_rule | FACT | Always | — | _compute_price_rule returns {product_id: (price, rule_id)}; first applicable rule wins | N-U54-046 |
| VDR-U54-C106 | PROD-PRICELIST-DOMAIN | product/models/product_pricelist.py:248 | `def _get_applicable_rules_domain(self, products, date, **kwargs):` | FACT | Always | — | Applicable rules domain includes pricelist_id, category parent_of, product, variant, and date range filters | N-U54-046 |
| VDR-U54-C107 | PROD-PRICELIST-FEATURE-GATE | product/models/product_pricelist.py:348 | if not self.env['res.groups']._is_feature_enabled | FACT | _get_partner_pricelist_multi | — | Pricelist partner resolution short-circuits with empty result if pricelist feature group disabled | N-U54-047 |
| VDR-U54-C108 | PROD-PLITEM-APPLIED-ON | product/models/product_pricelist_item.py:51 | applied_on = fields.Selection | FACT | Always | — | Four scope levels for pricelist rules; sorted descending by applied_on (0_ most specific) | N-U54-048 |
| VDR-U54-C109 | PROD-PLITEM-COMPUTE-PRICE | product/models/product_pricelist_item.py:106 | compute_price = fields.Selection | FACT | Always | — | Three price computation modes: percentage, formula, fixed | N-U54-048 |
| VDR-U54-C110 | PROD-PLITEM-BASE | product/models/product_pricelist_item.py:91 | base = fields.Selection | FACT | Always | — | Base price reference: list_price, cost (standard_price), or another pricelist | N-U54-048 |
| VDR-U54-C111 | PROD-PLITEM-FORMULA-MARGIN | product/models/product_pricelist_item.py:145 | price_min_margin = fields.Float | FACT | Always | — | Formula mode supports min/max margin constraints; min must be lower than max | N-U54-049 |
| VDR-U54-C112 | PROD-PLITEM-APPLICABLE | product/models/product_pricelist_item.py:526 | `def _is_applicable_for(self, product, qty_in_product_uom):` | FACT | Always | — | _is_applicable_for checks min_quantity, category (parent_path), product template, and variant match | N-U54-049 |
| VDR-U54-C113 | PROD-PLITEM-FORMULA-COMPUTE | product/models/product_pricelist_item.py:606 | elif self.compute_price == 'formula | FACT | _compute_price formula | — | Formula applies discount for non-cost base and negated markup for cost base | N-U54-049 |
| VDR-U54-C114 | PROD-PLITEM-RECURSION | product/models/product_pricelist_item.py:322 | def _check_pricelist_recursion(self) | FACT | constrains | — | DFS recursion check with memoization (seen set) on (from_pl, to_pl) pairs | N-U54-050 |
| VDR-U54-C115 | PROD-PLITEM-CREATE-SYNC | product/models/product_pricelist_item.py:479 | @api.model_create_multi | FACT | create() | — | create() auto-infers applied_on from presence of product_id/product_tmpl_id/categ_id | N-U54-050 |
| VDR-U54-C116 | PROD-SUPPLIERINFO-ORDER | product/models/product_supplierinfo.py:11 | `_order = 'sequence, min_qty DESC, price, id'` | FACT | Always | — | Supplier info ordered by sequence, then by min_qty descending, then price | N-U54-051 |
| VDR-U54-C117 | PROD-SUPPLIERINFO-VENDOR-FIELDS | product/models/product_supplierinfo.py:18 | 'Vendor Product Name | FACT | Always | — | Vendor-specific name and code override internal ones on purchase documents | N-U54-051 |
| VDR-U54-C118 | PROD-SUPPLIERINFO-DELAY | product/models/product_supplierinfo.py:52 | 'Lead Time', default=1, required=True | FACT | Always | — | delay is the number of days between purchase order confirmation and goods receipt; used by scheduler | N-U54-052 |
| VDR-U54-C119 | PROD-SUPPLIERINFO-DISCOUNT | product/models/product_supplierinfo.py:54 | discount = fields.Float | FACT | Always | — | Supplier line has a percentage discount field | N-U54-052 |
| VDR-U54-C120 | PROD-SUPPLIERINFO-DISCOUNTED | product/models/product_supplierinfo.py:71 | `rec.price_discounted = rec.product_uom_id._compute_price(rec.price, product_uom) * (1 - rec.discount / 100)` | FACT | _compute_price_discounted | — | price_discounted converts UoM then applies discount factor | N-U54-052 |
| VDR-U54-C121 | PROD-SUPPLIERINFO-FILTER | product/models/product_supplierinfo.py:118 | `def _get_filtered_supplier(self, company_id, product_id, params=False):` | FACT | Always | — | Filters by company (or no company) and active partner; optionally by product_id variant | N-U54-052 |
| VDR-U54-C122 | PROD-DOC-INHERITS | product/models/product_document.py:11 | _inherits = | FACT | Always | — | product.document delegates all attachment fields to ir.attachment via _inherits | N-U54-053 |
| VDR-U54-C123 | PROD-DOC-CASCADE | product/models/product_document.py:16 | ir_attachment_id = fields.Many2one | FACT | Always | — | Deleting an ir.attachment cascades to delete the product.document | N-U54-053 |
| VDR-U54-C124 | PROD-DOC-UNLINK | product/models/product_document.py:57 | def unlink(self) | FACT | unlink() | — | Deleting a product.document also deletes its underlying ir.attachment | N-U54-053 |
| VDR-U54-C125 | PROD-DOC-URL-CHECK | product/models/product_document.py:27 | for attachment in self | FACT | onchange | — | URL validation accepts only https, http, or ftp schemes | N-U54-053 |
| VDR-U54-C126 | PROD-DOC-COPY | product/models/product_document.py:44 | `def copy_data(self, default=None):` | FACT | copy | — | copy_data copies ir.attachment separately with context no_document=True and disable_product_documents_creation=True | N-U54-053 |
| VDR-U54-C127 | PAY-CAPTURE-WIZ-CAPTURED-AMT | payment/wizards/payment_capture_wizard.py:49 | full_capture_txs | FACT | _compute_captured_amount | — | captured_amount includes fully-done txs with no children plus done partial-capture children | N-U54-034 |
| VDR-U54-C128 | PAY-CAPTURE-WIZ-DRAFT-CHILDREN | payment/wizards/payment_capture_wizard.py:96 | def _compute_has_draft_children(self) | FACT | Always | — | has_draft_children flag detects in-flight child transactions in draft state | N-U54-035 |
| VDR-U54-C129 | PAY-TX-POST-PROCESS-BASIC | payment/models/payment_transaction.py:1112 | def _post_process(self) | FACT | Always | — | Base _post_process only marks the transaction as post-processed; modules override for document creation | N-U54-031 |
| VDR-U54-C130 | PROD-PRICELIST-MULTI-COMPUTE | product/models/product_pricelist.py:273 | `def _compute_price_rule_multi(self, products, quantity, uom=None, date=False, **kwargs):` | FACT | Always | — | _compute_price_rule_multi computes prices across all pricelists for multiple products; returns nested dict | N-U54-046 |
