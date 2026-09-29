# Source Map (candidate) — `website_forum`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_forum` |
| Display name | Forum |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `b318318a84e7725b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_forum/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `auth_signup`, `website_mail`, `website_profile`
- Direct dependents in 300-module list (1): `website_slides_forum`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Manage a forum with FAQ and Q&A
- Inventory of user-facing artifacts (counts): menu items 7, views 14, window actions 7, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 40
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (5): `forum.post.reason` (Post Closing Reason); `forum.post.vote` (Post Vote); `forum.forum` (Forum); `forum.post` (Forum Post); `forum.tag` (Forum Tag)
- Objects extended from other modules (10): `gamification.challenge`, `ir.attachment`, `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.multi.mixin`, `website.searchable.mixin`, `gamification.karma.tracking`, `res.users`, `website`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `forum.forum` ← Community: `website_slides_forum`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `gamification.challenge`, `ir.attachment`, `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.multi.mixin`, `website.searchable.mixin`, `gamification.karma.tracking`, `res.users`, `website`

## 6. Actions / states / validation / automation / security
- State fields found: `forum.post` → ['active', 'pending', 'close', 'offensive', 'flagged']
- Validation: 1 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 12 (of which company-scoped by text 0); access rows 15

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

