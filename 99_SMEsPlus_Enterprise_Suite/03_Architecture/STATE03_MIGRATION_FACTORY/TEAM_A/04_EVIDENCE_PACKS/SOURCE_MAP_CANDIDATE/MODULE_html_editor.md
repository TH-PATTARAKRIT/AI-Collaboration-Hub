# Source Map (candidate) — `html_editor`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `html_editor` |
| Display name | HTML Editor |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `5cf7d4199fe8c311` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/html_editor/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `bus`, `web`
- Direct dependents in 300-module list (6): `html_builder`, `mail`, `portal`, `web_unsplash`, `website`, `website_profile`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `point_of_sale`, `test_html_field_history`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / 
        A Html Editor component and plugin system
    
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 15
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `html_editor.converter.test` (Html Editor Converter Test); `html_editor.converter.test.sub` (Html Editor Converter Subtest); `html.field.history.mixin` (Field html History)
- Objects extended from other modules (21): `ir.http`, `base`, `ir.attachment`, `ir.qweb`, `ir.qweb.field`, `ir.qweb.field.integer`, `ir.qweb.field.float`, `ir.qweb.field.many2one`, `ir.qweb.field.contact`, `ir.qweb.field.date`, `ir.qweb.field.datetime`, `ir.qweb.field.text`, `ir.qweb.field.selection`, `ir.qweb.field.html`, `ir.qweb.field.image`, `ir.qweb.field.monetary`, `ir.qweb.field.duration`, `ir.qweb.field.relative`, `ir.qweb.field.qweb`, `ir.ui.view`, `ir.websocket`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `html.field.history.mixin` ← Community: `project`, `test_html_field_history`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `ir.http`, `base`, `ir.attachment`, `ir.qweb`, `ir.qweb.field`, `ir.qweb.field.integer`, `ir.qweb.field.float`, `ir.qweb.field.many2one`, `ir.qweb.field.contact`, `ir.qweb.field.date`, `ir.qweb.field.datetime`, `ir.qweb.field.text`, `ir.qweb.field.selection`, `ir.qweb.field.html`, `ir.qweb.field.image`, `ir.qweb.field.monetary`, `ir.qweb.field.duration`, `ir.qweb.field.relative`, `ir.qweb.field.qweb`, `ir.ui.view`, `ir.websocket`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

