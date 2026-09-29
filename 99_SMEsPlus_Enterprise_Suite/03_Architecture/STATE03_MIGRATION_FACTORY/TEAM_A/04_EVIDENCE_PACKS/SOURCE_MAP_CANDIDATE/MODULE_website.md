# Source Map (candidate) — `website`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website` |
| Display name | Website |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `ed2e376c059f3cea` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `digest`, `web`, `html_editor`, `http_routing`, `portal`, `social_media`, `auth_signup`, `mail`, `google_recaptcha`, `utm`, `html_builder`
- Direct dependents in 300-module list (17): `theme_buzzy`, `theme_cobalt`, `theme_common`, `theme_default`, `theme_paptic`, `website_cf_turnstile`, `website_crm`, `website_links`, `website_livechat`, `website_mail`, `website_mail_group`, `website_partner` … (+5)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (8): `marketing_card`, `test_import_export`, `test_website`, `test_website_modules`, `theme_test_custo`, `website_event`, `website_mass_mailing`, `website_sale`
- Custom / third-party modules that declare a dependency (name — license only) (1): `product_brand_sale` — AGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Enterprise website builder
- Inventory of user-facing artifacts (counts): menu items 24, views 54, window actions 14, server actions 2, reports 0, mail templates 0, scheduled jobs 2, wizards 8, web routes 53
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (30): `website.robots` (Robots.txt Editor); `website.custom_blocked_third_party_domains` (User list of blocked 3rd-party domains); `website.seo.metadata` (SEO metadata); `website.cover_properties.mixin` (Cover Properties Website Mixin); `website.page_visibility_options.mixin` (Website page/record specific visibility options); `website.page_options.mixin` (Website page/record specific options); `website.multi.mixin` (Multi Website Mixin); `website.published.mixin` (Website Published Mixin); `website.searchable.mixin` (Website Searchable Mixin); `website.controller.page` (Model Page); `website.technical.page` (Website Technical Page); `website.menu` (Website Menu); `website.page` (Page); `website.assets` (Assets Utils); `website.page.properties.base` (Page Properties Base); `website.page.properties` (Page Properties); `website.route` (All Website Route); `website.rewrite` (Website rewrite); `website.snippet.filter` (Website Snippet Filter); `theme.ir.asset` (Theme Asset); `theme.ir.ui.view` (Theme UI View); `theme.ir.attachment` (Theme Attachments); `theme.website.menu` (Website Theme Menu); `theme.website.page` (Website Theme Page); `theme.utils` (Theme Utils) … (+5)
- Objects extended from other modules (25): `portal.wizard.user`, `base.language.install`, `base.partner.merge.automatic.wizard`, `ir.module.module`, `res.lang`, `ir.rule`, `base`, `ir.http`, `ir.attachment`, `ir.model.data`, `website.published.multi.mixin`, `ir.model`, `ir.model.fields`, `ir.binary`, `ir.ui.menu`, `ir.qweb.field.contact`, `ir.qweb.field.html`, `ir.ui.view`, `ir.asset`, `res.company`, `ir.qweb`, `res.users`, `res.config.settings`, `ir.actions.server`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `website.seo.metadata` ← Community: `test_website`, `website_blog`, `website_event`, `website_event_track`, `website_forum`, `website_hr_recruitment`, `website_partner`, `website_sale`, `website_slides`; open-license custom/third-party scanned: —
- `website.cover_properties.mixin` ← Community: `website_blog`, `website_event`, `website_slides`; open-license custom/third-party scanned: —
- `website.page_visibility_options.mixin` ← Community: `website_blog`, `website_event`; open-license custom/third-party scanned: —
- `website.multi.mixin` ← Community: `website_blog`, `website_forum`, `website_sale`, `website_sale_loyalty`; open-license custom/third-party scanned: —
- `website.published.mixin` ← Community: `test_website`, `website_crm_partner_assign`, `website_customer`, `website_event_exhibitor`, `website_event_track`, `website_profile`, `website_slides`; open-license custom/third-party scanned: —
- `website.searchable.mixin` ← Community: `test_website`, `website_blog`, `website_event`, `website_event_exhibitor`, `website_event_track`, `website_forum`, `website_hr_recruitment`, `website_sale`, `website_slides`; open-license custom/third-party scanned: —
- `website.menu` ← Community: `website_event`, `website_event_track`, `website_sale`; open-license custom/third-party scanned: —
- `website.page` ← Community: `website_hr_recruitment`, `website_livechat`, `website_project`, `website_sale`; open-license custom/third-party scanned: —
- `website.snippet.filter` ← Community: `website_blog`, `website_event`, `website_sale`; open-license custom/third-party scanned: —
- `theme.utils` ← Community: `theme_anelusia`, `theme_artists`, `theme_avantgarde`, `theme_aviato`, `theme_beauty`, `theme_bewise`, `theme_bistro`, `theme_bookstore`, `theme_buzzy`, `theme_clean` … (+20); open-license custom/third-party scanned: —
- `website` ← Community: `l10n_ar_website_sale`, `l10n_br_website_sale`, `test_themes`, `test_website`, `website_blog`, `website_crm`, `website_crm_partner_assign`, `website_customer`, `website_event`, `website_event_exhibitor` … (+12); open-license custom/third-party scanned: `product_brand_sale`
- `website.track` ← Community: `website_sale`; open-license custom/third-party scanned: —
- `website.visitor` ← Community: `website_crm`, `website_crm_sms`, `website_event`, `website_event_track`, `website_livechat`, `website_sale`, `website_sms`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `portal.wizard.user`, `base.language.install`, `base.partner.merge.automatic.wizard`, `ir.module.module`, `res.lang`, `ir.rule`, `base`, `ir.http`, `ir.attachment`, `ir.model.data`, `website.published.multi.mixin`, `ir.model`, `ir.model.fields`, `ir.binary`, `ir.ui.menu`, `ir.qweb.field.contact`, `ir.qweb.field.html`, `ir.ui.view`, `ir.asset`, `res.company`, `ir.qweb`, `res.users`, `res.config.settings`, `ir.actions.server`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 11 declarative constraint method(s), 4 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Website Visitor : clean inactive visitors every 1 days; Disable unused snippets assets every 1 weeks
- Security: groups declared 7 (`group_website_restricted_editor`, `group_website_designer`, `website_page_controller_expose`, `base.group_public`, `base.group_portal`, `group_multi_website` … (+1)); record rules 8 (of which company-scoped by text 0); access rows 44

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

