> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: web_chatter_resize

## 0. Header
- Module: web_chatter_resize
- License (confirmed in manifest): LGPL-3 (web_chatter_resize/__manifest__.py:33)
- Author (manifest): Somchart Jabsung (web_chatter_resize/__manifest__.py:32)
- Version (manifest): 19.0.1.1.0 (web_chatter_resize/__manifest__.py:30)
- Path: addons_Extramodule/addons/web_chatter_resize
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Narrows the side chatter panel (messages, log notes, activities) that appears at the right of form views, from the core fixed width of about 530 px to 15 percent of the screen width with a floor of 300 px (manifest:4-28; web_chatter_resize/static/src/scss/chatter_resize.scss:16-27). On screens under about 2000 px wide the floor applies, so the panel is 300 px there (manifest:26-28).
- Pure styling. Nothing is hidden and no access rights are involved; the manifest itself states no models, views or data are touched (manifest:17-18). The module has no Python files apart from an empty package marker (web_chatter_resize/__init__.py).

## 2. Attachment to CORE
- Depends declared: mail, web (manifest:34).
- Targets two CSS classes of the mail form layout (chatter_resize.scss:23-24) which core defines at core:mail/static/src/chatter/web/form_renderer.scss:8-16 (the fixed width rule at :16) and adds in the form compiler at core:mail/static/src/chatter/web/form_compiler.js:27.
- Effect: ADDS a later stylesheet that overrides the core width rule using important flags (chatter_resize.scss:25-26). No core method overridden; no ALTERS CORE CONTROL.

## 3. New objects, security, automation, external calls
- None (no models, ACLs, groups, rules, cron, external calls). The width is configured by editing two variables in the stylesheet (manifest:22-28).

## 4. Odoo 19 compatibility
- Core selectors and variable names cited in the stylesheet exist in the Community 19 tree (pointers above). Not visually tested.
- Interaction with web_responsive: that module also patches chatter and control-panel behaviour on small screens (see its file); conflicts on very narrow screens are not evaluated here.

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: rendering of the panel with long content or attachment previews at the reduced width (not viewed).
