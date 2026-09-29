# Source Map (candidate) — `portal`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `portal` |
| Display name | Customer Portal |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `4415ca5bfdb7bfe9` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/portal/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`, `html_editor`, `http_routing`, `mail`, `auth_signup`
- Direct dependents in 300-module list (15): `account`, `auth_passkey_portal`, `auth_password_policy_portal`, `auth_totp_portal`, `digest`, `event`, `loyalty`, `mail_group`, `payment`, `portal_rating`, `project`, `spreadsheet` … (+3)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `mass_mailing_sms`, `test_mail_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / Customer Portal
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 2, server actions 1, reports 0, mail templates 0, scheduled jobs 0, wizards 5, web routes 6
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (4): `portal.share` (Portal Sharing); `portal.wizard` (Grant Portal Access); `portal.wizard.user` (Portal User Config); `portal.mixin` (Portal Mixin)
- Objects extended from other modules (8): `ir.http`, `mail.thread`, `ir.ui.view`, `ir.qweb`, `res.config.settings`, `mail.message`, `res.partner`, `res.users.apikeys.description`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `portal.share` ← Community: `project`; open-license custom/third-party scanned: —
- `portal.wizard.user` ← Community: `website`; open-license custom/third-party scanned: —
- `portal.mixin` ← Community: `account`, `l10n_in_ewaybill`, `point_of_sale`, `project`, `purchase`, `sale`, `test_mail_full`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `ir.http`, `mail.thread`, `ir.ui.view`, `ir.qweb`, `res.config.settings`, `mail.message`, `res.partner`, `res.users.apikeys.description`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 3

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

