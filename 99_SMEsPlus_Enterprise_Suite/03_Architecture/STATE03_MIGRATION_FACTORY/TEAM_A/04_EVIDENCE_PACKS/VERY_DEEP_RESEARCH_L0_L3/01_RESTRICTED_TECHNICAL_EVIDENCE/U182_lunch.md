# U182 — lunch: Restricted Technical Evidence
**Unit:** U182 | **Module:** lunch | **Group:** G09 | **Priority:** P2 | **Status:** NOT_STUDIED  
**Research Depth:** L3 (source-verified)  
**Source Base:** `odoo/addons/lunch/` — Odoo 19.0.post20260921 Community  

---

## VDR Claims Table — 20 Claims

| # | Claim ID | Category | Model / File | Field / Method | Observed Behaviour | Source Path (relative to addons/lunch/) | Confidence | Migration Risk |
|---|----------|----------|--------------|----------------|-------------------|----------------------------------------|------------|----------------|
| 1 | U182-C01 | State Machine | `lunch.order` | `state` Selection | Five-state FSM: `new` (To Order) → `ordered` (Ordered) → `sent` (Sent to supplier) → `confirmed` (Received) or `cancelled` (Cancelled). Default `new`. | models/lunch_order.py:35–40 | HIGH | LOW |
| 2 | U182-C02 | State Transition | `lunch.order` | `action_order()` | Transitions `new` → `ordered`; validates supplier available on date; calls `_check_wallet()` to enforce non-negative wallet. Raises `UserError` if supplier unavailable. | models/lunch_order.py:259–268 | HIGH | LOW |
| 3 | U182-C03 | State Transition | `lunch.order` | `action_send()` | Transitions `ordered` → `sent`. Called by supplier's `action_send_orders()` and auto-email cron. Direct assignment `self.state = 'sent'`. | models/lunch_order.py:290–291 | HIGH | LOW |
| 4 | U182-C04 | State Transition | `lunch.order` | `action_confirm()` | Transitions `sent` → `confirmed`. Triggered manually or via `action_confirm_orders()` on supplier (bulk). No wallet deduction at confirmation — debit registered at `ordered` state. | models/lunch_order.py:281–282 | HIGH | LOW |
| 5 | U182-C05 | Wallet / Cash Move | `lunch.cashmove` | Model fields | `lunch.cashmove` holds manual credits: `user_id`, `date`, `amount` (positive = credit), `description`, `currency_id`. Regular users cannot create cashmoves; only managers can (ACL). | models/lunch_cashmove.py:8–19; security/ir.model.access.csv:2–3 | HIGH | MEDIUM |
| 6 | U182-C06 | Wallet Balance | `lunch.cashmove` | `get_wallet_balance()` | Reads SQL view `lunch.cashmove.report`, sums all `amount` values for the user, rounds to 2 decimal places, then adds `company.lunch_minimum_threshold` (overdraft allowance). No Python loop over raw records — delegates to view. | models/lunch_cashmove.py:26–31 | HIGH | MEDIUM |
| 7 | U182-C07 | Wallet / SQL View | `lunch.cashmove.report` | `init()` SQL view | UNION of: (a) lunch_cashmove rows (positive credit amounts) and (b) lunch_order rows where `state IN ('ordered','confirmed')` and `active=True`, with price negated. Debit registered at `ordered` state, not `confirmed`. | report/lunch_cashmove_report.py:24–51 | HIGH | HIGH |
| 8 | U182-C08 | Bulk Confirm | `lunch.supplier` | `action_confirm_orders()` | Fetches today's `sent` orders for suppliers available today via `_get_current_orders(state='sent')`, calls `action_confirm()` on the set. No `_confirm_many()` method exists — bulk confirmation is supplier-scoped. | models/lunch_supplier.py:372–384 | HIGH | LOW |
| 9 | U182-C09 | Product Category | `lunch.product.category` | Model fields | Fields: `name` (translate), `company_id` (Many2one res.company), `product_count` (computed via `_read_group`), `active`, `image_1920` (default lunch.png). Inherits `image.mixin`. | models/lunch_product_category.py:11–27 | HIGH | LOW |
| 10 | U182-C10 | Category Cascade | `lunch.product.category` | `action_archive()` / `action_unarchive()` | Archiving/unarchiving a category propagates to its products via `_sync_active_products()` → `_sync_active_from_related()`. Product is archived only when both its supplier AND category are inactive. | models/lunch_product_category.py:35–47 | HIGH | MEDIUM |
| 11 | U182-C11 | Alert | `lunch.alert` | Model + `_notify_chat()` | Two modes: `alert` (in-app banner) and `chat` (Odoo Discuss notification via cron). Recipients filter: everyone / ordered last week/month/year. Weekday availability + optional `until` date. Each alert has its own `ir.cron`. | models/lunch_alert.py:19–195 | HIGH | MEDIUM |
| 12 | U182-C12 | Alert Cron | `lunch.alert` | `_sync_cron()` | Cron activated only when `mode=chat`, `active=True`, and not past `until`. Cron calls `_notify_chat()`. Multiple alerts each get a dedicated cron record; cron deleted on alert unlink. | models/lunch_alert.py:84–114 | HIGH | LOW |
| 13 | U182-C13 | Company Scope — Supplier | `lunch.supplier` | `company_id` | `company_id` is a related field from `partner_id.company_id`, stored=True. Multi-company ir.rule filters suppliers to `company_ids + [False]`. On write, if `company_id` changes, related orders are also updated. | models/lunch_supplier.py:52; security/lunch_security.xml:68–72 | HIGH | HIGH |
| 14 | U182-C14 | Company Scope — Order/Product | `lunch.order`, `lunch.product` | `company_id` ir.rules | Multi-company record rules on `lunch.order`, `lunch.product`, `lunch.product.category`, `lunch.location` all filter by `company_id in company_ids + [False]`. | security/lunch_security.xml:74–96 | HIGH | MEDIUM |
| 15 | U182-C15 | Auto-Confirm / Auto-Email | `lunch.supplier` | `_send_auto_email()` / cron | No `auto_confirm` field. Supplier has `send_by` (phone/mail). If `mail`, a cron fires daily at `automatic_email_time` to email today's ordered lines and transition them to `sent`. Phone suppliers require manual `action_send_orders()`. | models/lunch_supplier.py:129–293 | HIGH | MEDIUM |
| 16 | U182-C16 | No Accounting Integration | `lunch.order` | (none) | Lunch module has zero imports of or references to `account.move`. Wallet is internal (lunch.cashmove); no journal entries created. Lunch financial data is entirely within the lunch schema. | models/ (grep: no account.move reference) | HIGH | LOW |
| 17 | U182-C17 | Single-Line Model | `lunch.order` | `quantity` field | There is no separate `lunch.order.line` model. `lunch.order` IS the line, with a `quantity` Float field (default 1). The `create()` method merges duplicate lines by incrementing quantity instead of creating new records. | models/lunch_order.py:44, 159–175 | HIGH | HIGH |
| 18 | U182-C18 | Order Merge | `lunch.order` | `create()` / `_find_matching_lines()` | On create, if an identical `(user_id, product_id, date, note, toppings, lunch_location_id)` line already exists in state `new`, quantity is incremented on that line instead. On write with merge conditions, duplicate lines are deactivated and quantity moved. | models/lunch_order.py:159–207 | HIGH | HIGH |
| 19 | U182-C19 | Wallet Guard | `lunch.order` | `_check_wallet()` | After any quantity change or new order, `_check_wallet()` is called; raises `ValidationError` if wallet balance falls below 0 (after threshold). `update_quantity(-n)` also deactivates the line if quantity ≤ 0. | models/lunch_order.py:236–257 | HIGH | MEDIUM |
| 20 | U182-C20 | Record Rules — Security | `lunch.order` | ir.rules | Regular users can only delete orders in `new` or `cancelled` state. Write rule: user can only edit own non-confirmed orders. Managers bypass both rules. Cashmove: users see only their own records; managers see all. | security/lunch_security.xml:25–66 | HIGH | MEDIUM |

