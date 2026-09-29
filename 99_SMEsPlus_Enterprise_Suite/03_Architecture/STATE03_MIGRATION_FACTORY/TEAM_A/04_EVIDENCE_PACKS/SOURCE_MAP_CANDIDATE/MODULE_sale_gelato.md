# Source Map (candidate) — `sale_gelato`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_gelato` |
| Display name | Gelato |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `07b2753f74392316` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_gelato/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale`, `delivery`
- Direct dependents in 300-module list (1): `sale_gelato_stock`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `website_sale_gelato`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Place orders through Gelato's print-on-demand service
- Inventory of user-facing artifacts (counts): menu items 0, views 6, window actions 0, server actions 0, reports 0, mail templates 1, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (9): `sale.order`, `sale.order.line`, `product.document`, `product.template`, `product.product`, `res.company`, `delivery.carrier`, `res.partner`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `sale.order`, `sale.order.line`, `product.document`, `product.template`, `product.product`, `res.company`, `delivery.carrier`, `res.partner`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 39 of 39 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_gelato
Source revision: 19.0.post20260921 | Module: "Gelato" — print-on-demand ordering (sale_gelato/__manifest__.py:4-5) | depends: sale, delivery (:7) | NOT auto_install; LGPL-3 (:20)
Basis: static reading of all models, controller, utils, data; test names and one test list read (three test files); mail template body not opened.

## A. Capabilities and optionality
- A1. Sell print-on-demand products fulfilled and shipped by the external service Gelato: products are synchronised from a Gelato template, orders are sent to Gelato on confirmation, shipping is quoted by Gelato, status updates come back through a webhook. sale_gelato/models/product_template.py:51-93; sale_gelato/models/sale_order.py:68-77,101-138; sale_gelato/controlers/main.py:19-94
- A2. Optional module (installed explicitly); credentials are entered per company in Settings (API key, webhook secret; password-masked). sale_gelato/wizards/res_config_settings.py:9-10; sale_gelato/wizards/res_config_settings_views.xml:9-16
- A3. Two ready-made delivery methods (Standard, Express; rate-based) with zero-price service products used as the shipping line. sale_gelato/data/delivery_carrier_data.xml:4-20; sale_gelato/data/product_data.xml:4-22
- A4. Inventory bypass is added by sale_gelato_stock (see its note); web shop support by website_sale_gelato (manifest grep).

## B. Objects, relationships, lifecycle
- B1. Product template gets a Gelato template reference (entered by user), a Gelato product identifier (system-set, read-only; mirrored to variants), print images (documents flagged Gelato) and a "missing print images" flag. sale_gelato/models/product_template.py:13-47; sale_gelato/models/product_product.py:9; sale_gelato/models/product_document.py:9-12
- B2. Synchronisation button (visible when a template reference exists; not on variants): fetches the template from Gelato with the current company's key; a template with one variant sets the identifier directly; otherwise creates missing attributes, values and attribute lines, assigns the identifier to each matching variant and deletes variants that Gelato does not offer. sale_gelato/models/product_template.py:51-93,97-160; sale_gelato/views/product_template_views.xml:59-60
- B3. Print images: one per print placement (placement names "1"/"front" normalised to "default"); duplicates from multiple layers ignored; the user must upload the image files; Gelato images are hidden from ordinary product documents. sale_gelato/models/product_template.py:162-190,198-200
- B4. Order confirmation: after normal confirmation, for orders containing Gelato products the shipping address is checked (name, street, city, country, email, plus postcode except in listed countries), then a DRAFT order is created at Gelato (items with print image links, chosen shipping method or "cheapest", customer address trimmed to Gelato field lengths). sale_gelato/models/sale_order.py:68-77,81-117; sale_gelato/models/res_partner.py:11-28; sale_gelato/const.py:3-10
- B5. Commit safety: the draft is confirmed at Gelato only after the local transaction commits, and deleted at Gelato if it rolls back; failures at those later steps only post a chatter note. sale_gelato/models/sale_order.py:122-125,160-224
- B6. Items quantity is sent as whole number (fraction truncated). sale_gelato/models/sale_order.py:155
- B7. Webhook events (order-status): failed -> chatter note with Gelato comment; canceled -> the sales order is cancelled and noted; in transit -> status email with tracking links/codes posted on the order; delivered -> status email; returned -> chatter note. sale_gelato/controlers/main.py:40-93
- B8. Shipping rate: Gelato quote per product; price = sum over quotes of the cheapest matching method of the carrier's service type (normal/express); no matching method -> "not available". sale_gelato/models/delivery_carrier.py:59-116
- B9. Delivery choice: Gelato orders see only Gelato carriers, other orders never see Gelato carriers; the delivery wizard defaults to the first Gelato carrier. sale_gelato/models/delivery_carrier.py:24-57; sale_gelato/models/sale_order.py:54-66. (TEST) sale_gelato/tests/test_delivery_carrier.py:42-79

## C. Validations, security, multi-company
- C1. An order may not mix Gelato products with other goods; services and non-saleable lines (sections, notes) are allowed. Enforced on line create and write. sale_gelato/models/sale_order.py:33-50; sale_gelato/models/sale_order_line.py:11-20. (TEST) sale_gelato/tests/test_sale_order.py:16-50
- C2. Confirmation fails with a message when the shipping address is incomplete, or when Gelato refuses the order (whole confirmation rolls back). sale_gelato/models/sale_order.py:74-75,126-132. (TEST) test_sale_order.py:51
- C3. Credentials readable only by system administrators (field group). sale_gelato/models/res_company.py:9-10
- C4. Webhook is public with no CSRF but every status event must carry a signature equal to the company's stored secret (constant-time compare); missing secret or mismatch -> forbidden. Requests run under elevated rights. sale_gelato/controlers/main.py:19,35-37,97-116
- C5. Multi-company: the order's company supplies the key for ordering, quoting and webhook checks; template synchronisation uses the currently active company. sale_gelato/models/sale_order.py:119; sale_gelato/models/delivery_carrier.py:87; sale_gelato/models/product_template.py:61
- C6. Webhook when the order id does not exist: UNKNOWN — EVIDENCE INSUFFICIENT.
- C7. No new ACLs or record rules (no security folder).

## D. Handoffs
- D1. Fulfilment, printing, shipping, tracking: external Gelato service. Customer invoice and revenue: sale/account (unchanged). No purchase order or vendor bill is generated for the Gelato cost. UNKNOWN — EVIDENCE INSUFFICIENT on how Gelato's cost is accounted (not in this module).
- D2. Shipping charge: delivery (order line from carrier product, zero list price). sale_gelato/data/product_data.xml:11,21
- D3. Emails use template sale_gelato.order_status_update posted from the system partner. sale_gelato/controlers/main.py:75,82

## E. Configuration that changes outcomes
- E1. Company API key and webhook secret. sale_gelato/models/res_company.py:9-10
- E2. Product Gelato template reference and uploaded print images; variant attributes must match Gelato variants. sale_gelato/models/product_template.py:13,97-160
- E3. Carrier service type (standard/express). sale_gelato/models/delivery_carrier.py:15-20
- E4. Partner address completeness and country list without postcode. sale_gelato/const.py:3

## F. Effective extension path (modules)
- Depended on by: sale_gelato_stock, website_sale_gelato (manifest grep). Extends product.template/product/document, delivery.carrier, sale.order/line, res.partner/company/config settings.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: cost/margin handling for Gelato products, returns and refunds beyond the "returned" chatter note, order edits after confirmation (order changes are not resent), and the mail template content.

