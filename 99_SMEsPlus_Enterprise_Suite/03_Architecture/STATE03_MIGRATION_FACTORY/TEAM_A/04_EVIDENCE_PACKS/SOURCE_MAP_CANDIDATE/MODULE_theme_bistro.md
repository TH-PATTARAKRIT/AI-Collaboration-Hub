# Source Map (candidate) — `theme_bistro`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `theme_bistro` |
| Display name | Bistro Theme |
| Manifest version | 2.0.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / BOSS-SCOPE-REVIEW-THEME (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `bbfb16231e442a55` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/theme_bistro/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `theme_common`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_themes`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Theme/Food / Bistro, Restaurant, Bar, Pub, Cafe, Food, Catering
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `theme.utils`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `theme.utils`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 10 of 10 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# theme_bistro — Revision 19.0.post20260921
- Purpose: Odoo website theme, restaurant/bar/cafe/catering look; manifest summary: "Bistro, Restaurant, Bar, Pub, Cafe, Food, Catering". Category `Theme/Food`, version 2.0.0, sequence 220.
- Dependencies: `theme_common` (`theme_bistro/__manifest__.py:8`); auto_install none; application false.
- Models: one abstract model extending `theme.utils` (`theme_bistro/models/theme_bistro.py:4`), method `_theme_bistro_post_copy` (`:7`) toggles website views/assets when the theme is applied (calls: enable_view x2, enable_asset x2); no fields, no persisted business tables.
- Security / access / rules / groups: no (skeleton `access`, `rules`, `groups` empty; `security/` dir absent). Automation (cron/server actions/controllers): no (skeleton `crons`, `controllers` empty; no `controllers/` dir).
- Data: 47 snippet-override view files (`views/snippets/`); 101 QWeb templates, 112 `theme.ir.attachment` image records, 2 `<asset>` entries in `data/ir_asset.xml` (0 inactive legacy); data files: data/generate_primary_template.xml, data/ir_asset.xml, views/images_library.xml, views/layout.xml, views/new_page_template.xml. Executes `ir.module.module._generate_primary_snippet_templates` at install (`data/generate_primary_template.xml`).
- Manifest theme keys: `images_preview_theme`, `configurator_snippets`, `configurator_snippets_addons` (soft hook to `website_sale`, not a dependency), `theme_customizations`, `assets` (editor tour `static/src/js/tour.js`) — presentation/config metadata only.
- SCSS: bootstrap_overridden.scss, primary_variables.scss.
- Business objects / business-meaning data: none found in module (grep for cron/access/rule/group/automation/partner/product/blog/menu/page records in xml/py/csv returned no matches beyond prose text).
- UNKNOWN — EVIDENCE INSUFFICIENT: rendered visual output, image binary contents, translation (`i18n/*.po`) content, runtime effect on a live website.