---

## Key Source Files

| File | Purpose |
|------|---------|
| `models/lunch_order.py` | `lunch.order` — main order/line model, state machine, wallet check, merge logic |
| `models/lunch_cashmove.py` | `lunch.cashmove` — manual credit entries; `get_wallet_balance()` |
| `models/lunch_supplier.py` | `lunch.supplier` — vendor config, weekday schedule, cron, auto-email, bulk confirm |
| `models/lunch_product.py` | `lunch.product` — product definition, favorites, company scope |
| `models/lunch_product_category.py` | `lunch.product.category` — category with archive cascade |
| `models/lunch_alert.py` | `lunch.alert` — configurable alerts, chat cron |
| `models/lunch_location.py` | `lunch.location` — simple location (name, address, company_id) |
| `models/res_company.py` | `lunch_minimum_threshold` (overdraft), `lunch_notify_message` |
| `models/res_users.py` | `last_lunch_location_id`, `favorite_lunch_product_ids` extensions |
| `report/lunch_cashmove_report.py` | `lunch.cashmove.report` — SQL view (UNION credits + debits) |
| `security/lunch_security.xml` | Groups, record rules, multi-company rules |
| `security/ir.model.access.csv` | ACL table — user/manager read/write/create/delete rights |

---

## Absence Findings (Confirmed NOT Present)

| Feature | Verdict | Evidence |
|---------|---------|---------|
| `_confirm_many()` method | ABSENT — no such method anywhere in module | grep confirmed no output |
| `auto_confirm` field | ABSENT — not on supplier, location, or any model | grep confirmed no output |
| `lunch.order.line` model | ABSENT — `lunch.order` is the line | No such model found |
| `account.move` integration | ABSENT — no accounting imports or references | grep confirmed no output |
