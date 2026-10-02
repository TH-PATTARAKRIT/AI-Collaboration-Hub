# U129 — website_sale Wishlist / Loyalty / Gift-Card Cross-Module Chain (GAP-026 Depth)

**Unit:** U129 | **Group:** G12 | **Priority:** P1 | **Gap:** GAP-026  
**Researcher:** Claude Sonnet 4.6 | **Date:** 2026-10-02  
**Branch:** claude/local-odoo-source-research  

---

## L1 — Manifest / Dependencies

### website_sale
- File: `website_sale/__manifest__.py`
- Dependencies: `website`, `sale`, `website_payment`, `website_mail`, `portal_rating`, `digest`, `delivery`, `html_builder`
- License: LGPL-3; `post_init_hook`, `uninstall_hook` defined

### website_sale_wishlist
- File: `website_sale_wishlist/__manifest__.py`
- Dependencies: `website_sale`; `auto_install = True`

### website_sale_loyalty
- File: `website_sale_loyalty/__manifest__.py`
- Dependencies: `website_sale`, `website_links`, `sale_loyalty`; `auto_install = ['website_sale', 'sale_loyalty']`

### sale_loyalty
- File: `sale_loyalty/__manifest__.py`
- Dependencies: `sale`, `loyalty`; `auto_install = True`

---

## L2 — Models / Fields / ORM

### website_sale — sale.order extensions
File: `website_sale/models/sale_order.py:22-47`
- `website_id`: Many2one `website` (readonly, tracks originating website)
- `website_order_line`: One2many computed from order_line filtered by `_show_in_cart()`
- `cart_quantity`: Integer computed from `website_order_line.product_uom_qty` sum
- `only_services`: Boolean, True if all lines are services
- `is_abandoned_cart`: Boolean computed, searchable via `_search_abandoned_cart`
- `amount_delivery`: Monetary, tax-toggled depending on `show_line_subtotals_tax_selection`
- `shop_warning`: Char (transient warning for cart feedback)
- `cart_recovery_email_sent`: Boolean

### website_sale — website model fields
File: `website_sale/models/website.py:55-248`
- `add_to_cart_action`: Selection `stay` / `go_to_cart`
- `account_on_checkout`: Selection `optional` / `disabled` / `mandatory`
- `ecommerce_access`: Selection `everyone` / `logged_in`
- `cart_abandoned_delay`: Float (default 10.0 hours)
- `show_line_subtotals_tax_selection`: `tax_excluded` / `tax_included` (computed, storable)
- Session keys: `CART_SESSION_CACHE_KEY`, `FISCAL_POSITION_SESSION_CACHE_KEY`, `PRICELIST_SESSION_CACHE_KEY`, `PRICELIST_SELECTED_SESSION_CACHE_KEY` (module-level constants)

### website_sale_wishlist — product.wishlist
File: `website_sale_wishlist/models/product_wishlist.py:7-22`
- `_name = 'product.wishlist'`
- `partner_id`: Many2one `res.partner` (null for anonymous session)
- `product_id`: Many2one `product.product` (required)
- `currency_id`: related from `website_id.currency_id`
- `pricelist_id`: Many2one `product.pricelist` (snapshot at time of add)
- `price`: Monetary (price at time of add)
- `website_id`: Many2one `website` (cascade delete)
- `active`: Boolean (default True)
- Unique constraint: `UNIQUE(product_id, partner_id)`

### website_sale_loyalty — loyalty.program extension
File: `website_sale_loyalty/models/loyalty_program.py:7-20`
- `ecommerce_ok`: Boolean "Available on Website" (default True)
- `show_non_published_product_warning`: computed Boolean for ewallet with unpublished trigger products
- Inherits `website.multi.mixin` (multi-website capability)

### website_sale_loyalty — sale.order extensions
File: `website_sale_loyalty/models/sale_order.py:14-15`
- `disabled_auto_rewards`: Many2many `loyalty.reward` (tracks rewards user explicitly removed)

### website_sale_loyalty — loyalty.rule extension
File: `website_sale_loyalty/models/loyalty_rule.py:9-10`
- `website_id`: stored related from `program_id.website_id`
- Uniqueness constraint: promo codes must be unique per-website

