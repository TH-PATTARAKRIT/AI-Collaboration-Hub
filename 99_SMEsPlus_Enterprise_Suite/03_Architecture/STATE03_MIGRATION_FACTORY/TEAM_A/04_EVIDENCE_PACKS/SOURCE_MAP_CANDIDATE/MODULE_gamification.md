# Source Map (candidate) — `gamification`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `gamification` |
| Display name | Gamification |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `3e9e8a61e4e2b15a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/gamification/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `mail`
- Direct dependents in 300-module list (4): `gamification_sale_crm`, `hr_gamification`, `survey`, `website_profile`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources / —
- Inventory of user-facing artifacts (counts): menu items 7, views 26, window actions 10, server actions 0, reports 0, mail templates 4, scheduled jobs 2, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (10): `gamification.badge.user.wizard` (Gamification User Badge Wizard); `gamification.goal.wizard` (Gamification Goal Wizard); `gamification.challenge` (Gamification Challenge); `gamification.goal.definition` (Gamification Goal Definition); `gamification.badge.user` (Gamification User Badge); `gamification.karma.rank` (Rank based on karma); `gamification.karma.tracking` (Track Karma Changes); `gamification.badge` (Gamification Badge); `gamification.challenge.line` (Gamification generic goal for challenge); `gamification.goal` (Gamification Goal)
- Objects extended from other modules (3): `mail.thread`, `image.mixin`, `res.users`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `gamification.badge.user.wizard` ← Community: `hr_gamification`; open-license custom/third-party scanned: —
- `gamification.challenge` ← Community: `survey`, `website_forum`, `website_slides`; open-license custom/third-party scanned: —
- `gamification.badge.user` ← Community: `hr_gamification`; open-license custom/third-party scanned: —
- `gamification.karma.tracking` ← Community: `website_forum`, `website_slides`; open-license custom/third-party scanned: —
- `gamification.badge` ← Community: `hr_gamification`, `survey`, `website_profile`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.thread`, `image.mixin`, `res.users`

## 6. Actions / states / validation / automation / security
- State fields found: `gamification.challenge` → ['draft', 'inprogress', 'done']; `gamification.goal` → ['draft', 'inprogress', 'reached', 'failed', 'canceled']
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Gamification: Goal Challenge Check every 1 days; Gamification: Karma tracking consolidation every 1 months
- Security: groups declared 0 (—); record rules 3 (of which company-scoped by text 1); access rows 28

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

