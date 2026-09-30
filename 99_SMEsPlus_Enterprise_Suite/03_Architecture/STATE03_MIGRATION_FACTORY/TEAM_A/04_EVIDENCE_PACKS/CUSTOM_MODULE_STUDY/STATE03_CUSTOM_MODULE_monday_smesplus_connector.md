> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: monday_smesplus_connector

## 0. Header
- Module: monday_smesplus_connector
- License (confirmed in manifest): AGPL-3 (monday_smesplus_connector/__manifest__.py:48)
- Author (manifest): Cybrosys Techno Solutions (monday_smesplus_connector/__manifest__.py:31)
- Version (manifest): 19.0.1.0.0 (monday_smesplus_connector/__manifest__.py:24); the bundled release note still says 17.0.1.0.0 initial commit (monday_smesplus_connector/doc/RELEASE_NOTES.md:4-9)
- Path: addons_Extramodule/addons_extra/monday_smesplus_connector
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Same capability as monday_odoo_connector, re-branded "Monday.com SMEsPlus Connector" (manifest:23): one-way import of Monday.com boards (with groups, items and column texts), Monday users and customer contacts from a board named "Contacts" into the ERP (monday_smesplus_connector/wizard/monday_connector.py:36-59,61-125,126-148).
- Differences from monday_odoo_connector found by file comparison of the two folders: (1) only the module name, menu icon path and view names differ in the manifest/views; (2) the wizard now pre-loads the emails of already-imported Monday contacts and skips a contact whose email is already present or missing, adding new emails to the set as it goes (wizard/monday_connector.py:74-76,113-124); (3) the users import looks up existing logins in one query and skips users without an email (wizard/monday_connector.py:135-148). Security ACL file and models are identical (directory comparison reported no differences).

## 2. Attachment to CORE
- Same as monday_odoo_connector. Depends on contacts (manifest:35). Extends res.partner and res.users with a Monday reference field; creates res.partner and res.users records from Monday data (wizard/monday_connector.py:115-124,142-148).
- Global view change: inherits the core partner form/kanban/list and users simple form/kanban/list views to turn off Create and Excel export (views/res_users_views.xml:10-13,23-26,36-42; views/res_partner_views.xml, same pattern as sibling). Because base views are edited, standard Contacts and Users screens lose New/export while installed. BLOCKS-ALTERS a core UI control. ALTERS CORE CONTROL: yes (UI-level).
- No core Python method overridden.

## 3. New objects, security, automation, external calls
- Same models and ACL as the sibling: six models, all internal users with full access, including the credentials model holding the Monday API token (security/ir.model.access.csv identical to sibling; sibling pointer monday_odoo_connector/security/ir.model.access.csv:2-7). A credential-like value is expected in monday.credential.token at runtime; none found in source.
- EXTERNAL CALLS (business level): outbound HTTPS POST read queries to Monday.com GraphQL service with the stored token, timeout 10 s (wizard/monday_connector.py:55-59,64-68,128-130). Up to 100 items per board per run.
- Imported Monday users become Odoo users (login = email) with a fixed initial password literal in code (a credential-like value exists at monday_smesplus_connector/wizard/monday_connector.py:146; not reproduced).
- Board import still appends groups and items again for boards that already exist (no duplicate check; wizard/monday_connector.py:85-107 pattern, same as sibling).
- No cron; on-demand wizard only.

## 4. Odoo 19 compatibility
- Same as sibling: core views used exist (core:base/views/res_users_views.xml:56,247,261); user creation with plain password and no groups not verified for 19 rules.
- The manifest still lists application True (manifest:51) and root menu without group restriction (wizard/monday_connector_views.xml:52-54).

## 5. Custom-to-custom dependencies
- None declared. Duplicate of monday_odoo_connector (same model names monday.credential, monday.board, monday.group, monday.item, item.column.value, monday.connector): cannot be installed together.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: which connector is the intended one and whether it is in use.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether a Monday account/token exists for the business.
- UNKNOWN - EVIDENCE INSUFFICIENT: post-import user access rights policy.