---

## L3 — Workflow / State

### Cart lifecycle (website_sale)
File: `website_sale/models/website.py:668-858`
1. `_get_and_cache_current_cart()` resolves cart from session or abandoned cart search
2. Anonymous cart: stored as session key `sale_order_id` (int)
3. On login: `_update_address()` migrates session cart to logged-in partner
4. Abandoned cart: searched for logged-in users without session cart; revived via `_verify_cart()`
5. Payment lock: `state != 'draft'` or active payment transaction → session cleared → new cart

### Wishlist lifecycle (website_sale_wishlist)
File: `website_sale_wishlist/models/product_wishlist.py:25-69`
- Anonymous: wish IDs stored in `request.session['wishlist_ids']`; no `partner_id`
- On login: `_check_wishlist_from_session()` merges session wishes to `env.user.partner_id`, deduplicates
- `current()` filters: published product + `_is_add_to_cart_possible()` check

### Coupon/Loyalty workflow (website_sale_loyalty)
File: `website_sale_loyalty/models/sale_order.py:44-61`
1. `/coupon/<code>` → stores code in `request.session['pending_coupon_code']`
2. Next cart-mutating request → `_update_programs_and_rewards()` → `_try_pending_coupon()`
3. `_try_pending_coupon()` → `_try_apply_code(code)` (sale_loyalty engine)
4. If one reward and not multi-product → `_apply_program_reward()` auto-applied
5. `_auto_apply_rewards()` checks auto-applicable rewards; respects `disabled_auto_rewards`
6. On reward line deletion: `unlink()` in `sale_order_line.py:23` adds reward to `disabled_auto_rewards`

### Payment validation guard (website_sale_loyalty)
File: `website_sale_loyalty/controllers/payment.py:12-30`
- `_validate_transaction_for_order()` calls `_update_programs_and_rewards()` before finalizing
- If amount changes after reward update → raises `ValidationError` (prevents stale-reward payment)

---

## L4 — Cross-Module Call Chain

### Request setup chain
File: `website_sale/models/ir_http.py:28-33`
```
_frontend_pre_dispatch()
  → request.cart = lazy(website._get_and_cache_current_cart)
  → request.fiscal_position = lazy(website._get_and_cache_current_fiscal_position)
  → request.pricelist = lazy(website._get_and_cache_current_pricelist)
```
All three are lazy-loaded: evaluated only on first access, cached in session.

### Coupon code application chain
```
/coupon/<code> (website_sale_loyalty/controllers/main.py:37)
  → session['pending_coupon_code'] = code
  → order._try_pending_coupon() (website_sale_loyalty/models/sale_order.py:44)
    → order._try_apply_code(code) (sale_loyalty/models/sale_order.py:1455)
      → loyalty.rule search + FOR UPDATE NOWAIT lock on loyalty_program row
      → _get_claimable_rewards()
      → _apply_program_reward(reward, coupon) (sale_loyalty/models/sale_order.py:945)
        → sale.order.line.create() with reward fields
```

### Delivery ↔ Loyalty integration
File: `website_sale_loyalty/models/sale_order.py:176-183`
- `_set_delivery_method()` override: calls `super()._set_delivery_method()` then `_update_programs_and_rewards()`
- `_remove_delivery_line()` override: calls `super()._remove_delivery_line()` then `_update_programs_and_rewards()`

### Program domain substitution (eCommerce context)
File: `website_sale_loyalty/models/sale_order.py:17-38`
- When order has `website_id`: `sale_ok` leaf in program domain replaced with `ecommerce_ok`
- Adds `website_id IN (current_website, False)` constraint → multi-website isolation

### Wishlist → shop page injection
File: `website_sale_wishlist/controllers/website_sale.py:9-13`
- `_get_additional_shop_values()` override injects `products_in_wishlist` (set of product.template records) into shop template context

---

## L5 — Views / Wizards / Routes

