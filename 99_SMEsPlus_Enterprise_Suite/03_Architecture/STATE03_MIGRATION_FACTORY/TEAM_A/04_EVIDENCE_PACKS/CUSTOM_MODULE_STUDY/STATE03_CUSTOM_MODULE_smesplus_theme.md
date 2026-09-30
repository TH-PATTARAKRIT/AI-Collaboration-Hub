> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: smesplus_theme

## 0. Header
- Module: smesplus_theme
- License (confirmed in manifest): LGPL-3 (smesplus_theme/__manifest__.py:7)
- Author (manifest): SCG Legacy (Thailand) Co., Ltd. (smesplus_theme/__manifest__.py:8)
- Version (manifest): 19.0.2.3.0 (smesplus_theme/__manifest__.py:5)
- Path: Extra_Module_scgl/smesplus_theme
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Visual theme of the backend and login page on top of the OCA responsive client (manifest:3-4, :10): purple/teal palette, Thai-friendly system font stack and smaller base font size, light top bar of 48 px, card-like form sheets and kanban cards, striped list rows, full-screen app menu styled after the Odoo 19 home screen, and a dark-mode colour set (smesplus_theme/static/src/scss/primary_variables.scss; navbar.scss; views.scss; form.scss; apps_menu.scss; dark.scss).
- Login page: gradient background, a tagline "SMEsPlus · SCGL" above the login card, and a centred card style for the website login container if the website module is present (views/webclient_templates.xml:4-11; static/src/scss/login.scss).
- Hiding (view-level only): the "Upgrade" buttons that link to the vendor's paid-edition pricing page are made invisible on the Apps kanban and form (views/ir_module_views.xml:6-26; the comment at :4-5 states that module records are not deleted and only the view hides the link).
  - What is hidden: the Upgrade link on each not-installed paid-edition app card and form.
  - Access rights: NOT affected. No group, ACL, menu or record change; only the invisible attribute on the link. Users can still reach the same page by other means.
- The comment in apps_menu.scss says the look was matched from screenshots and that no paid-edition code was read (smesplus_theme/static/src/scss/apps_menu.scss:2-4); this is a statement in the source, not verified here.

## 2. Attachment to CORE
- Depends declared: web and web_responsive (manifest:10).
- Core objects extended: login layout template `web.login_layout` (core:web/views/webclient_templates.xml:110; anchors: body class variable at :113 and the login container at :118); Apps views `base.module_view_kanban` and `base.module_form` (core:base/views/ir_module_views.xml:149, :47; the pricing link at :67 and :184).
- Asset bundles: primary and secondary style variables (core:web/__manifest__.py:376, :380), backend bundle, dark bundle (core:web/__manifest__.py:346), frontend bundle (login styles).
- No Python code, no core method overridden. Variables are pre-pended before core primary variables (manifest:16-18) so they override core defaults by design. No ALTERS CORE CONTROL.

## 3. New objects, security, automation, external calls
- None: no models, fields, ACLs, groups, rules, cron. No external calls; fonts are system fonts only (primary_variables.scss note: no font download).

## 4. Odoo 19 compatibility
- Anchors exist in Community 19 (see pointers). The XPath for the pricing link is text-based (`contains(@href, 'odoo.com/pricing')`, views/ir_module_views.xml:11, :22) and would fail loading if the link disappears from a later core release (inference).
- Note that the core kanban pricing link at core:base/views/ir_module_views.xml:184 carries a group restriction (system administrators only); the module hides it for those users as well.
- SCSS uses variables from core files (e.g. font-weight tokens); not compile-tested here.

## 5. Custom-to-custom dependencies
- Depends on web_responsive (full-screen apps menu classes are styled in apps_menu.scss:19-32; see web_responsive file). Also styles the chatter container (form.scss last rule) without depending on the mail module directly.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the stylesheets compile without warnings under the deployed asset pipeline.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether other installed themes or branding modules also change the same variables (load order decides the result).
