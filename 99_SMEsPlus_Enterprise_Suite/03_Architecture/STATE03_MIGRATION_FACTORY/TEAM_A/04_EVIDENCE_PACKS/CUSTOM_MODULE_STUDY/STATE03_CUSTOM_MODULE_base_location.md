> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: base_location

## 0. Header
- Module: base_location
- License (confirmed in manifest): AGPL-3 (base_location/__manifest__.py:18)
- Author (manifest): Camptocamp, ACYSOS S.L., Alejandro Santana, Tecnativa, AdaptiveCity, Odoo Community Association (OCA) (base_location/__manifest__.py:10-17)
- Version (manifest): 19.0.1.0.3 (base_location/__manifest__.py:7)
- Path: addons_Extramodule/addons_extra/base_location
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds a "ZIP location" catalogue (postal code linked to a city, which is linked to state and country) and lets users pick a location once so that zip, city, state and country are filled consistently on partners, companies and employee private addresses (base_location/models/res_city_zip.py:11-26; models/res_partner.py:14-33,54-97; models/res_company.py:23-39; models/hr_employee.py:14-31).
- Validation: when a ZIP location is chosen, the partner's country, state, city and zip must all match it, otherwise a validation error names the partner and location (models/res_partner.py:99-138).
- Menus: Cities and Zips lists under the Contacts "Localization" menu (views/res_city_view.xml:55-60; views/res_city_zip_view.xml:42-48); a "Zips" button on the country form (views/res_country_view.xml:13-28).
- City uniqueness per state/country and zip uniqueness per city are intended (models/res_city.py:12-20; models/res_city_zip.py:28-35) - see section 4.

## 2. Attachment to CORE
- Depends on base_address_extended, contacts, hr (manifest:9).
- res.city (core:base_address_extended/models/res_city.py:7): adds one2many zip_ids and a uniqueness intent (models/res_city.py:8-20). ADDS after core.
- res.partner: adds stored, editable computed fields zip_id, and turns city_id, city, zip, country_id, state_id into computed-stored-editable fields (models/res_partner.py:14-33). Compute methods use hasattr(super()) fallbacks (res_partner.py:54-97). Extends core _address_fields with zip_id, city_id (res_partner.py:163-168; core:base/models/res_partner.py:660, core:base_address_extended/models/res_partner.py:21). ADDS after core.
- New constraint _check_zip on res.partner (res_partner.py:99-138): BLOCKS saving a partner whose address does not match the chosen ZIP location (skippable by a context flag skip_check_zip). ALTERS CORE CONTROL (adds a validation block on partner save, only when zip_id is set).
- res.company: adds city_id, zip_id, country_enforce_cities; extends core _get_company_address_field_names (res_company.py:41-48; core:base/models/res_company.py:121); wraps core _inverse_state / _inverse_country to set the skip flag (res_company.py:58-64; core:base/models/res_company.py:160,164). ADDS after core.
- hr.employee: redefines private_zip_id, private_city_id, private_city, private_zip, private_country_id, private_state_id as computed-stored fields, adds a similar constraint (models/hr_employee.py:14-31,97-136); also hr.employee.public related fields (hr_employee.py:169-178). See section 4.
- Model method _fields_view_get_address is overridden on res.partner (res_partner.py:149-161) and hr.employee (hr_employee.py:147-160). See section 4.
- Views inherit base.view_partner_form, base.view_company_form, base.view_country_form, hr.view_employee_form, base_address_extended.view_city_tree (views/*.xml, grep of inherit_id). Referenced core ids exist: base_address_extended.view_city_tree (core:base_address_extended/views/res_city_view.xml:4), contacts.menu_localisation (core:contacts/views/contact_views.xml:65), hr.view_employee_form (core:hr/views/hr_employee_views.xml:85), base.view_country_form (core:base/views/res_country_views.xml:18).
- The module also defines its own res.country search view record (views/res_country_view.xml:3-11).

## 3. New objects, security, automation, external calls
- New model: res.city.zip (models/res_city_zip.py:11). Display name shows "zip, city, state, country" (res_city_zip.py:37-45).
- ACLs (security/ir.model.access.csv:2-3): everyone (row with no group) read-only on res.city.zip; group Contact Creation (base.group_partner_manager) full access. The first row has an empty group column, i.e. read access is not restricted to internal users.
- No record rules, no company scoping on res.city.zip. No cron, no external calls in this module (data import is in the separate geonames import module).
- Demo data: demo/res_city_zip.xml (manifest:30).

## 4. Odoo 19 compatibility
- Class attribute _sql_constraints on res.city (models/res_city.py:12-20) and res.city.zip (models/res_city_zip.py:28-35): core 19 warns the attribute is no longer supported and expects models.Constraint (core:orm/model_classes.py:162-164). The uniqueness rules are probably not database-enforced (not executed).
- Method _fields_view_get_address: no definition or caller anywhere in the Community 19 tree (grep of core for the name returned nothing). The overrides at models/res_partner.py:149-161 and models/hr_employee.py:147-160 call super() on a method that does not exist in core 19 - dead code if never called, an error if called. Consequence: the domain on zip_id set by this method would not be applied by this route.
- hr.employee private address fields: in core 19 these live on hr.version and are delegated to hr.employee (core:hr/models/hr_version.py:89-97; core:hr/models/hr_employee.py:45). This module re-declares private_city, private_zip, private_state_id, private_country_id on hr.employee as own stored computed fields (models/hr_employee.py:27-31). Interaction with the delegated definitions is not verified. Also core hr.employee no longer defines _address_fields (grep of core hr), yet hr_employee.py:160-166 calls super()._address_fields().
- models/hr_employee.py:86 reads record.state_id on an employee where the private state field is intended; no state_id field found on hr.employee in core (grep core:hr/models/hr_employee.py, hr_version.py) - possible defect on that branch.
- Views: res_company_view.xml:21-22 hides the plain city field when country_enforce_cities is false and shows city_id otherwise - semantics not verified against core 19 company form.
- Core fields used exist: res.country.enforce_cities (core:base_address_extended/models/res_country.py:10), partner country_enforce_cities (core:base_address_extended/models/res_partner.py:18).
- Extends partner form domain expression "=?" - not checked.

## 5. Custom-to-custom dependencies
- None declared in manifest. Depended on by base_location_geonames_import (base_location_geonames_import/__manifest__.py:23); indirectly extended by l10n_th_base_location (via the importer; l10n_th_base_location/__manifest__.py:11).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the redefinition of hr.employee private_* fields is compatible with the hr.version delegation in core 19 at install/upgrade time (not executed).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the intended city/zip uniqueness is enforced by the database in Odoo 19.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the employee-side constraint is exercised by the suite's HR use.
