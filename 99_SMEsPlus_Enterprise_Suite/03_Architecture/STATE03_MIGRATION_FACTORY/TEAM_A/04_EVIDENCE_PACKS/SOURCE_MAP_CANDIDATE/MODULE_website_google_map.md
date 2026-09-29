# Source Map (candidate) — `website_google_map`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_google_map` |
| Display name | Google Maps |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `2e65b6067f309d22` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_google_map/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base_geolocalize`, `website_partner`
- Direct dependents in 300-module list (2): `website_crm_partner_assign`, `website_customer`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Show your company address on Google Maps
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 36 of 37 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_google_map (Google Maps)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_google_map.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: show partner/company addresses on a Google map; the API key is configured in the website settings (website_google_map/__manifest__.py:6,9).

## A. Capabilities / functions
- Optional add-on (no `auto_install`); depends on base_geolocalize and website_partner (website_google_map/__manifest__.py:11). Pulled in as a dependency by website_customer (website_customer/__manifest__.py:15).
- Core: a public map page (`/google_map`) meant to be embedded in a website page inside a frame; it plots published partners with clustering and links each marker to the partner detail page (website_google_map/controllers/main.py:10-25, 30-74; website_google_map/views/google_map_templates.xml:3-27).
- Selection modes: an explicit list of partner ids (only companies), or a named domain provided by extension code, otherwise nothing is plotted (website_google_map/controllers/main.py:27-28, 35-49).
- Result count is capped at 80 unless a limit is supplied (website_google_map/controllers/main.py:43).
- Output per partner: id, name, address text, latitude and longitude (website_google_map/controllers/main.py:51-62).
- Link target: `/customers/` when the caller's link base mentions customers, else `/partners/` (website_google_map/controllers/main.py:63-66).
- Uses the website's Google Maps key if set; otherwise loads the map library without a key (website_google_map/controllers/main.py:68-73; website_google_map/views/google_map_templates.xml:17-22). The key is a field on the website record (website/models/website.py:188).

## B. Business objects, relationships, lifecycle
- No own model. Reads published contacts (res.partner from base, publication from website_partner / website multi-website mixin) and their stored coordinates (from base_geolocalize) (website_google_map/controllers/main.py:32-47, 60-61; website/models/res_partner.py:10; base_geolocalize/models/res_partner.py:33-52).
- Coordinates are produced by the geocoding action of base_geolocalize and stored with a localisation date; failed geocoding notifies the user (base_geolocalize/models/res_partner.py:33-60). Partners without coordinates are returned with empty coordinates (website_google_map/controllers/main.py:60-61); how the map page treats them: UNKNOWN — EVIDENCE INSUFFICIENT.

## C. Validations, automation, security, multi-company
- Public route, elevated read of partners (website_google_map/controllers/main.py:30,32). Only records published on the current website are included, always added to the domain (website_google_map/controllers/main.py:45-47). For the id-list mode, non-numeric ids are silently ignored (website_google_map/controllers/main.py:36-38).
- Exposed publicly for each plotted partner: name, address, coordinates (website_google_map/controllers/main.py:56-62). Whether a published contact's address is intended to be public: UNKNOWN — EVIDENCE INSUFFICIENT.
- The `limit` value is converted to an integer without a range check (website_google_map/controllers/main.py:43). Effect of bad input: UNKNOWN — EVIDENCE INSUFFICIENT.
- Partner data is embedded as safe script data (website_google_map/controllers/main.py:7,71).
- No access-control rows or record rules; no company scoping other than website publication.
- Geocoding is skipped during import, tests, module loading and demo install unless forced (base_geolocalize/models/res_partner.py:34-39).

## D. Handoffs to other modules
- base_geolocalize (owner): geocoding providers, latitude/longitude, date localised (base_geolocalize/__manifest__.py:11). website_partner: partner page target `/partners/<id>` and publication (website_partner/controllers/main.py:10).
- website_customer (references): supplies its own selection (assigned partners, filtered by industry and country) via the domain hook and uses the `/customers/` link base (website_customer/controllers/main.py:15-32; website_customer/views/website_customer_templates.xml:178).
- website (owner of the Google Maps key and the static-map/link helpers on partners) (website/models/website.py:188; website/models/res_partner.py:14-30).
- website_crm_partner_assign: depends on this module and reuses the map controller (website_crm_partner_assign/__manifest__.py:25; website_crm_partner_assign/controllers/main.py:12,188) - see its note.

## E. Configuration / defaults that change outcomes
- Website Google Maps API key (per website): absent means the map library loads keyless, which may be restricted by the provider (website/models/website.py:188). Provider terms: UNKNOWN — EVIDENCE INSUFFICIENT.
- Domain hook default returns nothing (website_google_map/controllers/main.py:27-28): extension modules define the meaning of "dom".

## F. Effective extension path (module names only)
- Controller GoogleMap subclassed by: website_customer (website_customer/controllers/main.py:15), website_crm_partner_assign (website_crm_partner_assign/controllers/main.py:188). Whether the latter overrides the domain hook: UNKNOWN — EVIDENCE INSUFFICIENT.
- res.partner in this family: website, website_partner, website_customer, website_crm_partner_assign, base_geolocalize.

## G. Not verified
- Map rendering scripts and marker behaviour in the browser (static JS not traced): UNKNOWN — EVIDENCE INSUFFICIENT. Tests: none.

