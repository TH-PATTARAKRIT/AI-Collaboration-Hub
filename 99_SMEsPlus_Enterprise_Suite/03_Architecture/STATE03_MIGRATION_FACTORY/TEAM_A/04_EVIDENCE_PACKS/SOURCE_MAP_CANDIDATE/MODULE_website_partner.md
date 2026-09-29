# Source Map (candidate) — `website_partner`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_partner` |
| Display name | Website Partner |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c37b00abefe1ae3f` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_partner/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `website`
- Direct dependents in 300-module list (5): `website_blog`, `website_crm_partner_assign`, `website_customer`, `website_google_map`, `website_profile`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `website_event`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Partner module for website
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `res.partner`, `website.seo.metadata`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.partner`, `website.seo.metadata`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 27 of 28 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_partner (Website Partner)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_partner.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: base module holding website-related data for contacts (website_partner/__manifest__.py:9-11).

## A. Capabilities / functions
- Optional base module (not `auto_install`), depends only on website (website_partner/__manifest__.py:12). Installed as a dependency of website_customer, website_event, website_google_map, website_profile, website_blog and website_crm_partner_assign (their manifests).
- Core: gives each contact a public web page at `/partners/<name-id>` with picture, contact details and a rich-text description (website_partner/controllers/main.py:10-27; website_partner/views/website_partner_templates.xml:3-52).
- Core: contact fields for a short and a full public description, plus a published flag with change tracking (website_partner/models/res_partner.py:11-13).
- Core: contact form shows a website publish/unpublish button (website_partner/views/res_partner_views.xml:10-12).
- Core: chatter events "Partner published" / "Partner unpublished" (website_partner/data/website_partner_data.xml:9-20; website_partner/models/res_partner.py:21-27).
- Core: the contact's website URL is computed from the slug (website_partner/models/res_partner.py:15-19).
- Company's own contact is published by default at install (website_partner/data/website_partner_data.xml:3-5). Demo data (not test) publishes several demo contacts (website_partner/data/website_partner_demo.xml).

## B. Business objects, relationships, lifecycle
- Contact (res.partner, owned by base) enriched with SEO metadata, description fields and publication state (website_partner/models/res_partner.py:8-13); publication behaviour comes from the website multi-website publish mixin (website/models/res_partner.py:10; website/models/mixins.py:201-207).
- Lifecycle: unpublished -> published (visible to anyone at the partner URL) -> unpublished; each change is logged with a distinct subtype (website_partner/models/res_partner.py:21-27).
- Slug redirect: a request with a stale/incorrect slug is redirected to the canonical URL (website_partner/controllers/main.py:18-20).

## C. Validations, automation, security, multi-company
- The page is public but shown only if the contact is published on the current website; website editors (restricted editor group and above) can preview unpublished ones (website_partner/controllers/main.py:16-17). Otherwise a not-found response (website_partner/controllers/main.py:27).
- The page reads the partner with elevated rights by design ("do not use semantic controller due to SUPERUSER_ID") (website_partner/controllers/main.py:9,15). Fields rendered publicly: image, name, address, website, phone, email, description (website_partner/views/website_partner_templates.xml:22-48). Any data protection consequence for publishing a contact: UNKNOWN — EVIDENCE INSUFFICIENT.
- Description HTML is sanitised (styles stripped, override allowed) (website_partner/models/res_partner.py:11).
- No access-control rows or new record rules in this module. Website scoping through the multi-website publish mixin (website/models/res_partner.py:10); exact per-website behaviour: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs to other modules
- base/contacts: contact record; website: layout, publish mixin, SEO mixin (website_partner/models/res_partner.py:9).
- Downstream users that add partner-directory-like content: website_customer (references), website_crm_partner_assign (resellers), website_event (speakers), website_profile, website_blog (author) - by manifest dependency.
- mail (chatter subtypes) (website_partner/data/website_partner_data.xml:9-20).

## E. Configuration / defaults that change outcomes
- Published flag is the single switch controlling public visibility; default off except the company contact (website_partner/data/website_partner_data.xml:3-5).
- Translatable descriptions (website_partner/models/res_partner.py:11-12).

## F. Effective extension path (module names only)
- res.partner (website-family inheritors): website, website_partner, website_customer, website_crm_partner_assign, website_sale, website_sale_wishlist, website_slides.
- Templates `partner_detail` / `partner_page` have extension points for left/right columns used by dependents (website_partner/views/website_partner_templates.xml:36,49).

## G. Not verified
- Tests: none in this module. Multi-website publication semantics and SEO behaviours: UNKNOWN — EVIDENCE INSUFFICIENT.

