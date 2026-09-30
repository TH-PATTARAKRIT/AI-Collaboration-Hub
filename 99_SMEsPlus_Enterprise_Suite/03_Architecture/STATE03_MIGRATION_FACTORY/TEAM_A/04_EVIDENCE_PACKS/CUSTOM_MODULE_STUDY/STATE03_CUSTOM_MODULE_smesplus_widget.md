> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: smesplus_widget

## 0. Header
- Module: smesplus_widget
- License (confirmed in manifest): LGPL-3 (smesplus_widget/__manifest__.py:14)
- Author (manifest): SMESplus (smesplus_widget/__manifest__.py:11)
- Version (manifest): 19.0.1.0.0 (smesplus_widget/__manifest__.py:4)
- Path: addons_Extramodule/addons/smesplus_widget
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Front-end field widgets (no server code) for readability of lists and forms:
  - `many2one_avatar_product`: shows the product picture as a small round image next to the product name, including in the drop-down suggestions (smesplus_widget/static/src/js/many2one_avatar_product.js:23-44; static/src/xml/many2one_avatar_product.xml:4-27).
  - `many2one_wrap`: read-only relational values wrap to the next line instead of being cut with an ellipsis (static/src/js/many2one_wrap.js:23-44; static/src/xml/many2one_wrap.xml:10-45).
  - `char_wrap`: same wrapping for text and short text fields in list views (static/src/js/char_wrap.js:19-28; static/src/css/char_wrap.css:1-32).
  - A list-renderer patch that adds the core "text" cell class for the two wrap widgets (static/src/js/list_renderer_patch.js:16-31).
- The manifest lists only two widgets (manifest:5-10); `char_wrap` and the renderer patch are extra.
- Menu hiding: none. Access rights: not affected. A form/list view must opt in with the widget name to use any of this.

## 2. Attachment to CORE
- Depends declared: web (manifest:15).
- Core front-end objects reused: many2one field building blocks `computeM2OProps`, `Many2One`, `buildM2OFieldDescription`, `extractM2OFieldProps`, `Many2OneField` (core:web/static/src/views/fields/many2one/many2one.js:27, :73; core:web/static/src/views/fields/many2one/many2one_field.js:61, :71, :95); core char field component (imported at char_wrap.js:3); list renderer (core:web/static/src/views/list/list_renderer.js:961 for `getCellClass`; the core text class at :78).
- Overrides: `getCellClass` of the list renderer (list_renderer_patch.js:18-31): ADDS after core — appends the text class when the column widget is one of the two wrap widgets. Presentation only. No ALTERS CORE CONTROL.
- Product image URL used by the avatar widget is the generic image route for products with the 128 pixel image field (xml:11, :21); access to that image follows the core image route rules.

## 3. New objects, security, automation, external calls
- None: no models, ACLs, groups, rules, cron; no external calls.
- Manifest flags the module as an application (manifest:30), so it shows as an app in the Apps list; a technical widget module normally is not one (observation).

## 4. Odoo 19 compatibility
- All imported core symbols exist in the Community 19 tree (pointers above).
- The wrap template builds the record link from the relation name and id with a fixed URL pattern (xml:25) instead of a core helper; correctness of that link pattern in 19 not tested.

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: which custom views actually use these widgets (widget names were searched only inside this module).
