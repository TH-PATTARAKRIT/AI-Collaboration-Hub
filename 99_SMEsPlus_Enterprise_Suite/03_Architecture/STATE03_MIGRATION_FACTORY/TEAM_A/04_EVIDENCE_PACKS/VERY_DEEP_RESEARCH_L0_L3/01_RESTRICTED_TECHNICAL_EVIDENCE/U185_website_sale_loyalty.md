# U185 — website_sale_loyalty: Technical Evidence (L3)

**Unit**: U185 | **Module**: website_sale_loyalty | **Group**: G12 | **Priority**: P2
**Status**: PRESENT (Odoo 19.0.post20260921 Community)
**Research Level**: L3 — Deep source reading of controllers, models, templates, and JS interactions
**Date**: 2026-10-02

---

## 1. Module Identity and Dependencies

**Path**: `odoo/addons/website_sale_loyalty/`
**Manifest name**: "Coupons, Promotions, Gift Card and Loyalty for eCommerce"
**Version**: 1.0
**Auto-install condition**: `['website_sale', 'sale_loyalty']` — activates automatically when both are present.

**Declared depends**:
```
['website_sale', 'website_links', 'sale_loyalty']
```
**No dependency on `pos_loyalty`**. POS loyalty is a fully separate module. `website_sale_loyalty` is purely eCommerce-facing and reuses the `sale_loyalty` base engine.

---

## 2. Controllers

### 2.1 `controllers/main.py` — WebsiteSale (inherits `website_sale.controllers.main.WebsiteSale`)

**Route 1: `pricelist()` (overrides `/shop/pricelist`)**
```python
@route()
def pricelist(self, promo, reward_id=None, **post):
```
- Called when the coupon input form is submitted on the cart page.
- Calls `order_sudo._try_apply_code(promo)` from `sale_loyalty`.
- If result has `not_found`: falls back to parent pricelist logic (e.g., applying a pricelist).
- If result has `error`: stores the message in `request.session['error_promo_code']`.
- On success: if exactly one coupon and one reward match and not multi-product, calls `self._apply_reward()`. Stores `request.session['successful_code'] = promo`.
- Always redirects to `post.get('r', '/shop/cart')`.

**Route 2: `/coupon/<string:code>` — `activate_coupon()`**
```python
@route(['/coupon/<string:code>'], type='http', auth='public', website=True, sitemap=False)
def activate_coupon(self, code, r='/shop', **kw):
```
- Used for shareable coupon links (e.g., from `coupon.share` wizard).
- Stores `code` in `request.session['pending_coupon_code']`.
- If a cart exists, calls `order._try_pending_coupon()` immediately.
- On error: appends `?coupon_error=...` to redirect URL.
- On success: appends `?notify_coupon=<code>` to redirect URL.
- If no cart: returns a warning that code will apply when items are added.

**Route 3: `/shop/claimreward` — `claim_reward()`**
```python
@route('/shop/claimreward', type='http', auth='public', website=True, sitemap=False)
def claim_reward(self, reward_id, code=None, **post):
```
- Called when customer clicks "Use" or "Claim" on a displayed reward.
- Looks up `loyalty.reward` by `reward_id`.
- Searches `_get_claimable_and_showable_rewards()` to find the associated coupon.
- Calls `self._apply_reward(order_sudo, reward_sudo, coupon)`.

**`_apply_reward()` helper**:
```python
def _apply_reward(self, order, reward, coupon):
```
- Calls `order._apply_program_reward(reward, coupon, product=product)` from `sale_loyalty`.
- On `UserError` or `error` key in result: stores in `request.session['error_promo_code']`.
- On success: calls `order._update_programs_and_rewards()`.
- For `free_over` carrier + non-payment rewards: re-rates shipping to reflect discount.

### 2.2 `controllers/cart.py` — Cart (inherits `website_sale.controllers.cart.Cart`)

**Overrides `/shop/cart` GET handler**:
```python
@route()
def cart(self, **post):
    if order_sudo := request.cart:
        order_sudo._update_programs_and_rewards()
        order_sudo._auto_apply_rewards()
    return super().cart(**post)
```
Every cart page load triggers reward recalculation and auto-application.

**`/wallet/top_up` (POST, auth=user)**:
Adds the ewallet trigger product to cart and redirects to `/shop/cart` for ewallet top-up flow.

