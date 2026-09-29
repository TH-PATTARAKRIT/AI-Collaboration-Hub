# Source Map (candidate) — `website`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

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
- Core/optional/conditional behavior and business meaning of each capability: see section 10

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
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 100 of 102 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — website
Source revision: 19.0.post20260921 | Module: "Website" (website/__manifest__.py:5) | Category Website/Website (:6) | Application (:223) | License LGPL-3 (:518)
Basis: static reading of manifest, security XML/CSV, core models (website, page, menu, view, visitor, form, users, company, partner), page-serving hooks, form and home controllers, selected tests (TEST). Skeleton: sourcemap/website.json (orientation only).

## A. Capabilities; core vs optional vs conditional
- A1. Public-site builder: pages, menus, themes, SEO metadata, redirects/rewrites, multi-language, multi-website. website/__manifest__.py:5-8; website/models/website.py:99-101
- A2. Depends on digest, web, html_editor, http_routing, portal, social_media, auth_signup, mail, google_recaptcha, utm, html_builder; needs a geolocation library at install. website/__manifest__.py:11-23. Not auto_install; standalone application.
- A3. Core: website record (domain, company, languages, public user, homepage, social links, analytics keys, CDN, custom head/footer code, robots.txt). website/models/website.py:111-216
- A4. Core: static pages tied to a template view, plus "model pages" that list/show records of a chosen model publicly. website/models/website_page.py:24-45; website/models/website_controller_page.py:7-60
- A5. Core: menus per website (nested, optional mega-menu, per-group visibility). website/models/website_menu.py:15-59
- A6. Core: visitor tracking of tracked pages (sessions of anonymous or signed-in people). website/models/website_visitor.py:29-70; website/models/ir_http.py:183-199
- A7. Core: form builder — any model opted in may receive public form submissions. website/models/website_form.py:22-30; website/controllers/form.py:31-110
- A8. Conditional: page visibility modes Public / Signed In / Restricted Group / With Password. website/models/ir_ui_view.py:25-33, 403-430
- A9. Conditional: cookies bar and blocking of third-party embeds (default on) per website. website/models/website.py:131-137, 2372-2430
- A10. Conditional: multi-website switch is a setting that adds a user group; adding a 2nd website turns it on for all standard user groups automatically. website/models/res_config_settings.py:104-106; website/models/website.py:325-331
- A11. Conditional: designer-only tools (custom code, robots editing, theme install, configurator with external service). website/models/website.py:194-205 ; website/security/ir.model.access.csv:40,44
- A12. Snippet filters, technical pages list, digest tips, unused-snippet asset cleanup weekly. website/models/website_snippet_filter.py:14; website/data/ir_cron_data.xml:3-10
- A13. Homepage fallback: configured homepage -> page "/" -> first reachable menu -> 404. website/controllers/main.py:89-134

## B. Business objects, relationships, lifecycle
- B1. Website 1..n; each belongs to exactly one company and has one public user; the default website cannot be deleted. website/models/website.py:124,193,436-440
- B2. Company -> its first website (by sequence) is computed; archiving a company with a linked website is blocked. website/models/res_company.py:10-32
- B3. Page = view (template) + URL + publishing state + optional date + menus; generic pages (no website) can be specialised per website. website/models/website_page.py:38-50,85-105; website/models/ir_ui_view.py:20-22
- B4. Page publication: page is "visible" when published and its publication date has passed. website/models/website_page.py:64-67
- B5. Copy-on-write: editing a generic view/asset while in a website context creates a website-specific copy, leaving other websites unchanged. website/models/ir_ui_view.py:93-140; website/models/ir_asset.py:78-90; attachments default to the current website. website/models/ir_attachment.py:15-21
- B6. Website-restricted records use "website_id empty = all websites" semantics; the current-website check applies on record-bound routes (404 if other website). website/models/mixins.py:179-198; website/models/ir_http.py:206-220
- B7. Published mixin: published flag, can-publish flag, public URL; "published" is evaluated per current website for multi-website records. website/models/mixins.py:201-224,275-310
- B8. Partner: partners are publishable/multi-website; partner also carries visitors. website/models/res_partner.py:8-11
- B9. Users: login uniqueness is per (login, website); portal signups may be tied to a website. website/models/res_users.py:14-36,52-63
- B10. Visitor lifecycle: created on first tracked page (token = signed-in partner id or a hash of address, browser, session); revisit after 8 hours counts a new visit; page-view tracks stored at most once per 30 minutes per page filter; on login the anonymous visitor is merged into the user's visitor; inactive anonymous visitors deleted after 60 days by daily job. website/models/website_visitor.py:34-46,214-236,305-312,314-332,334-360; website/models/res_users.py:70-95
- B11. Rewrite/redirect rules: 301/302/308/404 types, per website. website/models/website_rewrite.py:60-83
- B12. Theme templates (theme.* models) are copied into website-specific records when a theme is applied. website/models/theme_models.py:13,51,111,135,176,357-403

