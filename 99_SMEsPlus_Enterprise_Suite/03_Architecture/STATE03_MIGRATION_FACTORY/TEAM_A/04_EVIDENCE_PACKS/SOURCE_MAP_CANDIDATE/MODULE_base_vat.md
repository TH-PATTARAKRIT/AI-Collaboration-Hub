# Source Map (candidate) — `base_vat`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `base_vat` |
| Display name | VAT Number Validation |
| Manifest version | 2.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `1b363746f15f714b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/base_vat/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (43): `l10n_at`, `l10n_be`, `l10n_bg`, `l10n_cl`, `l10n_cy`, `l10n_cz`, `l10n_de`, `l10n_dk`, `l10n_dz`, `l10n_es`, `l10n_fi`, `l10n_fr_account` … (+31)
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / —
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 1, wizards 1, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (4): `res.country`, `res.company`, `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.country`, `res.company`, `res.config.settings`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Base VAT: Sync updates from IAP VIES every 1 days
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 27 of 27 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: base_vat
Source revision: 19.0.post20260921 | Path root: odoo/addons | Method: read-only source reading, neutral wording
Note: the module description text (base_vat/__manifest__.py:`description`) says VIES "replaces" the offline check; the code and tests show a different flow (see B). Code and tests are treated as authoritative.

## A. Capabilities
- Country-aware tax-ID (VAT) format/check-digit validation on partner records, with normalisation of the stored value (base_vat/models/res_partner.py:107-164, 346-351, 946-955). Optional module (depends `account`), no auto-install (base_vat/__manifest__.py:`depends`).
- Optional online intra-community (VIES) status per partner via an Odoo-operated IAP service, shown as "Intra-Community Valid"; gated by a per-company checkbox "Verify VAT Numbers" (base_vat/models/res_company.py:10; base_vat/views/res_config_settings_views.xml:9-17; res_partner.py:92-99, 201-216, 271-298).
- Asynchronous update of pending VIES results: a daily scheduled job plus an inbound signed web callback (base_vat/data/ir_cron.xml:5-14; res_partner.py:299-330; base_vat/controllers/webhook.py:11-23).
- Expected-format hints per country shown in error messages (res_partner.py:25-88, 353-388).
- Fiscal-position hook: "VAT required" positions additionally require a valid VIES status in some cases (res_partner.py:962-972).
- Partner form shows label "Tax ID" and the VIES flag when applicable (base_vat/views/res_partner_views.xml:10-24). Country helper flag on whether a country has a foreign fiscal position (base_vat/models/res_country.py:9-18).
- Swiss-specific alternate VAT spellings offered for EDI partner matching (res_partner.py:174-187; TEST base_vat/tests/test_partner_matching.py:6-45).

## B. Tax-ID validation rules and where enforced (business level)
- Trigger: any create/edit of partner tax ID or country runs the check as a field "inverse" on both fields (res_partner.py:97-104, 166-168); on-screen changes run a soft check that only formats and never blocks (res_partner.py:170-172). The check is framework-called from `account`: the base hook that returns the value unchanged is owned by `account` (account/models/partner.py:849-873); base_vat overrides that hook.
- Country used = the country of the partner's commercial (parent/company) entity (account/models/partner.py:849-853). No country or no tax ID: value accepted as is (res_partner.py:109-110; TEST base_vat/tests/test_vat_numbers.py:74-98).
- Single character "/" is the accepted way to say "no valid tax ID"; any other single character raises an error (res_partner.py:111-119).
- A two-letter alphabetic prefix is treated as country code; prefix "EU" is accepted without checking for non-European partners; Greece is written "EL", UK Northern Ireland "XI" (res_partner.py:120-124, 132-142, 218-223; base/models/res_partner.py:28-31). If the country belongs to a "prefixed-VAT" group the prefix is stripped and checked against that country; else an EU-style prefixed number is checked against the prefix's country (res_partner.py:125-137, 154-163; TEST base_vat/tests/test_vat_numbers.py:74-98, 223-232).
- Number is normalised (spaces/punctuation removed, country specific formatting) before checking (res_partner.py:946-955; TEST test_vat_numbers.py:223-232 "BE0477.47.27.01" stored compact).
- Check function: a country-specific rule if this module defines one (about 30 countries, e.g. CH, RO, GR, HU, IE, MX, NO, PE, RU, TR, SA, UA, UY, IN, BR, VN, ID, TW, DE, IL - res_partner.py:391-945), else the generic library rule for that country, else the number passes (res_partner.py:346-351). "For unsupported countries only the country code is validated" (manifest description).
- Failure handling: mode "error" raises a message with expected-format sample; mode "setnull" blanks the tax ID instead (res_partner.py:107, 146-164; used with setnull by partner_autocomplete/models/res_partner.py:172, account_edi_ubl_cii/models/account_edi_common.py:694, 1270, 1298, l10n_es_edi_facturae/models/account_move.py:675).
- Bypass: context key `no_vat_validation` stores value unchecked (res_partner.py:144-146); used by portal/controllers/portal.py:548 and l10n_tr_nilvera_edispatch/models/stock_picking.py:317, 419.
- Double prefix (e.g. BEBE...) rejected (res_partner.py:149-151).
- VIES status flow: (1) offline check must pass first (TEST base_vat/tests/test_vies_iap.py:44-47); (2) only if at least one company has the checkbox on, the tax ID is posted to the IAP service (res_partner.py:201-216, 271-298); (3) result states "valid", "unassigned", "pending", "fault": partner flag is True only for "valid"; each result posts a note in the partner's message log for pending/fault/valid/unassigned (res_partner.py:332-344; TEST test_vies_iap.py:49-92); (4) pending results are resolved later by the daily job or the signed callback (res_partner.py:299-330; webhook.py:18-23; TEST test_vies_iap.py:94-131, 157-169).
- Inheritance: child contact with same tax ID as its parent copies the parent's VIES flag and computes after it (res_partner.py:202-216; TEST test_vies_iap.py:133-155); contact->company creation copies the flag without re-check (res_partner.py:987-992; TEST test_vat_numbers.py:122-139); imports skip recomputation (res_partner.py:974-985).
- Service failure (network error) -> status "fault", not a blocking error (res_partner.py:271-298).

## C. Validations / security / multi-company
- Enforcement points: save-time inverse (blocking, error mode); onchange (non-blocking); EDI/autocomplete callers (blank-on-fail). See B.
- Webhook security: signed, expiring (7 days) token derived from the tax ID; invalid token is logged and ignored; the update then runs with superuser rights on all partners with that tax ID (webhook.py:11-23; res_partner.py:283-285).
- IAP credentials: generated and stored as system parameters on first use; test mode uses dummy values; endpoint restricted to two fixed hosts (production or test) (res_partner.py:225-269).
- The VIES flag is tracked in the record history (res_partner.py:94-99). The module adds no access-rights file or record rules (manifest `data` lists only cron and views).
- Multi-company: checkbox is per company; UI display of VIES flag depends on the current company and whether the tax ID prefix equals the company's fiscal-country code (res_partner.py:189-199). The compute step runs if ANY company has the checkbox on (res_partner.py:204), regardless of the current company - so one company's setting causes lookups for shared partners. Fiscal-position rule uses the company passed in (res_partner.py:962-972; TEST test_vat_numbers.py:36-52).
- Error text uses the current/company-context country's custom tax label (res_partner.py:353-388).

## D. Handoffs
- Fiscal position auto-detection (`account`): "VAT required" positions call the hook overridden here (account/models/partner.py:216-222; base_vat/models/res_partner.py:962-972).
- Duplicate-partner detection by tax ID (`base`) considers prefix variants (base/models/res_partner.py:455-475).
- IAP service (external, Odoo-operated) receives: tax ID, database UUID, client identifier/token, callback URL (res_partner.py:271-298). This is an external integration.
- EDI import/export, partner autocomplete, LATAM check issuer VAT reuse the check: account_edi_ubl_cii, partner_autocomplete, l10n_es_edi_facturae, l10n_latam_check (callers listed in B and l10n_latam_check/models/l10n_latam_check.py:218).
- No ledger entry, stock or approval effect.

## E. Configuration that changes outcomes
- Company setting `vat_check_vies` (default off) (res_company.py:10; settings help text: default fiscal position depends on VIES result - base_vat/views/res_config_settings_views.xml:13).
- Partner country and tax ID prefix determine which rules run; context `no_vat_validation`; "/" placeholder; system parameters `iap_vies.endpoint`, `iap_vies.client_identifier`, `iap_vies.client_token` (res_partner.py:225-269); daily cron active by default (ir_cron.xml:10).
- Demo/test database uses the test IAP endpoint (res_partner.py:263-266).

## F. Extension path (module names only)
- Modules with base_vat in manifest dependencies: l10n_at, l10n_be, l10n_bg, l10n_cl, l10n_cy, l10n_cz, l10n_de, l10n_dk, l10n_dz, l10n_es, l10n_fi, l10n_fr_account, l10n_gr, l10n_hr, l10n_hu, l10n_id, l10n_ie, l10n_in, l10n_it, l10n_latam_base, l10n_latam_check, l10n_lu, l10n_lv, l10n_mr, l10n_mt, l10n_ng, l10n_nl, l10n_no, l10n_pe, l10n_ph, l10n_pl, l10n_pt, l10n_ro, l10n_rs, l10n_sa_edi, l10n_se, l10n_si, l10n_sk, l10n_tr_nilvera_base_vat, l10n_tw_edi_ecpay, l10n_uk, l10n_uz, l10n_za.
- Modules extending the partner object (res.partner) in general (not necessarily VAT logic): account, account_add_gln, account_edi_ubl_cii, account_peppol, account_peppol_response, auth_signup, base_address_extended, base_geolocalize, base_vat, bus, calendar, contacts, crm, delivery, event, hr, l10n_ar, l10n_au, l10n_be, l10n_br, l10n_ca, l10n_cl, l10n_de, l10n_es, l10n_fr, l10n_hu, l10n_in, l10n_it_edi, l10n_latam_base, l10n_nz, l10n_pe, l10n_ph, l10n_pl, l10n_ro, l10n_sa_edi, l10n_se, l10n_sg, l10n_th, l10n_tr_nilvera, l10n_uy, l10n_uz, loyalty, mail, partner_autocomplete, phone_validation, point_of_sale, portal, product, project, purchase, sale, stock, survey, website, website_sale (subset; full grep list is longer, ~130 modules).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: precise check-digit algorithms of the generic per-country rules delivered by the external library (not in this source tree).
- UNKNOWN — EVIDENCE INSUFFICIENT: content and behaviour of the remote IAP service; only request fields and returned statuses are visible.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the description-text claim "fall back to simple check if service unavailable" applies literally; code shows offline check always runs first and service failure only sets status "fault".
- UNKNOWN — EVIDENCE INSUFFICIENT: contents of the "prefixed-VAT" country group beyond its definition in base data (base/data/res_country_data.xml:1648 only located, members not read).

