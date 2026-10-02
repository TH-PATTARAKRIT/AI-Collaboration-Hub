# U125 — sale_subscription Community Presence Check
**Unit:** U125 | **G-Group:** G05 | **Priority:** P2 | **Date:** 2026-10-02
**GAP:** GAP-049 / Rank-12 | **Researcher:** DeepSeek Worker (Claude Sonnet 4.6)

## Presence Determination

**RESULT: ABSENT**

The directory `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_subscription` does not exist.

Verified via: `ls <addons>/sale_subscription` → exit code 1, "No such file or directory"

## sale_* Modules Present in Community (v19.0.post20260921)

Confirmed present (from `ls <addons> | grep "^sale"`):
- sale, sale_crm, sale_edi_ubl, sale_expense, sale_expense_margin
- sale_gelato, sale_gelato_stock, sale_loyalty, sale_loyalty_delivery
- sale_management, sale_margin, sale_mrp, sale_mrp_margin
- sale_pdf_quote_builder, sale_product_matrix, sale_project
- sale_project_stock, sale_project_stock_account, sale_purchase
- sale_purchase_project, sale_purchase_stock, sale_service
- sale_sms, sale_stock, sale_stock_margin, sale_stock_product_expiry
- sale_timesheet, sale_timesheet_margin, sales_team

**Subscription-adjacent modules also ABSENT:**
- `sale_temporal` — not found
- `sale_renting` — not found
- `product_rental` — not found

## sale.order / sale.order.line — Recurrence Fields Check

Grep of `subscription`, `recurrence`, `recurring`, `is_subscription`, `recurrence_id` across:
- `<addons>/sale/models/sale_order.py` — **zero matches**
- `<addons>/sale/models/sale_order_line.py` — **zero matches**
- `<addons>/sale/models/` (all files) — **zero functional matches**

The only reference to `sale_subscription` in the entire `sale` module appears in a docstring comment at:

**File:** `<addons>/sale/models/product_template.py:273-276`
**Content (comment only):**
> "Or by computing a different price (e.g. in `sale_subscription`, we ignore super when computing subscription prices). In some cases, the order of the overrides matters, which is why we need 2 separate methods (e.g. in `website_sale_subscription`, we must compute the subscription price before applying taxes)."

This is a developer note describing extension patterns, not a functional dependency. It confirms that `sale_subscription` and `website_sale_subscription` are treated as separate add-on modules that override Community hooks — they are not distributed in Community.

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U125-C01 | PRESENCE | addons/sale_subscription (directory) | ls exit=1 | ABSENT | Unconditional | GAP | Directory sale_subscription does not exist under odoo/addons in Community v19.0.post20260921 | Recurring subscription module not distributed in Community edition |
| U125-C02 | PRESENCE | addons/ (directory listing) | grep ^sale | ABSENT | Unconditional | GAP | No sale_temporal, sale_renting, or product_rental modules present in Community | Subscription-adjacent rental and temporal pricing modules absent from Community edition |
| U125-C03 | FIELD-CHECK | addons/sale/models/sale_order.py | grep subscription,recurrence | ABSENT | Unconditional | GAP | sale.order model contains zero fields for is_subscription, recurrence_id, or recurring_invoice | Base sales order model carries no subscription or recurrence fields |
| U125-C04 | FIELD-CHECK | addons/sale/models/sale_order_line.py | grep subscription,recurrence | ABSENT | Unconditional | GAP | sale.order.line model contains zero fields for is_subscription or recurrence_id | Sales order line model carries no recurrence or subscription tracking fields |
| U125-C05 | COMMENT-REF | addons/sale/models/product_template.py:273-276 | docstring comment | C1 | Developer note only | GAP | product_template.py docstring references sale_subscription as an extension hook override pattern, confirming it is a separate non-Community module | Product template code comment acknowledges subscription pricing as an enterprise extension pattern |
| U125-C06 | INVOICE-GEN | addons/sale_subscription (absent) | N/A | ABSENT | Unconditional | GAP,C1 | No recurring invoice generation method present in Community — _recurring_create_invoice equivalent does not exist | Automated recurring invoice creation requires the subscription extension module not present in Community |
| U125-C07 | CONTRACT | addons/sale_subscription (absent) | N/A | ABSENT | Unconditional | GAP | Contract start/end/renewal date logic absent from Community — no next_invoice_date or date_end fields on any sale model | Subscription contract lifecycle management including renewal dates is absent from Community edition |

## Summary Finding

`sale_subscription` is an **Enterprise-only** module in Odoo v19. Community v19.0.post20260921 provides no recurring subscription invoicing, no subscription contract management, no cron-triggered recurring billing, and no subscription stage model. The base `sale.order` and `sale.order.line` models have zero recurrence fields. GAP-049 is **OPEN** — this is a material gap for any SMEsPlus client requiring SaaS-style recurring billing.