### 2.3 `controllers/payment.py` — PaymentPortal

**`_validate_transaction_for_order()` override**:
```python
super()._validate_transaction_for_order(transaction, sale_order)
if sale_order.exists():
    initial_amount = sale_order.amount_total
    sale_order._update_programs_and_rewards()
    if sale_order.currency_id.compare_amounts(sale_order.amount_total, initial_amount):
        raise ValidationError(...)
```
Re-evaluates all rewards before payment is processed. If the order total changed (reward expired, or conditions no longer met), a `ValidationError` is raised with message: "Cannot process payment: applied reward was changed or has expired. Please refresh the page and try again."

### 2.4 `controllers/delivery.py` — WebsiteSaleLoyaltyDelivery

Overrides `_order_summary_values()` to append `amount_delivery_discounted` (for free-shipping rewards) and `discount_reward_amounts` (per-reward discount amounts grouped by `reward_id`) to the delivery summary JSON response. The `checkout.js` JS interaction consumes these to update cart summary display without page reload.

### 2.5 `controllers/portal.py` — CustomerPortalLoyalty

Overrides `portal_get_card_history_values()` to add published trigger products list (with price) to loyalty program card history data, enabling the customer portal to show ewallet top-up products.

---

## 3. Model Extensions

### 3.1 `models/sale_order.py` — SaleOrder

**New field**:
```python
disabled_auto_rewards = fields.Many2many("loyalty.reward", relation="sale_order_disabled_auto_rewards_rel")
```
Tracks rewards the customer has manually removed — prevents them from being re-auto-applied in the same session.

**`_get_program_domain()` / `_get_trigger_domain()` overrides**:
When the order has a `website_id`, replaces the `sale_ok` filter with `ecommerce_ok` and adds a website scope filter `('website_id', 'in', (self.website_id.id, False))`. This ensures only programs published on the correct website (or all websites) are considered.

**`_try_pending_coupon()`**:
```python
def _try_pending_coupon(self):
    pending_coupon_code = request.session.get('pending_coupon_code')
    if pending_coupon_code:
        status = self._try_apply_code(pending_coupon_code)
        if 'error' not in status:
            request.session.pop('pending_coupon_code')
            # auto-apply single non-multi-product reward
        return status
    return True
```
Called from `_update_programs_and_rewards()` on every cart update. Applies any pending coupon stored in session (e.g., from a share link visited before adding items).

**`_auto_apply_rewards()`**:
Iterates `_get_claimable_rewards()`. Applies a reward automatically if:
- Program has exactly 1 reward
- Program is not nominative
- Reward is not a multi-product reward
- Reward not in `disabled_auto_rewards`
- Reward not already on order lines

**`_compute_website_order_line()` override**:
Merges multiple discount lines from the same program (caused by different tax groups) into a single virtual line for display. The actual tax-split lines are hidden; a `new()` virtual line with combined subtotal is shown instead. This is purely visual — actual tax calculation lines remain.

**`get_promo_code_error()` / `get_promo_code_success_message()`**:
Session-based read/pop methods used by QWeb templates to display one-shot success/error feedback.

**`_get_claimable_and_showable_rewards()`**:
Extends `_get_claimable_rewards()` by also searching `loyalty.card` records for the order's partner, filtered by program domain and code/trigger type. Includes partner's existing cards that have sufficient points, even if not currently applied to the order. Filters expired cards and zero-total orders.

**`_gc_abandoned_coupons()` (`@api.autovacuum`)**:
Removes `applied_coupon_ids` from draft website orders older than N days (default 4, controlled by `website_sale_coupon.abandonned_coupon_validity` ir.config_param). Prevents permanent lock on coupon points by abandoned carts.

**`_allow_nominative_programs()` override**:
Returns `False` for public (unauthenticated) website users. Nominative programs (tied to a specific partner) are only available to logged-in customers.

**`_cart_update_order_line()` override**:
When a reward line is deleted (quantity set to 0 or below), adds `website_sale_loyalty_delete=True` to context, triggering `SaleOrderLine.unlink()` to register the reward in `disabled_auto_rewards`.

**`_verify_cart_after_update()` override**:
Calls `_update_programs_and_rewards()` and `_auto_apply_rewards()` after every cart modification to keep rewards in sync.

