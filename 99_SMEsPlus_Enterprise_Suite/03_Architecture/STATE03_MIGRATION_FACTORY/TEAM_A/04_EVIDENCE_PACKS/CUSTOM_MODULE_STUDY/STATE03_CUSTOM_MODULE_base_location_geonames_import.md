> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: base_location_geonames_import

## 0. Header
- Module: base_location_geonames_import
- License (confirmed in manifest): AGPL-3 (base_location_geonames_import/__manifest__.py:13)
- Author (manifest): Akretion, Agile Business Group, Tecnativa, AdaptiveCity, Odoo Community Association (OCA) (base_location_geonames_import/__manifest__.py:15-21)
- Version (manifest): 19.0.0.0.2 (base_location_geonames_import/__manifest__.py:10)
- Path: addons_Extramodule/addons_extra/base_location_geonames_import
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- A wizard that downloads a public postal-code list for chosen countries from the geonames.org service and loads it as states, cities and ZIP locations into the location catalogue provided by base_location (wizard/geonames_import.py:24-28,98-125,195-199; wizard/geonames_import_view.xml:8-11).
- New entries are created when missing; existing ones are matched by name and kept (geonames_import.py:127-193,217-254).
- The wizard text states it will "delete missing entries" from the new file (wizard/geonames_import_view.xml:11): after a full import (not a test import limited by a context row cap), ZIPs and cities of that country that are absent from the downloaded file are removed; if a bulk delete fails the code retries one by one and only logs the failures (geonames_import.py:201-215,255-260).
- Option to convert city and state names to title case or upper case (geonames_import.py:30-50).
- Per-country column mapping for the state name/code in the source file is stored on the country record, seeded for Spain and Italy (models/res_country.py:11-12; data/res_country_data.xml:2-9).

## 2. Attachment to CORE
- Depends only on base_location (manifest:23), which brings base_address_extended, contacts, hr.
- Extends core res.country with two integer settings (models/res_country.py:9-12); shown to developer-mode users on the country form (views/res_country_view.xml, groups base.group_no_one; inherits base.view_country_form, core:base/views/res_country_views.xml:18).
- Writes to core models res.country.state and res.city (geonames_import.py:132,158,190). No core method is overridden. ADDS only. ALTERS CORE CONTROL: no override, but the wizard can create states and delete cities/zips in bulk for a country (data operation, not a control).
- Menu "Import from Geonames" under the Contacts Localization menu (wizard/geonames_import_view.xml:39-44; core:contacts/views/contact_views.xml:65).

## 3. New objects, security, automation, external calls
- New model: city.zip.geonames.import (transient wizard) (geonames_import.py:24-26).
- ACL: only system administrators (base.group_system) have access to the wizard (security/ir.model.access.csv:2).
- No record rules, no company scoping (location data is global). No cron.
- EXTERNAL CALL (business level): on import the server issues an HTTP GET to the public postal-code download address of geonames.org per selected country, timeout 15 seconds; the base address is read from a system parameter named "geonames.url" and defaults to a plain http address (geonames_import.py:98-105). The response archive is extracted into a temporary server folder (geonames_import.py:113-118). No credentials are used in this module.

## 4. Odoo 19 compatibility
- Models used exist in core 19: res.city (core:base_address_extended/models/res_city.py:7), res.country.state, res.country (fields geonames_* are added by this module). res.city.zip comes from base_location.
- Imports the requests library at module load (geonames_import.py:16); not declared in the manifest external_dependencies (manifest has none) - environment must provide it.
- Line geonames_import.py:215 formats a message with a malformed placeholder ("%d ... %") using item.name - a likely runtime formatting error only on the failed-delete path.
- Depends on base_location's res.city.zip whose uniqueness constraints use the unsupported _sql_constraints attribute in 19 (see base_location file); imported duplicates would not be blocked by DB in that case (not executed).
- Test file present (tests/) - not checked.

## 5. Custom-to-custom dependencies
- Depends on base_location (manifest:23). Is the dependency of l10n_th_base_location (l10n_th_base_location/__manifest__.py:11).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the server in the target environment permits outbound access to the geonames download address, or whether a mirror is configured via the "geonames.url" system parameter.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether deleting cities/ZIPs can break partner records that reference them (ondelete rules of referencing fields not fully traced; res.city.zip.city_id cascades on city delete: base_location/models/res_city_zip.py:22).
- UNKNOWN - EVIDENCE INSUFFICIENT: the source data license/terms of the geonames.org dataset for redistribution in a product.
