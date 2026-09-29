# Source Map (candidate) — `theme_common`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `theme_common` |
| Display name | Theme Common |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / BOSS-SCOPE-REVIEW-THEME (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `95d1cbcceceacbd0` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/theme_common/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `website`
- Direct dependents in 300-module list (24): `theme_anelusia`, `theme_artists`, `theme_avantgarde`, `theme_aviato`, `theme_beauty`, `theme_bewise`, `theme_bistro`, `theme_bookstore`, `theme_clean`, `theme_enark`, `theme_graphene`, `theme_kea` … (+12)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / Snippets Library
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 7 of 8 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# theme_common — Revision 19.0.post20260921
- Purpose: hidden shared "Snippets Library" for themes (legacy `old_snippets` SCSS/JS, fonts/mixins SCSS, header preheader JS); manifest `theme_common/__manifest__.py:1-17`. Category Hidden, version 1.1.
- Dependencies: `website` (`theme_common/__manifest__.py:7`). Required by 24 of the 27 feature themes (not by theme_buzzy, theme_cobalt, theme_paptic, which depend directly on `website`; nor by theme_default).
- Models: yes, one abstract `theme.utils` extension (`theme_common/models/theme_common.py:4`); `_theme_common_post_copy` (`:7-15`) disables 7 optional colour-variable assets on theme switch. No fields, no tables.
- Security / rules / groups / crons / controllers: no (skeleton lists empty).
- Data: manifest loads `data/data.xml` (empty `<odoo>` element, `:1-3`) and 3 stub view files under `views/old_snippets/` (comment-only, 6 lines each). `data/ir_asset.xml` (59 `theme.ir.asset` records) is NOT listed in the manifest and is flagged as dead code in its own header comment (`theme_common/data/ir_asset.xml:4-9`).
- Static: 32 `static/src/old_snippets/*` folders (SCSS, 3 small JS), `static/src/scss/` (compat/mixins/fonts/options), `static/src/js/preheader.js:6` (patches header affix widget), `static/lib/YTPlayer/jquery.mb.YTPlayer.js` (third-party library).
- Business objects / business-meaning data: none.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether any downstream production database still references the dead asset records; rendered output.

