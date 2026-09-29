# Source Map (candidate) — `partner_autocomplete`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `partner_autocomplete` |
| Display name | Partner Autocomplete |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `4fd292b7bfbc383d` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/partner_autocomplete/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `iap_mail`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `point_of_sale`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / Auto-complete partner companies' data
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `iap.autocomplete.api` (IAP Partner Autocomplete API)
- Objects extended from other modules (4): `ir.http`, `res.company`, `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.http`, `res.company`, `res.config.settings`, `res.partner`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 47 of 47 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — partner_autocomplete
Source revision: 19.0.post20260921 | Module: "Partner Autocomplete" (partner_autocomplete/__manifest__.py:6) | category Hidden/Tools (:12) | LGPL-3 (:36)
Basis: static reading of manifest, models, data, views; front-end files inspected only by search; tests by title.
## A. Capabilities and optionality
- A1. Suggests company data (name, address, VAT, logo, industry, language, etc.) while a user types a company name, VAT or DUNS on partner/company forms, and enriches a record when a suggestion is chosen. partner_autocomplete/__manifest__.py:7-10; partner_autocomplete/models/res_partner.py:85-194,217-225; partner_autocomplete/static/src/js/partner_autocomplete_core.js:135-160
- A2. Bridge/utility module: auto_install with dependency on iap_mail. Enabled from the general settings option "Partner Autocomplete" (installs this module). partner_autocomplete/__manifest__.py:13-15,21; base_setup/models/res_config_settings.py:28; base_setup/views/res_config_settings_views.xml:110-111
- A3. Paid, credit-based: service "Partner Autocomplete", unit "Enrichments"; balance is integer credits. partner_autocomplete/data/iap_service_data.xml:4-10. Settings show a "buy more credits" widget and an insufficient-credit flag. partner_autocomplete/views/res_config_settings_views.xml:8-10; partner_autocomplete/models/res_config_settings.py:10-21
- A4. Automatic enrichment of a newly created company at creation time by an administrator (not in test or demo installation). partner_autocomplete/models/res_company.py:20-28,40-47
- A5. Fallback: a VAT lookup that gets no answer from the paid service tries the European VIES public check and uses its name/address if valid. partner_autocomplete/models/res_partner.py:102-138
## B. Objects and lifecycle
- B1. No new business model; one technical service object (iap.autocomplete.api) that calls the external service. partner_autocomplete/models/iap_autocomplete_api.py:13-16
- B2. Adds to company: "Enrich Done" flag (hidden on form). partner_autocomplete/models/res_company.py:18; partner_autocomplete/views/res_company_views.xml:8-10
- B3. Company auto-enrichment flow: pick domain (from e-mail unless a free-mail provider, else from website; localhost/example.com ignored) -> ask service -> fill only empty partner fields (logo always overwritten when provided) -> mark done. partner_autocomplete/models/res_company.py:49-101; (TEST) partner_autocomplete/tests/test_res_company.py:14-27
- B4. Returned codes are translated into Odoo records: country and state (by code, then name), city (when base_address_extended is installed and the country enforces cities: matched by zip, else name), industry, language (exact then generic). partner_autocomplete/models/res_partner.py:16-76; (TEST) partner_autocomplete/tests/test_autocomplete_address_extended.py:38-96
- B5. Tags: service-supplied classification codes become partner categories, using UNSPSC translated names when product_unspsc is installed; missing tags are created. partner_autocomplete/models/res_partner.py:196-215
- B6. After enrichment a chatter note listing the received data can be posted using an iap_mail template. partner_autocomplete/models/res_partner.py:227-254
## C. Validations, automation, security, external service
- C1. External service endpoint default https://partner-autocomplete.odoo.com (overridable by system parameter). Sent: database UUID, version, language, IAP account token, current company country and zip, plus the query (name/VAT/DUNS/GST/domain). Timeout 15 s (5 s for company auto-enrichment). partner_autocomplete/models/iap_autocomplete_api.py:16-34; partner_autocomplete/models/res_company.py:12,59
- C2. Refuses to call when no IAP account token exists or when running tests. partner_autocomplete/models/iap_autocomplete_api.py:20-24
- C3. Errors are absorbed into result codes ("Insufficient Credit", "No account token", connection errors) rather than blocking record creation. partner_autocomplete/models/iap_autocomplete_api.py:43-55; partner_autocomplete/models/res_partner.py:141-162
- C4. VAT returned by enrichment is re-validated when base_vat is installed; an invalid VAT is blanked ("set null"). partner_autocomplete/models/res_partner.py:164-173; (TEST) partner_autocomplete/tests/test_res_company.py:64
- C5. Auto-enrichment runs only for system administrators and only once per company (flag). partner_autocomplete/models/res_company.py:40-47. The web session tells administrators when enrichment is still pending. partner_autocomplete/models/ir_http.py:10-15
- C6. User-interface behaviour: autocomplete widget is attached to name, VAT and DUNS fields of partner and company forms; no new lookup if a shorter query already returned nothing; 15-character input is treated as an Indian GST number. partner_autocomplete/models/res_partner.py:217-225; partner_autocomplete/models/res_company.py:30-38; partner_autocomplete/static/src/js/partner_autocomplete_core.js:42,81,135-160
- C7. Security groups / access files / record rules: none defined by this module. partner_autocomplete/__manifest__.py:16-20. Any user who can edit a partner form can trigger a lookup — UNKNOWN — EVIDENCE INSUFFICIENT for server-side group checks (methods are plain model methods).
- C8. Company scoping: lookups use the current company's country and zip as search context. partner_autocomplete/models/iap_autocomplete_api.py:30-31
- C9. Privacy implication: typed company names/VAT and the database identifier are sent to Odoo's service; enrichment can be avoided by not installing/disabling the module. partner_autocomplete/models/iap_autocomplete_api.py:25-34
## D. Handoffs
- D1. Credits, account token, service registry, buy-credits widget: iap (and iap_mail). partner_autocomplete/models/iap_autocomplete_api.py:7,22; iap/models/iap_account.py:197,231-238
- D2. Address city data: base_address_extended (optional, checked at run time). partner_autocomplete/models/res_partner.py:42-56
- D3. VAT validation: base_vat (optional, checked at run time). partner_autocomplete/models/res_partner.py:166-172
- D4. Indian GST enrichment used by l10n_in for partner VAT/GST fill. l10n_in/models/res_partner.py:243
- D5. Point of sale reuses this module's front-end assets and lists it as a dependency. point_of_sale/__manifest__.py:10,203
- D6. Settings toggle: base_setup. base_setup/models/res_config_settings.py:28
## E. Configuration that changes outcomes
- E1. Installed or not (settings toggle); IAP credit balance; system parameter for service endpoint. base_setup/views/res_config_settings_views.xml:110-111; partner_autocomplete/models/iap_autocomplete_api.py:33
- E2. Company e-mail/website (drives auto-enrichment domain); company country and zip (search context). partner_autocomplete/models/res_company.py:93-101
- E3. Country "enforce cities" setting and installed language list influence what gets filled. partner_autocomplete/models/res_partner.py:44,70-75
## F. Extension path
- Modules referencing this module or its methods: iap, base_setup, point_of_sale, l10n_in, base (view tests). Enrichment result formatting can be extended through the res.partner formatting methods (owner here).
## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: cost per lookup and which lookups consume credit (service-side; only the message "no credit was consumed" on failure is visible).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end trigger thresholds (minimum characters, delay) beyond the snippets read; static/src/js not read in full.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether enrichment overwrites non-empty partner data when a user picks a suggestion in the UI (server-side company path only fills empty fields).
- UNKNOWN — EVIDENCE INSUFFICIENT: server-side access control for the lookup methods.

