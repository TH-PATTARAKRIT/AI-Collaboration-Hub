# Source Map (candidate) — `uom`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `uom` |
| Display name | Units of measure |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `0660e409a9e97e43` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/uom/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`
- Direct dependents in 300-module list (4): `analytic`, `barcodes_gs1_nomenclature`, `hr_timesheet`, `product`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `l10n_cl`
- Custom / third-party modules that declare a dependency (name — license only) (2): `odoo19_uom_ext` — no-license, `smesplus_uom_ext` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / —
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `uom.uom` (Product Unit of Measure)
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `uom.uom` ← Community: `account`, `hr_timesheet`, `l10n_ar`, `l10n_cl`, `l10n_eg_edi_eta`, `l10n_es_edi_facturae`, `l10n_hu_edi`, `l10n_id_efaktur_coretax`, `l10n_in`, `l10n_tr_nilvera` … (+3); open-license custom/third-party scanned: `smesplus_uom_ext`
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`group_uom`); record rules 0 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 60 of 60 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — uom
Source revision: 19.0.post20260921 | Module: "Units of measure" (uom/__manifest__.py:5), category Sales/Sales (:7), LGPL-3 (:26). Depends only on base (:8). Basis: static reading of models, data, security, views, tests, and a grep for consumers.

## A. Capabilities and optionality
- A1. Master list of units of measure (UoM) with a conversion ratio expressed against a "reference unit"; used to convert quantities and unit prices between units. uom/models/uom_uom.py:17-19,36-38,147-176,196-203
- A2. Units form a chain/tree rather than fixed categories: each unit says "contains N of [reference unit]"; the absolute factor is the product along the chain. Units with no reference unit are the roots (e.g., Units, Hours, mm, m², ml, g, KWH). uom/models/uom_uom.py:20-21,36-43,69-75; uom/data/uom_data.xml:12-15,29-32,45-48,68-71,74-77,91-94,188-191
- A3. One shared rounding precision for every unit, taken from the decimal-precision setting named "Product Unit" (default 2 digits, created with forcecreate and noupdate). uom/models/uom_uom.py:62-67; uom/data/uom_data.xml:2,5-8
- A4. Helper operations offered to other modules: round, compare, is-zero with that precision; convert quantity; convert price; round a quantity to a multiple of a packaging quantity; test whether two units share a root reference. uom/models/uom_uom.py:116-137,147-230
- A5. Conversion rounding defaults to rounding UP into the destination unit; when source equals destination there is no conversion. Optional switch to skip rounding. uom/models/uom_uom.py:147-176 (TEST) uom/tests/test_uom.py:29-38 (Score example: 2 units become 1 Score)
- A6. Multi-unit feature is conditional: the group "Manage Multiple Units of Measure" (uom.group_uom) exists here but is not granted to anyone by this module; other modules gate unit fields/columns on it. uom/security/uom_security.xml:4-6; e.g. sale/views/sale_order_line_views.xml:17, mrp/report/mrp_report_bom_structure.py:104, product/models/product_catalog_mixin.py:131
- A7. Switch that grants the group: setting "Units of Measure & Packagings" (implied group) in product; shown in Sales, Purchase, Accounting and Inventory settings. product/models/res_config_settings.py:9; sale/wizard/res_config_settings_views.xml:25; purchase/views/res_config_settings_views.xml:60; account/views/res_config_settings_views.xml:199; stock/views/res_config_settings_views.xml:144
- A8. Also enabled by force: sale_timesheet makes every internal user (base.group_user) imply this group; Mexican localisation sets the setting on at install. sale_timesheet/data/sale_service_data.xml:15-16; l10n_mx/__init__.py:5-7, l10n_mx/__manifest__.py:48
- A9. Optionality: not auto_install, not an application; it is a hard dependency of product (and thus of most trade modules) and of analytic, hr_timesheet, barcodes_gs1_nomenclature, l10n_cl (direct-dependency scan of all manifests). uom/__manifest__.py:8,19
- A10. UI: menu entries are contributed by other modules under names "Units & Packagings" (sale, purchase, stock). sale/views/sale_menus.xml:148-151; purchase/views/purchase_views.xml:42; stock/views/stock_menu_views.xml:30. Client widget "many2one_uom" and a tag autocomplete component are shipped as backend assets. uom/__manifest__.py:20-24; uom/static/src/components/many2one_uom/many2one_uom_field.js:79

## B. Objects and relationships
- B1. Single business object uom.uom "Product Unit of Measure": name (translatable), contains-quantity (relative factor, must be non-zero), reference unit, related child units, absolute factor (stored, computed recursively), display order, active flag. uom/models/uom_uom.py:34-44
- B2. Hierarchy is maintained as a parent tree; deleting a reference unit removes its dependent units (cascade). uom/models/uom_uom.py:20-21,41,44
- B3. Default display order = sequence; sequence defaults to 100 x factor capped at 1000. uom/models/uom_uom.py:22,53-60
- B4. Lifecycle: active/archived only; no state machine. Seed data: many imperial and secondary units are shipped archived (e.g., cm, km, m³, oz, lb, in, ft, yd, mi, ft², gal, dozen). uom/data/uom_data.xml:25,53,64,87,112,118,126,132,138,144
- B5. Stored absolute factor is unlimited-precision numeric so that conversions such as dozen to unit do not drift (TEST). uom/models/uom_uom.py:36-37; uom/tests/test_uom.py:16-22
- B6. Consumers hold the unit on their own lines: product (unit + additional packagings + packaging barcodes), stock, purchase, sale, manufacturing, POS. product/models/product_template.py:118-122; product/models/product_uom.py:8-16

## C. Validations, security, automation
- C1. Conversion ratio cannot be 0 (database check). uom/models/uom_uom.py:46-49
- C2. A unit with no reference unit must have ratio exactly 1; otherwise "Reference unit of measure is missing". uom/models/uom_uom.py:97-101
- C3. System-provided units cannot be deleted (only archived), except three exempt ones: hours, dozens, pack of 6. When Timesheet is installed the hours unit also becomes protected. uom/models/uom_uom.py:24-32,105-112,205-216; hr_timesheet/models/uom_uom.py:10-17
- C4. Editing the ratio of a protected unit older than 1 day raises an on-screen warning that existing records will not be recalculated. uom/models/uom_uom.py:79-93
- C5. Access: group base.group_system (Settings administrators) full CRUD; every internal user (base.group_user) read-only. uom/security/ir.model.access.csv:2-3
- C6. No record rules and no company field: units are global across companies. uom/models/uom_uom.py:34-44 (no company field); skeleton lists rules: none. No audit/tracking of changes (no chatter, no tracking flags in this file).
- C7. Product form view makes name/ratio/reference read-only when opened from a product context. uom/views/uom_uom_views.xml:24,27,28
- C8. Compute-quantity has an argument "raise_if_failure" whose docstring promises an error for incompatible units, but the body does not test compatibility; callers rely on _has_common_reference separately. uom/models/uom_uom.py:147-176,218-230; sale_timesheet/models/sale_order_line.py:49,100 (observed; behaviour on incompatible roots otherwise UNKNOWN — EVIDENCE INSUFFICIENT beyond this reading).

## D. Handoffs (which module owns what)
- D1. Product templates hold the default unit (default = "Units" record), packaging units (uom_ids), a warning on changing unit and a re-conversion of existing lines: owner product. product/models/product_template.py:29-36,118-123,474-481,586-588
- D2. Unit price conversion for pricelists/sales/purchase/margin/POS/website: sale, purchase, product, website_sale, sale_margin, pos_sale (grep of _compute_price callers). Quantity conversion for stock moves, MRP, purchase, timesheets etc.: stock (12 call sites), mrp (11), purchase_stock, sale_timesheet, hr_timesheet, and ~30 further modules.
- D3. Package types and routes on a unit: stock. stock/models/product.py:1368-1371; stock/views/uom_uom_views.xml:9,20,32
- D4. Packaging barcodes per unit and product: product (model product.uom). product/models/uom_uom.py:19-30
- D5. E-invoice unit codes (UNECE table) and lookup from code: account. account/models/uom_uom.py:6-35,48-59. Localisation-specific unit codes: l10n_ar, l10n_cl, l10n_eg_edi_eta, l10n_es_edi_facturae, l10n_hu_edi, l10n_id_efaktur_coretax, l10n_in, l10n_tr_nilvera (inheritance scan; contents not read).
- D6. POS groupable-unit flag and POS data loading: point_of_sale. point_of_sale/models/uom.py:8,18
- D7. Timesheet display widget per unit: hr_timesheet. hr_timesheet/models/uom_uom.py:20
- D8. Peppol/UBL import uses same-root test for unit compatibility: account_edi_ubl_cii. account_edi_ubl_cii/models/account_edi_common.py:976,1410
- D9. Label and delivery-slip logic that tests "is unit of the same family as Units": stock. stock/wizard/product_label_layout.py:60; stock/report/picking_templates.xml:11

## E. Configuration/defaults that change outcomes
- E1. Decimal precision "Product Unit" (default 2) controls rounding of every conversion and every quantity field declared with that precision (sale, stock etc.). uom/data/uom_data.xml:5-8; sale/models/sale_order_line.py:130,234
- E2. Rounding method defaults to UP on conversion, HALF-UP on round(), and packaging multiples; different callers may override. uom/models/uom_uom.py:116,152,178
- E3. Setting "Units of Measure & Packagings" decides whether unit columns and unit names are shown at all; when off, trade documents typically hide unit fields. See A6-A8. purchase_stock/views/product_views.xml:31 (shows plain "Units" label when group is off)
- E4. Seed units archived by default; activating them is a data choice (test setup activates dozen) (TEST). uom/tests/common.py:18

## F. Effective extension path (module names only)
- Extend uom.uom directly: account, hr_timesheet, l10n_ar, l10n_cl, l10n_eg_edi_eta, l10n_es_edi_facturae, l10n_hu_edi, l10n_id_efaktur_coretax, l10n_in, l10n_tr_nilvera, point_of_sale, product, stock. Modules with views on the list/form: stock, l10n_ar.
- Direct dependents in manifests: analytic, barcodes_gs1_nomenclature, hr_timesheet, l10n_cl, product.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of conversion between two units with different root references (no check found in this module; see C8).
- UNKNOWN — EVIDENCE INSUFFICIENT: contents of the l10n_* unit-code extensions.
- UNKNOWN — EVIDENCE INSUFFICIENT: how many users receive uom.group_uom by default in a fresh install with sale_timesheet absent (only the setting switch and the timesheet implication were traced).
- UNKNOWN — EVIDENCE INSUFFICIENT: JS widget behaviour beyond file presence (many2one_uom field and tag autocomplete were opened only at file head).

