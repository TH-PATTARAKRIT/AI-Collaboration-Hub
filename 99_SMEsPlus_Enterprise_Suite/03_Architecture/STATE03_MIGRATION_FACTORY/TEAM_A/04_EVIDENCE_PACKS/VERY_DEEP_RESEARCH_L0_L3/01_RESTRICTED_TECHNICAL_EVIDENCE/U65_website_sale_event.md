# U65 — Website Sale, Event & Mass Mailing — Restricted Technical Evidence
**Pack:** VERY_DEEP_RESEARCH_L0_L3 | **Unit:** U65 | **Modules:** 18 | **Prepared:** 2026-10-02
**Source root:** odoo-19.0.post20260921/odoo/addons

---

## CAP-U65-01 — Website Sale Product Catalog

### Overview
Products appear in the shop only when published. The `is_published` Boolean (inherited from the multi-website publish mixin) gates shop visibility. `_get_combination_info` assembles variant price data, applying the active pricelist. Products hidden from public view are excluded via domain filtering. The sequence integer controls grid sort order.

### Key findings

**F01-01** `ProductTemplate` in `website_sale` inherits `website.published.multi.mixin`, making `is_published` the primary visibility toggle. When `is_published` becomes True, `_compute_publish_date` stamps the current datetime on `publish_date` (line 210-213).

**F01-02** The shop domain filters out unpublished products for non-internal users: `domain &= Domain('is_published', '=', True)` is applied at line 287 when `not self.env.user._is_internal()`.

**F01-03** `_get_combination_info` (line 471) resolves the matching variant, calls `_get_additionnal_combination_info`, and returns a dict including `price`, `list_price`, `has_discounted_price` and optional `product_tracking_info`.

**F01-04** Inside `_get_additionnal_combination_info` (line 584), `pricelist._get_product_price_rule` computes the price and rule. If `_show_discount_on_shop` returns True for the rule, a pre-discount price is also computed.

**F01-05** `_is_add_to_cart_allowed` (line 142) returns False if `not self.active or not self.website_published`. Admin users bypass this check. The method also verifies the product passes the website product domain and that `prevent_zero_price_sale` is not violated.

**F01-06** `website_sequence` (line 103) is an indexed Integer that controls grid display order; new products get the current maximum + 5.

**F01-07** `public_categ_ids` (line 110) is a Many2many to `product.public.category`. Setting categories auto-sets `website_published = True` (via onchange at product_product.py line 153).

**F01-08** `compare_list_price` (line 158 in product_template) is a Monetary field that shows a strikethrough price; it is suppressed when a pricelist is active.

**F01-09** `_show_discount_on_shop` (product_pricelist_item.py line 9) returns True for percentage-rule items and for formula items with a positive `price_discount` based on `list_price` or another pricelist — enabling strikethrough display on the shop.

**F01-10** `website_size_x` and `website_size_y` (product_template.py lines 100-101) define the grid cell span of a product tile in the shop layout.

---

## CAP-U65-02 — Website Sale Cart and Checkout

### Overview
The cart is a draft sale order stored in the HTTP session. `add_to_cart` fetches or creates the cart order, validates the product, and calls `_cart_add` on the order model. The checkout step (`/shop/checkout`) validates the order state, resolves delivery methods, and renders the checkout page. `_check_cart` enforces draft state and non-empty line requirement before any checkout step proceeds.

### Key findings

**F02-01** `add_to_cart` (cart.py line 83) resolves or creates the cart via `request.cart or request.website._create_cart()`. Integer cast enforces no float quantities in eCommerce by default.

**F02-02** `_cart_add` (sale_order.py line 347) checks for an existing matching line via `_cart_find_product_line`. If found, quantity is incremented; if not, `_create_new_cart_line` is called.

**F02-03** `update_cart` (cart.py line 317) calls `_cart_update_line_quantity` with a new absolute quantity, then returns a JSON payload including updated cart totals and line data.

**F02-04** `shop_checkout` (main.py line 1038) stores `sale_last_order_id` in the session, calls `_check_cart_and_addresses`, resolves available delivery methods, sets the preferred one if needed, and renders the checkout template.

**F02-05** `_check_cart` (main.py line 1740) verifies the order exists and is in `draft` state, then verifies `order_line` is non-empty. Non-compliant carts are redirected to the shop or cart page.

**F02-06** `_get_shop_payment_values` (main.py line 1562) merges checkout page values with payment form values, setting `transaction_route` to `/shop/payment/transaction/{order.id}` and `landing_route` to `/shop/payment/validate`.

**F02-07** `shop_payment` (main.py line 1618) calls `_check_cart_and_addresses`, then `_recompute_cart`, then renders the payment page. If errors exist, payment method options are suppressed.

**F02-08** `is_abandoned_cart` (sale_order.py line 46) is a computed Boolean that is True when the order is draft, linked to a website, older than `cart_abandoned_delay` hours, and has a non-public partner.

**F02-09** `_show_in_cart` (sale_order_line.py line 80) returns False for delivery lines, display-only lines, and combo item lines, preventing them from appearing in the cart display.

---

## CAP-U65-03 — Website Sale Payment Integration

### Overview
Payment is initiated via `/shop/payment/transaction/{order_id}` which creates a draft `payment.transaction`. The order row is locked with `FOR NO KEY UPDATE NOWAIT` to prevent concurrent payments. Token reuse is suppressed during express checkout. After the provider callback, `/shop/payment/validate` either auto-confirms zero-amount orders or verifies transaction state.

### Key findings

**F03-01** `shop_payment_transaction` (payment.py line 25) acquires a `FOR NO KEY UPDATE NOWAIT` row-level lock (line 44) to prevent race conditions from concurrent payment attempts.

**F03-02** On `LockNotAvailable`, the controller raises `UserError("Payment is already being processed.")` (payment.py line 51), providing a safe concurrent payment error.

**F03-03** The transaction is created with `sale_order_ids: [Command.set([order_id])]` (payment.py line 73), linking the order to the transaction.

**F03-04** When `flow == 'token'`, `delay_token_charge=True` is set in the context (line 72) and `tx_sudo._charge_with_token()` is called after validation, enabling asynchronous token charge.

**F03-05** `PaymentToken._get_available_tokens` (payment_token.py line 8) returns an empty recordset when `is_express_checkout=True`, suppressing token reuse in express checkout flows.

**F03-06** `shop_payment_validate` (main.py line 1645) falls back to `sale_last_order_id` if `sale_order_id` is missing from the session, protecting against premature session expiry after provider redirect.

**F03-07** For zero-amount orders with no transaction, `shop_payment_validate` (line 1679) calls `order_sudo._check_cart_is_ready_to_be_paid()` then `order_sudo._validate_order()` to auto-confirm without a payment step.

**F03-08** After payment validation, `request.website.sale_reset()` clears the cart session context, then the user is redirected to `/shop/confirmation` (main.py line 1683).

---

## CAP-U65-04 — Website Sale Order → Sale Order

