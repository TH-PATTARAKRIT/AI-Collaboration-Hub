> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: partner_company_type

## 0. Header
- Module: partner_company_type
- License (confirmed in manifest): AGPL-3 (partner_company_type/__manifest__.py:8)
- Author (manifest): ACSONE SA/NV, Odoo Community Association (OCA) (partner_company_type/__manifest__.py:9)
- Version (manifest): 19.0.1.0.0 (partner_company_type/__manifest__.py:7)
- Path: addons_Extramodule/addons_extra/partner_company_type
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Lets each partner that is a company carry a "legal form" (for example a company type with an abbreviation), chosen from a maintained list (partner_company_type/models/res_partner_company_type.py:7-13; models/res_partner.py:10-12; manifest:6).
- This on-disk copy ALSO re-creates a personal "Title" (honorific) list and field on partners, which is not part of the upstream summary (partner_company_type/models/res_partner.py:13-21; view field placed for non-company partners at views/res_partner.xml:10-11).
- Adds a "Company Types" configuration menu under the Contacts configuration menu (views/res_partner_company_type.xml:48-53).
- A demo record "Anonymous Company" is loaded only in demo mode (demo/res_partner_company_type.xml:5-8).

## 2. Attachment to CORE
- Depends declared: base, contacts (manifest:11).
- Core objects extended: `res.partner` (new fields, models/res_partner.py:7-13); core partner form `base.view_partner_form` (views/res_partner.xml:7, fields added after website at :9-17); Contacts configuration menu (views/res_partner_company_type.xml:51 references the Contacts configuration menu; core:contacts/views/contact_views.xml:50 (menu id res_partner_menu_config)).
- No Community method overridden. No ALTERS CORE CONTROL.
- Note on `title`: the Community 19 partner model has no title field and the Community 19 tree has no partner-title model (text search of core addons finds only translation files). This module redefines a `title` Many2one on the partner (models/res_partner.py:13) and a new model `res.partner.title` under the same name as the removed core object (models/res_partner.py:15-21). Effect: re-introduces a removed core concept; ADDS, does not replace core.

## 3. New objects, security, automation, external calls
- New models: `res.partner.company.type` (name required, translatable; abbreviation) (models/res_partner_company_type.py:7-13); `res.partner.title` (models/res_partner.py:15-21).
- New fields on partner: `partner_company_type_id` (label "Legal Form"), `title` (models/res_partner.py:10-13).
- ACLs: company type — read for internal users, full access for the partner-manager group (security/res_partner_company_type.xml:4-21); partner title — full read/write/create/delete for all internal users (security/ir.model.access.csv:2). No record rules, no company scoping.
- Uniqueness of company type name is declared through an old-style constraint list (models/res_partner_company_type.py:15-17); see section 4.
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- Old-style `_sql_constraints` is no longer supported in Community 19: the loader logs a warning and expects `models.Constraint` (core:odoo/orm/model_classes.py:162-163). So the company type name-uniqueness rule (models/res_partner_company_type.py:15-17) is likely NOT enforced in the database — inference from the loader message; runtime not tested.
- Absent from Community 19: partner `title` field and `res.partner.title` model (described above).
- Confirmed present: `base.view_partner_form` (core:base/views/res_partner_views.xml:103), `website` and `is_company` on the partner (core:base/models/res_partner.py:246, :277), Contacts configuration menu (core:contacts/views/contact_views.xml:50).
- View attribute `invisible="is_company==False"` uses expression form valid in 17+; not runtime-tested.

## 5. Custom-to-custom dependencies
- None declared. Functionally shares the partner form with partner_firstname (both edit the partner form; their `title`/name handling is independent).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether existing partner titles were migrated from an earlier Odoo version in the deployed database.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether other installed modules also define a partner `title` field (conflict not searched outside this module).
