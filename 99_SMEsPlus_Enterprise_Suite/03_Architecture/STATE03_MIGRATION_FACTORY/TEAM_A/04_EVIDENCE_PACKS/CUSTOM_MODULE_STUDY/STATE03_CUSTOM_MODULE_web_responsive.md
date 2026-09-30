> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: web_responsive

## 0. Header
- Module: web_responsive
- License (confirmed in manifest): LGPL-3 (web_responsive/__manifest__.py:16)
- Author (manifest): LasLabs, Tecnativa, ITerra, Onestein, Odoo Community Association (OCA) (web_responsive/__manifest__.py:15)
- Version (manifest): 19.0.1.1.0 (web_responsive/__manifest__.py:12)
- Path: Extra_Module_scgl/_REQUIRED_OCA_DEPENDS/web_responsive
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Community-supported responsive web client: full-screen application launcher with search (three search styles: canonical, fuse fuzzy, and the standard command palette) and two launcher themes; mobile-friendly form buttons, statusbar, control panel that hides on scroll, sticky list headers, chatter and file-viewer tweaks (manifest:25-64; static/src/components/*).
- Per-user preferences: launcher search type, launcher theme, and "Redirect to Home" (open the launcher after sign-in unless the user has a home action) (models/res_users.py:10-42; views/res_users_views.xml:5-38, :64-77).
- Menu hiding: the standard drop-down menu of applications is REPLACED by the full-screen launcher (visibility/navigation change only). Menus, actions and access rights are not changed; all entries remain reachable through the launcher and through search. Source: template registration and patches (static/src/components/apps_menu/apps_menu.esm.js:24-50, :166-202; manifest:38-45).
- Feature turned off: the file-preview panel next to the chatter in forms is disabled by forcing the "has file" check to false (static/src/views/form/form_renderer.esm.js:7-11), so the side preview is never opened from the form; attachments still open in the file viewer.

## 2. Attachment to CORE
- Depends declared: web, web_tour, mail (manifest:18); `excludes` the paid web client module (manifest:21).
- Core objects extended (Python): `res.users` (fields), `ir.http.session_info` (models/ir_http.py:10-19): ADDS after core — appends the user's launcher preferences to the session info (core:web/models/ir_http.py:84). Not a control.
- Core front-end classes patched: WebClient (apps_menu.esm.js:24-50; core web client), NavBar and BurgerMenu (:166-202), ControlPanel (control_panel.esm.js:43-73), Chatter (chatter.esm.js:10-27; core mail chatter at core:mail/static/src/chatter/web_portal/chatter.js), AttachmentList (file_viewer_hook_patch.esm.js:4-22; core mail method at core:mail/static/src/core/common/attachment_list.js:93), FormRenderer (form_renderer.esm.js; the method disabled is defined by the mail module at core:mail/static/src/chatter/web/form_renderer.js:39), CommandPalette (command_palette/main.esm.js:6-19). All ADD or REPLACE presentation logic. The launcher patch decides which screen opens after login when "Redirect to Home" is set (apps_menu.esm.js:28-50). No ALTERS CORE CONTROL (no permission logic).
- Views: adds a user preference form and window action (res_users_views.xml:5-62) and inserts the redirect option into the user form group `other_preferences` (res_users_views.xml:64-77; core anchor core:base/views/res_users_views.xml:184).
- The manifest declares the two primary-variable files as a set literal rather than a list (manifest:26-29), so their load order is not fixed (observation).

## 3. New objects, security, automation, external calls
- New fields on users: `apps_menu_search_type`, `apps_menu_theme`, `is_redirect_home` (models/res_users.py:10-33). No ACLs, groups, record rules, company scoping.
- Front end reads the user's own redirect flag with a direct read at start-up (apps_menu.esm.js:32-38). The module does not extend the list of fields users may read or write on their own record; core defines these lists (core:base/models/res_users.py:176-200). Whether ordinary internal users can save their preferences through the preference form was not tested (risk).
- Automation: none. External calls: none (the fuzzy search library is bundled locally, manifest:31).
- A stray closing bracket character sits inside the inherited user-form record (views/res_users_views.xml:74); effect is harmless text in the data node (observation).

## 4. Odoo 19 compatibility
- Core classes patched all exist in the Community tree (web command palette, burger menu, navbar, mail chatter and attachment list). Chatter patch relies on state names (`isAttachmentBoxOpened`, `scrollToAttachments`) that exist in the mail chatter patch files (core:mail/static/src/chatter/web/chatter_patch.js), not in the base chatter file; behaviour not tested.
- Session info hook and `action_id` on users exist in Community 19 (core:web/models/ir_http.py:84; core:base/models/res_users.py:229).
- Version tag 19.0.1.1.0 with manifest set-literal asset entries (see above); loading behaviour in 19 not tested.

## 5. Custom-to-custom dependencies
- None declared. Required by smesplus_theme (which styles the launcher classes defined here).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether non-admin users can change their own launcher preferences.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the launcher hides or shows apps according to menu groups exactly as core does (menu filtering is done by core data supplied to the client; module code did not show extra filtering).
