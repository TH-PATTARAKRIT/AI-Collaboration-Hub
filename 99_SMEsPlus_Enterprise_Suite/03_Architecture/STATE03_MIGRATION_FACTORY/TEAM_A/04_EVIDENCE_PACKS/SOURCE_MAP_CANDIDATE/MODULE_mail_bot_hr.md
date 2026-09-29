# Source Map (candidate) — `mail_bot_hr`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mail_bot_hr` |
| Display name | OdooBot - HR |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `011b53f55d136652` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mail_bot_hr/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mail_bot`, `hr`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Discuss / Bridge module between hr and mailbot.
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 12 of 13 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: mail_bot_hr (OdooBot / HR bridge)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/mail_bot_hr.json. Pointers are `module/path:LINE`; (TEST) = derived from tests.

## A. Capabilities / functions
- Presentation-only bridge so the browser-notification prompt (the "notification alert" banner) appears correctly in the employee-facing user Preferences form. Depends on mail_bot and hr (mail_bot_hr/__manifest__.py:9).
- Conditional-on-install: auto_install true (mail_bot_hr/__manifest__.py:11), so it is added automatically when both parents exist. Note mail_bot itself is auto_install and depends only on mail (mail_bot/__manifest__.py:10-11).
- Behaviour (two view edits): the alert banner is removed from HR's simplified Preferences form (mail_bot_hr/views/res_users_views.xml:4-12) and re-inserted above the form body of HR's employee "profile preferences" form (mail_bot_hr/views/res_users_views.xml:14-24). The banner originates in the base Preferences form (base/views/res_users_views.xml:410).
- The manifest description claims it also adds the OdooBot state to the HR-modified user form (mail_bot_hr/__manifest__.py:5); the shipped views contain only the banner relocation. The OdooBot state field itself is placed by mail_bot on the administrator-facing user form and only for technical-mode users and internal users (mail_bot/views/res_users_views.xml:10-13).

## B. Business objects, relationships, lifecycle
- Only the user record's Preferences screens are touched (mail_bot_hr/views/res_users_views.xml:6, 16). No new data, no lifecycle.
- OdooBot onboarding state itself (states, onboarding start) belongs to mail_bot: it initialises for internal users whose state is empty or "not initialized" (mail_bot/models/res_users.py:11, 30) and the field is exposed to users as self-readable (mail_bot/models/res_users.py:26). Detail of state transitions: UNKNOWN — EVIDENCE INSUFFICIENT (not traced beyond these lines).

## C. Validations, automation, security, multi-company
- None of its own: no python, no ACL, no rules (skeleton: models [], access []).
- Security/company scoping unchanged; owned by base/hr/mail_bot.

## D. Accounting / payroll / analytic handoffs
- None.

## E. Configuration / defaults that change outcomes
- No settings. Behaviour changes only through installation state (both parents present) and the view priority given to the simplified-form edit (mail_bot_hr/views/res_users_views.xml:8, priority 15).

## F. Effective extension path (module names only)
- Views extended: hr (two preferences views), base (banner origin), mail_bot (parent bridge). Manifest dependents of mail_bot_hr: none found.

## G. Not verified
- Whether the banner shows in the standard (non-HR) Preferences form after this bridge is installed: UNKNOWN — EVIDENCE INSUFFICIENT (only the HR forms are edited by this module).
- Full OdooBot conversation flow: UNKNOWN — EVIDENCE INSUFFICIENT (owned by mail_bot, out of this module).
- Revision `19.0.post20260921`.

