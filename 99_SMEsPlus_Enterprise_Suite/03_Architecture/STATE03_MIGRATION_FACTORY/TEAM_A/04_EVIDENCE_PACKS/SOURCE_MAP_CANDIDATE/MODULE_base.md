# Source Map (candidate) — `base`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `base` |
| Display name | Base |
| Manifest version | 1.3 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `0ad4109fd814b921` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/base/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): —
- Direct dependents in 300-module list (25): `analytic`, `auth_ldap`, `auth_oauth`, `base_address_extended`, `base_automation`, `base_setup`, `base_sparse_field`, `bus`, `calendar`, `contacts`, `fleet`, `html_builder` … (+13)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (19): `l10n_cn`, `l10n_ec`, `l10n_fr`, `l10n_gt`, `l10n_hn`, `l10n_ma`, `l10n_mz`, `l10n_pt`, `l10n_us`, `test_assetsbundle`, `test_converter`, `test_inherit` … (+7)
- Custom / third-party modules that declare a dependency (name — license only) (39): `product_sequence` — LGPL-3, `partner_company_type` — AGPL-3, `19_bhpro_product_part` — OPL-1, `nthub_binary_field_preview` — LGPL-3, `19_bhpro_purchase_ext` — OPL-1, `order_line_sequence` — AGPL-3, `19_sale_lazada` — OPL-1, `product_brand_sale` — AGPL-3, `app_icon_hide` — LGPL-3, `19_bhpro_menu_general` — OPL-1, `scgl_inventory_lot_filter` — LGPL-3, `19_attachment_dedup_fix` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 66, views 177, window actions 66, server actions 2, reports 2, mail templates 0, scheduled jobs 2, wizards 22, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (124): `base.partner.merge.line` (Merge Partner Line); `base.partner.merge.automatic.wizard` (Merge Partner Wizard); `base.module.uninstall` (Module Uninstall); `wizard.ir.model.menu.create` (Create Menu Wizard); `base.language.import` (Language Import); `base.module.upgrade` (Upgrade Module); `base.module.update` (Update Module); `base.language.export` (Language Export); `base.language.install` (Install Language); `ir.default` (Default Values); `res.lang` (Languages); `properties.base.definition.mixin` (Properties Base Definition Mixin); `ir.mail_server` (Mail Server); `ir.rule` (Record Rule); `base` (Base); `_unknown` (Unknown); `ir.model` (Models); `ir.model.fields` (Fields); `ir.model.inherit` (Model Inheritance Tree); `ir.model.fields.selection` (Fields Selection); `ir.model.constraint` (Model Constraint); `ir.model.relation` (Relation Model); `ir.model.access` (Model Access); `ir.model.data` (Model Data); `ir.autovacuum` (Automatic Vacuum) … (+99)
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 1 field(s); company-consistency auto-check declared on 1 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `base.partner.merge.automatic.wizard` ← Community: `account`, `loyalty`, `mail`, `website`, `website_slides`; open-license custom/third-party scanned: —
- `base.module.uninstall` ← Community: `base_import_module`, `mail`; open-license custom/third-party scanned: —
- `base.language.install` ← Community: `website`; open-license custom/third-party scanned: —
- `res.lang` ← Community: `http_routing`, `point_of_sale`, `spreadsheet`, `survey`, `website`; open-license custom/third-party scanned: —
- `properties.base.definition.mixin` ← Community: `mass_mailing`, `test_orm`; open-license custom/third-party scanned: —
- `ir.mail_server` ← Community: `google_gmail`, `mail`, `mass_mailing`, `microsoft_outlook`; open-license custom/third-party scanned: —
- `ir.rule` ← Community: `website`; open-license custom/third-party scanned: —
- `base` ← Community: `base_import`, `base_sparse_field`, `hr`, `html_editor`, `mail`, `phone_validation`, `sms`, `transifex`, `web`, `web_hierarchy` … (+1); open-license custom/third-party scanned: —
- `ir.model` ← Community: `bus`, `mail`, `marketing_card`, `mass_mailing`, `sms`, `spreadsheet`, `web`, `website`; open-license custom/third-party scanned: —
- `ir.model.fields` ← Community: `base_sparse_field`, `mail`, `website`; open-license custom/third-party scanned: —
- `ir.model.data` ← Community: `website`; open-license custom/third-party scanned: —
- `ir.actions.report` ← Community: `account`, `account_edi`, `account_edi_ubl_cii`, `hr_expense`, `l10n_ch`, `l10n_de`, `l10n_din5008`, `l10n_th`, `purchase`, `sale` … (+3); open-license custom/third-party scanned: `account_financial_report`, `l10n_th_withholding_tax_report`, `mis_builder`, `report_xlsx`, `report_xlsx_helper`
- `ir.http` ← Community: `account`, `auth_password_policy_portal`, `auth_password_policy_signup`, `auth_signup`, `auth_timeout`, `barcodes`, `barcodes_gs1_nomenclature`, `base_import_module`, `base_setup`, `bus` … (+32); open-license custom/third-party scanned: `web_responsive`
- `res.country` ← Community: `base_address_extended`, `base_vat`, `l10n_ar`, `l10n_cl`, `payment`, `point_of_sale`, `pos_self_order`; open-license custom/third-party scanned: `base_location_geonames_import`
- `res.country.group` ← Community: `account`, `product`; open-license custom/third-party scanned: —
- `res.country.state` ← Community: `l10n_in`, `point_of_sale`; open-license custom/third-party scanned: `l10n_th_base_location`
- `ir.attachment` ← Community: `account`, `account_edi`, `api_doc`, `attachment_indexation`, `bus`, `cloud_storage`, `cloud_storage_azure`, `cloud_storage_google`, `cloud_storage_migration`, `hr_expense` … (+14); open-license custom/third-party scanned: `19_attachment_dedup_fix`
- `res.users.settings` ← Community: `bus`, `calendar`, `google_calendar`, `im_livechat`, `mail`, `microsoft_calendar`, `project`, `web`; open-license custom/third-party scanned: —
- `res.bank` ← Community: `l10n_cl`, `l10n_mx`, `l10n_pe`, `l10n_us_account`; open-license custom/third-party scanned: —
- `res.partner.bank` ← Community: `account`, `account_qr_code_emv`, `account_qr_code_sepa`, `base_iban`, `hr`, `l10n_ar`, `l10n_au`, `l10n_br`, `l10n_ch`, `l10n_hk` … (+7); open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: `base.partner.merge.automatic.wizard` → ['option', 'selection', 'finished']; `base.module.update` → ['init', 'done']; `base.language.export` → ['choose', 'get']; `ir.model` → ['manual', 'base']; `ir.model.fields` → ['manual', 'base']; `res.users.deletion` → ['todo', 'done', 'fail']; `ir.module.module` → ['uninstallable', 'uninstalled', 'installed', 'to upgrade', 'to remove', 'to install']; `ir.actions.server` → ['object_write', 'object_create', 'object_copy', 'code', 'webhook', 'multi']
- Validation: 46 declarative constraint method(s), 41 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Base: Auto-vacuum internal data every ? ?; Base: Portal Users Deletion every ? ?
- Security: groups declared 2 (`default_user_group`, `base.group_portal`); record rules 32 (of which company-scoped by text 7); access rows 146

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

