# Source Map (candidate) — `base_address_extended`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `base_address_extended` |
| Display name | Extended Addresses |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `33e87ecac076802e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/base_address_extended/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `contacts`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `l10n_br`, `l10n_cn_city`, `l10n_pe`, `l10n_tw`
- Custom / third-party modules that declare a dependency (name — license only) (1): `base_location` — AGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Add extra fields on addresses
- Inventory of user-facing artifacts (counts): menu items 1, views 5, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `res.city` (City)
- Objects extended from other modules (2): `res.country`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `res.city` ← Community: `l10n_br`, `l10n_pe`, `l10n_pe_pos`; open-license custom/third-party scanned: `base_location`
- This module's own extension of other modules' objects: `res.country`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 26 of 27 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: base_address_extended (Odoo 19.0.post20260921)
Scope: only pointers cited; anything else is UNKNOWN — EVIDENCE INSUFFICIENT.

## A. Capabilities
- Splits a street into street name, house number and door number, kept in sync both directions with the single street line. base_address_extended/models/res_partner.py:10-15,24-37.
- Adds a managed list of cities (name, zip, country, state) and lets an address pick a city from it. base_address_extended/models/res_city.py:6-15; base_address_extended/models/res_partner.py:17.
- Per-country option "Enforce Cities": when on, the address form shows a city picker instead of free-text city. base_address_extended/models/res_country.py:10-13; base_address_extended/views/base_address_extended.xml:28-39.
- Purpose stated: pick city from a list in specific countries, mainly for e-invoicing/EDI codes. base_address_extended/__manifest__.py:13-15.
- Optional module (not auto-install); depends on base and contacts. base_address_extended/__manifest__.py:23.

## B. Business objects, relationships, lifecycle
- City (new): belongs to one country (required), optional state limited to that country; ordered by name; searchable by name or zip; label shows "name (zip)". base_address_extended/models/res_city.py:9-21.
- Contact/partner (extended): optional link to a City; city_id becomes part of the address block copied between related contacts. base_address_extended/models/res_partner.py:17,20-22.
- Country (extended): the enforce flag; a "Cities" shortcut button on the country form. base_address_extended/views/res_country_view.xml:9-21.
- Lifecycle: choosing a city fills city text, zip and state; clearing it (on an existing record) empties them; changing country clears a city that belongs to another country. base_address_extended/models/res_partner.py:47-62.
- Contact-type children inherit the parent's city link (TEST). base_address_extended/tests/test_street_fields.py:46-67.

## C. Validations, automation, security
- Street parsing rules are exercised across many international formats (TEST). base_address_extended/tests/test_street_fields.py:15-44. Exact parsing logic lives in shared tools: odoo/tools/misc.py:1950 (outside addons; not read in detail): UNKNOWN — EVIDENCE INSUFFICIENT.
- No hard constraint found that blocks saving an address without a city when the country enforces cities; enforcement is by form visibility only. base_address_extended/views/base_address_extended.xml:32,38 (observation; server-side constraint not found in module).
- Access: partner managers full rights on cities; all internal users read-only. base_address_extended/security/ir.model.access.csv:2-3.
- Public (website visitor) lookups of a city by name run with elevated rights to allow autocomplete/checkout. base_address_extended/models/res_partner.py:64-76.
- No record rules or company scoping: cities are shared across companies (no company field). base_address_extended/models/res_city.py:12-15.
- Street/address fields of a contact-type child with a parent are read-only in the form. base_address_extended/views/base_address_extended.xml:15,33.
- No audit or session implications found.

## D. Handoffs
- contacts menu: Cities menu placed under Contacts > Configuration > Localisation. base_address_extended/views/res_city_view.xml:39-42.
- Partner form (base) and its child-contact form: city picker injected. base_address_extended/views/base_address_extended.xml:58-90.
- Country form (base). base_address_extended/views/res_country_view.xml:6-21.
- Other Community modules that depend on it: l10n_br, l10n_pe, l10n_cn_city, l10n_tw (manifests); address autocomplete uses city lookup: google_address_autocomplete/controllers/google_address_autocomplete.py:77; partner_autocomplete/models/res_partner.py (references city_id).
- Base partner defines a same-named city lookup that this module overrides. base/models/res_partner.py:1258.

## E. Configuration/defaults
- "Enforce Cities" per country: default off (plain boolean). base_address_extended/models/res_country.py:10-13.
- Cities are master data to be loaded by the user or localization modules; none loaded by this module (no data files). base_address_extended/__manifest__.py:17-22.

## F. Effective extension path
- contacts, base; localizations l10n_br, l10n_pe, l10n_cn_city, l10n_tw; google_address_autocomplete, partner_autocomplete.

## G. Not verified
- Behaviour of website address forms and portal editing with city list: UNKNOWN — EVIDENCE INSUFFICIENT.
- Effect on printed address layouts / reports: UNKNOWN — EVIDENCE INSUFFICIENT.
- Universal rules: none stated.