### website_sale routes
- `GET /shop` — product listing with category/search filters
- `POST /shop/cart/add` (jsonrpc) — `website_sale/controllers/cart.py:75`
- `POST /shop/cart/update` (jsonrpc) — `website_sale/controllers/cart.py:309`
- `GET /shop/cart` (http) — cart display
- `GET /shop/delivery_methods` (jsonrpc) — `website_sale/controllers/delivery.py:14`
- `POST /shop/set_delivery_method` (jsonrpc) — `website_sale/controllers/delivery.py:37`
- `GET /shop/payment` (http) — payment step
- `POST /shop/payment/transaction/<order_id>` (jsonrpc) — `website_sale/controllers/payment.py:24`
- `GET /shop/payment/validate` (http) — post-payment handler
- `GET /shop/confirmation` (http) — confirmation page

### website_sale_wishlist routes
- `POST /shop/wishlist/add` (jsonrpc) — `website_sale_wishlist/controllers/main.py:9`
- `GET /shop/wishlist` (http) — wishlist page
- `POST /shop/wishlist/remove/<wish_id>` (jsonrpc)
- `GET /shop/wishlist/get_product_ids` (jsonrpc, readonly)

### website_sale_loyalty routes
- `GET /coupon/<code>` (http) — `website_sale_loyalty/controllers/main.py:37`
- `POST /shop/claimreward` (http) — `website_sale_loyalty/controllers/main.py:55`
- `GET /wallet/top_up` (http, auth=user) — `website_sale_loyalty/controllers/cart.py:13`
- `/shop/cart` (overridden) — calls `_update_programs_and_rewards()` + `_auto_apply_rewards()` on load

---

## L6 — Access Control / Record Rules / Sudo

### website_sale security
File: `website_sale/security/ir_rules.xml`
- `product_template_public` ir.rule: public+portal groups limited to `website_published=True AND sale_ok=True`
- `empty_public_categories_rule`: hides product categories with no published products from public/portal
- `ecommerce_access` field: if set to `logged_in`, `has_ecommerce_access()` returns False for public users → redirect to login
- Pricelist company rules: `product.product_pricelist_comp_rule` deactivated; replaced with website-company-aware versions

### website_sale_wishlist security
File: `website_sale_wishlist/security/website_sale_wishlist_security.xml`
- `product_wishlist_rule`: portal+user can only see own wishlists (`partner_id = user.partner_id.id`)
- `all_product_wishlist_rule`: sale managers see all wishlists
- Anonymous users: `Wishlist.sudo()` used; wishes stored in session only (no DB `partner_id`)

### website_sale_loyalty access
File: `website_sale_loyalty/models/sale_order.py:221-225`
- `_allow_nominative_programs()`: returns False if `request.website.is_public_user()` — prevents anonymous users from accessing nominative loyalty programs

### Sudo escalation pattern
- Cart created via `env['sale.order'].with_user(SUPERUSER_ID)` then downgraded back: `website_sale/models/website.py:674-677`
- Wishlist add for public: `Wishlist.sudo()` used in controller: `website_sale_wishlist/controllers/main.py:15`

---

## L7 — Configuration Prerequisites

- `ecommerce_ok` per loyalty program (default True; must be True for loyalty to apply in website context)
- `website_id` per loyalty program: multi-website isolation (None = all websites)
- `account_on_checkout`: controls whether guest checkout is allowed
- `ecommerce_access`: controls public access gate
- `cart_abandoned_delay`: float hours for abandoned cart threshold (default 10.0)
- `send_abandoned_cart_email`: Boolean to enable abandoned cart email cron
- `show_line_subtotals_tax_selection`: toggles tax display on cart lines
- ICP `website_sale_coupon.abandonned_coupon_validity`: days before clearing coupons from abandoned orders (default 4)

---

## L8 — Immutability / Audit

- `disabled_auto_rewards`: M2M tracks which auto-rewards a user explicitly removed; prevents re-application
- `cart_recovery_email_sent`: Boolean flag prevents duplicate recovery emails
- Coupon `applied_coupon_ids`: accumulated set on sale.order; not purged after order confirmation
- @api.autovacuum `_gc_sessions`: wishlist session records deleted after 5 weeks
- @api.autovacuum `_gc_abandoned_coupons`: coupons cleared from abandoned orders after configurable days

