> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: l10n_th_partner

## 0. Header
- Module: l10n_th_partner
- License (confirmed in manifest): AGPL-3 (l10n_th_partner/__manifest__.py:9)
- Author (manifest): Ecosoft, Odoo Community Association (OCA) (l10n_th_partner/__manifest__.py:7)
- Version (manifest): 19.0.1.0.0 (l10n_th_partner/__manifest__.py:6)
- Path: addons_Extramodule/addons_extra/l10n_th_partner
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Thai partner master-data conventions: a "Tax Branch" text (branch code such as 0000/0001) on partners and companies (l10n_th_partner/models/res_partner.py:15; models/res_company.py:9-11; views/res_company_view.xml:6-8; views/res_partner_view.xml:22-26 for contact child forms).
- Company partners are named from a separate "Name Company" field combined with a legal-form prefix and suffix (e.g. Thai company forms such as limited company) so the displayed partner name follows Thai naming (models/res_partner.py:16-18,46-57; models/res_partner_company_type.py:9-10; data/res.partner.company.type.csv lists seven Thai legal forms with prefix/suffix).
- Persons: the display name is title + name parts (Thai honorific titles loaded from data/res.partner.title.csv, ~70 rows) (models/res_partner.py:38-44).
- On install, existing partners get their company-name field back-filled from their current name (hooks.py:6-10; models/res_partner.py:66-70).
- The name field on the partner form is made read-only, so names are edited through the component fields (views/res_partner_view.xml:9-11).
- Adds a "Legal Form" grouping filter in partner search (views/res_partner_view.xml:29-43) and a title field on the user form (views/res_users_view.xml:2-11).

## 2. Attachment to CORE
- Depends on two other addons, partner_company_type and partner_firstname (manifest:11); neither is a core Community module (see section 5). Core objects extended: res.partner, res.company, res.users (models/*.py).
- res.partner create override: ADDS before core create - copies the entered name into name_company for company records and, when no name is given, builds the name from lastname/firstname (models/res_partner.py:20-29). Declared with the single-record decorator while iterating over the argument as a list (see section 4). Core create at core:base/models/res_partner.py:927.
- res.partner _compute_name (name is composed from parts): the base compute comes from partner_firstname, not from core (no _compute_name in core:base/models/res_partner.py, grep). The override REPLACES the name for companies with prefix + company name + suffix and calls the parent for persons (res_partner.py:49-57).
- _get_computed_name and _check_name overrides also target methods from partner_firstname, not core (res_partner.py:38-44,72-80): _check_name relaxes the "at least one name" rule for companies that have a company name. Effect: RELAXES a validation of the parent module for company partners; not a core control. ALTERS CORE CONTROL: no core control altered directly.
- res.users: overrides _compute_name to re-trigger on first/last name onchange (models/res_users.py:10-12).
- Views inherit base.view_partner_form (core:base/views/res_partner_views.xml, exists), base.view_res_partner_filter (filter group_company exists at core:base/views/res_partner_views.xml:335), base.view_company_form (vat field at core:base/views/res_company_views.xml:41) and partner_firstname/partner_company_type views.
- post_init_hook runs a data back-fill on every install (manifest:20).

## 3. New objects, security, automation, external calls
- New fields: res.partner.branch, res.partner.name_company (indexed), res.company.branch (related to partner, editable), res.partner.company.type.prefix/suffix (translatable).
- Data: Thai partner titles and company legal forms loaded as seed data (manifest:13-14).
- No ACLs, groups, record rules, cron or external calls in this module.
- Company scoping: none added.

## 4. Odoo 19 compatibility
- models/res_partner.py:20-29 overrides create with @api.model and loops "for val in vals" as if vals were a list; core 19 create takes a list of value dictionaries (core:base/models/res_partner.py:927, decorator core:orm/decorators.py:357-372). With the single-record decorator, a dictionary argument would be iterated by key. Whether partner_firstname's create wrapper shields this is not verified (module not read).
- res_partner.py:41 reads self.title.name inside an api.model method (no record set) - may behave as an empty title; not verified.
- Methods _compute_name, _get_computed_name, _check_name and exceptions.EmptyNamesError belong to partner_firstname (imported at res_partner.py:7); absent from core 19 by design.
- res.partner.title / res.partner.company.type data loaded by CSV with external ids like title_001; no conflicts checked.
- View xpaths into core partner form (res_partner_view.xml:9-12,22) - structure of the 19 partner form not verified (not checked).
- from odoo import SUPERUSER_ID, api, _ (hooks.py:3) fine; the hook uses env directly (Odoo 19 hook signature).

## 5. Custom-to-custom dependencies
- partner_company_type and partner_firstname (manifest:11) - both exist as folders in the workspace under addons and addons_extra (directory listing); not read here (outside this assignment).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: behaviour of the inherited name compute and the create override with the actual partner_firstname code (not studied).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the read-only name field breaks import/API creation flows that only send the name.
- UNKNOWN - EVIDENCE INSUFFICIENT: how the tax branch value is consumed by tax reports/invoices (consumer modules not studied here; branch field appears unused inside this module beyond display).
