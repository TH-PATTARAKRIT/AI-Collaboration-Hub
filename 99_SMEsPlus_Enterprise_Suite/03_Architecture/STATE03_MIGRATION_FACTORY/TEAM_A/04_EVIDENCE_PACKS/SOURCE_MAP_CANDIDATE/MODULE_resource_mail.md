# Source Map (candidate) — `resource_mail`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `resource_mail` |
| Display name | Resource Mail |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `7d5f4a0e44e1c6f6` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/resource_mail/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `resource`, `mail`
- Direct dependents in 300-module list (1): `hr`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `resource.resource`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `resource.resource`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 17 of 17 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: resource_mail (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities
- Bridge module: lets features built for users in the messaging module (avatars, presence status, avatar cards) work for "resources" (people or material) in the resource module (resource_mail/__manifest__.py:8).
- CONDITIONAL: category Hidden, auto-installs when both resource and mail are present (resource_mail/__manifest__.py:7,9-10).
- Mostly front-end: assets loaded into the back-office (resource_mail/__manifest__.py:11-17). Only one Python file, no views, data, security or groups (skeleton files count: py 3, xml 0; resource_mail/models/resource_resource.py:1-18).

## B. Business objects and lifecycle
- Extends the Resource record only (resource_mail/models/resource_resource.py:9): adds a display colour, defaulting to a random pick from 11 (resource_mail/models/resource_resource.py:11-14) and a read-through "online status" taken from the linked user (resource_mail/models/resource_resource.py:15).
- Provides card data for the avatar popover by returning requested fields of the resource (resource_mail/models/resource_resource.py:17-18).
- No lifecycle/state of its own.

## C. Validations, automation, security
- No constraints, automation, groups, rules or access files in this module (skeleton lists no groups/rules/access; resource_mail/__manifest__.py:9-18 has no data section).
- Presence status is exposed via the linked user and the indicator shows only when the resource has a linked user (resource_mail/static/src/components/avatar_card_resource/avatar_card_resource_popover.xml:8).
- The chat/contact button on the card is hidden unless the resource has a user who is not a portal/share user (resource_mail/static/src/components/avatar_card_resource/avatar_card_resource_popover.xml:17-19).
- Privacy note: online/away/busy/offline presence becomes visible to anyone who can open the card (resource_mail/static/src/components/avatar_card_resource/avatar_card_resource_popover.xml:9-13).

## D. Handoffs
- Resource records and resource types (user vs material): resource module. Avatar and popover base components: mail. Employee-specific popover: hr (hr/static/src/components/avatar_card_employee/avatar_card_employee_popover.js:1).
- Material resources display a wrench symbol instead of a photo, user resources show avatar (resource_mail/static/src/views/fields/many2one_avatar_resource/many2one_avatar_resource_field.xml:7-16).

## E. Configuration
- No settings or parameters. Colour default is random per record, so it differs between records (resource_mail/models/resource_resource.py:12).

## F. Extension path
- hr depends on it (hr/__manifest__.py:17) and extends its popover (hr/static/src/components/avatar_card_resource/avatar_card_resource_popover.xml:3).
- Other modules inheriting the same resource object: hr, hr_holidays, hr_skills (model-inherit scan).

## G. Not verified
- Front-end runtime behaviour beyond template reading: UNKNOWN — EVIDENCE INSUFFICIENT.
- Front-end tests exist for both avatar fields (resource_mail/static/tests/) (TEST) but were not read in detail.

