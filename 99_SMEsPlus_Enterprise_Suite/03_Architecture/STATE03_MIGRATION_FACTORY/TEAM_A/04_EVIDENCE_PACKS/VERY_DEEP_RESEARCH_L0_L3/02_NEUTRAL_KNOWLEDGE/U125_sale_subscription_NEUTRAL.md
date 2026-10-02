# U125 — Subscription Billing Module: Neutral Knowledge
**Unit:** U125 | **G-Group:** G05 | **Priority:** P2 | **Date:** 2026-10-02
**GAP:** GAP-049 / Rank-12 | **Class:** ABSENT throughout

## Purpose

This neutral knowledge file documents the findings of unit U125 regarding recurring subscription billing capability in the Community edition of Odoo version 19. All claims use plain-prose neutral references per VDR Neutral-ref column rules.

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U125-N01 | PRESENCE | addons/sale_subscription (directory) | ls exit=1 | ABSENT | Unconditional | GAP | The recurring subscription module directory is absent from Community edition addons | Recurring subscription billing module is not distributed in Community edition |
| U125-N02 | PRESENCE | addons/ (directory listing) | grep sale modules | ABSENT | Unconditional | GAP | No rental or time-based pricing adjacent modules found alongside the absent subscription module | Rental and time-based product pricing extension modules are also absent from Community edition |
| U125-N03 | FIELD-CHECK | addons/sale/models/sale_order.py | zero grep matches | ABSENT | Unconditional | GAP | The base sales order model contains no fields to designate an order as a subscription or attach a recurrence schedule | Base sales order has no subscription designation or recurrence scheduling fields |
| U125-N04 | FIELD-CHECK | addons/sale/models/sale_order_line.py | zero grep matches | ABSENT | Unconditional | GAP | The sales order line model contains no fields for subscription status or recurrence identifiers | Sales order line has no subscription status or recurrence identifier fields |
| U125-N05 | COMMENT-REF | addons/sale/models/product_template.py:273-276 | docstring | C1 | Developer documentation only | GAP | A developer comment in the base product pricing hook explicitly references the subscription module as a separate extension that overrides Community pricing logic | Developer note in product pricing code acknowledges subscription pricing as a separate enterprise extension that overrides Community pricing logic |
| U125-N06 | INVOICE-GEN | addons/sale_subscription (absent) | N/A | ABSENT | Unconditional | GAP,C1 | No automated recurring invoice generation mechanism exists in Community edition | Automated recurring invoice generation for subscriptions is absent from Community edition |
| U125-N07 | CONTRACT | addons/sale_subscription (absent) | N/A | ABSENT | Unconditional | GAP | No contract renewal date, next billing date, or subscription stage tracking exists in any Community sale model | Subscription contract lifecycle management including renewal dates and stage tracking is absent from Community edition |

## Architectural Observation

The Odoo Community v19 sales module provides a complete one-time order-to-invoice workflow but has no recurring billing capability. The subscription module that provides contract management, recurring invoice scheduling, and payment-token-based automatic collection is confirmed to be an Enterprise-only component. Any migration plan for SaaS-oriented SMEsPlus clients must account for this gap through one of: (a) Enterprise edition adoption, (b) a third-party Community subscription add-on, or (c) custom development.
