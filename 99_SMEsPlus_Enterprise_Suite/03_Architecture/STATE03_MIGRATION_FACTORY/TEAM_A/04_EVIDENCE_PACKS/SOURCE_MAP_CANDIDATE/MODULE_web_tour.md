# Source Map (candidate) — `web_tour`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `web_tour` |
| Display name | Tours |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `935bdfdc6bb3d8b3` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/web_tour/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`
- Direct dependents in 300-module list (6): `crm`, `hr_expense`, `hr_recruitment`, `mail`, `project`, `survey`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `mass_mailing`, `test_http`, `test_main_flows`, `test_orm`
- Custom / third-party modules that declare a dependency (name — license only) (1): `web_responsive` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 1, views 3, window actions 1, server actions 1, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `web_tour.tour` (Tours); `web_tour.tour.step` (Tour's step)
- Objects extended from other modules (2): `ir.http`, `res.users`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.http`, `res.users`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 29 of 29 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: web_tour
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Guided on-screen tours (onboarding walkthroughs): stored tours with steps, an interactive/"onboarding" player, an automatic runner used for testing, and a recorder to author custom tours (web_tour/__manifest__.py:8,41-68).
- Conditional: depends on web only, installs automatically, category Hidden (web_tour/__manifest__.py:6,13,70). Assets are loaded in both backend and public-site bundles (web_tour/__manifest__.py:19-40).
- Onboarding tours run automatically only for internal users who have tours switched on; per-user switch is stored on the user (web_tour/models/tour.py:38-42; web_tour/models/res_users.py:7).
- Custom tours can be exported as a program file (attachment download) for reuse by developers (web_tour/models/tour.py:61-80; web_tour/views/tour_views.xml:78-87). A tour can be shared through an address that carries the tour name (web_tour/models/tour.py:14,25-28).

## B. Business objects, relationships, lifecycle
- Tour: unique name, starting address (default backend home), congratulation message (translatable, default "Good job!" text), display order, custom flag, list of users who consumed it, ordered steps (web_tour/models/tour.py:6-23).
- Step: trigger (required), text, tooltip position (bottom default), action to run, sequence; deleted with its tour (web_tour/models/tour.py:83-98).
- User attribute "Onboarding" (tour enabled): computed once from creation as on only if the user is an administrator, no installed module has demo data, and not running under tests; user may change it (web_tour/models/res_users.py:7-13).
- Lifecycle: on session start the web client is told whether tours are enabled and the next unconsumed non-custom tour (lowest order) is delivered as data (web_tour/models/ir_http.py:7-11; web_tour/models/tour.py:38-42). Finishing a tour links the user to it as consumed (web_tour/models/tour.py:30-36). Switching the flag off stops further tours for that user (web_tour/models/res_users.py:15-18). (TEST) current-tour selection respects the flag and order (web_tour/tests/test_tours.py:67-79).

## C. Validations, automation, security, credentials
- Unique tour name enforced (web_tour/models/tour.py:20-23).
- Access: system administrators full rights on tours and steps; all internal users read-only (web_tour/security/ir.model.access.csv:2-5). The "consume" action writes with elevated rights so ordinary users can mark their own completion (web_tour/models/tour.py:32-35); it applies only to internal users.
- Tour switch update is performed with elevated rights on the caller's own record only (web_tour/models/res_users.py:15-18).
- Data-exposure note: tour definitions (triggers, actions) are delivered to the browser; step "run" values are strings executed by the client tour engine; authoring is restricted to administrators by the access list (web_tour/models/tour.py:97; web_tour/security/ir.model.access.csv:2,4).
- Menu "Tours" under the technical menu (web_tour/views/tour_views.xml:75); no extra group restriction shown on the menu itself.
- No company scoping; no external services or credentials.

## D. Handoffs to other modules
- Other apps register their own onboarding tours through the client-side registry and rely on this player; concrete registrants: UNKNOWN — EVIDENCE INSUFFICIENT in scope.
- Session information and user model: web/base (web_tour/models/ir_http.py:7-11).
- Automatic-tour runner used by test suites across modules (web_tour/__manifest__.py:47-50) (TEST infrastructure).

## E. Configuration/defaults that change outcomes
- Default onboarding state depends on demo data: any installed demo data turns tours off for newly created users (web_tour/models/res_users.py:11-13).
- Rainbow-man (celebration) message default and per-tour override (web_tour/models/tour.py:15).
- Tour order by sequence then name (web_tour/models/tour.py:9,16).

## F. Effective extension path
- Modules ship tours as client-side registrations or as data records of the tour model with steps; users create custom tours through the recorder and export them (web_tour/models/tour.py:61-80).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side tour engine behavior (JS not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether custom tours are visible/applicable to all users or only the creator.

