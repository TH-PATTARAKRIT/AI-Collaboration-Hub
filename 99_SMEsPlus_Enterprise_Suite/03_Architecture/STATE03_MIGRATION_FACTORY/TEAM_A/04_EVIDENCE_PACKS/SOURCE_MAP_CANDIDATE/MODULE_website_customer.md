# Source Map (candidate) — `website_customer`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_customer` |
| Display name | Customer References |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `015dbece31857388` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_customer/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `website_crm_partner_assign`, `website_partner`, `website_google_map`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Publish your customer references
- Inventory of user-facing artifacts (counts): menu items 1, views 4, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 2
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `res.partner.tag` (Partner Tags - These tags can be used on website to find customers by sector, or ...)
- Objects extended from other modules (3): `website`, `res.partner`, `website.published.mixin`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `website`, `res.partner`, `website.published.mixin`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 0); access rows 6

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 48 of 48 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — website_customer
Source revision: 19.0.post20260921 | Module: "Customer References" (website_customer/__manifest__.py:5) | Category Website/Website (:6) | License LGPL-3 (:28)
Basis: static reading of manifest, models, controller, security files, views list, one test (TEST).

## A. Capabilities; core vs optional vs conditional
- A1. Publishes selected customers as public "business references" on the website under a customers page, filterable by country, industry, tag and text search, with paging (20 per page). website_customer/__manifest__.py:7,10; website_customer/controllers/main.py:16,54-162
- A2. Public detail page per published customer. website_customer/controllers/main.py:165-177
- A3. Adds "website tags" to partners for grouping references; tags are themselves publishable and default to published. website_customer/models/res_partner.py:10-17,23-40
- A4. Optional map view of references via the Google map layer (filter by country and industry). website_customer/controllers/main.py:18-33
- A5. Registers "References" as a suggested website page link. website_customer/models/website.py:10-13
- A6. Builder option for a customers filter in the website editor. website_customer/__manifest__.py:29-33
- A7. Not auto_install and not an application; installing pulls in website_crm_partner_assign (reseller/partner assignment, itself needing crm, account, partnership, portal) plus website_partner and website_google_map. website_customer/__manifest__.py:12-16; website_crm_partner_assign/__manifest__.py (depends list, module-level)
- A8. Conditional: a customer appears only if it is published AND has an "implemented by" partner (assigned reseller) set — customers without one never show. website_customer/controllers/main.py:69,25,177 ; assigned field owner: website_crm_partner_assign/models/res_partner.py:31-33
- A9. Demo customers only in demo mode. website_customer/__manifest__.py:17-19

## B. Business objects, relationships, lifecycle
- B1. Partner (owner: base; publishing and website scoping added by website; website description/SEO added by website_partner). website_customer/models/res_partner.py:7-8; website/models/res_partner.py:8-11; website_partner/models/res_partner.py:9-12
- B2. Partner Tag (new): name, colour class (info/primary/success/warning/danger), active flag, related partners, publish flag. website_customer/models/res_partner.py:23-37
- B3. Relationships: partner <-> tags (many-to-many); partner -> industry (owner: base) ; partner -> "Implemented by" partner (owner: website_crm_partner_assign). website_customer/models/res_partner.py:10-15; website_crm_partner_assign/models/res_partner.py:31-37
- B4. Lifecycle of a reference: partner record created -> assigned an implementing partner -> published (publish flag from website/website_partner) -> visible on list, detail and sitemap; unpublish or archive removes it. Tag: created published, can be archived or unpublished. website_customer/models/res_partner.py:39-40; website_customer/controllers/main.py:171
- B5. Detail URL is slug-checked; a wrong slug redirects to the canonical one; missing/unpublished gives not-found. website_customer/controllers/main.py:167-177
- B6. Sitemap entries for customers list, industries, and countries that have published assigned customers. website_customer/controllers/main.py:35-52

## C. Validations, automation, security, multi-company
- C1. Tag access: public and portal and all internal users read; Sales "Manager" role has full rights on tags; public and portal can read all industries. website_customer/security/ir.model.access.csv:2-7
- C2. Record rule: public and portal see only published tags. website_customer/security/ir_rule.xml:4-9
- C3. The customers pages read partner data with elevated rights (sudo) and depend on the publish flag and the assigned-partner filter rather than partner record rules; the code comment states semantic controller is avoided because of superuser use. website_customer/controllers/main.py:84,104,127,140,164-170
- C4. Search text matches partner name, website description, and industry name. website_customer/controllers/main.py:70-76
- C5. Tag list shown is limited to published tags attached to the partners on the current page. website_customer/controllers/main.py:143
- C6. Publishing a partner requires the publish right defined by the website mixin (write access to the record). website/models/mixins.py:246-266
- C7. Multi-company/multi-website: this module adds no company or website field. Partner website scoping (only show on a specific website) comes from the website module's multi-website mixin on partner, but the list query in this module does not filter on the current website. website/models/res_partner.py:8; website_customer/controllers/main.py:69. Consequence: a published reference is not restricted per website or per company by this module's query — UNKNOWN — EVIDENCE INSUFFICIENT whether other rules (e.g., partner record rules on company) still limit because sudo is used (sudo bypasses them).
- C8. No scheduled jobs, no constraints, no wizards.
- C9. (TEST) Technical-page test loads the /customers route only. website_customer/tests/test_website_customers_technical_page.py:8-9

## D. Handoffs
- D1. Reseller/partner assignment ("Implemented by"), grades, referral leads: website_crm_partner_assign. website_customer/__manifest__.py:13
- D2. Partner web profile fields (description, SEO): website_partner. website_customer/__manifest__.py:14
- D3. Map display and geolocation: website_google_map (uses geolocation base). website_customer/__manifest__.py:15; website_customer/controllers/main.py:8
- D4. Page, menu, sitemap, publish mixin, current website: website. website_customer/controllers/main.py:7; website_customer/models/website.py:7
- D5. Contacts menu (tags configuration menu placed under Contacts configuration): contacts (via crm dependency chain). website_customer/views/res_partner_views.xml:72-78; crm/__manifest__.py:20
- D6. Sales manager role for tag maintenance: sales_team (reached through the dependency chain). website_customer/security/ir.model.access.csv:5
- D7. Industry master data: base. website_customer/security/ir.model.access.csv:6-7

## E. Configuration / defaults that change outcomes
- E1. Per-partner publish flag (default not published for partners) decides visibility. website_partner/models/res_partner.py:13
- E2. Per-partner "Implemented by" value must be set for a partner to be listed. website_customer/controllers/main.py:69
- E3. Tags default to published and to colour class "info". website_customer/models/res_partner.py:36,39-40
- E4. Google Maps key per website enables map elements. website_customer/controllers/main.py:141; website/models/website.py:184
- E5. Page size fixed at 20. website_customer/controllers/main.py:16

## F. Effective extension path (module names only)
- website_crm_partner_assign, website_partner, website_google_map, website. No module in this tree lists website_customer as a dependency (manifest grep).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: contents of the customer list and detail page templates beyond link structure.
- UNKNOWN — EVIDENCE INSUFFICIENT: how website_google_map renders the map for this module.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether publishing a partner also needs consent handling (no privacy/consent logic seen in this module).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of the builder option (JavaScript not read).

