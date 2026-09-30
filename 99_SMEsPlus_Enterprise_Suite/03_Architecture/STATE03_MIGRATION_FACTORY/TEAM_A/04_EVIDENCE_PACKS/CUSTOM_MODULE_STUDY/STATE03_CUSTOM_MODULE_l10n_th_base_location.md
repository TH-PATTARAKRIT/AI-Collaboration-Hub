> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: l10n_th_base_location

## 0. Header
- Module: l10n_th_base_location
- License (confirmed in manifest): AGPL-3 (l10n_th_base_location/__manifest__.py:8)
- Author (manifest): Ecosoft, Odoo Community Association (OCA) (l10n_th_base_location/__manifest__.py:9)
- Version (manifest): 19.0.0.0.2 (l10n_th_base_location/__manifest__.py:6)
- Path: addons_Extramodule/addons_extra/l10n_th_base_location
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Loads Thai administrative locations (postal code with sub-district and district, province and codes) from two bundled files (Thai-language and English-language versions, about 7,400 rows each) instead of downloading from the internet (wizard/geonames_import.py:13-21,55-75; data/TH_th.txt, data/TH_en.txt line counts 7426 each).
- Adds district code and sub-district code to the ZIP location record (models/res_city_zip.py:8-14).
- Thai addressing behaviour: for Thai addresses the bundled "city" text is a pair "sub-district, district"; on partners the first part is written to the street2 line and the second to the city line (models/res_partner.py:10-18); on companies the same split happens when a ZIP location is picked (models/res_company.py:15-21).
- Thai province names are shown without the country suffix in state display names (models/res_country_state.py:10-17) - see section 4.
- The wizard adds a language choice (Thai/English) shown only when Thailand is selected (wizard/geonames_import.py:13-26; wizard/geonames_import_view.xml:11-18). Its own help text says that to fetch from Geonames again the module must be uninstalled (geonames_import.py:15-18).

## 2. Attachment to CORE
- Depends on base_location_geonames_import (manifest:11), thereby on base_location, base_address_extended, contacts, hr.
- res.partner: override of compute method _compute_city (ADDS after the base_location compute; then rewrites street2 and city for Thai partners with a ZIP location) (models/res_partner.py:10-18). Effect: for country code TH, city holds the district text and street2 holds the sub-district text. Note that the override writes street2, a core address field, as a side effect of a city compute.
- res.company: override of onchange handler _onchange_zip_id (ADDS after base_location) and of core _inverse_street2 (wraps core with the skip-zip-check flag) (models/res_company.py:10-21; core:base/models/res_company.py:148). ADDS after core.
- res.country.state: override of name_get (models/res_country_state.py:10-17): intended to REPLACE the display name for Thai states. name_get is not present in the Community 19 base models (grep of core:base/models returned nothing), so this override is probably not called in Odoo 19.
- city.zip.geonames.import (wizard from base_location_geonames_import): overrides prepare_zip (ADDS district codes, geonames_import.py:37-42) and get_and_parse_csv (REPLACES the download with a local file read when country is Thailand, else calls the original) (geonames_import.py:55-76). Original at base_location_geonames_import/wizard/geonames_import.py:92-95,97-125.
- Defines override of select_zip (geonames_import.py:44-53) but the parent wizard exposes only _select_zip (base_location_geonames_import/wizard/geonames_import.py:70-73); super().select_zip does not exist there - dead or failing code.
- ALTERS CORE CONTROL: none (address formatting/data only).
- Views inherit base_location.city_zip_tree (views/res_city_zip_view.xml:3-12; defined at base_location/views/res_city_zip_view.xml:15) and the geonames import form (wizard/geonames_import_view.xml:3-20).

## 3. New objects, security, automation, external calls
- New fields on res.city.zip (district_code, sub_district_code) and transient wizard fields is_thailand, location_thailand_language. No new models. No ACLs, groups or record rules added (inherits those of the parent modules).
- No cron. No external calls in the Thai path (local file read); non-Thai countries fall through to the parent wizard's internet download (see base_location_geonames_import file).
- Data files bundled: data/TH_th.txt, data/TH_en.txt; demo/TH_en.txt (used only when a test context flag is set, geonames_import.py:59-62). The demo files are not listed in the manifest data list (manifest:12).

## 4. Odoo 19 compatibility
- name_get override on res.country.state (models/res_country_state.py:10) - name_get not present in core 19 base models (grep core:base/models); likely inactive.
- select_zip override calls a non-existent parent method (see section 2).
- _compute_is_thailand calls ensure_one on a compute method (geonames_import.py:23-26): compute methods can be invoked on multi-record sets; behaviour with several wizard records is not verified.
- models/res_company.py:19-20 assumes the city name contains ", " (indexes [1]); the partner version guards against a missing comma (res_partner.py:17); company version does not.
- Leftover debug comment "import pdb" in models/res_partner.py:14 (comment only).
- Referenced parent view id base_location.city_zip_tree exists in the workspace copy of base_location (base_location/views/res_city_zip_view.xml:15).
- Tests use fixed data; not checked.

## 5. Custom-to-custom dependencies
- Depends on base_location_geonames_import (manifest:11) which depends on base_location. Also extends models added by base_location (res.city.zip) and by base_location_geonames_import (city.zip.geonames.import).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: source and licensing terms of the bundled Thai location data files (no attribution found in the files read; README not opened).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether Thai address printing on documents relies on street2 = sub-district and city = district (consumer modules not studied).
- UNKNOWN - EVIDENCE INSUFFICIENT: behaviour of the state display name in Odoo 19 for Thai provinces.
