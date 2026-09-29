# Source Map (candidate) — `base_automation`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `base_automation` |
| Display name | Automation Rules |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `85ba14f6e6be4e25` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/base_automation/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `digest`, `resource`, `mail`, `sms`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_base_automation`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / —
- Inventory of user-facing artifacts (counts): menu items 1, views 5, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 1, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `base.automation` (Automation Rule)
- Objects extended from other modules (4): `mail.thread`, `mail.activity.mixin`, `ir.actions.server`, `ir.cron`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `mail.thread`, `mail.activity.mixin`, `ir.actions.server`, `ir.cron`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 4 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Automation Rules: check and execute every 4 hours
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 64 of 65 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: base_automation (Automation Rules)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/base_automation.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests; tests of this module are in base_automation/tests and in the separate test module test_base_automation/tests.

## A. Capabilities / functions
- Core: lets an administrator define a rule on any non-abstract business model that runs one or more server actions when something happens to a record (base_automation/__manifest__.py:6-15; base_automation/models/base_automation.py:148-150).
- Trigger families (base_automation/models/base_automation.py:173-197): field-value shortcuts (stage set, user set, tag added, state set, priority set), archive / unarchive, create, update, create-and-edit, deletion, live UI change, three time-based variants (date field, after creation, after last update), incoming / outgoing message, and external webhook. "On update" is labelled deprecated in favour of "create and edit" (base_automation/models/base_automation.py:184).
- Action types available to a rule are the platform server-action types: update record, create record, duplicate record, execute code, send webhook notification, multi (base/models/ir_actions.py:612-618); mail, SMS, follower and activity types are contributed by the mail and sms modules (base_automation/__manifest__.py:15; base_automation/models/base_automation.py:319-321).
- Conditional: time-based rules are only driven by a scheduled job that ships switched off and is switched on automatically once any active time-based rule exists (base_automation/data/base_automation_data.xml:4-12; base_automation/models/base_automation.py:664-688).
- Conditional: webhook rules expose a public URL built from a random identifier; identifier can be rotated; call logging is optional (base_automation/models/base_automation.py:160-164, 288-294, 561-563, 565-573; base_automation/controllers/main.py:6-18).
- Optional: working-calendar aware day delays (base_automation/models/base_automation.py:237-242, 1131-1161). Depends on resource (base_automation/__manifest__.py:15).
- Back-office: Automation menu entry under the platform "Automation" menu (base_automation/views/base_automation_views.xml:265-266); digest tip for system admins (base_automation/data/digest_data.xml:4-8).

## B. Business objects, relationships, lifecycle
- Automation Rule (base.automation) -> target model (required) and -> its Actions (server actions with usage "automation rule"); rule is a chatter-enabled record with tracked name/model/trigger/date fields (base_automation/models/base_automation.py:141-160; base_automation/models/ir_actions_server.py:14-17).
- Rule may carry: "before update" condition, "apply on" condition (post condition), watched fields, trigger date field with delay/unit/mode, calendar, webhook record-finder, last-run stamp, active flag (base_automation/models/base_automation.py:216-269).
- Lifecycle of a rule: created/edited -> patches to the target model are reinstalled and other workers notified; only edits touching model, active, trigger or on-change fields do this; delay edits only refresh the schedule (base_automation/models/base_automation.py:272-273, 507-538, 690-696). Inactive rules never run (base_automation/models/base_automation.py:165, 704-708).
- Lifecycle of execution on a record: (1) rule picked by model and trigger; (2) before-condition evaluated on existing records before an edit (not on create); (3) change applied; (4) after-condition evaluated on changed records; (5) records whose watched fields actually changed are passed to actions (base_automation/models/base_automation.py:864-916, 745-771, 832-849).
- Field-value shortcuts are translated into an automatic condition: state/priority equals chosen value; stage equals chosen stage; tag added is a "not previously present / now present" pair; user set = not empty; archive/unarchive = active false/true (base_automation/models/base_automation.py:395-432). Those shortcuts locate their field by conventional names (stage, tag, priority, state, user, active, and "x_studio_" variants); if the model lacks them the field stays empty (base_automation/models/base_automation.py:575-603).
- A rule fires once per record per chain: a per-transaction ledger records which rules already ran on which records, which stops infinite loops but still allows rule A -> rule B chaining (base_automation/models/base_automation.py:783-810); (TEST) chain of state changes across four rules ends after each has run once (test_base_automation/tests/test_flow.py:442-516).
- Also fires on stored computed-field recalculation, not only direct edits (base_automation/models/base_automation.py:918-957); (TEST) recompute cases (test_base_automation/tests/test_flow.py:260-441).
- Message triggers: not fired for internal notes, internal subtypes, notifications, automatic comments, or messages posted while a rule is already running; author without a partner or an external (portal/share) partner counts as "received", otherwise "sent" (base_automation/models/base_automation.py:1013-1038); (TEST) (test_base_automation/tests/test_flow.py:1541-1595).
- Time-based execution: scheduled job finds records whose date field falls between last run and now (shifted by the delay, before or after); a failure rolls back that rule, is logged, and the last failure is re-raised at the end so the job shows as failed (base_automation/models/base_automation.py:1104-1220).
- Rule copy also copies its actions (base_automation/models/base_automation.py:540-546); (TEST) (test_base_automation/tests/test_flow.py:1089).

## C. Validations, automation, security, multi-company
- Mail triggers only on models with discussion (chatter) (base_automation/models/base_automation.py:167-171); (TEST) (test_base_automation/tests/test_flow.py:1541-1544).
- Every action must target the same model as the rule; changing the rule model drops non-matching actions (base_automation/models/base_automation.py:275-286, 328-337; base_automation/models/ir_actions_server.py:26-38, 45-52).
- Delay cannot be negative for time triggers (base_automation/models/base_automation.py:300-304). Actions carrying configuration warnings block saving the rule (base_automation/models/base_automation.py:306-313); (TEST) (test_base_automation/tests/test_flow.py:1139).
- Live-UI-change rules accept only "execute code" actions; deletion rules reject email/follower/activity actions (base_automation/models/base_automation.py:314-326).
- Rule actions cannot be reused as children of a multi action (base_automation/models/ir_actions_server.py:40-43).
- Access: only the system administration group has any access to rules (base_automation/security/ir.model.access.csv:2). No record rules and no company field exist on the rule; rules are found with elevated rights, so a rule applies to records of all companies on that model: multi-company scoping is therefore not enforced by this module (base_automation/models/base_automation.py:707; absence of a security rules file).
- Execution runs with elevated rights: rule actions are run as superuser, so a restricted user's create/edit can trigger changes that user could not make directly (base_automation/models/base_automation.py:824-827); (TEST) restricted user creating/editing a record still gets the archive action applied (base_automation/tests/test_automation.py:48-86).
- Rule conditions are evaluated with elevated rights but results are brought back into the caller's environment; a condition on a related model the user cannot read does not fail (base_automation/models/base_automation.py:745-771); (TEST) (test_base_automation/tests/test_flow.py:550-601).
- Webhook endpoint is public, needs only the secret identifier, accepts GET or POST, has no CSRF check, and replies 404 for unknown identifier, 500 on any failure, 200 otherwise (base_automation/controllers/main.py:6-18); (TEST) (test_base_automation/tests/test_flow.py:1857-1881). Record-finder expression and the incoming payload are evaluated in a restricted expression context (base_automation/models/base_automation.py:634-652, 710-726).
- Failure inside an action is re-raised (not swallowed), so the triggering user action fails and is rolled back, with the rule name added to the error for internal users (base_automation/models/base_automation.py:773-781, 826-830).
- Live-update rules run their code actions with elevated rights and apply only the returned values, domains and warnings to the open form (base_automation/models/base_automation.py:983-1009); (TEST) works for a restricted user (base_automation/tests/test_automation.py:88-112); more cases (test_base_automation/tests/test_flow.py:857-946).

## D. Handoffs
- Server-action engine, action types, execution rights: owned by base (base/models/ir_actions.py:1151-1242).
- Message posting, followers, activities, email templates: mail; SMS action: sms; working calendars for day delays: resource; admin tips: digest (base_automation/__manifest__.py:15).
- Outbound webhook action posts after commit (TEST) (test_base_automation/tests/test_flow.py:1905-1931). Inbound webhook writes to whatever model the rule targets; no accounting, sale or portal logic lives here.
- Reverse dependency in Community: only the test module test_base_automation depends on it; other modules using it: UNKNOWN — EVIDENCE INSUFFICIENT beyond the manifest search of the addons folder.

## E. Configuration/defaults that change outcomes
- Scheduled job defaults: every 4 hours, inactive; interval tightens to about 10% of the smallest time delay, minimum 1 minute, maximum 4 hours, and only ever shortens (base_automation/data/base_automation_data.xml:9-11; base_automation/models/base_automation.py:680-688, 728-743); (TEST) (base_automation/tests/test_automation.py:175-253).
- Empty watched-field list means every field change qualifies; create counts as all fields changed (base_automation/models/base_automation.py:832-849).
- Month delay is a fixed 30-day block in scheduling maths (base_automation/models/base_automation.py:85, 94).
- Webhook default record-finder reads model name and id from the payload; call logging is off by default (base_automation/models/base_automation.py:162-164).
- Debug-mode-only form fields: webhook rotate/log controls, before-update domain, raw domain editing (base_automation/views/base_automation_views.xml:12, 73, 91, 104).

## F. Effective extension path
- base (server actions), mail, sms, resource, digest; test_base_automation (test harness); any business model module can be targeted by rules without code changes.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: contents of mail/sms server-action types and the outbound webhook action (only their existence and type names were confirmed).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end form behaviour (static/src) and view layout beyond items cited.
- UNKNOWN — EVIDENCE INSUFFICIENT: effect on very large batch writes or performance (a performance test suite was not traced).
- Revision `19.0.post20260921`; findings apply to this revision only and are not universal rules.

