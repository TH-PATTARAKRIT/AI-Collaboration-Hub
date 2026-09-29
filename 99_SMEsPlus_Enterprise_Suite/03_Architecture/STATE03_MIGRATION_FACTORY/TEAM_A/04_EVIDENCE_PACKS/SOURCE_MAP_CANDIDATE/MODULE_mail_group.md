# Source Map (candidate) — `mail_group`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mail_group` |
| Display name | Mail Group |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `50e43c069373fb23` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mail_group/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `mail`, `portal`
- Direct dependents in 300-module list (1): `website_mail_group`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: None / Manage your mailing lists
- Inventory of user-facing artifacts (counts): menu items 2, views 12, window actions 6, server actions 0, reports 0, mail templates 3, scheduled jobs 1, wizards 1, web routes 9
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (5): `mail.group.message.reject` (Reject Group Message); `mail.group.member` (Mailing List Member); `mail.group` (Mail Group); `mail.group.message` (Mailing List Message); `mail.group.moderation` (Mailing List black/white list)
- Objects extended from other modules (1): `mail.alias.mixin`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `mail.group` ← Community: `website_mail_group`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.alias.mixin`

## 6. Actions / states / validation / automation / security
- State fields found: `mail.group.moderation` → ['allow', 'ban']
- Validation: 6 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Mail List: Notify group moderators every 1 days
- Security: groups declared 2 (`group_mail_group_manager`, `base.group_system`); record rules 10 (of which company-scoped by text 0); access rows 9

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

