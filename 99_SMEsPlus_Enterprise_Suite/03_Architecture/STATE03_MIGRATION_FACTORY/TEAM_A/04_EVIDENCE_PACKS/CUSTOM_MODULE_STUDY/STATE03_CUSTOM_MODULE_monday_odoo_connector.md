> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: monday_odoo_connector

## 0. Header
- Module: monday_odoo_connector
- License (confirmed in manifest): AGPL-3 (monday_odoo_connector/__manifest__.py:48)
- Author (manifest): Cybrosys Techno Solutions (monday_odoo_connector/__manifest__.py:31)
- Version (manifest): 19.0.1.0.0 (monday_odoo_connector/__manifest__.py:24)
- Path: addons_Extramodule/addons/monday_odoo_connector
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- One-way import of data from the Monday.com work-management service into the ERP: boards (with owner, groups and items with their column texts), Monday users, and customer contacts taken from a board named "Contacts" (monday_odoo_connector/wizard/monday_connector.py:36-49,51-59,61-122,124-141; manifest description :26-28).
- Operators choose what to import in a wizard (users, boards, customers); groups and items always come with boards (wizard/monday_connector.py:36-59). The ledger of imported records is browsable under a "Monday" application menu: Boards, Groups, Items, Customers, Users, plus Configuration > Credentials and Connector (wizard/monday_connector_views.xml:52-67; views/*.xml).
- Nothing is sent to Monday except read queries; no write-back or export code exists although the wizard docstring mentions "Import and Export" (wizard/monday_connector.py:52-53).

## 2. Attachment to CORE
- Depends on contacts (manifest:35). Extends core res.partner (adds Boolean monday_reference, models/res_partner.py) and res.users (adds Char monday_reference, models/res_users.py).
- Creates core records: res.partner (name, phone, email, company name) for Monday contacts (wizard/monday_connector.py:107-122) and res.users (name, email, login = email, monday id) for Monday users (wizard/monday_connector.py:133-141). ADDS.
- View inheritance that changes core screens for everyone: the module inherits the core partner form, kanban and list views and the core users simple form, kanban and list views to switch off the Create button and Excel export (views/res_partner_views.xml:9-13,22-26,34-41; views/res_users_views.xml:10-14,23-27,36-43; core views base.view_partner_form, base.res_partner_kanban_view, base.view_partner_tree, base.view_users_simple_form, core:base/views/res_users_views.xml:56,247,261). Because inheritance edits the base views globally, not only the Monday menus, the standard Contacts and Users screens lose the New button and list export while the module is installed (view-level only; model access is unchanged). BLOCKS-ALTERS a core UI control (creation entry point and export in the standard partner and user lists). ALTERS CORE CONTROL: yes (UI-level).
- No core Python method is overridden.

## 3. New objects, security, automation, external calls
- New models: monday.credential (name, token), monday.board, monday.group, monday.item, item.column.value, monday.connector (transient wizard).
- ACLs (security/ir.model.access.csv:2-7): ALL internal users (base.group_user) have full read/write/create/delete on all six models including the credentials model. No groups, no record rules, no company scoping.
- Credential handling: an API access token for Monday is stored in a plain Char field on monday.credential (models/monday_credential.py, field token) and displayed masked in the form (views/monday_credential_views.xml:10,23); because of the ACL any internal user can read or overwrite it via the API. A credential-like value is expected there at runtime; no token value found in source.
- EXTERNAL CALLS (business level, outbound): HTTPS POST queries to Monday.com's public GraphQL service with the stored token in the Authorization header, timeout 10 s (wizard/monday_connector.py:55-59,64-68,126-128). Boards query pulls up to 100 items per board plus column texts, groups, owner names (wizard/monday_connector.py:64-68). Users query pulls id, name, email.
- Data effects to note: (a) every imported Monday user becomes an Odoo user with login equal to the email and a fixed initial password literal in code (a credential-like value exists at monday_odoo_connector/wizard/monday_connector.py:139; not reproduced); (b) board imports append groups and items again for boards that already exist, with no duplicate check (wizard/monday_connector.py:82-106); (c) the duplicate check for customers compares the email to a list of the boolean flags of all partners, so it never matches and customers are re-created on each run (wizard/monday_connector.py:110-113,114-122). The sibling module monday_smesplus_connector fixes (c) and the user duplicate lookup.
- Automation: none scheduled; runs on demand from the wizard.

## 4. Odoo 19 compatibility
- Core views referenced exist in 19: base.view_users_simple_form, base.view_users_tree, base.view_res_users_kanban (core:base/views/res_users_views.xml:56,247,261); partner views not re-verified by id.
- Uses ORM x2many command tuples (0, 0, vals) (wizard/monday_connector.py:86-106), still accepted in 19.
- res.users create with a plain password value and no groups (wizard/monday_connector.py:135-141): Odoo 19 user-creation/group rules not verified.
- Manifest marks the module as an application (manifest:51) and its root menu has no group restriction (wizard/monday_connector_views.xml:52-54).
- Not checked: static/ assets, i18n.

## 5. Custom-to-custom dependencies
- None declared. It is a near-duplicate of monday_smesplus_connector (same model names, same fields, same wizard); both cannot coexist because they define the same model names (monday.credential etc., models/*.py) and change the same core views.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether a Monday account, token or "Contacts" board exists for the business; no data or configuration was read.
- UNKNOWN - EVIDENCE INSUFFICIENT: which of the two Monday connector modules is meant to be installed in the target suite.
- UNKNOWN - EVIDENCE INSUFFICIENT: the license/security posture for storing third-party API tokens without restricted access.
- UNKNOWN - EVIDENCE INSUFFICIENT: how imported users are meant to be given (or denied) access rights after creation.
