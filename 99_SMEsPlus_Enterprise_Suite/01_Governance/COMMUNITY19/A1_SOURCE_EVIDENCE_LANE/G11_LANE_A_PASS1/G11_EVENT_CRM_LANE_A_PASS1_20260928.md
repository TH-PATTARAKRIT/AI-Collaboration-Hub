> **CANDIDATE-ROSTER PILOT — G11 membership is DERIVED, not Boss-confirmed; not Formal Coverage; not a precedent for opening any other G02–G16 group.** See MASTER_DECISION_LOG_G01_20260927.md MD-17/MD-18.

# G11 EVENTS (pilot) — Module `event_crm` — LANE A PASS-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Group | G11 EVENTS (CANDIDATE-ROSTER PILOT; DERIVED membership, not CONFIRMED) |
| Module | `event_crm` |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/event_crm/`) |
| Retrieval | raw.githubusercontent.com at pinned commit; blob SHA-1 verified with `git hash-object` against `git ls-tree` of the same pinned commit |
| Date | 2026-09-28 |
| Scope | PASS-1 breadth: manifest, models, security CSV/XML, action/cron data. Views, merge-template body detail, demo data, JS test tour, i18n, tests NOT studied. |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |

Clean-room note: neutral WHAT/WHY/RISK abstractions only; no verbatim vendor code reproduced beyond short field/method-name pointers. No runtime proof, no Formal Coverage, no percentages, no GMVQ QID answered. `depends` in section 3 is a dependency relationship only, not a group-membership claim (MD-07/08).

## 1. Evidence Pointer Table (14 blobs)

| Path (addons/event_crm/…) | git blob SHA-1 (fetched, hash-verified) | Purpose |
|---|---|---|
| `__manifest__.py` | 2a617b66cf921e9cabe518bd18a3f38a362d3317 | Name "Event CRM", depends `event`+`crm`, `auto_install: True` |
| `__init__.py` | dc5e6b693d19dcacd224b7ab27b26f75e66cb7b2 | Package init |
| `data/crm_lead_merge_template.xml` | ff8c515a5ca14d4fb88f5db9c32e1b22fecaaf10 | Lead-merge related data (not deeply read) |
| `data/ir_action_data.xml` | 52e56107dfe20ed8e179726fce0a61805616819d | Server action "Generate Leads" bound to `event.event`, restricted to Event Managers |
| `data/ir_cron_data.xml` | b2c5cffc81495a81758e90fb6b40b3016c76522d | Daily cron driving batched lead generation |
| `models/__init__.py` | 0def19f2cc5ed0755624a1a6374c4c29f78f6751 | Model import roster |
| `models/crm_lead.py` | f4be80d00733e73ac6139d072755ee3b806c967e | `crm.lead` extension: rule/event/registration links |
| `models/event_event.py` | f57b2bb4e1219221e22c4dd8eb4e13b3d253eff7 | `event.event` extension: lead roll-up, `action_generate_leads` |
| `models/event_lead_request.py` | 018d22a092f92415639fa550f01c64a46c9da73b | `event.lead.request`: batching/progress model for the cron |
| `models/event_lead_rule.py` | 06abf2ddf00f894bee77a97e9231c45a31469fc0 | `event.lead.rule`: the rule engine (filters, triggers, per-attendee/per-order) |
| `models/event_question_answer.py` | 312a566e3fba6ceff671929b25d1d0c4f5843e5b | `event.question.answer` extension: "create rule from this answer" shortcut |
| `models/event_registration.py` | 178f726a5ab5b920ad9531f2a134c414f97cfa55 | `event.registration` extension: rule trigger hooks (create/write), lead sync |
| `security/event_crm_security.xml` | 5435f32ff51d70a3fee85713551f0265259f08dd | Multi-company `ir.rule` on `event.lead.rule` |
| `security/ir.model.access.csv` | 85fe42ff819d5286295110eebfd107f050d60dd6 | Model ACL (5 rows) |

Blobs cited: **14**. All returned HTTP 200 and hash-verified against the pinned-commit tree.

## 2. Findings by A1 completion-card section

### 2.1 Manifest / dependencies / purpose
1. WHAT: `event_crm` auto-generates and maintains CRM leads/opportunities from event registrations, driven by configurable "lead rules" (filter + trigger + default lead values). `depends`: `event`, `crm`; `auto_install: True` (installs automatically once both are present — not an independent installation decision). (`__manifest__.py`)
2. A `web.assets_tests` bundle adds a JS tour for question-answer-based rule creation (not read). (`__manifest__.py`)

### 2.2 Data — models, inheritance, key fields, identity/uniqueness
3. `event.lead.rule` (new model): `lead_creation_basis` (attendee | order, default attendee — "per attendee" = one lead per registration/B2C, "per order" = one lead per registration batch/B2B), `lead_creation_trigger` (create | confirm | done, default create), filter fields `event_type_ids`/`event_id`/`company_id`/`event_registration_filter` (a free-text domain), and lead-default fields `lead_type`/`lead_sales_team_id`/`lead_user_id`/`lead_tag_ids`. No uniqueness constraint on the rule itself. (`models/event_lead_rule.py`)
4. `event.lead.request` (new, technical, `_log_access = False`): a per-event batching/progress record used only while a manual "(re)generate all leads" request for a large event is being processed by cron; holds `event_id` (required, cascade), `event_lead_rule_ids` (which rules to (re)apply — empty means "all"), `processed_registration_id` (cursor). Identity: unique constraint on `event_id` — only one in-flight generation request per event at a time. Batch size constant `_REGISTRATIONS_BATCH_SIZE = 200`. (`models/event_lead_request.py`)
5. `crm.lead` extension adds `event_lead_rule_id` (which rule created this lead), `event_id` (source event), `registration_ids` (many2many, field-group-restricted to `event.group_event_registration_desk`+) and a computed `registration_count` (same restriction). `event.event` extension adds `lead_ids`/`lead_count` (field-group-restricted to `sales_team.group_sale_salesman`). `event.registration` extension adds `lead_ids` (many2many, same sales-group restriction, `readonly=True`, not copied) and a computed `lead_count`. (`models/crm_lead.py`, `models/event_event.py`, `models/event_registration.py`)

### 2.3 Business rules / states / lifecycle / exceptions
6. Trigger wiring on `event.registration`: `create()` runs `create`-trigger rules immediately (unless a context flag `event_lead_rule_skip` is set, used by data-import code paths to avoid spurious lead creation while bootstrapping a database — see `_load_records_create`/`_load_records_write` overrides). `write()` additionally runs `confirm`-trigger rules when `state` is written to `open`, and `done`-trigger rules when written to `done`; both run sudo (registration desk/CRM permission mismatch is bridged deliberately here). `write()` also separately updates already-created leads' contact/description fields when tracked registration fields change (`_update_leads`), independent of trigger firing. (`models/event_registration.py`)
7. Rule matching (`event.lead.rule._filter_registrations`): a rule applies to a registration only if (a) an optional free-text domain filter matches, (b) the rule's company (if set) equals the registration's company, and (c) the rule's event/event-type restriction (if either is set) matches the registration's event or its event type — company and event/type conditions are ANDed with the domain filter, but event vs event-type within (c) is OR'd. All matching rules run; more than one lead can be created per registration if more than one rule matches — documented as intentional in the model's own design docstring, not a bug. (`models/event_lead_rule.py`)
8. Duplicate-avoidance: before creating any new leads, `_run_on_registrations` searches (including archived/lost leads, `active_test=False`) for existing leads already linked to the same `(registration, rule)` pair and excludes those registrations from re-processing — this is what makes re-running rules (e.g. via the manual "Generate Leads" action) idempotent rather than duplicating leads. (`models/event_lead_rule.py`)
9. Order-based ("per order") lead creation groups registrations by `(event_id, create_date)` — the module's own docstring flags this as a heuristic proxy for "created in the same batch," acknowledging that `event_sale`'s actual sale-order grouping is a planned refinement not implemented in this module; "update an existing group lead" is explicitly noted as unsupported (`False` is always passed for `existing_lead` in `_get_lead_grouping`). RISK: two unrelated batches created in the same second for the same event could be merged into one lead. (`models/event_lead_rule.py`)
10. Contact-value heuristic (`_get_lead_contact_values`): in single-registration ("attendee") mode, the registration's linked partner is used as the lead contact only if its email and (formatted) phone match the registration's own email/phone; otherwise the registration's own contact fields are used and the partner link is dropped for the lead, specifically to avoid unintentionally overwriting partner records via lead/partner field synchronization. In order/batch mode, any non-public partner found among the registrations is used directly as the contact. RISK: the public-partner check is called out in-source as "CHECKME: broader than just public partner," i.e. the source author flags this heuristic as possibly too broad. (`models/event_registration.py`)
11. Manual regeneration (`event.event.action_generate_leads`): restricted to `event.group_event_manager` (`UserError` otherwise). If the event(s) have at most 200 non-draft/non-cancelled registrations combined, rules run synchronously and the user gets an immediate lead count; above that, an `event.lead.request` batching record is created per event and the cron is `_trigger()`-ed for background processing, with an "in progress" notification instead of a count. (`models/event_event.py`)
12. Cron batching (`event.lead.request._cron_generate_leads`, daily, `job_limit=100` requests per run, `registrations_batch_size` default 200): for each pending request, processes up to one batch of registrations (ordered by id, resuming from `processed_registration_id`), commits after each request/batch (outside test mode) specifically because lead creation can send emails and must not be re-processed/duplicated on a later crash, and re-triggers itself if any request is still incomplete after this run; a request is deleted only once fully processed. (`models/event_lead_request.py`)
13. Merge behavior: `crm.lead._merge_dependences` is overridden to carry over `registration_ids` from merged-away opportunities (sudo, since CRM users may lack event permissions), and `_merge_get_fields` adds `event_lead_rule_id`/`event_id` to the set of fields preserved on merge. (`models/crm_lead.py`)
14. UI shortcut: `event.question.answer.action_add_rule_button` opens a pre-filled "create rule" wizard/action whose default filter domain restricts to registrations that answered the given question with the given suggested answer — a convenience for building `event_registration_filter` domains without hand-writing them. (`models/event_question_answer.py`)

### 2.4 Security
15. ACL (5 rows): `event.lead.rule` — read-only for `group_event_registration_desk`, `group_event_user`, and `sales_team.group_sale_salesman`; full CRUD only for `group_event_manager`. `event.lead.request` — full CRUD but restricted to `base.group_system` (technical/administrative model, not exposed to ordinary event or sales users). (`security/ir.model.access.csv`)
16. One `ir.rule`: `event.lead.rule` is scoped to `company_id in company_ids + [False]`, but only applied when `base.group_multi_company` is active (`groups` eval on the rule) — i.e. the rule is a no-op in single-company databases. (`security/event_crm_security.xml`)
17. The "Generate Leads" server action is itself group-restricted to `event.group_event_manager` at the action level (`data/ir_action_data.xml`) — consistent with, and layered on top of, the model-level check in `action_generate_leads` (finding 11), so the restriction is enforced twice (defense in depth, not contradictory).
18. Field-level restriction: `crm.lead.registration_ids`/`registration_count`, `event.event.lead_ids`/`lead_count`, and `event.registration.lead_ids` are all gated behind `event.group_event_registration_desk` or `sales_team.group_sale_salesman` groups respectively — an event user without CRM access cannot see which leads a registration produced, and vice versa a salesperson without event access cannot see which registrations fed a lead's `registration_ids` unless they also hold the event group. (`models/crm_lead.py`, `models/event_event.py`, `models/event_registration.py`)

### 2.5 UI surfaces (names only, not fetched/read)
19. `views/`: `crm_lead_views.xml`, `event_registration_views.xml`, `event_lead_rule_views.xml`, `event_event_views.xml`, `event_question_views.xml`. File presence only.

### 2.6 Jobs / config / integrations
20. Cron: `ir_cron_generate_leads` ("Event CRM: Generate Leads based on Rules"), daily, calling `event.lead.request._cron_generate_leads()`; additionally self-`_trigger()`-ed on demand whenever a manual bulk regeneration exceeds the synchronous threshold or a batch run leaves work unfinished — so, like `event`'s mail scheduler, it can fire far more often than daily in practice. (`data/ir_cron_data.xml`, `models/event_event.py`, `models/event_lead_request.py`)
21. Server action: `action_generate_leads`, bound to `event.event`, group-restricted to Event Managers (finding 17). (`data/ir_action_data.xml`)
22. No `ir.config_parameter` reads found in this module's fetched files.

## 3. Cross-module edges
23. Depends on `event` and `crm` (dependency relationship only, not group membership per MD-07/08); `auto_install: True` means this module's presence in a database is a consequence of both being installed, not a separate choice — worth flagging to A1 the same way as `event_booth_sale`. (`__manifest__.py`)
24. Reuses `event.group_event_registration_desk`/`group_event_user`/`group_event_manager` (from `event`) and `sales_team.group_sale_salesman`/`crm.group_use_lead` (from `crm`/`sale`) for ACL and field-group scoping, and `phone_validation`'s `_phone_format` helper (transitively available via `event`'s own dependency on `phone_validation`) for contact-matching. (`security/ir.model.access.csv`, `models/crm_lead.py`, `models/event_registration.py`)
25. `event.lead.rule`'s own docstring explicitly anticipates deeper integration with `event_sale` (order-based grouping) and `website_event` (batch registration) without those modules being direct dependencies here — a design note, not a verified cross-module code path in this fetch set.

## 4. Evidence gaps / contradictions
- G1: `data/crm_lead_merge_template.xml` fetched and hash-verified but its content was not read line-by-line beyond confirming it exists; not cited as a numbered finding.
- G2: Five view XML files not read.
- G3: `static/tests/tours/event_question_answers_rule_creation_tour.js` (JS test tour) not fetched.
- G4: `data/event_crm_demo.xml` (demo-only) not fetched.
- G5: i18n and the remaining tests not fetched.
- No contradictions observed between manifest, `__init__.py` roster, and fetched files. All 14 fetches returned HTTP 200 and hash-verified.

## 5. Limitations
Static source only, single pinned commit, no runtime/DB observation. CANDIDATE-ROSTER PILOT under MD-18 — G11 membership of this module is DERIVED, not Boss-confirmed. No GMVQ QID answered; no Formal Coverage claimed.
