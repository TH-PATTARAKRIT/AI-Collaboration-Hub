# Source Map (candidate) — `website_slides`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_slides` |
| Display name | eLearning |
| Manifest version | 2.7 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `f9f6740eaeb2eeee` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_slides/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `portal_rating`, `website`, `website_mail`, `website_profile`
- Direct dependents in 300-module list (3): `hr_skills_slides`, `website_slides_forum`, `website_slides_survey`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `mass_mailing_slides`, `test_discuss_full`, `test_website_modules`, `website_sale_slides`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/eLearning / Manage and publish an eLearning platform
- Inventory of user-facing artifacts (counts): menu items 15, views 50, window actions 16, server actions 0, reports 0, mail templates 6, scheduled jobs 0, wizards 3, web routes 39
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (12): `slide.channel.invite` (Channel Invitation Wizard); `slide.embed` (Embedded Slides View Counter); `slide.slide` (Slides); `slide.channel` (Course); `slide.question` (Content Quiz Question); `slide.answer` (Slide Question's Answer); `slide.tag` (Slide Tag); `slide.channel.partner` (Channel / Partners (Members)); `slide.slide.partner` (Slide / Partner decorated m2m); `slide.slide.resource` (Additional resource for a particular slide); `slide.channel.tag.group` (Channel/Course Groups); `slide.channel.tag` (Channel/Course Tag)
- Objects extended from other modules (20): `mail.composer.mixin`, `base.partner.merge.automatic.wizard`, `gamification.challenge`, `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.published.mixin`, `website.searchable.mixin`, `rating.mixin`, `mail.activity.mixin`, `website.cover_properties.mixin`, `website.published.multi.mixin`, `res.groups`, `gamification.karma.tracking`, `mail.activity`, `res.users`, `res.config.settings`, `website`, `mail.message`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `slide.slide` ← Community: `website_slides_survey`; open-license custom/third-party scanned: —
- `slide.channel` ← Community: `hr_skills_slides`, `mass_mailing_slides`, `website_sale_slides`, `website_slides_forum`, `website_slides_survey`; open-license custom/third-party scanned: —
- `slide.channel.partner` ← Community: `hr_skills_slides`, `website_slides_survey`; open-license custom/third-party scanned: —
- `slide.slide.partner` ← Community: `website_slides_survey`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.composer.mixin`, `base.partner.merge.automatic.wizard`, `gamification.challenge`, `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.published.mixin`, `website.searchable.mixin`, `rating.mixin`, `mail.activity.mixin`, `website.cover_properties.mixin`, `website.published.multi.mixin`, `res.groups`, `gamification.karma.tracking`, `mail.activity`, `res.users`, `res.config.settings`, `website`, `mail.message`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 9 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 5 (`group_website_slides_officer`, `group_website_slides_manager`, `website_slides.group_website_slides_officer`, `website_slides.group_website_slides_manager`, `base.default_user_group`); record rules 21 (of which company-scoped by text 0); access rows 41

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

