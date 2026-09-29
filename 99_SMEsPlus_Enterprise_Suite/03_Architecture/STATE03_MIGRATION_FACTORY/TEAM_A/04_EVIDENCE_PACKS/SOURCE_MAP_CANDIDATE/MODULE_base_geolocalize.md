# Source Map (candidate) — `base_geolocalize`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `base_geolocalize` |
| Display name | Partners Geolocation |
| Manifest version | 2.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `684519606d39b83c` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/base_geolocalize/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`
- Direct dependents in 300-module list (3): `hr_attendance`, `website_crm_partner_assign`, `website_google_map`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `website_sale_collect`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / —
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `base.geo_provider` (Geo Provider); `base.geocoder` (Geo Coder)
- Objects extended from other modules (2): `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.config.settings`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 33 of 33 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: base_geolocalize (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities
- Converts a partner's postal address into map coordinates (latitude/longitude) using an external geocoding service; manifest title "Partners Geolocation", depends only on base_setup (base_geolocalize/__manifest__.py:5,11).
- OPTIONAL: it is installed through a settings switch "GeoLocalize" on the general settings page, not core (base_setup/models/res_config_settings.py:29; base_setup/views/res_config_settings_views.xml:165-168). No auto_install in manifest (base_geolocalize/__manifest__.py:3-22).
- Two shipped providers: OpenStreetMap (default in practice) and Google Maps (needs a key) (base_geolocalize/data/data.xml:3-11).
- Also offers reverse lookup (coordinates to city/country/postcode) used by attendance check-in (base_geolocalize/models/base_geocoder.py:200-224; hr_attendance/controllers/main.py:63).

## B. Business objects and lifecycle
- Geo Provider: small list of named providers with a technical name (base_geolocalize/models/base_geocoder.py:16-21).
- Geo Coder: a service layer with no stored data; picks the configured provider, else the first provider found (base_geolocalize/models/base_geocoder.py:32-39).
- Partner gains "Geolocation Date" (base_geolocalize/models/res_partner.py:10); the coordinate fields themselves belong to the base partner (base/models/res_partner.py:270).
- Lifecycle: user presses "Compute based on address" / "Refresh" on a new "Partner Assignment" tab -> coordinates and date stored (base_geolocalize/views/res_partner_views.xml:9-29; base_geolocalize/models/res_partner.py:33-55).
- If an address is retried with only city/state/country when the full address finds nothing (base_geolocalize/models/res_partner.py:26-31).

## C. Validations, automation, security
- Changing any address element (street, zip, city, state, country) without also supplying new coordinates resets both coordinates to zero, so stale positions are not kept (base_geolocalize/models/res_partner.py:12-21).
- Geolocation is skipped during data import, tests, module install/demo load unless forced by context flag (base_geolocalize/models/res_partner.py:35-41).
- Addresses that cannot be matched trigger a warning notification to the acting user listing partner names (base_geolocalize/models/res_partner.py:58-64; (TEST) base_geolocalize/tests/test_geolocalize.py:42-63).
- Google provider without a key raises a blocking error and leaves coordinates unset (base_geolocalize/models/base_geocoder.py:131-136; (TEST) base_geolocalize/tests/test_geolocalize.py:26-36).
- Privacy implication: address text is sent to third-party services (OpenStreetMap or Google) (base_geolocalize/models/base_geocoder.py:92-95,142-147).
- Access: internal users may only read providers; no write/create/delete (base_geolocalize/security/ir.model.access.csv:2). No record rules or company scoping defined in this module (no rules file in data list, base_geolocalize/__manifest__.py:12-18).
- Provider form is view-only (create/delete disabled) (base_geolocalize/views/geo_provider_view.xml:9). Provider edit rights: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- Coordinates fields: base module. Settings page and on/off switch: base_setup. Attendance location capture: hr_attendance (hr_attendance/controllers/main.py:63). Partner-to-lead assignment by distance: website_crm_partner_assign (website_crm_partner_assign/models/crm_lead.py:114-126). Store pickup / warehouse coordinates: website_sale_collect (website_sale_collect/models/stock_warehouse.py:22; website_sale_collect/models/delivery_carrier.py:96). Map display: website_google_map (dependent by manifest).

## E. Configuration that changes outcomes
- Setting "API" chooses provider; stored as system parameter base_geolocalize.geo_provider (base_geolocalize/models/res_config_settings.py:10-15).
- Google key stored as system parameter, shown only when Google is selected (base_geolocalize/models/res_config_settings.py:17-21; base_geolocalize/views/res_config_settings_views.xml:14-16).
- Google queries reorder country names such as "X, Republic of" for better matching (base_geolocalize/models/base_geocoder.py:182-188).

## F. Extension path (Community modules depending on it)
- hr_attendance, website_crm_partner_assign, website_google_map, website_sale_collect (manifest dependency scan of addons).

## G. Not verified
- Live provider behaviour and usage limits of external services: UNKNOWN — EVIDENCE INSUFFICIENT.
- External-provider tests are tagged external and excluded from standard runs (base_geolocalize/tests/test_geolocalize.py:10).

