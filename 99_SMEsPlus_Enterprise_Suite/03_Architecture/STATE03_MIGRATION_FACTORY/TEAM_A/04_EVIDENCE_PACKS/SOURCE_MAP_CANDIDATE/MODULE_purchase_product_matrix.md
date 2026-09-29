# Source Map (candidate) — `purchase_product_matrix`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `purchase_product_matrix` |
| Display name | Purchase Matrix |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G03 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d236c38d7995d445` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/purchase_product_matrix/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `purchase`, `product_matrix`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Purchase / Add variants to your purchase orders through an Order Grid Entry.
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `purchase.order`, `purchase.order.line`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `purchase.order`, `purchase.order.line`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 23 of 23 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: purchase_product_matrix
Source revision: 19.0.post20260921 (Odoo 19.0 Community). Pointers `module/path:LINE`; (TEST) = test-derived.
Manifest: "Purchase Matrix", fills purchase orders by choosing variant quantities in a grid (purchase_product_matrix/__manifest__.py:2-9); depends purchase + product_matrix (:12).

## A. Capabilities
1. Grid entry of variant quantities for a configurable product template on a purchase order line (purchase_product_matrix/models/purchase.py:27-31 load, :36-116 apply). OPTIONAL: no `auto_install` key in the manifest (purchase_product_matrix/__manifest__.py:3-28), so it is installed on demand.
2. Print variant grids on the RFQ/quotation and purchase order PDFs (purchase_product_matrix/report/purchase_quotation_templates.xml:3-9; purchase_product_matrix/report/purchase_order_templates.xml:3-9). CONDITIONAL on order flag "Print Variant Grids" (default True) (purchase_product_matrix/models/purchase.py:11) and on `get_report_matrixes` rules (below).
3. Client widget on the line product field that opens the matrix when a template with several variants is picked, or on "edit configuration" (purchase_product_matrix/static/src/js/purchase_product_field.js:48-70).

## B. Objects and behaviour
- Extends purchase.order (technical non-stored fields grid, grid_update, grid_product_tmpl_id; purchase_product_matrix/models/purchase.py:23-25) and purchase.order.line (template, "is configurable", attribute values; :160-165). "Configurable" mirrors `has_configurable_attributes` on the product template (product/models/product_template.py:173).
- Apply logic per changed cell: find or create the variant for the attribute combination (:51 calling product/models/product_template.py:1198); compare with quantity already on lines of that variant/no-variant combination; no difference means skip (:54-62).
  - Quantity set to 0 on existing lines: lines removed if the order is draft/sent, otherwise quantity set to 0 (:66-73).
  - Existing single line: quantity updated (:89). More than one existing line for that variant: validation error "cannot change the quantity of a product present in multiple purchase lines" (:86-87).
  - No line yet: new line with default line values, sequence continuing the last line (:96-108).
  - Prices/dates/names of new or modified lines are recomputed via the standard product-change logic (:114-116; purchase/models/purchase_order_line.py:397).
- Grid for reading: built from product_matrix for the order's company and currency and overlaid with existing quantities (:118-139; product_matrix/models/product_template.py:11).
- Report grids: printed only when the flag is set, only for configurable templates that appear on more than one line, and rows whose quantities are all zero are dropped (:141-157).
- Order lifecycle states are owned by purchase: RFQ, RFQ Sent, To Approve, Purchase Order, Cancelled (purchase/models/purchase_order.py:105-111). This module only reads draft/sent to decide removal vs zeroing (:68).

## C. Validations, automation, security
- Single explicit validation: multiple-line quantity change (purchase_product_matrix/models/purchase.py:86-87).
- The hook `_must_delete_date_planned` is extended so that a grid change, like an order-line change, does not push order-level planned-date updates onto the lines' own planned dates (purchase_product_matrix/models/purchase.py:33-34; base purchase/models/purchase_order.py:424-437).
- Views: product template column replaces the variant column and is read-only when state is purchase/to approve/cancel (purchase_product_matrix/views/purchase_views.xml:9-25); the print flag is shown only to the technical/debug group `base.group_no_one` (:31-33).
- No ACL, record rules or groups added (no security folder). Company scoping is inherited from purchase order rules (purchase/security/purchase_security.xml:41-49). Multi-company only enters via the company passed to the matrix (purchase_product_matrix/models/purchase.py:125-127).

## D. Handoffs
- product owns variant creation and "configurable" definition; product_matrix owns the matrix computation and widget hook (purchase_product_matrix/static/src/js/purchase_product_field.js:3); purchase owns lines, pricing and states.
- Downstream inventory/accounting effects are those of the created PO lines (owned by purchase_stock/account); nothing specific is added here.
- (TEST) UI tour builds a matrix PO: dynamic variants are created only for non-zero cells; a variant with two zero cells is not created; purchased quantity totals per template/variant after confirmation (purchase_product_matrix/tests/test_purchase_matrix.py:14-43); never-variant attribute text is translated to the vendor's language on the line name (:45-67).

## E. Configuration that changes outcomes
- Product attribute "create variant" mode (dynamic/never) decides whether cells create variants or only no-variant attribute lines (tests :24-43, TEST).
- Vendor language affects the generated line name (TEST :45-67).
- Per-order "Print Variant Grids" flag (purchase_product_matrix/models/purchase.py:11).

## F. Effective extension path
- Extends purchase.order and purchase.order.line only.
- Other Community modules touching matrix helpers: product_matrix (base), sale_product_matrix (sales analogue). No other module was found extending these grid fields/methods on purchase.order.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour for products flagged not purchasable (domain on template field only, purchase_product_matrix/models/purchase.py:163).
- UNKNOWN — EVIDENCE INSUFFICIENT: mixed-UoM or multi-currency cell pricing beyond standard product-change recompute.
- UNKNOWN — EVIDENCE INSUFFICIENT: report template content of `product_matrix.matrix` (not opened; belongs to product_matrix).

