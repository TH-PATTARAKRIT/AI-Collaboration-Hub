# Source Map (candidate) — `hr_livechat`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_livechat` |
| Display name | HR - Livechat |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c27dbaaada4b2504` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_livechat/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr`, `im_livechat`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources / —
- Inventory of user-facing artifacts (counts): menu items 0, views 4, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 13 of 14 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_livechat (HR / Live Chat bridge)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_livechat.json. Pointers are `module/path:LINE`; (TEST) = derived from tests.

## A. Capabilities / functions
- View-only bridge between HR and Live Chat: it adds a "My Team" filter to three live-chat search screens. Depends on hr and im_livechat (hr_livechat/__manifest__.py:7).
- Conditional-on-install: auto_install is true, so it appears automatically when both parents are installed (hr_livechat/__manifest__.py:13). Not an application; no settings.
- Filter 1, Sessions search (the general session list): shows sessions in which a participant is the current user, or is an employee whose direct manager is the current user (hr_livechat/views/discuss_channel_views.xml:9-14).
- Filter 2, "Looking for help" session search: shows sessions where a participant's employee record is in the viewer's department (uses the department-membership indicator) (hr_livechat/views/discuss_channel_views.xml:23-25).
- Filter 3, Agent history search: sessions of the current user or of employees they manage (hr_livechat/views/im_livechat_channel_member_history_views.xml:8-10).
- Filter 4, Live-chat report search: same manager-based rule as filter 3 (hr_livechat/views/im_livechat_report_channel_views.xml:8-10).
- Each filter is inserted right after the parent's existing "My Sessions" filter (parent anchors: im_livechat/views/discuss_channel_views.xml:15, 275; im_livechat/views/im_livechat_channel_member_history_views.xml:57).

## B. Business objects, relationships, lifecycle
- Objects only referenced, none created: chat session (discuss channel), session participant history, live-chat report record, partner, employee (link partner -> employee list: hr/models/res_partner.py:11), and the employee's manager (hr_livechat/views/discuss_channel_views.xml:12).
- "My team" is defined through the reporting line (manager of the employee), except filter 2 which uses department membership. Two different meanings of "team" therefore coexist (manager-based: hr_livechat/views/discuss_channel_views.xml:12, department-based: line 24).
- No state, lifecycle or data of its own (skeleton: no models).

## C. Validations, automation, security, multi-company
- No constraints, automation, ACL, groups or record rules in this module (skeleton: models [], access [], rules []).
- The filters only narrow what the viewer already may see; they do not grant access. Visibility of sessions and reports stays governed by im_livechat's own rules (rule content not read here: UNKNOWN — EVIDENCE INSUFFICIENT).
- Department-membership indicator is a computed/searchable flag defined on the HR side (hr/models/hr_employee_public.py:22; hr/models/hr_version.py:128); its exact semantics (own department vs subordinate departments) were not traced: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Accounting / payroll / analytic handoffs
- None. No accounting, payroll, analytic or inventory link.

## E. Configuration / defaults that change outcomes
- Filter results depend on HR data quality: employee must be linked to the partner/user of the agent, and the manager field on the employee must be set to a person who has a user account.
- No settings, no defaults.

## F. Effective extension path (module names only)
- Extends views owned by im_livechat (three search views). Related consumer of the same domain: spreadsheet_dashboard_im_livechat (separate, does not use these filters).
- Manifest dependents on hr_livechat: none found (grep of manifests).

## G. Not verified
- Record-rule behaviour for non-managers using the filters: UNKNOWN — EVIDENCE INSUFFICIENT.
- Multi-company effect on "employee of partner" lookup: UNKNOWN — EVIDENCE INSUFFICIENT.
- Revision `19.0.post20260921`; nothing here asserted as a universal rule.

