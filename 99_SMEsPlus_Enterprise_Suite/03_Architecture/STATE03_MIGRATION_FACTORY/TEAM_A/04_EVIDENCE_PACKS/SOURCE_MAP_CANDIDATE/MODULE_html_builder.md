# Source Map (candidate) — `html_builder`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `html_builder` |
| Display name | HTML Builder |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `f6bab7c760312060` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/html_builder/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `html_editor`, `mail`
- Direct dependents in 300-module list (2): `website`, `website_blog`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (3): `mass_mailing`, `website_event`, `website_sale`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Uncategorized / Generic html builder
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 15 of 15 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — html_builder
Source revision: 19.0.post20260921 | Module: "HTML Builder" (html_builder/__manifest__.py:2) | License LGPL-3 (:69)
Basis: static reading of manifest, test, and static-asset directory listing. Front-end framework module (brief note).

## A. Capabilities; core vs optional
- A1. Provides a generic visual page/email content builder framework (sidebar, block gallery, customize panel, option plugins for background, image, shape, font, layout, alignment, borders, shadows, etc.). Stated purpose: used by the website builder and the mass-mailing editor. html_builder/__manifest__.py:3-8 (description); html_builder/static/src (directories: sidebar, snippets, plugins) (listing)
- A2. No data records, no menus, no access rules, no Python models, no controllers, no cron. Python package init is empty; manifest has no data section. html_builder/__init__.py (0 lines); html_builder/__manifest__.py (no 'data' key)
- A3. Optionality: not auto_install and not an application; it is present only because another module depends on it. html_builder/__manifest__.py:21 (depends only). Modules that list it as dependency: website, website_blog, website_event, website_sale, website_crm_partner_assign, mass_mailing, theme_test_custo (grep of manifests).
- A4. Its main script/style bundle is loaded lazily when the editor is ready; a separate bundle is loaded inside the editing iframe; another for the "add snippet" dialog; dark-mode styles go only to the dark backend bundle. html_builder/__manifest__.py:28-67

## B. Business objects
- B1. None defined. Editing state is client-side; persistence is done by the host module (for pages: website; for emails: mass_mailing) and by html_editor's view-saving methods. html_editor/models/ir_ui_view.py:295-360 (save of edited section, owner html_editor). UNKNOWN — EVIDENCE INSUFFICIENT how the builder client calls the save route (front-end not read).

## C. Validations, security, multi-company
- C1. No security artifacts in this module. Access is governed by the host module's routes and by html_editor's controllers (login required for attachment/media routes). html_editor/controllers/main.py:216,375,400 (auth user)
- C2. (TEST) A build-time check asserts the main builder bundle contains no "edit" stylesheets (these belong only to the iframe bundle). html_builder/tests/test_html_builder_assets_bundle.py:12-19
- C3. Multi-company: UNKNOWN — EVIDENCE INSUFFICIENT (no data model here).

## D. Handoffs
- D1. Editor core (text editing, media dialog, link tools, collaboration, AI text generation): html_editor. html_builder/__manifest__.py:21
- D2. Website page building, website-specific snippets/options: website (includes html_builder.assets in its editor bundle). website/__manifest__.py:445
- D3. Email design in mass mailing: mass_mailing. mass_mailing/__manifest__.py:84
- D4. Mail dependency exists only to support a test helper for mail models (comment in manifest). html_builder/__manifest__.py:18-20

## E. Configuration
- E1. None found in this module. Version marker 0.1. html_builder/__manifest__.py:14

## F. Extension path (module names only)
- website, website_blog, website_event, website_sale, website_crm_partner_assign, mass_mailing, theme_test_custo (asset/option extensions via manifests). Individual plugin registrations inside those modules: UNKNOWN — EVIDENCE INSUFFICIENT.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of individual builder options and plugins (JavaScript not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: which snippet templates each host module registers for the builder.
- UNKNOWN — EVIDENCE INSUFFICIENT: relation between this newer builder and the older web_editor-style flows still routed by /web_editor/* compatibility aliases (only alias existence seen in html_editor/controllers/main.py).

