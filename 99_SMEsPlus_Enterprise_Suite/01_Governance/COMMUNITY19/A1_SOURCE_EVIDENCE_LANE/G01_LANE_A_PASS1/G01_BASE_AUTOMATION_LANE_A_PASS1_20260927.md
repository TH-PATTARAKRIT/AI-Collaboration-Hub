# G01 PLATFORM_BASE — Lane A Pass-1 — `base_automation`

| Item | Value |
|---|---|
| Lane | SMEsPlus LANE A (blind source/static evidence) |
| Slot | T4 |
| Group | G01 PLATFORM_BASE |
| Module | `base_automation` (governed roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, path `addons/base_automation/` |
| Retrieval | raw.githubusercontent.com at anchor commit; blob SHA-1 via `git hash-object` on local copies |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (JS/static assets and tests intentionally out of scope; see Limitations) |

Clean-room note: findings are neutral WHAT / WHY / RISK abstractions. Identifiers are pointers only. Nothing here is a copy recommendation. Source presence does not prove runtime reachability. No GMVQ QIDs are answered.

## 1. Evidence Pointer Table

| # | Path (under addons/base_automation/) | git blob SHA-1 | Purpose |
|---|---|---|---|
| E1 | `__manifest__.py` | dc87400390755ec3b07ef6b55073451e6caa7b52 | Identity, dependencies, data load list, asset bundles, licence |
| E2 | `__init__.py` | 8c67f893b379e4144382f9199e8b147f81672112 | Loads models and controllers packages |
| E3 | `models/__init__.py` | d4a003005823d2568a6d4d63c742b57a8e4174da | Loads the rule model and the server-action extension |
| E4 | `models/base_automation.py` | 099ba2e3b5352a03fce94aec9f7bdc7219247144 | Rule model: triggers, filters, recursion guard, method patching, time-based processing, webhook execution |
| E5 | `models/ir_actions_server.py` | 69efd9a00029cc7b55fb8486790d60ba1b29ed37 | Extends server actions (usage, link to rule, eval context) and scheduled-job navigation |
| E6 | `controllers/__init__.py` | 12a7e529b674164f0ad189b131c5d5c8fb9ae0bc | Loads controller |
| E7 | `controllers/main.py` | e2eae519dd6ad74866240e10a242b37d323581b0 | Public webhook HTTP endpoint |
| E8 | `security/ir.model.access.csv` | 77253ff3e968d1325b73f05fcf65f09ef073df34 | Single ACL row for the rule model |
| E9 | `data/base_automation_data.xml` | a680e343b6339e7b18a1c44582e9aaf23afad54f | Scheduled job definition for time-based rules |
| E10 | `data/digest_data.xml` | 7330f4b3e4e1c841a4ff9366944dc51e1c9ff873 | Digest tip record (admin-group audience) |
| E11 | `views/base_automation_views.xml` | 32290c98655266f42ff8f332b9ade8a3b584f8ec | Form/list/kanban/search views, window action, menu |
| E12 | `views/ir_actions_server_views.xml` | 7afe06b4e22d7ddd466ec73f295759f2d26e21ce | Inherited server-action form: navigation back to owning rule |

Blob count: 12.

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
1. Purpose: user-configurable "automation rules" that fire server actions on arbitrary business models on record events, time conditions, messages, UI changes or inbound webhooks (E1 description).
2. Declared dependencies: `base`, `digest`, `resource`, `mail`, `sms` (E1). Licence LGPL-3; category Sales/Sales (E1).
3. `sms` is out-of-roster for G01 → **cross-group edge candidate**. No Python/XML reference to `sms` was found in the cited files (E4, E5, E11); the dependency is manifest-only in readable evidence (see Gaps G2).
4. Data load order: ACL → cron data → digest tip → views (E1). Backend and unit-test asset bundles declared but not inspected (E1).

### 2.2 Data (models, inheritance, key fields, constraints)
5. New model `base.automation` inheriting mail thread + activity mixins, so rules themselves are chattered/tracked (E4 class header). Name, model, trigger and date settings carry tracking.
6. Key field groups (E4): target model (required, cascade on model removal, non-abstract only); `trigger` (selection, required); trigger-helper fields (selection value, reference record, date field, delay amount/unit/mode, optional working calendar); `filter_pre_domain` (before-update condition) and `filter_domain` (apply-on condition) stored as text expressions; `trigger_field_ids` (watched fields; empty = all); `on_change_field_ids`; `action_server_ids` (one-to-many to server actions); webhook fields (`webhook_uuid` random per rule, non-copied; computed `url`; `record_getter` expression; `log_webhook_calls`); `last_run`; `active`.
7. Server action extension: adds usage value `base_automation` and back-link `base_automation_id` (cascade delete) (E5). Children-domain rule prevents multi-actions from linking rule-owned actions (E5 `_get_children_domain`). Available target models restricted to the rule's model (E5).
8. Constraints (E4): mail triggers only on mail-thread models (`_check_trigger`); every action's model must equal the rule model (`_check_action_server_model`); time delay must be non-negative (`_check_time_trigger`); no child action may carry warnings, "on UI change" requires code-type actions only, "on deletion" forbids mail/follower/activity actions (`_check_trigger_state`). E5 also emits a warning when action model ≠ rule model.
9. Copying a rule duplicates its actions (E4 `copy`).

### 2.3 Business rules / states / lifecycle / exceptions
10. Trigger taxonomy (E4 `trigger` selection): field-value-set family (stage, user, tag, state, priority), archive/unarchive, create, create-or-edit, update (marked deprecated in favour of create-or-edit), deletion, UI change (onchange), three time-based (date field, after creation, after last update), incoming/outgoing message, webhook.
11. Convenience triggers resolve a conventional field by name pattern, including customization-prefixed variants (E4 `_get_trigger_specific_field`); if none found, helper fields stay empty. RISK: behaviour depends on target model's field naming.
12. Mechanism: activating rules dynamically patches create/write/computed-field-recompute/unlink/message-post on target model classes and registers onchange hooks; rule create/write(critical fields)/unlink re-registers and invalidates the registry and template cache (E4 `_register_hook`, `_update_registry`, `create`/`write`/`unlink`). Missing target model → warning log, skip (E4).
13. Pre/post filtering: before-update condition evaluated before write; apply-on condition evaluated after create/write/recompute; only records passing both proceed (E4 `_filter_pre`, `_filter_post_export_domain`, `make_write`). On create/unlink only post-condition applies. Watched-field check compares old vs new values (E4 `_check_trigger_fields`).
14. Observation: the message-post path applies the **pre** condition (not the post condition) to decide eligible records (E4 `make_message_post`). Flag for A1 as semantic point; not a contradiction claim.
15. Message trigger classification: skipped for internal messages/subtypes and notification-type messages; "received" when author absent or a share (external) partner, else "sent" (E4 `make_message_post`).
16. Recursion guard: context map of rule → already-processed records; records are marked before action execution so re-entrant writes do not re-fire the same rule on the same record; a feedback flag lets filter-time recomputations register progress in place (E4 `_process`, `_get_actions`). Message path suppressed while any rule is in progress (E4).
17. Execution: each server action of the rule is run per record with active model/id context plus the post-domain (E4 `_process`). Optional stamp of a `date_automation_last` field if the target model has one (E4).
18. Exceptions: action errors re-raised after attaching rule id/name "postmortem" context for internal users (E4 `_add_postmortem`). Onchange rule errors likewise re-raised.
19. Time-based lifecycle: record selection window between rule `last_run` and now, shifted by signed delay; date vs datetime handled differently; optional working-calendar day planning with leaves; after-last-update fallback to creation date where applicable (E4 `_search_time_based_automation_records`). Per-rule commit progress; failed rule rolled back, others continue; last error re-raised to mark job failed (E4 `_cron_process_time_based_actions`).
20. Legacy entry point `_check` marked deprecated since 19.0 and restricted to automatic mode (E4).

### 2.4 Security
21. ACL: full CRUD on `base.automation` only for `base.group_system` (E8). No record rules shipped. Menu under `base.menu_automation` (E11) — its own group gating is outside this module (Gap G3).
22. Elevated context: rule lookup is performed with sudo (E4 `_get_actions`), action lists are iterated under sudo (E4 `_process`, onchange path), filter domains read under sudo and filtered with sudo'd records (E4 `_filter_pre`/`_filter_post_export_domain`). Whether the server action itself then runs as the triggering user or elevated is determined by `ir.actions.server.run` in `base` — not provable here (Gap G4).
23. Code-execution surface: filter domains and webhook `record_getter` are evaluated through a restricted evaluator with an eval context exposing model, user, uid and date helpers (+ payload for webhooks) (E4 `_get_eval_context`). Server-action code eval context is extended with a JSON helper and, when an HTTP request carries data, the request payload (E5 `_get_eval_context`). RISK: admin-authored expressions/code execute on arbitrary models; injection surface is the webhook payload.
24. Domain-field extraction deliberately uses a regex instead of evaluation because it can be reached from crafted onchange calls (E4 `_get_domain_fields` comment). WHY: hardening against malicious onchange input.
25. Webhook exposure: public, unauthenticated, CSRF-exempt, session-less route accepting GET and POST; rule resolved by UUID under sudo; UUID acts as bearer secret; rotation action provided; responses reduced to generic status JSON with 404/500/200 (E7, E4 `action_rotate_webhook_uuid`). RISK: secret-in-URL model; execution context of the webhook is the public-route environment elevated via sudo on the rule (Gap G4 for final identity).
26. Webhook logging to `ir.logging` via sudo when enabled, including payload and tracebacks (E4 `_execute_webhook`). RISK: sensitive payload retention.
27. Advanced UI elements (pre-domain editor, webhook log button, UUID rotation, log toggle, scheduled-job link) restricted to developer-mode group `base.group_no_one` in views (E11) — UI gating, not an access boundary.

### 2.5 UI surfaces (names only)
28. Route: `/web/hook/<rule_uuid>` (E7).
29. Views: `view_base_automation_form`, `_tree`, `_kanban`, `_search`; window action `base_automation_act`; menu `menu_base_automation_form` (E11). Inherited server-action form adds "open automation" navigation (E12, E5 `action_open_automation`, also on `ir.cron`).
30. Rule buttons: open scheduled action, rotate webhook UUID, view webhook logs (E4/E11).

### 2.6 Jobs / config
31. One scheduled job `ir_cron_data_base_automation_check` (noupdate, shipped inactive, 4-hour default) calling the time-based processor (E9).
32. Job auto-managed: activated when any active time-based rule exists; interval tightened to about one-tenth of the shortest delay, bounded 1 minute – 4 hours, only ever shortened automatically (E4 `_update_cron`, `_get_cron_interval`). Uses row lock on the job record.
33. Digest tip record targeted at `base.group_system` (E10).

## 3. Cross-module Edges
| Edge | Direction | Evidence | Note |
|---|---|---|---|
| `base` (ir.model, ir.model.fields, ir.actions.server, ir.cron, ir.logging, groups, menu root) | depends | E1, E4, E5, E8, E11 | Core execution substrate |
| `mail` (thread/activity mixins, message post hook, mail action types) | depends | E1, E4 | Mail triggers and rule chatter |
| `resource` (working calendar day planning) | depends | E1, E4 | Time-based day delays |
| `digest` (tip record) | depends | E1, E10 | Informational only |
| `sms` | depends | E1 only | **Out-of-roster cross-group edge candidate**; no in-module usage found |
| Any business model (dynamic patching) | outbound, runtime | E4 | Rules can attach to any non-abstract model; implicit edge to every group |
| External third parties via webhook | inbound | E7 | Unauthenticated HTTP entry |
| Customization-prefixed field names (`x_studio_*`) | soft | E4 | Implies accommodation of an external customization tool; not a declared dependency |

## 4. Evidence Gaps / Contradictions
- G1: `static/src/**` and `static/tests/**` (JS widgets, e.g. actions one-to-many widget referenced in E11) not inspected by instruction.
- G2: Reason for `sms` dependency not evidenced in cited files; may be relied on by SMS action types defined elsewhere or by JS. Unresolved.
- G3: Group gating of parent menu `base.menu_automation` lies in `base`; not read.
- G4: Effective user identity of `ir.actions.server.run` under the sudo'd action list (and in webhook/public context) is defined in `base`; not read. Security conclusion on privilege escalation is therefore open.
- G5: Test directory (`tests/`) not discovered via manifest/imports; not read.
- G6: No `i18n`, `migrations`, or report files discovered via manifest; absence not proven.
- Contradiction candidates: none confirmed. Point 14 (message path uses pre-condition) flagged for A1 review only.

## 5. Limitations
- Static reading only; no runtime proof; no Formal Coverage claim; no percentages.
- File discovery limited to manifest data list and Python import chain (api.github.com unavailable); files outside that chain may exist.
- Large model file (E4) read in targeted sections plus full structural scan; minor helper code may be summarised rather than itemised.
- GMVQ QIDs not answered; handoff is evidence-only to RED TEAM A1.
