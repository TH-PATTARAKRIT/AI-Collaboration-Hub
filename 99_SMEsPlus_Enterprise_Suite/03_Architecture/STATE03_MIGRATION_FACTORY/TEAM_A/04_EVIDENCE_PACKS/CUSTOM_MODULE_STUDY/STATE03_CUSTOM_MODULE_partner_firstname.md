> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: partner_firstname

## 0. Header
- Module: partner_firstname
- License (confirmed in manifest): AGPL-3 (partner_firstname/__manifest__.py:16)
- Author (manifest): Camptocamp, Grupo ESOC Ingenieria de Servicios, Tecnativa, LasLabs, ACSONE SA/NV, Odoo Community Association (OCA) (partner_firstname/__manifest__.py:10-15)
- Version (manifest): 19.0.1.0.0 (partner_firstname/__manifest__.py:9)
- Path: addons_Extramodule/addons_extra/partner_firstname
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Splits a person's name into first name and last name on partners and users, and rebuilds the full display name from them in a chosen order (last-first, last-first with comma, or first-last) (models/res_partner.py:19-27, :93-110; models/base_config_settings.py:14-32).
- A setting "Partner names order" on the General Settings page, with a button to recalculate names of all non-company partners when the order changes (views/base_config_view.xml:9-27; models/base_config_settings.py:50-69).
- On install a post-install hook splits names of existing partners into first and last parts (partner_firstname/hooks.py:7-11; models/res_partner.py:205-218).
- Companies keep the whole name in the last-name slot (models/res_partner.py:165-167).

## 2. Attachment to CORE
- Depends declared: base_setup (manifest:20).
- Core objects extended: `res.partner` (fields, name compute, create/copy/default_get), `res.users` (default_get, name onchange, copy), `res.config.settings` (setting), and core views `base.view_partner_simple_form`, `base.view_partner_form`, `base.view_users_form`, `base_setup.res_config_settings_view_form` (views/res_partner.xml:5, :31; views/res_user.xml:5; views/base_config_view.xml:7).
- Overrides of core methods by name:
  - Field `name` on partner (models/res_partner.py:21-27): ALTERS CORE CONTROL. Core defines the name as a plain stored text field (core:base/models/res_partner.py:213); the module turns it into a stored computed field built from first/last names, with an inverse that splits typed text. All code (including other modules) that writes the name now goes through this compute/inverse.
  - `create` on partner (models/res_partner.py:29-51): ADDS before core — pre-fills first/last name from the provided name (core create still runs, :51). In Community 19 an `@api.model` create is treated as multi-record create (core:odoo/orm/decorators.py:321-323), so iterating over the list is valid. It also deletes `default_name` from the shared context (:48-49).
  - `copy` on partner (:53-60): ADDS (context flag) before core copy.
  - `default_get` on partner (:62-76) and on users (models/res_users.py:11-26): ADDS after core — fills first/last name defaults. Core partner default_get at core:base/models/res_partner.py:201.
  - `copy` on users (models/res_users.py:34-49): ADDS naming for the copy before core copy; sets login of the copy with the "(copy)" suffix.
  - `_check_name` constraint (models/res_partner.py:193-203): ADDS an extra Python check that a contact or company has a first or last name.
  - `_sql_constraints` entry named `check_name` set to an always-true check (models/res_partner.py:220-222): intended to REPLACE the core rule "Contacts require a name" (core:base/models/res_partner.py:326-329, ALTERS CORE CONTROL if effective). In Community 19 old-style `_sql_constraints` is no longer supported (core:odoo/orm/model_classes.py:162-163), so this replacement is probably ignored and the core rule stays (inference; runtime not tested). Since the computed name is an empty text rather than absent for blank first and last names (models/res_partner.py:110), the core rule may still pass while the module's Python check blocks blank names.
- Views: makes the name field read-only for non-company partners and required for companies, and adds first/last name inputs (views/res_partner.xml:8-11, :34-50); makes the name read-only on the user form (views/res_user.xml:8-11).
- The name-order setting is read with elevated access from system parameters (models/res_partner.py:87-91).

## 3. New objects, security, automation, external calls
- New fields: `firstname`, `lastname` on partner, indexed (models/res_partner.py:19-20); settings fields `partner_names_order`, `partner_names_order_changed` stored as system parameters (models/base_config_settings.py:14-25).
- New exception class `EmptyNamesError` (partner_firstname/exceptions.py:6-12).
- ACLs, groups, record rules, company scoping: none added. Settings write follows core rules for settings and system parameters; the bulk recalculation button runs through the settings model (models/base_config_settings.py:59-69) and updates system parameter with elevated access (:60-62).
- Automation: post-init hook only. External calls: none.

## 4. Odoo 19 compatibility
- Old-style `_sql_constraints` no longer supported (see above) — models/res_partner.py:220-222.
- Confirmed in Community 19: `res.users` delegates to partner via `_inherits` (core:base/models/res_users.py:165), `name` on users is a related field (core:base/models/res_users.py:252), `div id="companies"` in settings (core:base_setup/views/res_config_settings_views.xml:57), simple partner form and user form (core:base/views/res_partner_views.xml:39; core:base/views/res_users_views.xml:96).
- Hook signature `post_init_hook(env)` with env as the argument (partner_firstname/hooks.py:7) matches the 19 style; not runtime-tested.
- The user-side onchange named `_compute_name` (models/res_users.py:28-32) sets a field name on `res.users` from partner data; behaviour with the new `name` compute not tested.

## 5. Custom-to-custom dependencies
- None declared. Overlaps in the partner form with partner_company_type (both inherit `base.view_partner_form`).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the core "Contacts require a name" database rule is still active in the deployed database.
- UNKNOWN — EVIDENCE INSUFFICIENT: how the module behaves on partners created by other modules or imports that write only the full name (compute/inverse path not tested).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the recalculation button is restricted beyond core settings access.
