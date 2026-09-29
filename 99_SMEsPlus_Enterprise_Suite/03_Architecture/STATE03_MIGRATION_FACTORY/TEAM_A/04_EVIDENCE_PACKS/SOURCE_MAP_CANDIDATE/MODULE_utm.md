# Source Map (candidate) — `utm`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `utm` |
| Display name | UTM Trackers |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c38c68b91300db61` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/utm/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `web`
- Direct dependents in 300-module list (7): `crm`, `event`, `hr_recruitment`, `im_livechat`, `link_tracker`, `sale`, `website`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `mass_mailing`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing / —
- Inventory of user-facing artifacts (counts): menu items 5, views 14, window actions 5, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (7): `utm.medium` (UTM Medium); `utm.mixin` (UTM Mixin); `utm.source` (UTM Source); `utm.source.mixin` (UTM Source Mixin); `utm.stage` (Campaign Stage); `utm.tag` (UTM Tag); `utm.campaign` (UTM Campaign)
- Objects extended from other modules (1): `ir.http`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `utm.medium` ← Community: `mass_mailing`, `mass_mailing_sms`; open-license custom/third-party scanned: —
- `utm.mixin` ← Community: `crm`, `hr_recruitment`, `link_tracker`, `sale`, `test_mass_mailing`; open-license custom/third-party scanned: —
- `utm.source` ← Community: `hr_recruitment`, `marketing_card`, `mass_mailing`; open-license custom/third-party scanned: —
- `utm.source.mixin` ← Community: `hr_recruitment`, `im_livechat`, `mass_mailing`, `test_mass_mailing`; open-license custom/third-party scanned: —
- `utm.campaign` ← Community: `crm`, `hr_recruitment`, `link_tracker`, `mass_mailing`, `mass_mailing_crm`, `mass_mailing_crm_sms`, `mass_mailing_sale`, `mass_mailing_sale_sms`, `mass_mailing_sms`, `sale`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `ir.http`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 4 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 10

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

