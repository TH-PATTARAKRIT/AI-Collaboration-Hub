# U182 — lunch Module: Neutral Knowledge Summary
**Unit:** U182 | **Module:** lunch | **Odoo Version:** 19.0 Community  
**Audience:** Migration designers, functional consultants, integration architects  

---

## Module Purpose

The lunch module provides an internal employee lunch-ordering system. Employees browse a menu of products offered by one or more vendors, place orders against a personal wallet balance, and receive notification when orders are delivered. Managers configure vendors, top up employee wallets, manage orders in bulk, and monitor the ledger.

---

## Core Concepts

### Order Lifecycle

An employee creates an order in the **To Order** state. After review the employee submits it, moving it to **Ordered**. A manager (or automated cron) sends the consolidated order to the vendor, moving it to **Sent**. When the food arrives the manager marks it **Received** (confirmed). At any point before delivery an order may be **Cancelled**.

The five states are: `new` → `ordered` → `sent` → `confirmed`, with `cancelled` reachable from `new` or `ordered`.

### Wallet System

Each employee has a virtual wallet. Manual top-ups (credits) are recorded as positive cash-move entries. When an employee submits an order the price is treated as a negative entry in the ledger. The running balance is the sum of all entries for that employee. A company-level overdraft threshold can be configured so employees may order slightly beyond their balance.

Wallet debits are registered at the **ordered** state, not at confirmation. If the wallet would go negative after placing an order, a validation error prevents the action.

### Vendor Configuration

Vendors (suppliers) hold: contact information (name, email, phone, address via a linked partner), a weekly availability schedule (boolean flags per weekday), an optional recurrency end date, a timezone, a responsible user (the person who places orders), a delivery mode (phone or email), and an automatic send time for email orders.

Each vendor has a dedicated background job (cron) that fires daily at the configured time. If the send mode is email, the cron compiles today's ordered lines and emails them to the vendor, then transitions those orders to sent. If the send mode is phone, the cron is inactive and a manager must manually trigger the send.

Archiving a vendor also archives all its products. Disabling a weekday on a vendor cancels any pending orders for that day in the future.

### Product and Category

Products belong to a vendor and a category. Price is stored in monetary form tied to the company currency. Products support three tiers of extras (toppings), each with a configurable label and quantity constraint (optional, one-or-more, or exactly-one). Each topping tier is stored in a dedicated many-to-many relationship.

Categories carry an image (defaulting to the lunch module icon) and a per-company scope. Archiving a category cascades to its products if the vendor is also inactive.

### Order Merging (Deduplication)

When an employee creates a second order for the same product, on the same date, at the same location, with the same notes and toppings, the system increments the quantity on the existing line rather than creating a duplicate record. The same merging logic applies when editing an order.

### Alerts

Managers can configure alerts to inform employees at lunch ordering time. An alert has a display mode: either an in-app banner visible when the employee opens the lunch portal, or a chat notification sent via Odoo Discuss at a configured time. Alerts support weekday schedules, an optional expiry date, recipient targeting (everyone or employees who ordered within the last week/month/year), and location filtering.

### Security Model

Two groups exist: **User** (can place and view own orders, read products and categories) and **Administrator** (full access: create products, top up wallets, manage orders, confirm/cancel).

Record rules enforce:
- Users can only edit their own non-confirmed orders.
- Users can only delete orders in `new` or `cancelled` state.
- Users can only see their own wallet entries; managers see all.
- All main models respect multi-company rules (orders, products, categories, suppliers, locations).

### No Accounting Integration

The lunch module operates entirely within its own ledger. There is no connection to Odoo's accounting module. No journal entries are created by lunch operations. Wallet balances exist only as `lunch.cashmove` records.

---

## Migration Design Notes

| Topic | Note |
|-------|------|
| Single-line model | `lunch.order` is both the order header and the line. Quantity is on the order. Any migration expecting a separate line model will find none. |
| Wallet debit timing | Wallet is debited at `ordered`, not `confirmed`. Reporting on confirmed orders only will miss in-flight debits. |
| SQL view for balance | Wallet balance uses a database view (`lunch.cashmove.report`) that unions manual credits with order debits. Custom reporting must replicate this view or query the underlying tables directly. |
| Auto-email cron per supplier | Each supplier owns a dedicated `ir.cron`. On migration, cron records must be recreated and linked. Bulk import of suppliers without cron creation will break the email flow. |
| Alert cron per alert | Same pattern: each `lunch.alert` owns a dedicated `ir.cron`. |
| Company_id on supplier | Derived from `partner_id.company_id`. Setting company scope on a supplier requires setting it on the partner first, not on the supplier directly. |
| No auto_confirm | There is no automatic order confirmation on delivery or timeout. Confirmation is always a manual manager action (individually or bulk via supplier button). |
| Overdraft threshold | `company.lunch_minimum_threshold` is added to the raw sum; a negative value creates an overdraft allowance. Default is 0. |
| Favorite products | `lunch.product.favorite_user_ids` many2many; managed per-user, company-scoped. |
