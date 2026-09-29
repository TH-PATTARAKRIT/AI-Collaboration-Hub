# Source Map (candidate) — `onboarding`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `onboarding` |
| Display name | Onboarding Toolbox |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `3e8369850e20abb5` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/onboarding/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`
- Direct dependents in 300-module list (2): `account`, `payment`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 2, views 4, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (4): `onboarding.onboarding.step` (Onboarding Step); `onboarding.progress` (Onboarding Progress Tracker); `onboarding.progress.step` (Onboarding Progress Step Tracker); `onboarding.onboarding` (Onboarding)
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `onboarding.onboarding.step` ← Community: `account`; open-license custom/third-party scanned: —
- `onboarding.onboarding` ← Community: `account`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 12

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 42 of 42 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — onboarding
Source revision: 19.0.post20260921 | Module: "Onboarding Toolbox" (onboarding/__manifest__.py:5), version 1.2 (:6), category Hidden (:7), LGPL-3 (:34). Infrastructure module (brief note). Basis: static reading of all models, access file, menu/view/template heads, and the consumer in account.

## A. Capabilities and optionality
- A1. Framework for guided "get started" panels: a named onboarding holds an ordered list of steps; each step opens a configured action and turns "done" when completed; progress is tracked and the panel can be hidden. onboarding/__manifest__.py:9-12; onboarding/models/onboarding_onboarding.py:8-37; onboarding/models/onboarding_onboarding_step.py:9-45
- A2. Each onboarding has a unique one-word route name, a completion message (default "Nice work! Your configuration is done."), and an optional close action. onboarding/models/onboarding_onboarding.py:15,18-26,40-43
- A3. Steps carry title, description, button text (default "Let's do it"), done text ("Step Completed!"), done icon (star), image with alt text, and the name of the action to run when opened. onboarding/models/onboarding_onboarding_step.py:17-33
- A4. Progress can be global or per company: a step is per-company by default; an onboarding counts as per-company if any of its steps is, or if any progress row has a company. onboarding/models/onboarding_onboarding_step.py:44; onboarding/models/onboarding_onboarding.py:45-54
- A5. Panel template (container with a "hide these tips" confirmation, then one block per step) is provided; a step-form controller marks the step done after saving from the dialog. onboarding/views/onboarding_templates.xml:3-40; onboarding/static/src/views/form/onboarding_step_form_controller.js:1-20
- A6. Back-office maintenance screens: "Onboardings" and "Onboarding Steps" under Settings > Technical > User Interface (technical menu). onboarding/views/onboarding_menus.xml:4-13; onboarding/views/onboarding_views.xml:98-108. Menu placement under the parent "User Interface": base/views/base_menus.xml:21
- A7. Optionality: not auto_install, not an application; depends on web only; it is pulled in by modules that depend on it (account, payment). onboarding/__manifest__.py:13; direct dependents from manifest scan: account, payment.

## B. Objects and relationships
- B1. onboarding.onboarding <-> onboarding.onboarding.step (many-to-many). onboarding/models/onboarding_onboarding.py:16; onboarding/models/onboarding_onboarding_step.py:15
- B2. onboarding.progress: one row per onboarding and company (or no company for global), with state (not done / just done / done, stored) and a "panel closed" flag; unique per onboarding+company; removed with the onboarding or the company. onboarding/models/onboarding_progress.py:14-28
- B3. onboarding.progress.step: one row per step and company (or global), with state (default not done); unique per step+company; removed with the step or company. onboarding/models/onboarding_progress_step.py:8-21
- B4. Lifecycle: step not_done -> just_done (marked when the user completes it) -> done (on the next panel render, so the celebratory state is shown once). An onboarding is done when every linked step is just_done/done; closed flag is separate and can be toggled. onboarding/models/onboarding_progress_step.py:23-31; onboarding/models/onboarding_progress.py:30-39,46-78
- B5. Progress rows are created lazily for the current company when first needed; adding or removing steps recomputes progress; changing a step's per-company flag deletes its progress rows and refreshes the onboarding. onboarding/models/onboarding_onboarding.py:71-77,92-123; onboarding/models/onboarding_onboarding_step.py:74-92,113-133

## C. Validations, security, audit
- C1. A step linked to an onboarding must name an opening action, otherwise validation error. onboarding/models/onboarding_onboarding_step.py:65-72
- C2. Route name unique; progress unique per company (null company treated as 0). onboarding/models/onboarding_onboarding.py:40-43; onboarding/models/onboarding_progress.py:28; onboarding/models/onboarding_progress_step.py:21 (TEST) onboarding/tests/test_onboarding.py:156-186; concurrency creation test: onboarding/tests/test_onboarding_concurrency.py:44
- C3. Access: all four models — full rights only for Settings administrators (base.group_system); explicit zero-rights rows for internal users and everyone else. No record rules. onboarding/security/ir.model.access.csv:2-13. Consumers therefore use elevated rights when they show progress to ordinary users (e.g., account uses sudo). account/models/company.py:464
- C4. Company scoping is by data (company on progress rows and the current company in context), not by record rules. onboarding/models/onboarding_onboarding.py:56-69
- C5. Removing a company removes its progress (TEST) onboarding/tests/test_onboarding.py:223.
- C6. No audit trail beyond standard create/write dates; no chatter or tracking.

## D. Handoffs
- D1. Owner of concrete onboardings (Accounting dashboard onboarding, invoice onboarding, their steps, actions and close methods): account. account/models/onboarding_onboarding.py:6-29; account/data/onboarding_data.xml:6,69-76; account/models/account_journal_dashboard.py:699-706
- D2. Payment depends on onboarding (manifest); which onboarding objects it defines: UNKNOWN — EVIDENCE INSUFFICIENT (grep found none in payment or payment_* modules). payment/__manifest__.py:8
- D3. Panel rendering hook: consumers override the value-preparation method to auto-complete steps from business facts (invoice existence for company). account/models/onboarding_onboarding.py:14-24
- D4. Web client (action service, RPC, dialogs): web.

## E. Configuration/defaults that change outcomes
- E1. Per-company flag on each step (default true) decides whether each company must complete steps separately. onboarding/models/onboarding_onboarding_step.py:44
- E2. Panel close action name, step opening action name, and completion text are data, editable in the technical menu. onboarding/models/onboarding_onboarding.py:18-26; onboarding/models/onboarding_onboarding_step.py:30-33
- E3. Styling variables and dark-mode variant are shipped as assets. onboarding/__manifest__.py:21-32

## F. Effective extension path (module names only)
- Modules extending onboarding models: account (grep of inheritance and record declarations). Manifest dependents: account, payment.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: what payment uses from onboarding (see D2).
- UNKNOWN — EVIDENCE INSUFFICIENT: the panel-rendering controller/route (onboarding has no HTTP controller in this module; rendering entry point sits in the account component). account/static/src/components/onboarding/onboarding.js (file presence only).
- UNKNOWN — EVIDENCE INSUFFICIENT: how many onboarding/step records exist in other modules' data beyond account.