---

## L9 — Accounting / Stock Postings

### Delivery amount computation
File: `website_sale/models/sale_order.py:57-63`
- `_compute_amount_delivery()`: sums `price_subtotal` or `price_total` from delivery lines based on `show_line_subtotals_tax_selection`

### Gift card SOL tax handling
File: `sale_loyalty/models/sale_order.py:610-634`
- When `reward_program.is_payment_program = True` and `program_type == 'gift_card'`: SOL receives mapped fiscal position taxes; price-include taxes extracted separately to maintain correct taxed amount

### Loyalty discount line merging (eCommerce display)
File: `website_sale_loyalty/models/sale_order.py:84-120`
- `_compute_website_order_line()` override: discount SOLs from same (reward_id, coupon_id) pair merged into single virtual `sale.order.line.new()` without taxes, for visual consolidation in cart

### Free shipping reward
File: `website_sale_loyalty/models/sale_order.py:186-190`
- `_get_non_delivery_lines()` overridden to exclude free-shipping reward lines from delivery computation
- `_get_free_shipping_lines()`: returns `order_line` filtered by `reward_id.reward_type == 'shipping'`

---

## L10 — Cron / Queue / Import-Export

### Abandoned cart cron
File: `website_sale/data/ir_cron_data.xml:3-10`
- `ir.cron: ir_cron_send_availability_email` — runs hourly, calls `model._send_abandoned_cart_email()`
- Target model: `website`; triggers recovery email for carts meeting abandonment criteria

### Autovacuum tasks
- `website_sale_wishlist/models/product_wishlist.py:67-72`: `@api.autovacuum _gc_sessions` removes anonymous wishlists >5 weeks old
- `website_sale_loyalty/models/sale_order.py:205-219`: `@api.autovacuum _gc_abandoned_coupons` clears `applied_coupon_ids` on abandoned eCommerce orders older than ICP-configured days

---

## L11 — API Surface

### Public jsonrpc endpoints (website_sale)
- `POST /shop/cart/add` — add product to cart; returns `{added_qty, line_id, quantity, warning}`
- `POST /shop/cart/update` — update line quantity; returns same shape
- `GET /shop/cart/quantity` (jsonrpc) — returns `cart_quantity` integer
- `POST /shop/cart/clear` (jsonrpc) — empties cart
- `GET /shop/delivery_methods` (jsonrpc) — renders delivery form HTML
- `POST /shop/set_delivery_method` (jsonrpc) — sets carrier; returns order summary dict
- `POST /shop/payment/transaction/<order_id>` (jsonrpc) — creates draft payment transaction; returns processing values
- `POST /shop/get_delivery_rate` (jsonrpc) — returns rate data for a delivery method

### website_sale_wishlist endpoints
- `POST /shop/wishlist/add` (jsonrpc, auth=public) — adds product to wishlist; returns wish record
- `GET /shop/wishlist` (http, auth=public) — renders wishlist page
- `POST /shop/wishlist/remove/<wish_id>` (jsonrpc, auth=public)
- `GET /shop/wishlist/get_product_ids` (jsonrpc, auth=public, readonly)

### website_sale_loyalty endpoints
- `GET /coupon/<code>` (http, auth=public) — activates coupon code via session
- `POST /shop/claimreward` (http, auth=public) — claims a claimable reward
- `POST /shop/pricelist` (overridden) — now also handles coupon codes before pricelist codes

---

## L12 — Runtime / AWT

### Lazy request attributes
File: `website_sale/models/ir_http.py:28-33`
- `request.cart`: lazy-evaluated `sale.order` sudoed; cached in session
- `request.fiscal_position`: lazy-evaluated `account.fiscal.position` sudoed; cached in session
- `request.pricelist`: lazy-evaluated `product.pricelist` sudoed; cached in session