**`_get_free_shipping_lines()`**:
Returns order lines where `reward_id.reward_type == 'shipping'`. Used by delivery controller and shipping-free-over logic.

**`_get_non_delivery_lines()` override**:
Excludes free-shipping reward lines from the non-delivery set, preventing them from interfering with standard delivery line handling.

### 3.2 `models/sale_order_line.py` — SaleOrderLine

- `_show_in_cart()`: Hides discount reward lines from `website_order_line` (they are replaced by merged visual lines).
- `_is_reorder_allowed()`: Reward lines cannot be reordered.
- `unlink()`: On deletion with `website_sale_loyalty_delete` context, registers reward in `order.disabled_auto_rewards`.
- `_should_show_strikethrough_price()`: Suppressed for reward lines.
- `_is_sellable()`: Returns False for reward lines (except free-product rewards which are shown in cart).

### 3.3 `models/loyalty_program.py` — LoyaltyProgram

Inherits `['loyalty.program', 'website.multi.mixin']`.

**New fields**:
- `ecommerce_ok = fields.Boolean("Available on Website", default=True)` — controls whether program is visible in eCommerce.
- `show_non_published_product_warning` (computed) — warns admin if ewallet trigger products are unpublished.

**`action_program_share()`**: Opens `coupon.share` wizard for sharing a program's promo code link.

### 3.4 `models/loyalty_card.py` — LoyaltyCard

Adds `action_coupon_share()` method to open the `coupon.share` wizard for a specific coupon.

### 3.5 `models/loyalty_rule.py` — LoyaltyRule

**`_constrains_code()`** (constrains on `code`, `website_id`, `active`):
- Enforces uniqueness of promo codes within the same website scope.
- Two programs with the same code on the same website (or global) are blocked.
- Also checks `loyalty.card` codes to prevent collision.

### 3.6 `models/product_product.py` — ProductProduct

- `_can_return_content()`: Allows public access to images of products linked to `loyalty.reward.discount_line_product_id`, regardless of publish state.
- `_get_product_placeholder_filename()`: Returns gift card or discount placeholder images for reward products.

---

## 4. Template Extensions (`views/website_sale_templates.xml`)

### 4.1 Cart coupon form (`sale_coupon_result`, inherits `website_sale.coupon_form`)
Updates placeholder text to "Gift card or discount code...". Removes the `code_not_available` block.

### 4.2 Reward panel (`modify_code_form`, inherits `website_sale.total`)
Injects a `<tr>` after the last totals row containing:
1. **Error banner** (alert-danger): shown when `get_promo_code_error()` returns a message.
2. **Success banner** (alert-success): shown when `get_promo_code_success_message()` returns a code.
3. **Claimable rewards loop**: iterates `_get_claimable_and_showable_rewards()` items. For each (coupon, rewards) pair:
   - Loyalty program header shows point balance.
   - Each reward renders a `<form action="/shop/claimreward">` with `reward_id`, `code`, CSRF token, and optional product selector (multi-product rewards).
   - Button label: "Use" (for code-triggered rewards) or "Claim" (for auto/loyalty rewards).
   - Gift card display: shows masked code (`••••••••••1234`) and expiration date.
   - eWallet display: shows balance alongside reward description.

### 4.3 Layout extension (`layout`, inherits `website.layout`)
Injects hidden `<div class="coupon-message ...">` elements at wrapwrap level from `request.params` (`coupon_error`, `notify_coupon`). These are converted to browser notification toasts by `CouponToaster` JS interaction.

### 4.4 Reduction code placeholder (`reduction_coupon_code`, inherits `website_sale.reduction_code`)
Overrides placeholder to "Discount code or gift card".

### 4.5 Reward type data attribute (`cart_summary`)
Adds `t-att-data-reward-type="line.reward_id.reward_type"` to cart summary price spans, enabling delivery.js to update shipping/discount amounts without page reload.

### 4.6 Quantity selector suppression (`cart_lines_quantity`)
Sets `should_show_quantity_selector = False` for free-product reward lines.

### 4.7 Used gift card display
Injects `sale_loyalty.used_gift_card` template into cart lines and cart summary for applied gift card visual feedback.

