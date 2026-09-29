# Source Map (candidate) — `product_margin`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `product_margin` |
| Display name | Margins by Products |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `391f8f65d2f99306` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/product_margin/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / —
- Inventory of user-facing artifacts (counts): menu items 1, views 4, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `product.margin` (Product Margin)
- Objects extended from other modules (1): `product.product`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `product.product`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 27 of 27 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — product_margin (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities; core / optional / conditional
- Adds a per-product margin report computed from posted (optionally draft) customer invoices/credit notes and vendor bills over a date range (product_margin/__manifest__.py:6-13; product_margin/models/product_product.py:119-212).
- Depends only on account; not auto_install; installed on demand (product_margin/__manifest__.py:14).
- Entry point: a menu "Product Margins…" under the accounting reports management menu, which opens a wizard, then a list/form/graph of products (product_margin/views/product_product_views.xml:87; product_margin/wizard/product_margin.py:21-56).

## B. Business objects, relationships, lifecycle
- No new stored business object. A transient wizard (from date, to date, invoice state) sets report context; margin figures are computed, non-stored fields added to Product Variant (product_margin/wizard/product_margin.py:9-19; product_margin/models/product_product.py:14-49).
- Measures: average sale unit price, average purchase unit price, quantities invoiced (sale/purchase), turnover, total cost, expected sale (catalog list price x quantity), normal cost (product standard cost x purchased quantity), gaps, total margin, expected margin, and margin rates (product_margin/models/product_product.py:22-49, :186-211).
- Invoice-state filter options: "Paid" (posted + in payment/paid/reversed), "Open and Paid" (posted + all payment states incl. not paid/partial; default), "Draft, Open and Paid" (adds draft) (product_margin/models/product_product.py:138-146; product_margin/wizard/product_margin.py:15-19).
- Credit notes/refunds reduce quantities and amounts (sign inverted for refunds; refund amounts taken as negative) (product_margin/models/product_product.py:159-164) (TEST: product_margin/tests/test_product_margin.py:98 negative price in move lines).
- Only product lines (excluding section/note lines) are counted (product_margin/models/product_product.py:180).

## C. Validations, automation, security, multi-company
- Wizard is read/create/write for accounting users group (account.group_account_user); no delete (product_margin/security/ir.model.access.csv:2).
- No automation/cron. Wizard makes the result window non-editable and non-creatable (product_margin/wizard/product_margin.py:23).
- Multi-company: figures are limited to a single company — the forced-company context value if given, else the current company (product_margin/models/product_product.py:147-150, :179). Amounts are converted with the invoice currency rate at the invoice date via company-specific rates (product_margin/models/product_product.py:155-173).
- Group-by totals on non-stored fields are recomputed by overriding grouping so sums are correct (product_margin/models/product_product.py:51-117) (TEST: product_margin/tests/test_product_margin.py:48 aggregates, :154 grouping sets).

## D. Handoffs (module ownership)
- Source data owned by account (invoice lines and moves; product_margin/models/product_product.py:151-153, :165-166). Product costs/prices owned by product (standard_price, list_price; product_margin/models/product_product.py:164, :207). No inventory or sales-order data is read; "expected" figures use product catalog price and standard cost, not stock valuation.

## E. Configuration/defaults that change outcomes
- Default period: current calendar year (Jan 1 to Dec 31) in both wizard and compute fallback (product_margin/wizard/product_margin.py:13-14; product_margin/models/product_product.py:126-127).
- Default invoice state "open_paid" (product_margin/models/product_product.py:128).
- Product standard cost (cost method setting on product) drives "normal cost" — configuration is in the product module (product_margin/models/product_product.py:207).

## F. Extension path (grep of _inherit)
- Extends only product.product (product_margin/models/product_product.py:12). No other module manifest in the addons tree lists it as a dependency (grep of manifests).

## G. Not verified
- Behaviour of margin with multi-currency edge cases beyond the rate join: UNKNOWN — EVIDENCE INSUFFICIENT.
- View-level column/group visibility (product_margin/views/product_product_views.xml beyond the menu): UNKNOWN — EVIDENCE INSUFFICIENT.

