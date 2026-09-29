# Source Map (candidate) — `sale_product_matrix`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_product_matrix` |
| Display name | Sale Matrix |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `69d7a7383c753d08` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_product_matrix/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale`, `product_matrix`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_sale_product_configurators`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Add variants to Sales Order through a grid entry.
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `sale.order`, `sale.order.line`, `product.template`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `sale.order`, `sale.order.line`, `product.template`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 25 of 25 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: sale_product_matrix (revision 19.0.post20260921)
Scope: Odoo Community read-only study. Pointers `module/path:LINE`. No tests exist in this module.

## A. Capabilities and activation
- Lets a salesperson enter quantities for many variants of one product in a grid instead of adding variants one at a time (sale_product_matrix/__manifest__.py:5-9). Depends on sale and product_matrix (sale_product_matrix/__manifest__.py:12); product_matrix itself depends on account (product_matrix/__manifest__.py:11).
- Optional module: no auto_install and no application flag (sale_product_matrix/__manifest__.py:3-28). Per-product choice is conditional: mode selector shows only when the product has configurable attributes (sale_product_matrix/views/product_template_views.xml:9-13).
- Printed quotation shows the grid before the line table (sale_product_matrix/report/sale_report_templates.xml:3-9).

## B. Business objects and behaviour
- Product template gains "Add product mode": Product Configurator (default) or Order Grid Entry (sale_product_matrix/models/product_template.py:9-17). The single-variant lookup reports the chosen mode only for products with configurable attributes; otherwise configurator (sale_product_matrix/models/product_template.py:19-25).
- Sales order gains a print-grids flag (default on; visible only in technical mode) and three non-stored working fields holding the grid being edited (sale_product_matrix/models/sale_order.py:14,26-34; sale_product_matrix/views/sale_order_views.xml:11-17).
- Opening a grid builds the matrix for the template with current order quantities filled in (sale_product_matrix/models/sale_order.py:36-41,121-150).
- Applying a grid processes only changed cells: finds or creates the variant for the attribute combination (sale_product_matrix/models/sale_order.py:53-58); if a line exists and quantity set to zero, the line is removed in Quotation/Quotation Sent, otherwise quantity is set to 0 (sale_product_matrix/models/sale_order.py:74-81); if quantity changed and exactly one line exists it is updated (sale_product_matrix/models/sale_order.py:94-97); new cells create new lines appended after last sequence (sale_product_matrix/models/sale_order.py:104-119). Combo-item lines are excluded from matching (sale_product_matrix/models/sale_order.py:62,146).
- Report grid appears only for grid-mode templates having more than one line on the order and only rows with non-zero quantity (sale_product_matrix/models/sale_order.py:152-169).
- Line exposes the template's mode as a related read-only field (sale_product_matrix/models/sale_order_line.py:9).

## C. Validations, security, multi-company
- Only explicit rule: changing quantity of a variant present in several lines is refused (sale_product_matrix/models/sale_order.py:94-95).
- No access rules, groups, or record rules defined here (no security directory; sale_product_matrix/__manifest__.py:13-17). Company scoping is inherited: the matrix is built with the order's company and currency (sale_product_matrix/models/sale_order.py:135-138).
- Observation: the view hides optional-products field when the mode equals "grid" (sale_product_matrix/views/product_template_views.xml:28), while the stored value is "matrix" (sale_product_matrix/models/product_template.py:12); whether the hide ever triggers: UNKNOWN — EVIDENCE INSUFFICIENT

## D. Handoffs
- Lines produced are ordinary sale order lines; pricing, taxes, delivery, invoicing owned by sale and downstream modules. Variant creation on demand is a product-module function (sale_product_matrix/models/sale_order.py:58). No accounting/purchase/analytic logic in this module.

## E. Configuration
- Per product template: add-product mode. Per order: print variant grids (sale_product_matrix/models/sale_order.py:14).

## F. Extension path
- Extends product.template, sale.order, sale.order.line (sale_product_matrix/models/*.py). Modules referencing it in manifests: test_sale_product_configurators (grep). No other module overrides its methods (grep of product_add_mode, _get_matrix, report_grids outside the module returned nothing).

## G. Not verified
- Client-side grid widget behaviour (sale_product_matrix/static/src/js): UNKNOWN — EVIDENCE INSUFFICIENT
- Grid rendering, extra-price display in product_matrix: UNKNOWN — EVIDENCE INSUFFICIENT
- Any automated test coverage: UNKNOWN — EVIDENCE INSUFFICIENT

