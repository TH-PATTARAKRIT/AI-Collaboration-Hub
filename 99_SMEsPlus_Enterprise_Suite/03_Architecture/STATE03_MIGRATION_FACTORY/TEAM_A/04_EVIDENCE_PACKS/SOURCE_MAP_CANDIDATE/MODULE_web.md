# Source Map (candidate) — `web`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `web` |
| Display name | Web |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e34b9cf41fb4219f` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/web/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`
- Direct dependents in 300-module list (29): `api_doc`, `attachment_indexation`, `auth_oauth`, `auth_passkey`, `auth_password_policy`, `auth_signup`, `auth_totp`, `barcodes`, `base_iban`, `base_import`, `base_import_module`, `base_setup` … (+17)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (8): `iot_base`, `test_http`, `test_import_export`, `test_orm`, `test_read_group`, `test_rpc`, `test_search_panel`, `test_testing_utilities`
- Custom / third-party modules that declare a dependency (name — license only) (18): `nthub_binary_field_preview` — LGPL-3, `scgl_jasper_api` — LGPL-3, `l10n_th_withholding_tax_cert_form` — AGPL-3, `oi_action_file` — OPL-1, `scgl_custom_title_and_favicon` — LGPL-3, `report_xlsx` — AGPL-3, `oi_pdf_viewer` — OPL-1, `hide_odoo_menu` — LGPL-3, `oi_jasper_report` — OPL-1, `date_range` — LGPL-3, `import_bridge_axis` — OPL-1, `web_chatter_resize` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 1, server actions 1, reports 3, mail templates 0, scheduled jobs 0, wizards 2, web routes 60
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `base.document.layout` (Company Document Layout); `res.users.settings.embedded.action` (User Settings for Embedded Actions)
- Objects extended from other modules (13): `ir.model`, `ir.http`, `base`, `res.company`, `res.users.settings`, `ir.ui.menu`, `ir.qweb.field.image`, `ir.qweb.field.image_url`, `ir.ui.view`, `properties.base.definition`, `res.users`, `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `base.document.layout` ← Community: `account`, `l10n_ca`, `l10n_cz`, `l10n_din5008`, `l10n_fr_account`, `l10n_ma`, `l10n_mu_account`, `l10n_my_ubl_pint`, `l10n_sk`, `sale`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `ir.model`, `ir.http`, `base`, `res.company`, `res.users.settings`, `ir.ui.menu`, `ir.qweb.field.image`, `ir.qweb.field.image_url`, `ir.ui.view`, `properties.base.definition`, `res.users`, `res.config.settings`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 2 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

