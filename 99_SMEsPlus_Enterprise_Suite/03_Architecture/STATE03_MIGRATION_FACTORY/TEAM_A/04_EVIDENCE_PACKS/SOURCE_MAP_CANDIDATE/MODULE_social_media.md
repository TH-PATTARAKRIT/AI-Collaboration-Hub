# Source Map (candidate) — `social_media`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `social_media` |
| Display name | Social Media |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `42f403e29a0ec1ce` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/social_media/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`
- Direct dependents in 300-module list (1): `website`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `mass_mailing`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Social Marketing / Social media connectors for company settings.
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `res.company`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.company`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 14 of 14 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: social_media
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Purely technical "front" module giving the company record a set of social-network account fields so other modules can reuse them (social_media/__manifest__.py:5-10).
- Optional: depends only on base; no auto-install flag, no settings toggle (social_media/__manifest__.py:13).
- Fields cover eight networks: X, Facebook, GitHub, LinkedIn, YouTube, Instagram, TikTok, Discord (social_media/models/res_company.py:10-17).

## B. Business objects, relationships, lifecycle
- Single extension of the Company record with eight free-text account fields; no new objects and no lifecycle (social_media/models/res_company.py:7-17).
- Fields are plain text (not validated as links) (social_media/models/res_company.py:10-17).
- Sample data: the main demo company is populated with public Odoo social links (social_media/demo/res_company_demo.xml:3-12) (demo only).

## C. Validations, automation, security, credentials
- No validation, constraint, automation, access rule or group is defined by the module (manifest lists only a view and demo data: social_media/__manifest__.py:15-20).
- Visibility: the Social Media section of the company form replaces the base placeholder section and is shown only to users in the technical/debug-features group (social_media/views/res_company_views.xml:9-10). Access to write follows Company record permissions from base: UNKNOWN — EVIDENCE INSUFFICIENT.
- No credentials are stored; values are public account references (social_media/models/res_company.py:10-17).

## D. Handoffs to other modules
- Company record and its form view are owned by base (social_media/views/res_company_views.xml:7).
- Consumers of these fields (e.g. website footers, email templates) are not in this module: UNKNOWN — EVIDENCE INSUFFICIENT for this scope.

## E. Configuration/defaults that change outcomes
- No defaults on fields (social_media/models/res_company.py:10-17). Demo data sets values only when demo data is loaded (social_media/__manifest__.py:18-20).
- Per-company values: fields live on the company, so each company can hold its own accounts (social_media/models/res_company.py:7-8).

## F. Effective extension path
- Modules that need social account fields depend on social_media rather than redefining them (stated intent: social_media/__manifest__.py:7-10). Specific dependents: UNKNOWN — EVIDENCE INSUFFICIENT.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: which modules consume these fields.
- UNKNOWN — EVIDENCE INSUFFICIENT: field-level access beyond the debug-group visibility of the section.