## C. Validations, automation, security, multi-company
- C1. Groups: Restricted Editor; Editor and Designer (implies restricted editor; implied by system administrators; granted to root/admin); Multi-website; "public access to exposed models" (implied for public and portal). website/security/website_security.xml:9-23,94-104; website/data/website_data.xml:4-6
- C2. Access: everyone (public, portal, internal) can read websites, menus, SEO metadata; only designers write. website/security/ir.model.access.csv:2-9,18-21
- C3. Visitors and tracks manageable only by designers and system admin (no create for visitors via UI). website/security/ir.model.access.csv:30-33
- C4. Record rules: menus limited by their group list; portal/public read only published pages and published model pages; public sees only public-visibility templates, portal sees public+signed-in ones; designers edit templates (qweb) only, system admin all views. website/security/website_security.xml:27-31,33-89,106-111
- C5. Rule context: in frontend requests the current website becomes available inside record rules (used by other modules for website-scoped rules). website/models/ir_rule.py:9-25
- C6. Website resolution order: session-forced website (switch), context website, host domain match, then first website. website/models/website.py:1375-1420,1422-1484; (TEST) website/tests/test_get_current_website.py:20
- C7. Constraints: domain unique and must not contain relative path segments; homepage URL must start with "/"; domain auto-prefixed with https. website/models/website.py:218-221,392-432; page URLs slugged and made unique. website/models/website_page.py:170-190
- C8. Publishing rights: create/change of "published" requires ability to modify the record, otherwise access error. website/models/mixins.py:238-250,255-266; website/models/website.py:1962-1968
- C9. Page visibility enforcement: signed-in pages refuse public users; password pages need a hashed-password match (unlock kept in session); group pages check view access; designers bypass. website/models/ir_ui_view.py:403-435; password stored hashed and visible only as masked text. website/models/ir_ui_view.py:34-47
- C10. Caching only for public GET requests without params and for pages without group restriction. website/models/website_page.py:321-331
- C11. Search on site excludes unpublished, non-indexed, password-protected, and (for public) signed-in pages; group pages need membership. website/models/website_page.py:202-222
- C12. Form builder security: model must be flagged for forms; only explicitly allowed fields writable (all fields default to blacklisted); CAPTCHA route flag; CSRF checked only for logged-in sessions; e-mail-sending forms require a signed value; unique-constraint errors return a generic false. website/models/website_form.py:22-60,134-156; website/controllers/form.py:31-60,62-110
- C13. Deleting a model field used by a website form is blocked. website/models/website_form.py:148-165
- C14. Model pages: chosen model must be concrete; creator needs read access; public exposure limited by page record domain and published flag. website/models/website_controller_page.py:52-66,96-100; website/controllers/model_page.py:24,42
- C15. Users: cannot become internal while linked to a website; user login checked per website. website/models/res_users.py:97-102; (TEST) website/tests/test_res_users.py:115
- C16. Multi-company: website carries company; frontend requests set allowed companies to the website's company when the user may use it, else the user's main company; public user is company-specific and is swapped when the website's company changes. website/models/ir_http.py:235-265; website/models/website.py:312-316,337-346; (TEST) website/tests/test_res_users.py:95
- C17. Signup: new external users get the website's company; may be tied to that website (setting "specific user account"); signup openness (invitation vs free) is per website. website/models/res_users.py:52-68; website/models/website.py:212-217; (TEST) website/tests/test_auth_signup_uninvited.py:9
- C18. Portal wizard (owner portal) is extended so "already registered" email check respects website scope. website/wizard/portal_wizard.py:9-58; (TEST) website/tests/test_website_visitor.py:544-615
- C19. Automation: daily visitor cleanup and weekly unused-snippet asset disable. website/data/website_visitor_cron.xml:3-10; website/data/ir_cron_data.xml:3-10
- C20. Enabling the cookies bar creates a published "cookie policy" page, disabling deletes it. website/models/website.py:359-377
- C21. Optional cookies (analytics-type) are allowed only if the bar is off or the visitor accepted. website/models/ir_http.py:427-448
- C22. Redirects from rewrite rules are served for 301/302; editors only can define them. website/models/ir_http.py:324-338

