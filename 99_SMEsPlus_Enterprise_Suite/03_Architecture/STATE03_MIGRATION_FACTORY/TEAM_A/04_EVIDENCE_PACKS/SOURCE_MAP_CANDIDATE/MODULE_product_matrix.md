# Source Map (candidate) — `product_matrix`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `product_matrix` |
| Display name | Product Matrix |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `5e4ae7b7447bbef0` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/product_matrix/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (2): `purchase_product_matrix`, `sale_product_matrix`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Technical module: Matrix Implementation
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `product.template`, `product.template.attribute.value`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `product.template`, `product.template.attribute.value`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`base.group_user`); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 18 of 18 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — product_matrix (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities; core / optional / conditional
- Technical support module: provides the grid ("matrix") of product variants used to enter many variant quantities at once; manifest states it is used through Sale Matrix or Purchase Matrix (product_matrix/__manifest__.py:5-8).
- Depends on account; not auto_install; pulled in as a dependency by sale_product_matrix (depends sale) and purchase_product_matrix (depends purchase) (product_matrix/__manifest__.py:11; sale_product_matrix/__manifest__.py:12; purchase_product_matrix/__manifest__.py:12).
- Front-end assets: matrix dialog and configurator hook loaded in the backend (product_matrix/__manifest__.py:20-27).
- Side effect on install: all internal users (base user group) are granted the product variants group, i.e. the variants feature is switched on for them (product_matrix/data/res_groups.xml:4-6).

## B. Business objects, relationships, lifecycle
- No new stored objects. Adds a matrix builder on Product Template: header row = values of the first attribute line; each further attribute-line combination becomes a row; each cell holds the attribute-value combination, a quantity starting at 0, and a flag whether the combination is possible (product_matrix/models/product_template.py:11-60).
- Only active attribute values of valid attribute lines are used (product_matrix/models/product_template.py:16-20).
- Header cells show attribute names joined; can show combined extra price converted from the template currency to the requested currency at today's date; a blank name is used when a template has a single attribute line (product_matrix/models/product_template.py:66-85).
- Report block renders the grids of an order (each grid: header row, body rows, extra price template) (product_matrix/views/matrix_templates.xml:3-29).
- No state transitions of its own.

## C. Validations, automation, security, multi-company
- No constraints, access CSV, record rules, cron or automation in this module (module file listing: no security directory; grep of files).
- Company for currency conversion: passed company, else template company, else current company (product_matrix/models/product_template.py:13).
- Impossible combinations are flagged, not rejected here (product_matrix/models/product_template.py:48-54); enforcement UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs (module ownership)
- Sale order side consumes the grid: sale_product_matrix (sale_product_matrix/models/sale_order.py:135). Purchase side: purchase_product_matrix (purchase_product_matrix/models/purchase.py:125). Order lines, pricing, stock and accounting stay with those modules and sale/purchase/account. Product/variant model owned by product.

## E. Configuration/defaults that change outcomes
- display_extra_price argument controls whether attribute extra prices appear (docstring notes it is used to hide extra prices on purchases) (product_matrix/models/product_template.py:15, :72-73).
- Variant creation mode of attributes (always / dynamic / no_variant) is exercised in tests (TEST: product_matrix/tests/common.py) — effect on grid content UNKNOWN — EVIDENCE INSUFFICIENT.

## F. Extension path (grep of _inherit)
- product_matrix extends product.template and product.template.attribute.value (product_matrix/models/product_template.py:9, :64). Dependants by manifest: sale_product_matrix, purchase_product_matrix, test_sale_product_configurators.

## G. Not verified
- Grid quantity-to-order-line conversion: UNKNOWN — EVIDENCE INSUFFICIENT (in sale/purchase matrix modules, not read).
- Front-end JS behaviour of the dialog: UNKNOWN — EVIDENCE INSUFFICIENT.
- Demo data content (product_matrix/data/product_matrix_demo.xml): UNKNOWN — EVIDENCE INSUFFICIENT.