### Overview
A website cart is a `sale.order` in `draft` state linked to `website_id`. On confirm, `action_confirm` assigns a salesman as SUPERUSER before delegating to the core sale confirm. For zero-amount carts, `_validate_order` triggers `action_confirm` directly. On confirm, stock rules launch procurement.

### Key findings

**F04-01** `sale.order` in `website_sale` gets `website_id = fields.Many2one` (line 24), which marks it as an eCommerce cart. The `create` method (line 170) copies company from the website when none is specified.

**F04-02** `action_confirm` (sale_order.py line 249) filters for `website_id` and, when running as superuser, re-computes the salesman assignment before delegating to the parent confirm.

**F04-03** `_validate_order` in `sale` (sale/models/sale_order.py line 1295) calls `self.with_context(send_email=True).action_confirm()`, triggering the confirmation email.

**F04-04** On `action_confirm`, `sale_stock` calls `self.order_line._action_launch_stock_rule()` (sale_stock/models/sale_order.py line 214) to create procurement orders and stock moves.

**F04-05** `_check_cart_is_ready_to_be_paid` (sale_order.py line 937) is called before creating the payment transaction to ensure the cart is fully valid (addresses confirmed, no errors).

**F04-06** `_compute_abandoned_cart` (sale_order.py line 78) marks a draft website order as abandoned when `date_order` precedes the configured abandonment delay and the partner is not the public user.

---

## CAP-U65-05 — Website Sale Extension Modules

### website_sale_autocomplete
**F05-01** Adds `google_places_api_key = fields.Char` to the website model (website_sale_autocomplete/models/website.py line 9), stored per website.

**F05-02** `WebsiteSaleAutoCompleteController._get_api_key` (controllers/main.py line 6) returns `get_current_website().sudo().google_places_api_key` for non-employee requests, falling back to the parent key for employee sessions.

**F05-03** `has_google_places_api_key` (models/website.py line 13) returns `bool(self.sudo().google_places_api_key)`, providing a safe check without exposing the raw key to views.

### website_sale_collect
**F05-04** `StockWarehouse.opening_hours` (models/stock_warehouse.py line 10) links warehouses to a `resource.calendar`, enabling pickup location display of opening hours.

**F05-05** `SaleOrder._compute_warehouse_id` (models/sale_order.py line 13) overrides the parent to keep the warehouse fixed from `pickup_location_data` when the carrier type is `in_store`, preventing recomputation from washing out user-selected pickup points.

**F05-06** `_get_free_qty` (website_sale_stock/models/sale_order.py line 85) falls through to `product.free_qty` scoped to the shop warehouse for non-collect orders, while collect orders check all in-store warehouses before a delivery method is set.

### website_sale_gelato
**F05-07** `ProductTemplate._check_print_images_are_set_before_publishing` (models/product_template.py line 9) raises `ValidationError` if a Gelato product is published without all print images defined, blocking premature publishing.

**F05-08** `action_create_product_variants_from_gelato_template` (models/product_template.py line 22) unpublishes the product whenever a Gelato sync adds new print images, forcing manual review before republishing.

**F05-09** `SaleOrder._verify_updated_quantity` (models/sale_order.py line 9) raises an error when a cart already contains a non-Gelato storable product and the new product has a `gelato_product_uid`, as Gelato products require separate fulfilment.

### website_sale_loyalty
**F05-10** `LoyaltyProgram.ecommerce_ok = fields.Boolean` (models/loyalty_program.py line 11, default True) gates whether a loyalty or coupon program is available on the website frontend.

**F05-11** `_try_pending_coupon` (models/sale_order.py line 43) reads `pending_coupon_code` from the HTTP session and auto-applies it to the cart when it exists, enabling URL-shared coupon codes to activate on first cart interaction.

**F05-12** `_auto_apply_rewards` (models/sale_order.py line 64) iterates claimable rewards and auto-claims them when the program has exactly one reward and that reward is not multi-product.

### website_sale_mrp
**F05-13** `_get_unavailable_quantity_from_kits` (models/sale_order.py line 12) explodes phantom bill-of-materials to compute how much component stock is already consumed by other kit lines in the cart, enabling correct availability display for kit products.

**F05-14** Kit explode uses `mrp.bom._bom_find` with `bom_type='phantom'` (models/sale_order.py line 26) to locate the phantom BoM, then calls `kit_bom.explode` to get component quantities per kit unit.

### website_sale_slides
**F05-15** `slide.channel.enroll` gains the `payment` selection value (models/slide_channel.py line 15), and a `product_id` Many2many to `product.product` filtered to `service_tracking = 'course'` provides the purchasable course product.

**F05-16** `SaleOrder._action_confirm` (models/sale_order.py line 8) searches for `slide.channel` records whose `product_id` matches confirmed order lines and calls `_action_add_members` for each partner, granting course access on purchase.

**F05-17** `_verify_updated_quantity` in `website_sale_slides` (models/sale_order.py line 34) returns a maximum of 1 for course products, preventing multiple enrolments via the cart.

### website_sale_stock
**F05-18** `allow_out_of_stock_order = fields.Boolean` (models/product_template.py line 16, default True) controls whether purchases are blocked when virtual stock reaches zero.

**F05-19** `_is_sold_out` (models/product_template.py line 20) returns True only when `is_storable` is True, `allow_out_of_stock_order` is False, and all variants report sold out.

**F05-20** `SaleOrderLine._check_availability` (models/sale_order_line.py line 39) compares cart quantity to `free_qty` via `_get_cart_and_free_qty`; if cart exceeds available, it calls `_set_shop_warning_stock` and returns False.

---

## CAP-U65-06 — Website Event Modules

### website_event
**F06-01** `event.event.website_published = fields.Boolean(tracking=True)` (models/event_event.py line 52) is the primary visibility toggle tracked in the chatter.

**F06-02** `/event/<event>/register` route (controllers/main.py line 212) renders the registration form via `_prepare_event_register_values`, passing slot and ticket data.

**F06-03** `registration_confirm` (controllers/main.py line 449) processes posted form data, calls `_verify_seats_availability`, creates attendee records, then redirects to the registration success page.

**F06-04** `_prepare_registration_new_values` (controllers/main.py line 286) performs a double-check on seat availability and ticket-order limits before presenting the attendee details form.

**F06-05** `event.registration.visitor_id = fields.Many2one('website.visitor')` (models/event_registration.py line 9) links a web registration to the anonymous or logged-in visitor record for tracking.

### website_event_booth
**F06-06** `event.event.booth_menu = fields.Boolean` (models/event_event.py line 12), computed from the event type or derived from `website_menu`, controls whether a booth sub-menu appears on the event website page.

**F06-07** `/event/<event>/booth` route (controllers/event_booth.py line 17) renders the booth registration page; it raises `Forbidden` if the user cannot read the event, enforcing the event's own access rules.