## D. Handoffs
- D1. Routing, language URL handling, slugs: http_routing. website/__manifest__.py:15
- D2. Editor and builder front-end: html_editor, html_builder; view saving: html_editor. website/__manifest__.py:14,22; html_editor/models/ir_ui_view.py:295-360
- D3. Customer portal, signup, login: portal, auth_signup. website/wizard/portal_wizard.py; website/models/res_users.py:52-68
- D4. CAPTCHA for forms: google_recaptcha (also website_cf_turnstile dependent). website/__manifest__.py:20; website/controllers/form.py:31
- D5. Social links: social_media; campaign source: utm; visitor contact e-mail: mail composer. website/__manifest__.py:17,21; website/models/website_visitor.py:173-192
- D6. Digest KPIs and tips: digest. website/__manifest__.py:12
- D7. Lead creation from forms: website_crm; hiring forms: website_hr_recruitment; project tasks: website_project; mailing list subscription: website_mass_mailing (each flags its model for forms). website_crm/data/ir_model_data.xml; website_hr_recruitment/data/config_data.xml; website_project/data/website_project_data.xml; website_mass_mailing/data/ir_model_data.xml
- D8. E-commerce, events, slides, blog, live chat, payments, links: website_sale, website_event, website_slides, website_blog, website_livechat, website_payment, website_links (dependents by manifest).
- D9. Partner web profiles and maps: website_partner (base for website_customer, website_profile, website_google_map, website_blog, website_event, website_crm_partner_assign).
- D10. Themes: theme_* modules and theme_common depend on website.

## E. Configuration / defaults that change outcomes
- E1. Website domain and default language decide which website answers a host and its language redirects. website/models/website.py:112-129,1422-1484
- E2. Homepage URL (empty by default = page "/"). website/models/website.py:199; website/controllers/main.py:106-108
- E3. Signup mode per website: default "on invitation" (b2b); free signup (b2c) optional. website/models/website.py:213-217; website/models/res_users.py:65-68
- E4. Specific user account off by default: portal users can then log in to all websites. website/models/res_users.py:55-61
- E5. Block third-party domains default on; cookies bar default off. website/models/website.py:131-137
- E6. Visitor retention parameter website.visitor.live.days default 60. website/models/website_visitor.py:349-360
- E7. CDN off by default with default URL filters. website/models/website.py:194-197
- E8. Pages tracked only if the template's track flag is on; bots, non-200 and X-Disable-Tracking are ignored. website/models/ir_http.py:183-199; website/models/ir_ui_view.py:24
- E9. Forms: metadata capture depends on system parameter website_form_enable_metadata. website/controllers/form.py:239
- E10. Rewrite redirect type default 302. website/models/website_rewrite.py:70-78

## F. Effective extension path (module names only)
- website_sale, website_event, website_slides, website_blog, website_livechat, website_crm, website_hr_recruitment, website_project, website_mass_mailing, website_mail, website_mail_group, website_links, website_payment, website_sms, website_timesheet, website_partner, website_profile, website_cf_turnstile, marketing_card, theme_common, theme_default and other theme_*.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end snippet catalogue and builder options.
- UNKNOWN — EVIDENCE INSUFFICIENT: configurator's external service behaviour and data sent.
- UNKNOWN — EVIDENCE INSUFFICIENT: sitemap and robots generation details.
- UNKNOWN — EVIDENCE INSUFFICIENT: full copy-on-write edge cases (only entry conditions read).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether visitor/track rows are company-scoped (no company field seen; multi-website only).
- UNKNOWN — EVIDENCE INSUFFICIENT: file-upload size or type limits on forms.

