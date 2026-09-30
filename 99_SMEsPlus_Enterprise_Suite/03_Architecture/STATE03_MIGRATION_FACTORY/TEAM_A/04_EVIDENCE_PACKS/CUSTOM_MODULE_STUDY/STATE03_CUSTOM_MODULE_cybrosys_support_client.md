> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: cybrosys_support_client

## 0. Header
- Module: cybrosys_support_client
- License (confirmed in manifest): LGPL-3 (cybrosys_support_client/__manifest__.py:47)
- Author (manifest): Cybrosys Techno Solutions (cybrosys_support_client/__manifest__.py:28)
- Version (manifest): 19.0.1.0.1 (cybrosys_support_client/__manifest__.py:24)
- Path: addons_Extramodule/base_accounting_kit-19.0.3.3.1/cybrosys_support_client
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- A "support assistant" form available from the top bar and the user menu that lets any signed-in user raise a support ticket with the module vendor without leaving the ERP (cybrosys_support_client/__manifest__.py:26; static/src/js/client_support_systray.js:29-33; static/src/js/client_support_user_menu.js:25).
- The form collects the user's name, email, phone (defaults from the user profile), subject, description, support type (functional/technical), category, priority and optional file attachments (wizard/client_support.py:46-91; wizard/client_support_views.xml:8-25).
- A preview option shows the data that will be sent, with attachment content hidden (client_support.py:84-91,133-144).
- On submit the details are transmitted to a vendor-hosted support service and a ticket reference plus a tracking link are shown to the user (client_support.py:161-169,171-250). A second button opens a WhatsApp chat to a vendor-owned contact number hard-coded in the code with the user's name, email and description as message text (client_support.py:252-268, number at line 262).
- Global keyboard shortcut alt+shift+h opens the form (static/src/js/client_support_systray.js:14).

## 2. Attachment to CORE
- Depends on base and web (manifest:32). Adds a systray entry (core registry category: core:web/static/src/webclient/navbar/navbar.js:19) and a user-menu item (core registry category user_menuitems: core:web/static/src/webclient/user_menu/user_menu_items.js:138). Uses the core display_notification client action (core:web/static/src/webclient/actions/client_actions.js:26), including links and class name parameters.
- No core model is inherited and no core method overridden. ADDS only. ALTERS CORE CONTROL: no.

## 3. New objects, security, automation, external calls
- New transient model client.support (client_support.py:42-44); field payload_preview computed.
- ACL: all internal users (base.group_user) full access to the wizard (security/ir.model.access.csv:2). No record rules; no company scoping. Any internal user can send.
- Config parameter seeded with the vendor support address: key cybrosys_support_client.endpoint_url, set at install and not updated afterwards (data/ir_config_parameter_data.xml:2-9; noupdate). The code reads the parameter, falling back to a default vendor address (client_support.py:32-37,146-151).
- EXTERNAL CALL (business level, outbound, from the ERP server): an HTTPS POST of a JSON body containing the user's name, email, phone, ticket text, support type, category, priority and the full content of any attached files (base64) to the vendor's support server; timeouts 5 s connect / 20 s read (client_support.py:37,93-131,161-169). Nothing is sent until the user presses Submit. No credentials are used or stored by the module; a fixed public vendor URL/number is embedded (see pointers). Also the browser opens a WhatsApp link (client_support.py:263-267).
- No automation or cron.

## 4. Odoo 19 compatibility
- Uses Odoo 19 style APIs (odoo.fields, requests, markupsafe); imports Markup (client_support.py:27) but is not used elsewhere in the read code. No references to models/fields absent from core 19 found in the Python; core registries used are present.
- Data privacy note: the attachment payload includes whatever record files the user attaches from the database attachment picker.
- Not checked: the CSS/XML template contents (static/src/xml, css).

## 5. Custom-to-custom dependencies
- None declared. It is packaged inside the folder base_accounting_kit-19.0.3.3.1 alongside sibling folders base_account_budget and base_accounting_kit (directory listing), but its own manifest does not depend on them.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the deployment allows outbound HTTPS to the vendor support host, and whether the business accepts sending user contact data and attachments to that vendor.
- UNKNOWN - EVIDENCE INSUFFICIENT: what the vendor service does with the submitted data (outside this source).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether this module is intended to be present in a rebranded product (it displays vendor branding and an alt+shift+h shortcut to all users).