**F06-08** `/event/<event>/booth/register` (controllers/event_booth.py line 26) collects multiple booth IDs from the form (via `getlist`) and redirects to the booth contact form, passing the full booth selection.

### website_event_booth_sale
**F06-09** `ProductTemplate._get_product_types_allow_zero_price` (models/product_template.py line 11) appends `"event_booth"` to the list, allowing zero-price booth products to be added to the cart without triggering `prevent_zero_price_sale` protection.

**F06-10** `SaleOrder._verify_updated_quantity` (models/sale_order.py line 24) raises an error and returns quantity 1 when an `event_booth`-tracked product is added with quantity > 1, since each booth occupies exactly one sale order line.

**F06-11** `SaleOrderLine._compute_name_short` (models/sale_order_line.py line 9) sets the short name for booth lines to the event name (from `event_booth_pending_ids.event_id.name`), improving cart display clarity.

### website_event_crm
**F06-12** `EventRegistration._get_lead_values` (models/event_registration.py line 29) extends the base lead generation dict to add `visitor_ids` from the registration's visitor and `lang_id` from the visitor's language, enriching CRM leads created from event registrations.

**F06-13** `_get_lead_description_registration` (models/event_registration.py line 11) appends question-and-answer data from the website registration form to the CRM lead description.

### website_event_sale
**F06-14** `_create_attendees_from_registration_post` (controllers/main.py line 22) detects ticket-based registrations. When at least one ticket is paid, it creates or retrieves the cart and calls `order_sudo._cart_add` for each slot-ticket combination.

**F06-15** When all chosen tickets are free and no cart exists (controllers/main.py line 33), the sale flow is bypassed and attendees are created directly without a sale order.

**F06-16** `registration_confirm` override (controllers/main.py line 63) auto-confirms zero-value ticket orders (`action_confirm`) and resets the cart, redirecting to `/shop/confirmation`; paid ticket orders are redirected to `/shop/checkout?try_skip_step=true`.

**F06-17** `_validate_transaction_for_order` (controllers/payment.py line 10) checks seat availability at payment time, raising `ValidationError` if tickets are no longer available, preventing overselling.

**F06-18** `SaleOrder._cart_find_product_line` (models/sale_order.py line 11) additionally filters by `event_slot_id` and `event_ticket_id`, ensuring that two registrations for different slots do not share a single cart line.

**F06-19** `_verify_updated_quantity` in `website_event_sale` (models/sale_order.py line 20) enforces per-ticket seat limits during cart update, blocking increases beyond available seats.

### website_event_track_quiz
**F06-20** `/event_track/quiz/submit` (controllers/event_track_quiz.py line 17) writes `quiz_completed=True` and `quiz_points` to the `event.track.visitor` record, returning per-question correctness feedback.

**F06-21** `/event_track/quiz/reset` (controllers/event_track_quiz.py line 35) allows quiz re-attempt only if `quiz_id.repeatable` is True or the user has `event.group_event_manager`, preventing unauthorized retries.

---

## CAP-U65-07 — Website Mass Mailing

**F07-01** `/website_mass_mailing/is_subscriber` (controllers/main.py line 14) looks up `mailing.subscription` for the list and contact field value; it returns `{'is_subscriber': bool, 'value': value}`, used by the subscription block snippet to show the correct button state.

**F07-02** `/website_mass_mailing/subscribe` (controllers/main.py line 37) validates an reCAPTCHA token before proceeding; on failure it returns a toast error without creating a subscription.

**F07-03** `subscribe_to_newsletter` (controllers/main.py line 54) searches for an existing subscription by list and contact field value. If absent, it creates a `mailing.contact` and `mailing.subscription`; if present but opted out, it flips `opt_out = False`. The email or mobile value is stored in the session for subsequent page loads.

**F07-04** `_get_value` (controllers/main.py line 24) retrieves the logged-in user's email or the session-stored `mass_mailing_email`, providing a pre-filled subscription form without requiring the user to type their address again.

**F07-05** The unsubscribe flow is handled by the base `mass_mailing` controller at `/mailing/<id>/unsubscribe_oneclick` (mass_mailing/controllers/main.py line 100), which calls `mailing_unsubscribe` and sets `opt_out=True` on the subscription.

---

## CAP-U65-08 — Test Modules

**F08-01** `test_mass_mailing` (manifest) depends on `mass_mailing`, `mass_mailing_sms`, `sms_twilio`, `test_mail`, and `test_mail_sms`; it provides performance and integration tests for mailing author assignment, link tracking, and blacklist behaviour.

**F08-02** `TestMassMailing.test_mailing_author` (tests/test_mailing.py line 14) verifies that the mailing's `user_id` is used as the author for outgoing mail records when sent as a different user.

**F08-03** `test_website_modules` (manifest) depends on `website_event_sale`, `website_sale_comparison`, `website_livechat`, `theme_default`, and several website add-ons; `TestWebEditorController.test_modify_image` (tests/test_controllers.py line 13) validates that image attachment modification through the website editor respects the user's access level.

**F08-04** `test_website_slides_full` (manifest) depends on `website_sale_slides`, `website_slides_forum`, `website_slides_survey` and provides a full end-to-end UI test of the certification purchase and survey completion flow.

---

## Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U65-C001 | WSALE.catalog.published | website_sale/models/product_template.py:210 | @api.depends('is_published') | FACT | always | — | When is_published becomes True, publish_date is set to the current datetime by _compute_publish_date | N-U65-001 |
| VDR-U65-C002 | WSALE.catalog.domain | website_sale/models/product_template.py:287 | domain &= Domain('is_published', '=', True) | FACT | non-internal user | — | Shop accessory product domain appends is_published=True filter for non-internal users, hiding unpublished products | N-U65-001 |
| VDR-U65-C003 | WSALE.catalog.combination | website_sale/models/product_template.py:471 | def _get_combination_info | FACT | always | — | _get_combination_info returns a dict with price, list_price, has_discounted_price, and optional Google Analytics tracking info for the current website pricelist | N-U65-002 |
| VDR-U65-C004 | WSALE.catalog.pricelist | website_sale/models/product_template.py:595 | :param website | FACT | always | — | _get_additionnal_combination_info calls pricelist._get_product_price_rule to compute the effective price and the matched rule id | N-U65-002 |
| VDR-U65-C005 | WSALE.catalog.discount | website_sale/models/product_pricelist_item.py:9 | def _show_discount_on_shop | FACT | always | — | Pricelist items show a strikethrough shop discount when compute_price is percentage or formula with a positive price_discount based on list_price or another pricelist | N-U65-002 |
| VDR-U65-C006 | WSALE.catalog.add_allowed | website_sale/models/product_product.py:142 | def _is_add_to_cart_allowed | FACT | always | — | _is_add_to_cart_allowed returns False when active is False or website_published is False; admins bypass the check | N-U65-001 |
| VDR-U65-C007 | WSALE.catalog.zero_price | website_sale/models/product_product.py:150 | return False | FACT | always | — | _is_add_to_cart_allowed also returns False when prevent_zero_price_sale is enabled and contextual price is zero | N-U65-001 |
| VDR-U65-C008 | WSALE.catalog.sequence | website_sale/models/product_template.py:103 | website_sequence = fields.Integer | FACT | always | — | website_sequence is an indexed Integer defaulting to current max+5 that determines the sort order in the eCommerce grid | N-U65-003 |
| VDR-U65-C009 | WSALE.catalog.category | website_sale/models/product_template.py:110 | public_categ_ids = fields.Many2many | FACT | always | — | public_categ_ids is a Many2many to product.public.category; setting a category auto-publishes the product via onchange | N-U65-003 |
| VDR-U65-C010 | WSALE.catalog.compare | website_sale/models/product_template.py:158 | compare_list_price = fields.Monetary | FACT | no pricelist | — | compare_list_price stores a strikethrough comparison price on the product; it is suppressed when a pricelist is active | N-U65-002 |
| VDR-U65-C011 | WSALE.cart.create | website_sale/controllers/cart.py:115 | request.cart or request.website._create_cart | FACT | always | — | add_to_cart resolves an existing session cart or creates a new one via _create_cart before any product validation | N-U65-004 |
| VDR-U65-C012 | WSALE.cart.add | website_sale/models/sale_order.py:347 | def _cart_add(self | FACT | always | — | _cart_add checks for an existing matching line; if found it increments quantity, otherwise creates a new order line | N-U65-004 |
| VDR-U65-C013 | WSALE.cart.update | website_sale/controllers/cart.py:317 | def update_cart | FACT | always | — | update_cart delegates to _cart_update_line_quantity with the new absolute quantity and returns JSON cart state | N-U65-004 |
| VDR-U65-C014 | WSALE.cart.show_in_cart | website_sale/models/sale_order_line.py:80 | def _show_in_cart | FACT | always | — | Delivery lines, display-type lines, and combo item lines are excluded from the cart view by _show_in_cart returning False | N-U65-004 |
| VDR-U65-C015 | WSALE.checkout.route | website_sale/controllers/main.py:1038 | def shop_checkout | FACT | always | — | shop_checkout stores sale_last_order_id in the session, resolves delivery methods, and optionally skips to the next step when no delivery is needed | N-U65-005 |
| VDR-U65-C016 | WSALE.checkout.validate | website_sale/controllers/main.py:1740 | def _check_cart(self, order_sudo) | FACT | always | — | _check_cart returns a redirect if the order does not exist, is not in draft state, or has no order lines | N-U65-005 |
| VDR-U65-C017 | WSALE.checkout.payment_vals | website_sale/controllers/main.py:1562 | def _get_shop_payment_values | FACT | always | — | _get_shop_payment_values sets transaction_route to /shop/payment/transaction/{order.id} and landing_route to /shop/payment/validate | N-U65-006 |
| VDR-U65-C018 | WSALE.checkout.payment_page | website_sale/controllers/main.py:1618 | """ Payment step. | FACT | always | — | shop_payment recomputes the cart, suppresses payment method display when errors are present, and renders website_sale.payment | N-U65-006 |
| VDR-U65-C019 | WSALE.checkout.abandoned | website_sale/models/sale_order.py:46 | is_abandoned_cart = fields.Boolean | FACT | draft website orders | — | is_abandoned_cart is True for draft website orders older than cart_abandoned_delay hours with a non-public partner and at least one order line | N-U65-005 |
| VDR-U65-C020 | WSALE.payment.lock | website_sale/controllers/payment.py:44 | FOR NO KEY UPDATE NOWAIT | FACT | always | — | shop_payment_transaction acquires a FOR NO KEY UPDATE NOWAIT row lock on the sale.order row to prevent concurrent payment races | N-U65-006 |
| VDR-U65-C021 | WSALE.payment.lock_error | website_sale/controllers/payment.py:51 | if order_sudo.state == "cancel | FACT | concurrent request | — | LockNotAvailable during the row lock raises UserError with message "Payment is already being processed." | N-U65-006 |
| VDR-U65-C022 | WSALE.payment.tx_create | website_sale/controllers/payment.py:73 | request.update_context | FACT | always | — | The payment transaction is created with sale_order_ids linking the order, allowing downstream modules to identify the origin order | N-U65-006 |
| VDR-U65-C023 | WSALE.payment.token_delay | website_sale/controllers/payment.py:72 | if delay_token_charge | FACT | token flow | — | When flow is token, delay_token_charge context is set and _charge_with_token is called after order validation, not at transaction creation | N-U65-006 |
| VDR-U65-C024 | WSALE.payment.express_token | website_sale/models/payment_token.py:8 | def _get_available_tokens | FACT | express checkout | — | _get_available_tokens returns an empty recordset when is_express_checkout is True, suppressing saved-token reuse in express checkout | N-U65-006 |
| VDR-U65-C025 | WSALE.payment.validate | website_sale/controllers/main.py:1645 | def shop_payment_validate | FACT | always | — | shop_payment_validate retrieves the order from sale_last_order_id when no sale_order_id is passed, protecting against session key clearing | N-U65-006 |
| VDR-U65-C026 | WSALE.payment.zero_amount | website_sale/controllers/main.py:1679 | order_sudo._validate_order() | FACT | free orders | — | For zero-amount orders with no transaction and state not sale, shop_payment_validate calls _validate_order to auto-confirm without a payment provider | N-U65-006 |
| VDR-U65-C027 | WSALE.payment.session_reset | website_sale/controllers/main.py:1683 | if tx_sudo and tx_sudo.state == 'draft | FACT | always | — | After validation, sale_reset clears the cart session and the user is redirected to /shop/confirmation | N-U65-006 |
| VDR-U65-C028 | WSALE.order.website_id | website_sale/models/sale_order.py:24 | website_id = fields.Many2one | FACT | always | — | sale.order gets a website_id Many2one that marks it as a website cart; company is copied from the website on create when not otherwise specified | N-U65-007 |
| VDR-U65-C029 | WSALE.order.confirm | website_sale/models/sale_order.py:249 | def action_confirm(self) | FACT | always | — | action_confirm in website_sale filters website orders and recomputes the salesman as SUPERUSER before calling the parent confirm | N-U65-007 |
| VDR-U65-C030 | WSALE.order.validate | sale/models/sale_order.py:1295 | def _validate_order(self) | FACT | always | — | _validate_order calls action_confirm with send_email=True context, triggering the confirmation email | N-U65-007 |
| VDR-U65-C031 | WSALE.order.stock | sale_stock/models/sale_order.py:214 | self.order_line._action_launch_stock_rule() | FACT | always | — | On sale order confirmation, sale_stock calls _action_launch_stock_rule to create procurement orders and stock moves | N-U65-007 |
| VDR-U65-C032 | WSALE.ext.autocomplete.key | website_sale_autocomplete/models/website.py:9 | google_places_api_key = fields.Char | FACT | always | — | website_sale_autocomplete adds google_places_api_key as a Char field on the website model, stored per website | N-U65-008 |
| VDR-U65-C033 | WSALE.ext.autocomplete.ctrl | website_sale_autocomplete/controllers/main.py:6 | def _get_api_key(self, use_employees_key) | FACT | always | — | _get_api_key returns the current website's google_places_api_key for public requests, delegating to parent for internal users | N-U65-008 |
| VDR-U65-C034 | WSALE.ext.autocomplete.check | website_sale_autocomplete/models/website.py:13 | def has_google_places_api_key | FACT | always | — | has_google_places_api_key returns bool of the sudo API key, providing a safe view-accessible Boolean without exposing the raw value | N-U65-008 |
| VDR-U65-C035 | WSALE.ext.collect.hours | website_sale_collect/models/stock_warehouse.py:10 | opening_hours = fields.Many2one | FACT | always | — | StockWarehouse gains opening_hours as a Many2one to resource.calendar, used to render pickup location schedule on the website | N-U65-009 |
| VDR-U65-C036 | WSALE.ext.collect.warehouse | website_sale_collect/models/sale_order.py:13 | def _compute_warehouse_id(self) | FACT | in_store carrier | — | For in_store carrier orders with pickup_location_data set, _compute_warehouse_id fixes the warehouse to the selected pickup point without recomputation | N-U65-009 |
| VDR-U65-C037 | WSALE.ext.collect.fiscal | website_sale_collect/models/sale_order.py:25 | def _compute_fiscal_position_id(self) | FACT | in_store carrier | — | Fiscal position for in-store pickup orders is determined from the warehouse partner address rather than the customer billing address | N-U65-009 |
| VDR-U65-C038 | WSALE.ext.gelato.publish | website_sale_gelato/models/product_template.py:9 | # === CONSTRAINT METHODS === # | FACT | on write | — | Gelato products with missing print images raise ValidationError on publish, blocking shop visibility until images are complete | N-U65-010 |
| VDR-U65-C039 | WSALE.ext.gelato.sync | website_sale_gelato/models/product_template.py:22 | def action_create_product_variants_from_ | FACT | on Gelato sync | — | When a Gelato template sync adds new images, the product is automatically unpublished, requiring manual re-review before going live | N-U65-010 |
| VDR-U65-C040 | WSALE.ext.gelato.mix | website_sale_gelato/models/sale_order.py:9 | def _verify_updated_quantity | FACT | mixed cart | — | Adding a Gelato product to a cart that already has a non-Gelato storable product raises a validation error, enforcing single-fulfillment-type carts | N-U65-010 |
| VDR-U65-C041 | WSALE.ext.loyalty.ok | website_sale_loyalty/models/loyalty_program.py:11 | ecommerce_ok = fields.Boolean | FACT | always | — | LoyaltyProgram gains ecommerce_ok Boolean (default True) controlling whether the program is accessible from the website frontend | N-U65-011 |
| VDR-U65-C042 | WSALE.ext.loyalty.pending | website_sale_loyalty/models/sale_order.py:43 | def _try_pending_coupon(self) | FACT | session has coupon | — | _try_pending_coupon reads pending_coupon_code from the HTTP session and auto-applies it, enabling URL-distributed coupon codes to activate on cart entry | N-U65-011 |
| VDR-U65-C043 | WSALE.ext.loyalty.auto | website_sale_loyalty/models/sale_order.py:64 | def _auto_apply_rewards(self) | FACT | single-reward programs | — | _auto_apply_rewards iterates claimable rewards and claims single-reward non-multi-product rewards automatically | N-U65-011 |
| VDR-U65-C044 | WSALE.ext.mrp.kit_avail | website_sale_mrp/models/sale_order.py:12 | def _get_unavailable_quantity_from_kits | FACT | kit products | — | _get_unavailable_quantity_from_kits uses phantom BoM explosion to compute stock consumed by other kit lines in the cart, correcting availability display | N-U65-012 |
| VDR-U65-C045 | WSALE.ext.mrp.explode | website_sale_mrp/models/sale_order.py:26 | kit_bom = self.env['mrp.bom'].sudo | FACT | phantom BoM | — | Kit availability is computed by calling kit_bom.explode with quantity=1.0 per BoM and aggregating component consumption across all kit lines | N-U65-012 |
| VDR-U65-C046 | WSALE.ext.slides.enroll | website_sale_slides/models/slide_channel.py:15 | enroll = fields.Selection(selection_add= | FACT | always | — | slide.channel gains a payment enrollment option; courses using this option require a linked product_id to be purchasable | N-U65-013 |
| VDR-U65-C047 | WSALE.ext.slides.confirm | website_sale_slides/models/sale_order.py:8 | def _action_confirm(self) | FACT | on confirm | — | On sale order confirmation, _action_confirm finds slide channels whose product_id matches any confirmed line and calls _action_add_members to enrol the buyer | N-U65-013 |
| VDR-U65-C048 | WSALE.ext.slides.qty | website_sale_slides/models/sale_order.py:34 | def _verify_updated_quantity | FACT | course products | — | Course products are limited to quantity 1 per cart line; attempts to increase quantity return 1 with a warning message | N-U65-013 |
| VDR-U65-C049 | WSALE.ext.stock.oos | website_sale_stock/models/product_template.py:16 | allow_out_of_stock_order = fields.Boolean | FACT | always | — | allow_out_of_stock_order (default True) controls whether storable products can be ordered when virtual stock is zero | N-U65-014 |
| VDR-U65-C050 | WSALE.ext.stock.sold_out | website_sale_stock/models/product_template.py:20 | def _is_sold_out(self) | FACT | storable no OOS | — | _is_sold_out returns True only when is_storable is True, allow_out_of_stock_order is False, and all variants report sold out | N-U65-014 |
| VDR-U65-C051 | WSALE.ext.stock.check | website_sale_stock/models/sale_order_line.py:39 | def _check_availability(self) | FACT | storable no OOS | — | _check_availability compares cart quantity to free_qty; on exceeding stock, it sets a shop warning and returns False | N-U65-014 |
| VDR-U65-C052 | WSALE.ext.stock.threshold | website_sale_stock/models/product_template.py:17 | available_threshold = fields.Float | FACT | always | — | available_threshold (default 5.0) is the quantity level below which the stock warning indicator appears on the product page | N-U65-014 |
| VDR-U65-C053 | WEVENT.event.published | website_event/models/event_event.py:52 | website_published = fields.Boolean(tracking=True) | FACT | always | — | event.event.website_published is a tracked Boolean that controls event visibility on the website and in search results | N-U65-015 |
| VDR-U65-C054 | WEVENT.event.register_route | website_event/controllers/main.py:212 | @http.route(['''/event/<model | FACT | always | — | The /event/<event>/register route serves the public registration page, passing slot and ticket availability data to the template | N-U65-015 |
| VDR-U65-C055 | WEVENT.event.seats_check | website_event/controllers/main.py:449 | def registration_confirm(self, event, **post) | FACT | limited seats | — | registration_confirm calls _verify_seats_availability before creating attendee records; insufficient seats redirect back with error code | N-U65-015 |
| VDR-U65-C056 | WEVENT.event.visitor | website_event/models/event_registration.py:9 | visitor_id = fields.Many2one | FACT | always | — | event.registration has visitor_id linking the registration to the anonymous or logged-in website visitor record | N-U65-015 |
| VDR-U65-C057 | WEVENT.event.new_form | website_event/controllers/main.py:286 | def _prepare_registration_new_values | FACT | always | — | _prepare_registration_new_values performs an availability check and a per-order ticket limit check before rendering the attendee details form | N-U65-015 |
| VDR-U65-C058 | WEVENT.booth.menu | website_event_booth/models/event_event.py:12 | booth_menu = fields.Boolean | FACT | always | — | booth_menu is computed from the event type default or from website_menu; it controls display of the booth sub-menu | N-U65-016 |
| VDR-U65-C059 | WEVENT.booth.route | website_event_booth/controllers/event_booth.py:17 | if not event.has_access('read') | FACT | always | — | /event/<event>/booth renders the booth selection page and raises Forbidden if the user cannot read the event | N-U65-016 |
| VDR-U65-C060 | WEVENT.booth.register | website_event_booth/controllers/event_booth.py:26 | @http.route('/event/<model | FACT | always | — | /event/<event>/booth/register collects all selected booth IDs via form.getlist and redirects to the contact registration form | N-U65-016 |
| VDR-U65-C061 | WEVENT.booth_sale.zero | website_event_booth_sale/models/product_template.py:11 | def _get_product_types_allow_zero_price(self) | FACT | always | — | website_event_booth_sale appends event_booth to the zero-price-allowed product types, enabling free booth products in the shop | N-U65-016 |
| VDR-U65-C062 | WEVENT.booth_sale.qty | website_event_booth_sale/models/sale_order.py:24 | def _verify_updated_quantity | FACT | booth products | — | Booth products are hard-capped at quantity 1 per line; attempts to set qty > 1 return 1 with a validation message | N-U65-016 |
| VDR-U65-C063 | WEVENT.booth_sale.name | website_event_booth_sale/models/sale_order_line.py:9 | @api.depends('event_booth_ids') | FACT | booth lines | — | The short name of a booth sale line is set to the event name from the pending booth's event_id, improving cart readability | N-U65-016 |
| VDR-U65-C064 | WEVENT.crm.lead_visitor | website_event_crm/models/event_registration.py:29 | def _get_lead_values(self, rule) | FACT | visitor exists | — | _get_lead_values adds the registration's visitor_id to lead visitor_ids and the visitor's language to lang_id, enriching CRM leads | N-U65-017 |
| VDR-U65-C065 | WEVENT.crm.lead_desc | website_event_crm/models/event_registration.py:11 | def _get_lead_description_registration | FACT | always | — | _get_lead_description_registration appends website form question-and-answer data to the CRM lead description | N-U65-017 |
| VDR-U65-C066 | WEVENT.sale.cart_add | website_event_sale/controllers/main.py:22 | # we have at least | FACT | paid tickets | — | When at least one ticket has an event_ticket_id, the controller creates or retrieves the cart and calls _cart_add for each slot-ticket combination | N-U65-018 |
| VDR-U65-C067 | WEVENT.sale.free_skip | website_event_sale/controllers/main.py:33 | # all chosen tickets | FACT | free tickets, no cart | — | When all selected tickets are free and no cart exists, attendees are created directly without a sale order, bypassing checkout | N-U65-018 |
| VDR-U65-C068 | WEVENT.sale.free_confirm | website_event_sale/controllers/main.py:63 | return super()._create_attendees_from_re | FACT | zero-value tickets | — | For orders containing only zero-price ticket lines, registration_confirm calls action_confirm and redirects to /shop/confirmation without payment | N-U65-018 |
| VDR-U65-C069 | WEVENT.sale.paid_redirect | website_event_sale/controllers/main.py:71 | if not any(line.event_ticket_id | FACT | paid tickets | — | For paid-ticket orders, registration_confirm redirects to /shop/checkout?try_skip_step=true, allowing address skip when already populated | N-U65-018 |
| VDR-U65-C070 | WEVENT.sale.seat_tx | website_event_sale/controllers/payment.py:10 | def _validate_transaction_for_order | FACT | always | — | _validate_transaction_for_order re-checks seat availability at payment transaction creation time, raising ValidationError on oversell | N-U65-018 |
| VDR-U65-C071 | WEVENT.sale.find_line | website_event_sale/models/sale_order.py:11 | def _cart_find_product_line | FACT | ticket lines | — | _cart_find_product_line filters by event_slot_id and event_ticket_id to ensure different slot or ticket combinations use separate cart lines | N-U65-018 |
| VDR-U65-C072 | WEVENT.quiz.submit | website_event_track_quiz/controllers/event_track_quiz.py:17 | def event_track_quiz_submit | FACT | always | — | /event_track/quiz/submit writes quiz_completed=True and the earned points to the event.track.visitor record and returns per-question correctness | N-U65-019 |
| VDR-U65-C073 | WEVENT.quiz.reset | website_event_track_quiz/controllers/event_track_quiz.py:35 | result = | FACT | always | — | Quiz reset is allowed only when quiz_id.repeatable is True or the user holds event.group_event_manager; otherwise Forbidden is raised | N-U65-019 |
| VDR-U65-C074 | WMMAIL.is_subscriber | website_mass_mailing/controllers/main.py:14 | value = self._get_value(subscription_type) | FACT | always | — | /website_mass_mailing/is_subscriber returns is_subscriber and the contact's email or mobile value for the subscription block snippet | N-U65-020 |
| VDR-U65-C075 | WMMAIL.subscribe.captcha | website_mass_mailing/controllers/main.py:37 | def subscribe(self | FACT | always | — | The subscribe route validates a reCAPTCHA token before processing; on failure it returns a toast danger response without creating a subscription | N-U65-020 |
| VDR-U65-C076 | WMMAIL.subscribe.create | website_mass_mailing/controllers/main.py:54 | def subscribe_to_newsletter | FACT | always | — | subscribe_to_newsletter creates a mailing.contact and mailing.subscription if none exists; if the contact has opted out, it flips opt_out to False | N-U65-020 |
| VDR-U65-C077 | WMMAIL.subscribe.session | website_mass_mailing/controllers/main.py:72 | elif subscription.opt_out | FACT | always | — | The subscribed email or mobile is stored in the HTTP session under mass_mailing_email for pre-filling the form on return visits | N-U65-020 |
| VDR-U65-C078 | WMMAIL.prefill | website_mass_mailing/controllers/main.py:24 | def _get_value(self, subscription_type) | FACT | logged in or session | — | _get_value returns the logged-in user's email or the session-cached mass_mailing_email, enabling pre-fill without user re-entry | N-U65-020 |
| VDR-U65-C079 | WMMAIL.unsub | mass_mailing/controllers/main.py:100 | @http.route(['/mailing/<int:mailing_id>/ | FACT | always | — | The base mass_mailing controller provides /mailing/<id>/unsubscribe_oneclick which delegates to mailing_unsubscribe and sets opt_out=True | N-U65-020 |
| VDR-U65-C080 | WTEST.mass_mailing.deps | test_mass_mailing/__manifest__.py:1 | # -*- coding: utf-8 -*- | FACT | always | — | test_mass_mailing depends on mass_mailing, mass_mailing_sms, sms_twilio, test_mail, and test_mail_sms, providing integration and performance tests | N-U65-021 |
| VDR-U65-C081 | WTEST.mass_mailing.author | test_mass_mailing/tests/test_mailing.py:14 | @mute_logger('odoo.addons.mail.models.mail_mail') | FACT | always | — | test_mailing_author verifies that outgoing mail records carry the author from the mailing's user_id when sent on behalf of another user | N-U65-021 |
| VDR-U65-C082 | WTEST.website_modules.deps | test_website_modules/__manifest__.py:1 | # -*- encoding: utf-8 -*- | FACT | always | — | test_website_modules depends on website_event_sale, website_sale_comparison, website_livechat, theme_default and related website modules | N-U65-022 |
| VDR-U65-C083 | WTEST.website_modules.image | test_website_modules/tests/test_controllers.py:13 | class TestWebEditorController | FACT | always | — | test_modify_image validates that image attachment modification through the website editor respects user access level | N-U65-022 |
| VDR-U65-C084 | WTEST.slides_full.deps | test_website_slides_full/__manifest__.py:1 | # -*- coding: utf-8 -*- | FACT | always | — | test_website_slides_full depends on website_sale_slides, website_slides_forum, website_slides_survey and tests the full certification purchase flow | N-U65-023 |
| VDR-U65-C085 | WSALE.checkout.skip | website_sale/controllers/main.py:1071 | checkout_page_values.update | FACT | services only | — | When no deliverable products are in the cart and try_skip_step is true, shop_checkout immediately redirects to the next step | N-U65-005 |
| VDR-U65-C086 | WSALE.payment.check_ready | website_sale/controllers/payment.py:56 | _check_cart_is_ready_to_be_paid | FACT | always | — | shop_payment_transaction calls _check_cart_is_ready_to_be_paid before transaction creation to validate addresses and cart integrity | N-U65-006 |
| VDR-U65-C087 | WSALE.payment.amount_check | website_sale/controllers/payment.py:65 | compare_amounts | FACT | always | — | The controller compares the submitted amount to the order total using currency-aware compare_amounts, raising ValidationError on mismatch to prevent stale cart payments | N-U65-006 |
| VDR-U65-C088 | WSALE.payment.already_paid | website_sale/controllers/payment.py:68 | raise ValidationError | FACT | already paid | — | If amount_paid equals amount_total, UserError is raised with "The cart has already been paid" to prevent double payment | N-U65-006 |
| VDR-U65-C089 | WSALE.order.cart_line | website_sale/models/sale_order.py:403 | def _cart_find_product_line | FACT | always | — | _cart_find_product_line accepts linked_line_id to find lines for optional or combo child products linked to a parent cart line | N-U65-004 |
| VDR-U65-C090 | WSALE.order.uom | website_sale/models/sale_order.py:360 | # Fall back on product | FACT | multi-uom products | — | _cart_add falls back to the product's default UoM when uom_id is not specified or the product does not support multiple UoMs | N-U65-004 |
| VDR-U65-C091 | WEVENT.event.recaptcha | website_event/controllers/main.py:451 | that we have enough | FACT | public route | — | registration_confirm verifies a reCAPTCHA token under key website_event_registration; failed verification redirects with registration_error_code=recaptcha_failed | N-U65-015 |
| VDR-U65-C092 | WEVENT.event.slot | website_event/controllers/main.py:267 | @http.route(['/event/<model | FACT | slotted events | — | /event/<event>/registration/slot/<slot_id>/tickets renders the ticket modal for a specific slot, passing per-slot seat availability | N-U65-015 |
| VDR-U65-C093 | WSALE.ext.stock.free_qty | website_sale_stock/models/sale_order.py:85 | def _get_free_qty(self, product) | FACT | always | — | _get_free_qty returns product.free_qty scoped to the shop warehouse, ensuring availability checks are warehouse-specific | N-U65-014 |
| VDR-U65-C094 | WSALE.ext.stock.warning | website_sale_stock/models/sale_order_line.py:9 | def _set_shop_warning_stock | FACT | over-stock cart | — | _set_shop_warning_stock writes an informational message to shop_warning when the cart quantity exceeds available stock | N-U65-014 |
| VDR-U65-C095 | WSALE.catalog.website_url | website_sale/models/product_product.py:75 | def _compute_product_website_url(self) | FACT | always | — | Each product variant's website_url is computed by appending the variant's attribute value ids to the template's website_url | N-U65-003 |
| VDR-U65-C096 | WEVENT.sale.pricelist_warn | website_event_sale/models/product_pricelist.py:10 | def _onchange_event_sale_warning(self) | OBSERVATION | pricelist item | — | A pricelist item with a positive min. quantity will not be applied to event ticket products, and an onchange warns the user | N-U65-018 |
| VDR-U65-C097 | WSALE.ext.loyalty.disabled | website_sale_loyalty/models/sale_order.py:15 | disabled_auto_rewards = fields.Many2many | FACT | always | — | disabled_auto_rewards is a Many2many of loyalty.reward tracking which auto-rewards have been dismissed for the current order | N-U65-011 |
| VDR-U65-C098 | WEVENT.booth.copy | website_event_booth/models/event_event.py:36 | def copy_event_menus(self, old_events) | FACT | event copy | — | copy_event_menus re-parents booth menu entries under the new event's top-level menu when an event is duplicated | N-U65-016 |
| VDR-U65-C099 | WEVENT.event.success_route | website_event/controllers/main.py:479 | if not visitor | FACT | always | — | /event/<event>/registration/success fetches attendee records filtered by visitor_id to prevent cross-visitor access to registration confirmation data | N-U65-015 |
| VDR-U65-C100 | WSALE.ext.slides.product | website_sale_slides/models/product_template.py:10 | service_tracking | FACT | always | — | website_sale_slides adds a course service tracking option to product.template, allowing course products to be created via the standard product form | N-U65-013 |
| VDR-U65-C101 | WSALE.ext.slides.zero | website_sale_slides/models/product_template.py:21 | return super()._get_product_types_allow_ | FACT | always | — | Course products are added to the zero-price-allowed list, enabling free course products to be added to the cart | N-U65-013 |
| VDR-U65-C102 | WSALE.cart.combo | website_sale/controllers/cart.py:133 | combos_sudo = product.sudo | FACT | combo products | — | For combo products, add_to_cart validates that the number of selected combo items matches the number of available combo choices before proceeding | N-U65-004 |
| VDR-U65-C103 | WEVENT.booth_sale.find | website_event_booth_sale/models/sale_order.py:10 | def _cart_find_product_line | FACT | booth lines | — | _cart_find_product_line for booth sales returns the existing line that shares any of the requested pending booth ids, preventing duplicate booth lines | N-U65-016 |
| VDR-U65-C104 | WSALE.ext.gelato.express | website_sale_gelato/models/sale_order.py:38 | def _allow_express_checkout(self) | FACT | Gelato products | — | Express checkout is disabled for any order containing a product with a gelato_product_uid, as Gelato requires a full checkout flow | N-U65-010 |
| VDR-U65-C105 | WEVENT.crm.fields | website_event_crm/models/event_registration.py:24 | def _get_lead_description_fields | FACT | always | — | _get_lead_description_fields extends the base list with website-specific registration fields, enriching the CRM lead description | N-U65-017 |
| VDR-U65-C106 | WSALE.payment.tx_session | website_sale/controllers/payment.py:80 | request.session['__website_sale_last_tx_id'] | FACT | always | — | After transaction creation, the transaction id is stored in session under __website_sale_last_tx_id and any previous draft transaction reference is replaced | N-U65-006 |
| VDR-U65-C107 | WSALE.ext.collect.geocode | website_sale_collect/models/stock_warehouse.py:17 | return (loc_.partner_latitude | FACT | always | — | _prepare_pickup_location_data geo-locates the warehouse partner; on failure it assigns invalid coordinates (1000, 1000) to skip future API calls | N-U65-009 |
| VDR-U65-C108 | WEVENT.sale.order_line | website_event_sale/controllers/main.py:43 | cart_data = {} | FACT | paid tickets | — | Each unique slot-ticket combination gets its own cart line; the sale order line id is stored in cart_data keyed by the combination tuple | N-U65-018 |
| VDR-U65-C109 | WSALE.catalog.gist_index | website_sale/models/product_template.py:178 | _name_gist_idx | FACT | trigram enabled | — | product.template gets GiST trigram indexes on name, description, description_sale, and description_ecommerce for fuzzy search support | N-U65-003 |
| VDR-U65-C110 | WSALE.ext.mrp.component | website_sale_mrp/models/sale_order.py:38 | component = bom_line.product_id | FACT | kit products | — | Component unavailability is tracked per-component across all kit lines; max available kits are recomputed from the most-constrained component | N-U65-012 |
| VDR-U65-C111 | WSALE.payment.cancel | website_sale/controllers/payment.py:53 | raise ValidationError | FACT | cancelled order | — | shop_payment_transaction raises ValidationError("The order has been cancelled.") if the sale order is in the cancel state | N-U65-006 |
| VDR-U65-C112 | WEVENT.quiz.completed | website_event_track_quiz/controllers/event_track_quiz.py:23 | return {'error': 'track_quiz_done'} | FACT | repeated attempt | — | If the track visitor record already has quiz_completed=True, the submit endpoint returns error track_quiz_done without modifying the score | N-U65-019 |
| VDR-U65-C113 | WSALE.checkout.confirmation | website_sale/controllers/main.py:1689 | def shop_payment_confirmation(self, **post) | FACT | always | — | /shop/confirmation reads sale_last_order_id from the session and renders the confirmation page; missing session data redirects to the shop | N-U65-005 |
| VDR-U65-C114 | WSALE.ext.stock.threshold2 | website_sale_stock/models/product_template.py:18 | show_availability = fields.Boolean | FACT | always | — | show_availability (default False) enables display of the exact available quantity on the product page when set to True | N-U65-014 |
| VDR-U65-C115 | WSALE.order.company | website_sale/models/sale_order.py:172 | if vals.get('website_id') | FACT | on create | — | When a new cart is created with a website_id, the website's company_id is used as the order company if no explicit company is provided | N-U65-007 |
| VDR-U65-C116 | WEVENT.event.published_visible | website_event/models/event_event.py:152 | _compute_is_visible_on_website | FACT | always | — | _compute_is_visible_on_website applies additional logic beyond website_published to determine whether an event shows in search and listing results | N-U65-015 |
| VDR-U65-C117 | WSALE.ext.loyalty.program_domain | website_sale_loyalty/models/sale_order.py:18 | def _get_program_domain(self) | FACT | always | — | _get_program_domain adds an ecommerce_ok=True filter so only loyalty programs flagged for website use are applied to web cart orders | N-U65-011 |
| VDR-U65-C118 | WEVENT.sale.product_ticket | website_event_sale/models/product.py:10 | event_ticket_ids | FACT | always | — | product.product gains event_ticket_ids One2many pointing to event.event.ticket, linking the product to its ticket definitions | N-U65-018 |
| VDR-U65-C119 | WMMAIL.subscribe.opt_in | website_mass_mailing/controllers/main.py:67 | # inline add_to_list | FACT | existing opt-out | — | When re-subscribing, if an existing subscription has opt_out=True, it is reset to False rather than creating a duplicate subscription record | N-U65-020 |
| VDR-U65-C120 | WSALE.ext.slides.revenue | website_sale_slides/models/slide_channel.py:20 | product_sale_revenues = fields.Monetary | FACT | always | — | slide.channel computes product_sale_revenues by summing price_total from sale.report for confirmed orders containing the channel's product | N-U65-013 |
| VDR-U65-C121 | WSALE.cart.warning | website_sale/models/sale_order.py:393 | if not self.env.context.get | FACT | restricted products | — | _cart_add stores any quantity warning from _verify_updated_quantity in shop_warning on the order or line for display in the cart notification | N-U65-004 |
| VDR-U65-C122 | WEVENT.event.register_url | website_event/models/event_event.py:175 | _compute_event_register_url | FACT | always | — | _compute_event_register_url builds the canonical registration URL for the event, used in email communications and website link generation | N-U65-015 |
| VDR-U65-C123 | WSALE.ext.collect.delivery_reset | website_sale_collect/models/sale_order.py:49 | def _set_delivery_method | FACT | delivery change | — | When switching away from an in_store delivery method, _set_delivery_method triggers recomputation of warehouse_id and fiscal_position_id | N-U65-009 |
| VDR-U65-C124 | WSALE.checkout.delivery_error | website_sale/controllers/main.py:1599 | def _get_shop_payment_errors(self, order) | FACT | deliverable products | — | _get_shop_payment_errors returns a shipping error tuple when the order has deliverable products but no available delivery methods for the address | N-U65-005 |
| VDR-U65-C125 | WEVENT.sale.confirm_page | website_event_sale/controllers/sale.py:10 | def _prepare_shop_payment_confirmation_values | FACT | event ticket orders | — | The payment confirmation page is extended to include the events linked to ticket order lines and a grouped list of confirmed registrations | N-U65-018 |