### 4.8 Purchased gift card (`website_sale_purchased_gift_card`, inherits `website_sale.confirmation`)
Calls `sale_loyalty.sale_purchased_gift_card` on the order confirmation page to display purchased gift card codes with a copy-to-clipboard button.

---

## 5. JavaScript Interactions (`static/src/interactions/`)

### 5.1 `checkout.js`
Patches `Checkout._updateCartSummary()` from `@website_sale/interactions/checkout`.
- Updates `[data-reward-type="shipping"]` element with `result.amount_delivery_discounted`.
- Updates all `[data-reward-type=discount]` elements with `result.discount_reward_amounts` array. If count mismatches (reward added/removed), forces `location.reload()`.

### 5.2 `coupon_toaster.js`
`CouponToaster` class (selector `.coupon-message`) reads hidden div content injected by the layout template and shows browser notifications:
- `.coupon-info-message` → `type: "success"` notification
- `.coupon-error-message` → `type: "danger"` notification
- `.coupon-warning-message` → `type: "warning"` notification

### 5.3 `gift_card_copy.js`
`GiftCardCopy` class (selector `.o_purchased_gift_card .copy-to-clipboard`) uses `browser.navigator.clipboard.writeText()` to copy gift card codes on click.

---

## 6. Coupon Code Validation Flow (`sale_loyalty._try_apply_code()`)

Source: `sale_loyalty/models/sale_order.py:1455`

1. Search `loyalty.rule` for `mode='with_code'` and `code=<code>` within program domain.
2. If found: check if already applied → return `{'error': "This promo code is already applied."}`.
3. If not found as rule: search `loyalty.card` for code.
   - No card / inactive program / empty rewards / out of domain → `{'error': "This code is invalid (%s).", 'not_found': True}`
   - Expired (expiration_date < today) → `{'error': "This coupon is expired."}`
   - Points < required_points (all rewards) → `{'error': "This coupon has already been used."}`
4. If program type is `loyalty` or `ewallet` → `{'error': "This program cannot be applied with code."}`
5. Row-level `FOR UPDATE NOWAIT` lock on `loyalty_program` to prevent concurrent application.
6. Usage limit exceeded → `{'error': "This code is expired (%s)."}`
7. Applies program/coupon via `_try_apply_program()`.
8. Returns `_get_claimable_rewards(forced_coupons=coupon)` — dict of `{loyalty.card: loyalty.reward recordset}`.

---

## 7. Gift Card Balance at Checkout

`_get_real_points_for_coupon(coupon)` in `sale_loyalty` (used by website templates and claimable rewards logic):
```
usable_points = coupon.points
               + pending_earned_points (from coupon_point_ids, if applies_on != 'future')
               - sum(order_line.points_cost where coupon_id == coupon)
```
For gift cards, `points` represent monetary value in the order currency. The `_format_points()` method on `loyalty.card` renders the balance for display. The template calls `coupon._format_points(website_sale_order._get_real_points_for_coupon(coupon))` to show available balance.

No separate `website_sale_gift_card` module exists. Gift card handling is fully unified within `website_sale_loyalty`.

---

## 8. Wizard: `wizard/coupon_share.py` — CouponShare

Transient model `coupon.share`:
- Generates shareable URLs of the form `{base_url}/coupon/{code}?r={redirect}`.
- Optionally creates a short link via `link.tracker`.
- Constrained to programs that require a code (`trigger == 'with_code'`, or `rule_ids.code != False`, or `program_type == 'coupons'`).
- Validates that coupon programs always have a coupon specified.
- Validates website scope consistency.

---

## 9. Security

`security/ir.model.access.csv` — Provides access rules for `coupon.share` transient model.

---

## 10. Key Architectural Notes

- `website_sale_loyalty` is the **sole eCommerce loyalty integration module** — no separate `website_sale_gift_card`.
- All validation logic lives in `sale_loyalty._try_apply_code()` (upstream). `website_sale_loyalty` provides only the HTTP routing, session management, and template rendering.
- Error feedback is **session-based** (not URL-based except for activate_coupon flow): stored in `request.session['error_promo_code']` / `request.session['successful_code']`, read once and deleted by QWeb methods.
- Concurrent coupon application is guarded by a PostgreSQL `FOR UPDATE NOWAIT` row lock on `loyalty_program`.
- Abandoned cart cleanup is automated via `@api.autovacuum` (default 4-day window).