### Session keys
- `sale_order_id`: current cart ID (integer)
- `website_sale_cart_quantity`: cached cart quantity
- `pending_coupon_code`: coupon waiting to be applied
- `error_promo_code`: error message from last coupon attempt
- `successful_code`: code that was successfully applied
- `wishlist_ids`: list of anonymous wishlist record IDs
- `fiscal_position_id`: cached fiscal position ID
- `website_sale_current_pl`: cached pricelist ID
- `website_sale_selected_pl_id`: explicitly selected pricelist ID

### Concurrency guard
File: `sale_loyalty/models/sale_order.py:1496-1500`
- `SELECT id FROM loyalty_program WHERE id=%s FOR UPDATE NOWAIT` — serialization lock on loyalty program during `_try_apply_code()`; triggers retry on concurrent access

### Cart quantity sync
File: `website_sale_loyalty/models/sale_order.py:196-198`
- After `_auto_apply_rewards()`, if request present: `request.session['website_sale_cart_quantity'] = self.cart_quantity` — keeps frontend counter accurate after reward lines change cart count

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U129-C01 | website_sale.manifest.deps | website_sale/__manifest__.py:10-11 | `'depends': ['website', 'sale', 'website_payment', 'website_mail', 'portal_rating', 'digest', 'delivery', 'html_builder']` | C1 | Always | C1 | website_sale declares 8 hard dependencies including sale, delivery, and website_payment | eCommerce module dependency list from manifest |
| U129-C02 | website_sale.ir_http.lazy_cart | website_sale/models/ir_http.py:31 | `request.cart = lazy(request.website._get_and_cache_current_cart)` | C1 | Every frontend request | C1 | The active cart is resolved lazily per request via _get_and_cache_current_cart and cached in session | Lazy cart resolution injected into every frontend dispatch |
| U129-C03 | website_sale.website._create_cart | website_sale/models/website.py:668-682 | `sale_order_sudo = self.env['sale.order'].with_user(SUPERUSER_ID).with_company(self.company_id).create(so_data)` | C1 | New cart creation | C1 | New carts are created with SUPERUSER_ID then immediately downgraded back to the request user via sudo | New cart created under superuser then downgraded to request user |
| U129-C04 | website_sale.sale_order.website_id | website_sale/models/sale_order.py:23-27 | `website_id = fields.Many2one('website', readonly=True)` | C1 | Always | C1 | sale.order gains a readonly website_id field linking it to the originating website | Sales order extended with readonly website reference field |
| U129-C05 | website_sale.sale_order.cart_quantity | website_sale/models/sale_order.py:37-38 | `cart_quantity = fields.Integer(string="Cart Quantity", compute='_compute_cart_info')` | C1 | Always | C1 | Cart quantity is a computed integer summing product_uom_qty across website_order_line | Computed integer field counting product units in visible cart lines |
| U129-C06 | website_sale.access.public_rule | website_sale/security/ir_rules.xml:4-16 | `domain_force='[("website_published", "=", True), ("sale_ok", "=", True)]'` applied to public+portal groups | C1 | Public/portal user read | C1 | Public and portal users can only read product templates that are both published and sale-enabled | Record rule restricting product template reads for public and portal groups |
| U129-C07 | website_sale.ecommerce_access | website_sale/models/website.py:238-245 | `ecommerce_access = fields.Selection([('everyone','All users'),('logged_in','Logged in users')])` | C2 | Config | C2 | The website ecommerce_access config field controls whether anonymous users can access the shop | Website config field gating shop access to authenticated users only |
| U129-C08 | website_sale.cron.abandoned_cart | website_sale/data/ir_cron_data.xml:3-10 | `model._send_abandoned_cart_email()` on `ir.cron` running hourly | C1 | Hourly | C1 | A scheduled action runs hourly to send recovery emails for abandoned carts matching the configured delay threshold | Hourly cron job that dispatches abandoned cart recovery emails |
| U129-C09 | website_sale.checkout.payment_validate | website_sale/controllers/main.py:1645 | `@route('/shop/payment/validate', type='http', auth='public')` | C1 | Post-payment | C1 | The shop payment validate route clears the cart session and redirects to confirmation after a successful transaction | HTTP route handling post-payment session cleanup and confirmation redirect |
| U129-C10 | wishlist.model.partner_id | website_sale_wishlist/models/product_wishlist.py:13 | `partner_id = fields.Many2one('res.partner', index='btree_not_null')` | C1 | Always | C1 | Wishlist records store an optional partner_id; anonymous items have no partner and are tracked only via session | Wishlist model optional partner linkage enabling session-to-user migration |
| U129-C11 | wishlist.current.public_filter | website_sale_wishlist/models/product_wishlist.py:25-38 | `if request.website.is_public_user(): wish = self.sudo().search([('id', 'in', request.session.get('wishlist_ids', []))])` | C1 | Public user | C1 | For public users, the current() method resolves wishlists from the session list of IDs using sudo; authenticated users query by partner_id | Public user wishlist resolved from session IDs via sudo search |
| U129-C12 | wishlist.session_merge | website_sale_wishlist/models/product_wishlist.py:57-65 | `_check_wishlist_from_session()`: assigns session wishes to `env.user.partner_id`, deletes duplicates | C1 | Login event | C1 | On login, anonymous session wishes are migrated to the authenticated partner, with duplicate products removed | Session wishlist items transferred to authenticated partner on login with deduplication |
| U129-C13 | wishlist.autovacuum | website_sale_wishlist/models/product_wishlist.py:67-72 | `@api.autovacuum _gc_sessions`: deletes anonymous wishes older than 5 weeks | C1 | Autovacuum | C1 | An autovacuum method removes anonymous (no partner_id) wishlist records older than 5 weeks | Autovacuum garbage collection of stale anonymous wishlist records |
| U129-C14 | wishlist.access.own_rule | website_sale_wishlist/security/website_sale_wishlist_security.xml:4-11 | `domain_force='[("partner_id","=", user.partner_id.id)]'` for portal+user groups | C1 | Authenticated user | C1 | Portal and internal users are limited by record rule to viewing only their own wishlist items | Record rule limiting wishlist reads to the owner partner |
| U129-C15 | loyalty.manifest.auto_install | website_sale_loyalty/__manifest__.py:13 | `'auto_install': ['website_sale', 'sale_loyalty']` | C1 | Always | C1 | website_sale_loyalty auto-installs when both website_sale and sale_loyalty are present | Loyalty eCommerce bridge auto-installs on combined website and sales loyalty presence |
| U129-C16 | loyalty.program.ecommerce_ok | website_sale_loyalty/models/loyalty_program.py:11 | `ecommerce_ok = fields.Boolean("Available on Website", default=True)` | C1 | Always | C1 | Loyalty programs gain an ecommerce_ok Boolean that must be True for the program to be discoverable in an eCommerce order's program domain | Boolean field gating loyalty program availability in the eCommerce channel |
| U129-C17 | loyalty.domain.substitution | website_sale_loyalty/models/sale_order.py:17-38 | `_get_program_domain()`: replaces `sale_ok` leaf with `ecommerce_ok` when `self.website_id` is set; adds `website_id IN (current, False)` | C1 | eCommerce order | C1 | When an order has a website_id, the loyalty program domain substitutes sale_ok with ecommerce_ok and adds website isolation to prevent cross-site program leakage | Program domain rewritten for website orders to use ecommerce flag and website isolation |
| U129-C18 | loyalty.pending_coupon | website_sale_loyalty/models/sale_order.py:44-61 | `_try_pending_coupon()`: reads `request.session['pending_coupon_code']`, calls `_try_apply_code()`, pops key on success | C1 | Cart mutation with pending code | C1 | Coupon codes are stored in session and applied lazily on the next cart-mutating operation via _update_programs_and_rewards | Deferred coupon code application triggered by next cart modification |
| U129-C19 | loyalty.auto_apply | website_sale_loyalty/models/sale_order.py:63-100 | `_auto_apply_rewards()`: iterates claimable rewards; skips nominative, multi-reward programs, multi-product rewards, disabled rewards | C1 | Cart update | C1 | Auto-applicable rewards are claimed automatically on cart update if the program has exactly one reward that is not multi-product and not nominative and not in disabled_auto_rewards | Automatic reward claiming with guards against nominative and multi-product programs |
| U129-C20 | loyalty.disabled_auto_rewards | website_sale_loyalty/models/sale_order.py:14-15 | `disabled_auto_rewards = fields.Many2many("loyalty.reward", relation="sale_order_disabled_auto_rewards_rel")` | C1 | Always | C1 | A Many2many field tracks rewards the user explicitly removed so they are not re-applied by the auto-claim logic | Many-to-many field preventing re-application of user-dismissed auto rewards |
| U129-C21 | loyalty.payment.amount_guard | website_sale_loyalty/controllers/payment.py:12-30 | `_validate_transaction_for_order()`: calls `_update_programs_and_rewards()`, compares amounts; raises ValidationError if changed | C1 | Payment transaction creation | C1 | Before a payment transaction is finalized, rewards are recalculated and a ValidationError is raised if the total amount changes, preventing stale-reward payments | Pre-payment guard recalculates rewards and blocks transaction if order total changes |
| U129-C22 | loyalty.delivery.integration | website_sale_loyalty/models/sale_order.py:176-183 | `_set_delivery_method()` and `_remove_delivery_line()` both call `_update_programs_and_rewards()` after super | C1 | Delivery change | C1 | Changing or removing a delivery method triggers full loyalty reward recalculation to update free-shipping rewards and delivery-contingent discounts | Delivery method change triggers loyalty reward recalculation |
| U129-C23 | loyalty.gift_card.tax_handling | sale_loyalty/models/sale_order.py:610-634 | `if reward_program.program_type == 'gift_card'`: extracts price-include taxes; adjusts price_unit and sets tax_ids on SOL | C1 | Gift card reward line | C1 | Gift card reward order lines receive special tax handling: price-include taxes from the discount product are extracted via compute_all and the line is adjusted to reflect correct taxed amounts | Gift card reward lines apply fiscal-position-mapped taxes with price-include extraction |
| U129-C24 | loyalty.discount_merge | website_sale_loyalty/models/sale_order.py:84-120 | `_compute_website_order_line()` override creates `sale.order.line.new()` merging multiple tax-split discount lines into one visual line | C1 | eCommerce cart display | C1 | Multiple discount reward lines for the same program split across different tax groups are merged into a single virtual line for display in the eCommerce cart, with taxes removed and amounts summed | Multiple tax-split discount lines merged into single virtual cart line for eCommerce display |
| U129-C25 | loyalty.free_shipping | website_sale_loyalty/models/sale_order.py:186-190 | `_get_free_shipping_lines()` returns lines with `reward_id.reward_type == 'shipping'`; excluded from delivery amount base | C1 | Free shipping reward | C1 | Free shipping rewards create order lines that are excluded from the delivery amount base computation and reported separately in the order summary | Free shipping reward lines excluded from delivery amount base and surfaced separately in order summary |
| U129-C26 | loyalty.concurrency_lock | sale_loyalty/models/sale_order.py:1496-1500 | `SELECT id FROM loyalty_program WHERE id=%s FOR UPDATE NOWAIT` during _try_apply_code | C1 | Concurrent coupon application | C1 | The loyalty program row is locked with FOR UPDATE NOWAIT during code application to prevent concurrent over-redemption; serialization errors trigger transaction retry | Database-level row lock on loyalty program prevents concurrent coupon redemption race |
| U129-C27 | loyalty.nominative_block | website_sale_loyalty/models/sale_order.py:221-225 | `_allow_nominative_programs()`: returns False if `request.website.is_public_user()` | C1 | Public user | C1 | Nominative loyalty programs are blocked for anonymous (public) website users | Nominative program access denied to anonymous eCommerce visitors |
| U129-C28 | loyalty.abandoned_coupon_gc | website_sale_loyalty/models/sale_order.py:205-219 | `@api.autovacuum _gc_abandoned_coupons`: searches orders with `state=draft, website_id!=False, applied_coupon_ids!=False, write_date < validity`, clears `applied_coupon_ids` | C1 | Autovacuum | C1 | An autovacuum method removes applied coupons from abandoned eCommerce draft orders older than the ICP-configured number of days (default 4) | Autovacuum garbage collection of coupons from long-abandoned eCommerce draft orders |
