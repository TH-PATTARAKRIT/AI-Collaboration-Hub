# Source Map (candidate) — `hr_gamification`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_gamification` |
| Display name | HR Gamification |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `8f74841f9949a7b3` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_gamification/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `gamification`, `hr`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources / —
- Inventory of user-facing artifacts (counts): menu items 4, views 6, window actions 3, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (6): `gamification.badge.user.wizard`, `hr.employee.public`, `hr.employee`, `res.users`, `gamification.badge.user`, `gamification.badge`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `gamification.badge.user.wizard`, `hr.employee.public`, `hr.employee`, `res.users`, `gamification.badge.user`, `gamification.badge`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 4 (of which company-scoped by text 0); access rows 5

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 27 of 28 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_gamification (HR Gamification)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton: sourcemap/hr_gamification.json. Pointers `module/path:LINE`; (TEST) = test-derived.

## A. Capabilities / functions
- Connects the generic gamification engine (challenges, goals, badges) to employees: badges can be granted to employees rather than only to system users, received badges show on the employee profile, and HR officers manage challenges and badges (hr_gamification/__manifest__.py:8-12).
- Conditional: auto-installs when gamification and hr are both present; not an application (hr_gamification/__manifest__.py:7,21).
- Adds an HR "Challenges" menu block under HR configuration: Badges (all HR users who can see the HR configuration menu), Challenges and Goals (HR Officers only) (hr_gamification/views/gamification_views.xml:137-141). Challenges and goals lists in HR are restricted to challenges categorised "Human Resources / Engagement" (hr_gamification/views/gamification_views.xml:96,112; category options defined in gamification/models/gamification_challenge.py:140-144).
- "Badges" tab on the employee form (full and public/limited form), with a "Grant a Badge" button; shown only when the employee has a linked user (hr_gamification/views/hr_employee_views.xml:11-25,40-54).
- Badge count of granted employees on the badge and a shortcut to list them (hr_gamification/models/gamification.py:59-83).
- Notification email to the recipient gets a "View Your Badge" button pointing to the employee profile badges tab when the badge is tied to an employee (hr_gamification/models/gamification.py:40-56).

## B. Business objects, relationships, lifecycle
- Badge grant (record of a badge given to a user) gains an optional employee link (hr_gamification/models/gamification.py:10-12). Employee <-> user identity comes from the employee's user link (hr_gamification/wizard/gamification_badge_user_wizard.py:29-32).
- Granting flow: the granter picks an employee (user derived from it), a badge and a comment; the grant is created with the granter as sender and the employee filled, then the badge is sent (hr_gamification/wizard/gamification_badge_user_wizard.py:15-27). No approval step; grant is immediate.
- Employee "all badges" = badges linked directly to the employee plus badges linked only to the employee's user (with no employee), so historical user-only badges still show (hr_gamification/models/hr_employee.py:29-38).
- Employee goals = the linked user's goals from challenges of the HR category (hr_gamification/models/hr_employee.py:21-27); goals only visible to HR officers (hr_gamification/models/hr_employee.py:9-10).
- Public/limited employee record mirrors badge list and flag read-only (hr_gamification/models/hr_employee_public.py:4-14).
- A badge grant can be opened as a read-only-style popup "Received Badge" (hr_gamification/models/gamification.py:27-38).

## C. Validations, automation, security, multi-company
- Consistency check: the employee on a grant must be one of the recipient user's employees (searched across the user's companies) else blocked ("employee does not correspond to the user") (hr_gamification/models/gamification.py:15-20).
- No self-grant: a user cannot send a badge to themselves (hr_gamification/wizard/gamification_badge_user_wizard.py:17-18).
- Access to grants (all employees): every internal user can read/create grants (hr_gamification/security/ir.model.access.csv:6); edit/delete limited to the person who created the grant, HR Officers can edit/delete any grant (hr_gamification/security/gamification_security.xml:14-35); (TEST) creator can edit and delete, other user cannot, HR officer can (hr_gamification/tests/test_gamification_current_badge.py:44-80).
- HR Officers: full rights on challenges, challenge lines, badges, badge grants (hr_gamification/security/ir.model.access.csv:2-5). HR Officers can also see and update any goal (no create/delete) (hr_gamification/security/gamification_security.xml:4-12).
- Privacy implication (business level): badge history (with comments) is visible on employees' public profile tabs to internal users; goals are restricted to HR Officers (hr_gamification/models/hr_employee.py:9-10,17-19 field-level group restrictions).
- Multi-company: only the employee/user match check spans the user's companies (hr_gamification/models/gamification.py:18-19); no company rule defined here (skeleton rules list).

## D. Accounting / payroll / analytic handoffs
- None.

## E. Configuration / defaults that change outcomes
- Challenge "Appears in" (default Human Resources / Engagement) determines whether it appears in the HR menus and on the employee's goals (gamification/models/gamification_challenge.py:140-144; hr_gamification/models/hr_employee.py:26).
- Badge granting permissions (who may grant a given badge: everyone, selected users, having-badge holders) are governed by the gamification module (UNKNOWN — EVIDENCE INSUFFICIENT: not read for this note).

## F. Effective extension path
- Extends: gamification (badge, badge grant, wizard), hr (employee, public employee), res.users. Gamification score/goal computing is owned by gamification.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: challenge scheduling, reward mail cron, badge limits per day/month (gamification module).

