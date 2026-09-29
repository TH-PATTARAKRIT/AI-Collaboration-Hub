# Source Map (candidate) — `google_address_autocomplete`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `google_address_autocomplete` |
| Display name | Google Address Autocomplete |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `ccb9aa97317164b4` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/google_address_autocomplete/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `point_of_sale`, `website_sale_autocomplete`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / Assist with automatic completion & suggestions when filling address
- Inventory of user-facing artifacts (counts): menu items 0, views 4, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 2
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.config.settings`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 31 of 31 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: google_address_autocomplete
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Suggests and completes street addresses while a user types, using the Google Places service, and fills street, city, state, ZIP, country and street number (google_address_autocomplete/__manifest__.py:5-9; google_address_autocomplete/controllers/google_address_autocomplete.py:23-33,97-191).
- Optional: enabled from the General Settings integration toggle; depends only on web; no auto-install flag (google_address_autocomplete/__manifest__.py:11; base_setup/models/res_config_settings.py:32).
- Conditional on a stored Google Places API key: without a key the suggestion endpoint returns an empty list (google_address_autocomplete/controllers/google_address_autocomplete.py:206-210).
- Applied to the street field of the contact form, the contact address form and the company form (google_address_autocomplete/views/res_partner_views.xml:8-10,19-21; google_address_autocomplete/views/res_company_views.xml:9-11). Also applied to street fields in all form views of contacts, but only when the country model carries the "enforce cities" capability, i.e. when city-list localization is present (google_address_autocomplete/models/res_partner.py:8-13).

## B. Business objects, relationships, lifecycle
- No new stored business objects. One added setting: Google Places API key kept as a system parameter (google_address_autocomplete/models/res_config_settings.py:9-12).
- Flow: user types at least 6 characters (default threshold 5, exclusive) -> list of suggestions (formatted address + place id) -> on pick, second call returns address components -> translated into contact address fields with country and state matched to existing country/state records (google_address_autocomplete/controllers/google_address_autocomplete.py:98-103,44-81,142-191).
- Field mapping priority: country, street number, locality, postal town, route, postal code, admin levels; first value wins, later ones do not overwrite (google_address_autocomplete/controllers/google_address_autocomplete.py:35-37,51-52).
- City matching: if a city record exists for the name and country it is attached; state is derived from the city when Google gave none (google_address_autocomplete/controllers/google_address_autocomplete.py:74-80).
- House number: if Google omits it, guessed from what the user typed after removing zip/street/city (google_address_autocomplete/controllers/google_address_autocomplete.py:83-95,179-181). Street display prefers the longer of Google's formatted street and the assembled one to avoid abbreviations (google_address_autocomplete/controllers/google_address_autocomplete.py:183-190).

## C. Validations, automation, security, credentials
- Suggestion endpoint (public route): returns nothing when the caller is not an internal user (assertion caught) or no key is stored (google_address_autocomplete/controllers/google_address_autocomplete.py:196-211).
- Full-detail endpoint: internal users only; other callers get an access error (google_address_autocomplete/controllers/google_address_autocomplete.py:213-218). (TEST) an unauthenticated call to the full endpoint returns an access error (google_address_autocomplete/tests/test_ui.py:237-261).
- External-service implication: each keystroke-driven lookup sends the typed partial address plus a session token, optional country and language, to Google over the internet with the company's API key; timeout 2.5 seconds; timeouts or invalid replies degrade to empty results; service error messages are logged (google_address_autocomplete/controllers/google_address_autocomplete.py:38-39,105-131,154-161,193-194). Billing must be enabled on the Google project (link in settings: google_address_autocomplete/views/res_config_settings_views.xml:18-21).
- Credential implication: one shared API key stored as a system parameter, retrieved with elevated rights server-side; not returned to the browser by these routes (google_address_autocomplete/controllers/google_address_autocomplete.py:196-198).
- The `use_employees_key` argument is accepted but not used to select a different key (google_address_autocomplete/controllers/google_address_autocomplete.py:196-198).
- Settings key field visible only when the module toggle is on; the standard warning block is removed (google_address_autocomplete/views/res_config_settings_views.xml:10,25).
- Company scoping: none; key and threshold are database-wide parameters.

## D. Handoffs to other modules
- Settings page and toggle: base_setup (google_address_autocomplete/views/res_config_settings_views.xml:7; base_setup/models/res_config_settings.py:32).
- Contacts, company, countries, states, cities: base and city-localization modules (google_address_autocomplete/controllers/google_address_autocomplete.py:54,62,77). City-list module name: UNKNOWN — EVIDENCE INSUFFICIENT.
- Web client widget and website use of the endpoints (route flagged for website context): website module if present (google_address_autocomplete/controllers/google_address_autocomplete.py:200,213); consumers: UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration/defaults that change outcomes
- System parameter for API key (google_address_autocomplete/models/res_config_settings.py:12).
- System parameter for minimum partial-address size, default 5 (google_address_autocomplete/controllers/google_address_autocomplete.py:98).
- Country/language restriction parameters accepted by the search function (google_address_autocomplete/controllers/google_address_autocomplete.py:97,112-115); not exposed by the public route.

## F. Effective extension path
- Localization modules that use their own street field templates are supported by widget assignment to street or street-name fields (google_address_autocomplete/models/res_partner.py:11-13). Extension of the Google call is via overriding the route call method (used in tests: google_address_autocomplete/tests/test_ui.py:242-246).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side widget behavior (debounce, error display).
- UNKNOWN — EVIDENCE INSUFFICIENT: Google usage cost or quota handling.

