# U53 — mail bridges, MRP family: mail_bot_hr, mail_plugin, mrp remaining, mrp_product_expiry, subcontracting extensions (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U53
- Modules: mail_bot_hr, mail_plugin, mrp (remaining), mrp_product_expiry, mrp_subcontracting_landed_costs, mrp_subcontracting_repair
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: DELTA-FIRST for mrp (U14 covered selectively). Full study for mail_bot_hr, mail_plugin, mrp_product_expiry, mrp_subcontracting_landed_costs, mrp_subcontracting_repair. Source evidence only; RT flags for runtime unknowns.

---

## CAP-U53-01 — OdooBot HR Bridge (mail_bot_hr)

### D1 — Module Identity
`mail_bot_hr` is a bridge between `mail_bot` and `hr`. It is declared `auto_install: True`, meaning it activates automatically when both `mail_bot` and `hr` are installed.

### D2 — Manifest Dependencies
The module depends on `['mail_bot', 'hr']` and contributes only a view extension: `views/res_users_views.xml`. There are no Python model files beyond `__init__.py` (which is empty).

### D3 — Scope
The module delivers OdooBot state and notification extensions on the user form view modified by the `hr` module. All logic is view-layer; no ORM model overrides are present in this revision.

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| Model layer | No Python model overrides; view-only bridge | FACT |
| Auto-install | auto_install True; activates when mail_bot + hr both present | FACT |
| Dependencies | mail_bot, hr | FACT |
| Data | views/res_users_views.xml only | FACT |
| Python files | __init__.py empty; __manifest__.py only substantive file | FACT |
| Runtime behaviour | Chatbot HR responses handled by mail_bot base logic; this module contributes view context | RT |
| HR leave via chat | Description states HR leave requests; no Python code confirmed in this module | INFERENCE |
| License | LGPL-3 | FACT |
| Category | Productivity/Discuss | FACT |
| Version | 1.0 | FACT |

---

## CAP-U53-02 — Mail Plugin: Authentication

### D1 — Auth Controller
`mail_plugin/controllers/authenticate.py` defines class `Authenticate(http.Controller)` with routes `/mail_plugin/auth` (GET, renders app_auth template) and `/mail_plugin/auth/confirm` (POST, generates temporary auth code).

### D2 — Auth Code Generation
`_generate_auth_code` creates a JSON dict with `scope`, `name`, `timestamp`, `uid`, signs it with HMAC via `odoo.tools.misc.hmac`, base64-encodes both halves, and returns `"<data>.<sig>"`. Auth codes expire in 3 minutes.

### D3 — Token Exchange
`auth_access_token` (route `/mail_plugin/auth/access_token`, auth=none, CORS=*) accepts the temporary auth code, verifies HMAC and timestamp, then calls `res.users.apikeys._generate(scope='odoo.plugin.outlook', ...)` to issue a persistent API key. Expiration is configurable via `ir.config_parameter` key `mail_plugin.access_token_expiration_days`, default 30 days.

### D4 — `_auth_method_outlook`
`mail_plugin/models/ir_http.py` defines `_auth_method_outlook` on `ir.http`. It reads `Authorization: Bearer <token>` from the request header and calls `res.users.apikeys._check_credentials(scope='odoo.plugin.outlook', key=...)`. On success it calls `request.update_env(user=user_id)` and `request.update_context(**request.env.user.context_get())`.

### D5 — Version Check Route
`/mail_plugin/auth/check_version` (auth=none, POST/OPTIONS) returns integer `1`; allows the mail plugin client to detect module presence and version compatibility.

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| Auth flow | Temporary auth code → persistent API key exchange | FACT |
| HMAC signing | odoo.tools.misc.hmac used; key='mail_plugin'; 3-minute expiry | FACT |
| Token scope | 'odoo.plugin.outlook' | FACT |
| Token lifetime | default 30 days; configurable via ir.config_parameter | FACT |
| Auth method | Custom _auth_method_outlook on ir.http | FACT |
| Internal-only | _generate_auth_code raises NotFound if user not internal | FACT |
| CORS | All plugin routes use cors="*" | FACT |
| Backward compat | Old routes /mail_client_extension/* kept; deprecated saas-14.3 | FACT |
| Gmail connector | state param forwarded in auth_confirm for Gmail connector | OBSERVATION |
| Runtime token check | _check_credentials is a runtime call; result depends on DB state | RT |

---

## CAP-U53-03 — Mail Plugin: Partner Lookup and Enrichment

### D1 — Partner Get Route
`/mail_plugin/partner/get` (auth=outlook, CORS=*) accepts `email`, `name`, and/or `partner_id`. If `partner_id` supplied it browses directly. Otherwise normalises email, rejects notification addresses from `mail.alias.domain`, then searches `res.partner` by `email_normalized`. On miss returns `{'id': -1, ...}` placeholder.

### D2 — Notification Address Guard
The controller reads `mail.alias.domain` notification emails via `sudo()` and rejects any exact match, returning a custom error `'type': 'odoo_custom_error'`.

### D3 — Company Auto-Creation
When no partner found AND user has create access on `res.partner`, `_create_company_from_iap(normalized_email)` is called. This enriches via IAP and creates a new `res.partner` record flagged `is_company=True`.

### D4 — IAP Enrichment
`_iap_enrich(domain)` first checks `iap_tools._MAIL_PROVIDERS` to avoid enriching public mail domains (gmail.com etc). On success it calls `iap.enrich.api._request_enrich`. Returns error types `missing_data`, `insufficient_credit`, `no_data`, or `other`.

### D5 — Partner Search Route
`/mail_plugin/partner/search` (auth=outlook) accepts `search_term` and `limit` (default 30). Searches `email_normalized`, `complete_name`, `ref`, or `email` depending on whether the term is a valid email.

### D6 — Partner Create Route
`/mail_plugin/partner/create` (auth=outlook) creates a minimal `res.partner` record. Rejects notification emails with `Forbidden`.

### D7 — Log Mail Content Route
`/mail_plugin/log_mail_content` (auth=outlook) calls `message_post` on the target record. Model must be in `_mail_content_logging_models_whitelist()` (base whitelist: `['res.partner']`; extensible by submodules).

### D8 — Enrich and Update Company Route
`/mail_plugin/partner/enrich_and_update_company` enriches an existing company partner using IAP. Updates phone, website, city, zip, street if not already set. Downloads logo image (requests.get, timeout=2 s). Posts a chatter note via `message_post_with_source('iap_mail.enrich_company', ...)`.

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| Partner search | email_normalized ilike, complete_name ilike, ref exact, email ilike | FACT |
| No-partner fallback | Returns id=-1 stub; client side must handle | FACT |
| IAP provider guard | iap_tools._MAIL_PROVIDERS list blocks public domains | FACT |
| IAP error surface | insufficient_credit, no_data, missing_data, other types | FACT |
| Model whitelist | _mail_content_logging_models_whitelist extensible; base=['res.partner'] | FACT |
| Image download | requests.get with 2s timeout; failure silently skipped | FACT |
| Access check | has_access('create') checked before auto-company creation | FACT |
| CRM extension | modules_get returns ['contacts','crm']; CRM route available via override | OBSERVATION |
| CORS | All routes cors="*" | FACT |
| Chatter note | enrich_update posts message via message_post_with_source, subtype mail.mt_note | FACT |

---

## CAP-U53-04 — Mail Plugin: Partner IAP Cache Model

### D1 — Model Definition
`res.partner.iap` (`_name='res.partner.iap'`) stores IAP enrichment response per partner. Unique constraint `UNIQUE(partner_id)` enforced at DB level.

### D2 — Fields
`partner_id` (Many2one res.partner, ondelete cascade, required); `iap_search_domain` (Char, domain or email used for lookup); `iap_enrich_info` (Text, JSON string, readonly).

### D3 — Separation Rationale
Model docstring states: "separate model to not add heavy field (iap_enrich_info) on res.partner model".

### D4 — Partner Compute/Write Override
`res.partner` gains computed fields `iap_enrich_info` and `iap_search_domain` via `_compute_partner_iap_info`. These are backed by the `res.partner.iap` table. `create` and `write` on `res.partner` synchronise the IAP table via sudo.

### D5 — IAP Search Domain Logic
`_get_iap_search_term` returns `"@domain"` for non-blacklisted domains, or full email for blacklisted domains (e.g. gmail addresses stored as full email to uniquely identify).

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| Model name | res.partner.iap | FACT |
| Unique constraint | UNIQUE(partner_id); Constraint API | FACT |
| Cascade delete | ondelete='cascade' on partner_id | FACT |
| Computed on partner | iap_enrich_info and iap_search_domain are computed on res.partner | FACT |
| Sudo used | partner.iap records created/searched with sudo() | FACT |
| Domain vs email key | _MAIL_DOMAIN_BLACKLIST controls whether domain or full email stored | FACT |
| JSON storage | iap_enrich_info is Text (raw JSON), not structured | FACT |
| No duplication guard | Unique constraint prevents double-enrichment of same partner | FACT |
| Write sync | write on res.partner creates missing partner.iap if absent | FACT |
| Read access | compute method runs under sudo to bypass access checks | FACT |

---

## CAP-U53-05 — MRP Work Order: Model and Fields

### D1 — Model Identity
`mrp.workorder` (`_name='mrp.workorder'`, `_description='Work Order'`, `_order='sequence, leave_id, date_start, id'`).

### D2 — State Field
`state` is a Selection: `('blocked','Blocked')`, `('ready','To Do')`, `('progress','In Progress')`, `('done','Finished')`, `('cancel','Cancelled')`. Computed, stored, index=True.

### D3 — Timing Fields
`date_start` and `date_finished` are computed from `leave_id` (a `resource.calendar.leaves` record). `duration_expected` (float, minutes, stored). `duration` (float, real, computed from `time_ids`). `duration_unit` (avg aggregator). `duration_percent` (deviation %).

### D4 — Barcode Field
`barcode` is computed as `f"{production_id.name}/{workorder.id}"`.

### D5 — Dependency Fields
`blocked_by_workorder_ids` and `needed_by_workorder_ids` use M2M on `mrp_workorder_dependencies_rel` table, guarded by `allow_workorder_dependencies`.

### D6 — Working User Tracking
`is_user_working`, `working_user_ids`, `last_working_user_id` computed from `time_ids` (One2many to `mrp.workcenter.productivity`) filtered by `date_end=False`.

### D7 — Costs Hour
`costs_hour` stored at work order level to preserve the hourly cost at time of completion (comment: "to keep consistent cost").

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| Order sorting | sequence, leave_id, date_start, id | FACT |
| Barcode format | production_id.name/workorder.id | FACT |
| State computation | _compute_state driven by qty_ready | FACT |
| Leave-based scheduling | date_start/date_finished computed from resource.calendar.leaves leave_id | FACT |
| Cyclic dependency check | _check_no_cyclic_dependencies constraint on blocked_by_workorder_ids | FACT |
| Cost capture | costs_hour stored at done time to freeze cost | FACT |
| Scrap count | scrap_count via read_group on stock.scrap.workorder_id | FACT |
| Qty reporting | qty_reported_from_previous_wo carries quantity in backorder chain | FACT |
| Progress percent | progress = duration * 100 / duration_expected; 100 when done | FACT |
| Move tracking | move_raw_ids and move_finished_ids linked via workorder_id | FACT |

---

## CAP-U53-06 — MRP Work Order: Lifecycle Buttons

### D1 — button_start
Creates `mrp.workcenter.productivity` timeline record with `_prepare_timeline_vals`. If workcenter calendar exists, creates a `resource.calendar.leaves` leave slot. Sets production `date_start` if not in progress.

### D2 — button_pending / end_previous
`button_pending` calls `end_previous()` which closes open productivity timelines by setting `date_end`. `doall=True` variant closes all users; default closes only current user.

### D3 — button_finish / end_all
`button_finish` marks `state='done'`, sets `qty_produced`, captures `date_finished`, captures `costs_hour` from workcenter. Calls `end_all()` to close any open time logs. Marks raw/byproduct moves as `picked=True`.

### D4 — action_cancel
`action_cancel` unlinks `leave_id`, calls `end_all()`, writes `state='cancel'` on non-cancelled workorders.

### D5 — set_state Helper
`set_state(state)` is a generic helper that routes to `button_pending`, `action_cancel`, `action_mark_as_done`, or `button_start` based on desired state. Skips if already in target state or in done/cancel production.

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| Timer start | _prepare_timeline_vals creates mrp.workcenter.productivity record | FACT |
| Leave slot on start | resource.calendar.leaves created on button_start if no leave_id | FACT |
| Finish captures cost | costs_hour = workcenter.costs_hour at button_finish | FACT |
| Cancel cleans leave | leave_id unlinked on action_cancel | FACT |
| picked flag | moves set picked=True on button_finish | FACT |
| Pending pause | end_previous closes productivity timeline for current user | FACT |
| Progress bar | _compute_progress: done=100, else duration/expected*100 | FACT |
| State recheck | set_state skips done/cancel production workorders | FACT |
| Workcenter block guard | button_start raises UserError if workcenter working_state=='blocked' | FACT |
| Qty producing sync | qty_producing write propagates to production_id.qty_producing | FACT |

---

## CAP-U53-07 — MRP Work Order: Scheduling (Plan Workorder)

### D1 — _plan_workorder
`_plan_workorder(replan=False)` first recurses on `blocked_by_workorder_ids`. Sets `date_start = max(production.date_start, now())` and advances past predecessors' `date_finished`. Then calls `workcenter._get_first_available_slot(date_start, duration_expected)` for each of `workcenter_id | alternative_workcenter_ids`.

### D2 — Best Slot Selection
Iterates all workcenters (primary + alternatives), picks the one with earliest `to_date`. Writes `leave_id`, `workcenter_id`, `duration_expected` on selected slot.

### D3 — _calculate_date_finished
Uses `resource_calendar_id.plan_hours(duration/60, date_start, compute_leaves=True, domain=[time_type in ['leave','other']])` when a calendar is present, otherwise adds a simple timedelta.

### D4 — Duration Expected Computation
`_get_duration_expected` computes setup + cleanup + (cycle_number × time_cycle × 100 / time_efficiency). For alternative workcenters recalculates `capacity`, `cycle_number`, `setup`, `cleanup` using the alternative's `_get_capacity`.

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| Recursive planning | blocked predecessors planned first | FACT |
| Alternative workcenter | _plan_workorder iterates primary + alternatives | FACT |
| Max iterations | mrp.workcenter_max_planning_iterations ir.config_parameter, default 50; 50×14=700 days | FACT |
| Slot algorithm | Intervals-based conflict check vs existing leave slots | FACT |
| Calendar used | resource.calendar.leaves with time_type='other' | FACT |
| Conflict detection | _get_conflicted_workorder_ids uses raw SQL OVERLAPS | FACT |
| Duration formula | setup + cleanup + cycles * time_cycle * 100 / time_efficiency | FACT |
| Replan flag | replan=True unlinks existing leave_id before replanning | FACT |
| No slot error | UserError if no slot available in 700 days | FACT |
| MO date propagation | First WO date_start propagated to production_id; last WO date_finished propagated | FACT |

---

## CAP-U53-08 — MRP Workcenter Model

### D1 — Model Identity
`mrp.workcenter` inherits `['mail.thread', 'resource.mixin']`. Default resource_type='material' forced at create.

### D2 — OEE Metrics
`oee` field computed as `productive_time * 100 / (productive_time + blocked_time)` over last month. `oee_target` default 90. `performance` = `duration_expected_sum * 100 / duration_sum` over last month done WOs.

### D3 — Working State
`working_state` is computed from open (date_end=False) productivity records. `loss_type in ('productive','performance')` → 'done' (in progress). Other loss types → 'blocked'. No open records → 'normal'.

### D4 — Capacity Model
`capacity_ids` One2many to `mrp.workcenter.capacity`. `_get_capacity(product, unit, default)` returns `(capacity, setup, cleanup)` tuple by looking up product-specific capacity rows; falls back to workcenter `time_start`/`time_stop`.

### D5 — First Available Slot Algorithm
`_get_first_available_slot` iterates up to `max_planning_iterations` windows of 14 days. For each available interval it checks conflict against `resource.calendar.leaves` (time_type='other') and extra_leaves. Forward and backward modes supported.

### D6 — Kanban Dashboard Graph
`kanban_dashboard_graph` computes weekly load (hours) for past week + current + 3 future weeks. If no workorders exist, returns random demo data.

### D7 — Alternative Workcenter Guard
`_check_alternative_workcenter` constraint prevents self-reference in `alternative_workcenter_ids`.

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| Resource mixin | inherits resource.mixin; time_efficiency and active relayed to resource_id | FACT |
| OEE formula | productive / (productive + blocked) * 100, last month | FACT |
| Blocked state | open productivity record with non-productive/performance loss_type | FACT |
| Capacity lookup | product-specific capacity rows; fallback to time_start/time_stop | FACT |
| unblock | unblock() closes open timelines (date_end = now) | FACT |
| Archive warning | archiving workcenter with routing lines shows sticky warning | FACT |
| Dashboard demo data | Random data injected when no workorders found | OBSERVATION |
| Self-alternative guard | ValidationError on self-reference in alternative_workcenter_ids | FACT |
| Config parameter | mrp.workcenter_max_planning_iterations; default 50 | FACT |
| Costs hour | costs_hour tracked field on workcenter | FACT |

---

## CAP-U53-09 — MRP Routing: mrp.routing.workcenter

### D1 — Model Identity
`mrp.routing.workcenter` (_name='mrp.routing.workcenter', inherits mail.thread + mail.activity.mixin). Ordered by `bom_id, sequence, id`.

### D2 — Time Mode
`time_mode` Selection: `('manual','Fixed')` or `('auto','Computed')`. In auto mode, `time_cycle` is computed from last `time_mode_batch` done workorders.

### D3 — Auto Time Cycle Computation
`_compute_time_cycle` for auto-mode: queries last N done workorders filtered by `operation_id`, sums `duration` and computes `cycle_number = sum(qty_produced / capacity)`. `time_cycle = total_duration / cycle_number`.

### D4 — Operation Dependencies
`blocked_by_operation_ids` and `needed_by_operation_ids` M2M on `mrp_routing_workcenter_dependencies_rel`. Cyclic check via `_has_cycle`. `allow_operation_dependencies` relayed from BoM.

### D5 — Variant Filtering
`bom_product_template_attribute_value_ids` M2M for variant-specific operations. `_skip_operation_line` returns True if archived or if product variant does not match attribute values.

### D6 — Cost Mode
`cost_mode` Selection: `('actual','Actual time')` or `('estimated','Theorical time')`. Cost computed as `time_total / 60 * costs_hour`.

### D7 — Copy to BoM Action
`copy_to_bom()` copies operation to BoM referenced in context key `bom_id`. `copy_existing_operations()` opens list view to select operations to copy.

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| BoM cascade | bom_id ondelete='cascade' | FACT |
| Auto time cycle | computed from last N done WOs | FACT |
| N configurable | time_mode_batch integer field, default 10 | FACT |
| Cyclic dependency | _has_cycle used; ValidationError if cycle detected | FACT |
| Variant filter | _skip_operation_line checks attribute value match | FACT |
| Cost mode | actual vs estimated on operation | FACT |
| Tracking fields | workcenter_id, time_mode, time_cycle_manual, cost_mode tracked | FACT |
| archive side-effect | archive clears operation_id from BoM lines and byproducts | FACT |
| create side-effect | create calls _set_outdated_bom_in_productions | FACT |
| Company check | _check_company_auto = True | FACT |

---

## CAP-U53-10 — MRP Unbuild Order

### D1 — Model Identity
`mrp.unbuild` (_name='mrp.unbuild', inherits mail.thread + mail.activity.mixin, ordered `id desc`). States: draft, done.

### D2 — Sequence Auto-name
`create` auto-assigns name from `ir.sequence` code `mrp.unbuild`.

### D3 — Action Unbuild
`action_unbuild` generates consume moves (finished products coming back) and produce moves (components going back to stock). Confirms both via `_action_confirm()`. Calls `produce_moves._action_done()`, `consume_moves._action_done()`, `finished_moves._action_done()`.

### D4 — MO-linked Unbuild
When `mo_id` is set: `_generate_consume_moves` iterates `mo.move_finished_ids` state='done', proportioned by `factor = unbuild_qty / mo_qty_produced`. Lot tracking from original move lines.

### D5 — BOM-linked Unbuild
When no MO: uses `bom_id.explode` to determine components, creates moves from BoM lines.

### D6 — Serial Number Handling
For serial-tracked products, `product_qty` defaults to 1. Lot filtering uses `produce_line_ids.lot_id` cross-reference. Previously unbuilt lots tracked to avoid double-return.

### D7 — Insufficient Qty Guard
`action_validate` checks available qty via `stock.quant._get_available_quantity`. If insufficient, opens `stock.warn.insufficient.qty.unbuild` wizard.

### D8 — Chatter Post on MO
On completion, posts a chatter note on `mo_id` with unbuilt qty and unbuild order HTML link.

### D9 — Delete Guard
`_unlink_except_done` prevents deletion of done unbuild orders.

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| States | draft, done only | FACT |
| MO link | mo_id domain restricts to state='done' productions | FACT |
| Factor calculation | unbuild_qty / mo_qty_produced proportions moves | FACT |
| Lot cross-reference | produce_line_ids.lot_id used to match component lots from original MO | FACT |
| Previously unbuilt | previous unbuild lots tracked to avoid double return | FACT |
| putaway applied | _apply_putaway_strategy called on each unbuild move line | FACT |
| Delete protection | UserError on unlink if any state='done' | FACT |
| Quantity constraint | DB constraint check(product_qty > 0) | FACT |
| Insufficient qty wizard | stock.warn.insufficient.qty.unbuild model extends stock.warn.insufficient.qty | FACT |
| Chatter note | mo_id.message_post with subtype mail.mt_note on completion | FACT |

---

## CAP-U53-11 — MRP Wizards

### D1 — change.production.qty
`change_production_qty` wizard updates raw move quantities (proportional `factor = new_qty / old_qty`), calls `_update_finished_moves` on finished product and byproducts, adjusts work order `duration_expected` and `qty_producing`. Triggers scheduler for confirmed/progress MO raw moves.

### D2 — mrp.production.backorder
`mrp.production.backorder` presents lines per MO (`mrp_production_backorder_line_ids`) each with `to_backorder` boolean. `action_backorder` collects flagged MO ids and calls `button_mark_done` with context `mo_ids_to_backorder`. `action_close_mo` passes `skip_backorder=True` to skip backorder creation.

### D3 — mrp.production.split / mrp.production.split.multi
`mrp.production.split` wizard: `max_batch_size` from BoM `batch_size` if `enable_batch_size` set, else full `product_qty`. `num_splits` = ceil(qty / max_batch_size). `production_detailed_vals_ids` auto-computed lines. `action_split` calls `production_id._split_productions`.

### D4 — mrp.production.serials
Assigns serial numbers to production. `action_generate_serial_numbers` calls `stock.lot.generate_lot_names`. `action_split_and_assign_serials` splits into N serial MOs via `_split_productions`. `action_apply` assigns lots to `production_id.lot_producing_ids`.

### D5 — mrp.consumption.warning
`mrp.consumption.warning` surfaces when components consumed deviate from BoM under `warning` or `strict` mode. `action_confirm` passes `skip_consumption=True` context. `action_set_qty` resets consumed quantities to expected values; creates missing stock moves if needed.

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| change_production_qty | proportional factor update on raw and finished moves | FACT |
| backorder wizard | per-MO to_backorder flag | FACT |
| split wizard | batch_size aware; _split_productions called | FACT |
| serial wizard | generate_lot_names + split_productions for serial-tracked | FACT |
| consumption warning | strict/warning modes gated; skip_consumption context key | FACT |
| scheduler trigger | move_raw_ids._trigger_scheduler on qty change | FACT |
| missing moves | action_set_qty creates additional=True moves if lines missing | FACT |
| backorder context | mo_ids_to_backorder context key controls which MOs get backorder | FACT |
| Multi-split | mrp.production.split.multi handles N MOs simultaneously | FACT |
| Serial dedup | _onchange_serial_numbers removes duplicate lot names | FACT |

---

## CAP-U53-12 — mrp_product_expiry: Expiry Enforcement on MO

### D1 — Module Dependencies
`mrp_product_expiry` depends on `['mrp', 'product_expiry']`, auto_install=True.

### D2 — pre_button_mark_done Override
`mrp.production.pre_button_mark_done` is overridden. Before calling `super()`, it calls `_check_expired_lots()`.

### D3 — _check_expired_lots Logic
Filters `move_raw_ids.move_line_ids` for those where `lot_id.product_expiry_alert == True`. If any expired lots found, opens `expiry.picking.confirmation` wizard. Context key `skip_expired` bypasses the check when set.

### D4 — expiry.picking.confirmation Extension
`ExpiryPickingConfirmation` inherits `expiry.picking.confirmation` and adds `production_ids` M2M and `workorder_id` Many2one fields. `_compute_descriptive_fields` customises message text for MO context (shows product name + lot name for single expired lot).

### D5 — confirm_produce
`confirm_produce` method: pops `default_lot_ids` from context, sets `skip_expired=True`, calls `production_ids.button_mark_done()`.

### D6 — confirm_workorder
`confirm_workorder` method: similar to confirm_produce but calls `workorder_id.record_production()`.

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| Trigger | pre_button_mark_done; expiry checked before finalization | FACT |
| Alert field | lot_id.product_expiry_alert (from product_expiry module) | FACT |
| Skip key | context key skip_expired bypasses check | FACT |
| Wizard model | expiry.picking.confirmation (from stock_picking_expiry base) | FACT |
| MO fields added | production_ids M2M, workorder_id M2O added to wizard | FACT |
| Single lot message | product name + lot name shown for single expired lot | FACT |
| Multi lot message | show_lots=True when multiple expired lots; listed in view | FACT |
| Workorder path | confirm_workorder calls record_production() on workorder | FACT |
| Auto-install | auto_install=True when mrp + product_expiry both present | FACT |
| Source | mrp_product_expiry/models/mrp_production.py:10-39 | FACT |

---

## CAP-U53-13 — mrp_subcontracting_landed_costs

### D1 — Module Identity
`mrp_subcontracting_landed_costs` depends on `['stock_landed_costs', 'mrp_subcontracting']`. auto_install=True. Category: Supply Chain/Manufacturing.

### D2 — _get_targeted_move_ids Override
Inherits `stock.landed.cost`. In `_get_targeted_move_ids`, for any move where `is_subcontract=True`, the move itself is replaced by its `move_orig_ids` (originating moves, i.e., the component supply moves). Non-subcontract moves pass through unchanged.

### D3 — Rationale
For subcontracting receipts, the cost should be applied to the upstream supply/component moves rather than the finished receipt move. This override redirects cost allocation to the correct upstream moves.

### D4 — OrderedSet Usage
`OrderedSet` from `odoo.tools` used to preserve order while deduplicating move IDs.

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| Override target | stock.landed.cost._get_targeted_move_ids | FACT |
| Is_subcontract check | move.is_subcontract boolean checked | FACT |
| Upstream redirect | move_orig_ids used instead of move itself | FACT |
| OrderedSet dedup | OrderedSet preserves insert order | FACT |
| Auto-install | auto_install=True | FACT |
| View contribution | views/stock_landed_cost_views.xml (search view extension) | FACT |
| No wizard | No wizard model; pure model override | FACT |
| Dependency | stock_landed_costs + mrp_subcontracting | FACT |
| Category | Supply Chain/Manufacturing | FACT |
| Purpose | Correct cost allocation for subcontracted goods | FACT |

---

## CAP-U53-14 — mrp_subcontracting_repair

### D1 — Module Identity
`mrp_subcontracting_repair` depends on `['mrp_subcontracting', 'repair']`. auto_install=True. Category: Supply Chain/Repair. Description: "Bridge module between MRP subcontracting and Repair".

### D2 — File Content
The module contains only `__init__.py` (empty in source) and `__manifest__.py`. No Python model overrides are present in this revision; the bridge is manifest-declaration only.

### D3 — Purpose Inference
As a bridge module, it likely ensures correct installation sequencing and may contribute XML views/data. No Python logic confirmed at this revision.

### Ten-dimension table

| Dimension | Finding | Flag |
|---|---|---|
| Dependencies | mrp_subcontracting, repair | FACT |
| Python models | None in this revision | FACT |
| auto_install | True | FACT |
| Purpose | Bridge/sequencing between subcontracting and repair | FACT |
| Runtime behaviour | Any integration logic presumed in view/data layer | RT |
| Category | Supply Chain/Repair | FACT |
| License | LGPL-3 | FACT |
| Version | 1.0 | FACT |
| XML data | not confirmed from Python; views likely in data dir | INFERENCE |
| Odoo SA authored | author 'Odoo S.A.' | FACT |

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U53-C001 | mail_bot_hr manifest | mail_bot_hr/__manifest__.py:3 | `'name': "OdooBot - HR"` | FACT | always | — | Module name is "OdooBot - HR" | N-U53-001 |
| VDR-U53-C002 | mail_bot_hr auto-install | mail_bot_hr/__manifest__.py:11 | `'auto_install': True` | FACT | when mail_bot+hr installed | — | auto_install=True activates bridge automatically | N-U53-001 |
| VDR-U53-C003 | mail_bot_hr deps | mail_bot_hr/__manifest__.py:9 | `'depends': ['mail_bot', 'hr']` | FACT | always | — | Depends on mail_bot and hr | N-U53-001 |
| VDR-U53-C004 | mail_bot_hr no Python | mail_bot_hr/__manifest__.py:3 | OdooBot - HR | FACT | always | — | Module has no Python model overrides; only manifest and data files | N-U53-001 |
| VDR-U53-C005 | mail_plugin manifest | mail_plugin/__manifest__.py:6 | 'version': '1.0 | FACT | always | — | mail_plugin depends on web, contacts, iap | N-U53-002 |
| VDR-U53-C006 | auth route | mail_plugin/controllers/authenticate.py:21 | `@http.route(['/mail_client_extension/auth', '/mail_plugin/auth'], type='http', auth="user"` | FACT | always | — | Auth GET route renders app_auth template for internal users only | N-U53-003 |
| VDR-U53-C007 | auth confirm route | mail_plugin/controllers/authenticate.py:34 | `@http.route(['/mail_client_extension/auth/confirm', '/mail_plugin/auth/confirm'], type='http', auth="user", methods=['POST'])` | FACT | always | — | Auth confirm is a POST route generating temp auth code | N-U53-003 |
| VDR-U53-C008 | auth code expiry | mail_plugin/controllers/authenticate.py:106 | if datetime.datetime.utcnow | FACT | always | — | Auth codes expire after 3 minutes | N-U53-003 |
| VDR-U53-C009 | token exchange route | mail_plugin/controllers/authenticate.py:65 | `@http.route(['/mail_client_extension/auth/access_token', '/mail_plugin/auth/access_token'], type='jsonrpc', auth="none", cors="*"` | FACT | always | — | Access token exchange route is auth=none, CORS=* | N-U53-003 |
| VDR-U53-C010 | token scope | mail_plugin/controllers/authenticate.py:83 | `scope = 'odoo.plugin.' + auth_message.get('scope', '')` | FACT | always | — | Token scope is 'odoo.plugin.outlook' | N-U53-003 |
| VDR-U53-C011 | token expiry config | mail_plugin/controllers/authenticate.py:84-86 | expiration_days | FACT | always | — | Token lifetime configurable via ir.config_parameter key mail_plugin.access_token_expiration_days; default 30 days | N-U53-003 |
| VDR-U53-C012 | auth method outlook | mail_plugin/models/ir_http.py:14 | def _auth_method_outlook(cls) | FACT | always | — | Custom auth method _auth_method_outlook defined on ir.http | N-U53-003 |
| VDR-U53-C013 | bearer token check | mail_plugin/models/ir_http.py:22 | `user_id = request.env["res.users.apikeys"]._check_credentials(scope='odoo.plugin.outlook', key=access_token)` | FACT | on each request | RT | API key credentials checked against scope odoo.plugin.outlook | N-U53-003 |
| VDR-U53-C014 | internal-only guard | mail_plugin/controllers/authenticate.py:115 | if not request.env.user._is_internal() | FACT | always | — | Only internal users can generate auth codes | N-U53-003 |
| VDR-U53-C015 | partner get route | mail_plugin/controllers/mail_plugin.py:132 | @http.route(['/mail_client_extension/partner/get | FACT | always | — | Partner get route accepts email/name/partner_id params | N-U53-004 |
| VDR-U53-C016 | notification email guard | mail_plugin/controllers/mail_plugin.py:156-166 | `notification_emails = request.env['mail.alias.domain'].sudo().search([]).mapped('default_from_email')` | FACT | always | — | Notification addresses from mail.alias.domain excluded from partner matches | N-U53-004 |
| VDR-U53-C017 | partner not found stub | mail_plugin/controllers/mail_plugin.py:177-183 | if not response['partner'] | FACT | when no partner | — | Missing partner returns id=-1 stub for backward compatibility | N-U53-004 |
| VDR-U53-C018 | auto company creation | mail_plugin/controllers/mail_plugin.py:186-191 | can_create_partner | FACT | when no partner and create access | — | Company auto-created via IAP when partner not found | N-U53-004 |
| VDR-U53-C019 | IAP provider guard | mail_plugin/controllers/mail_plugin.py:281-283 | if domain in iap_tools._MAIL_PROVIDERS | FACT | always | — | Public mail provider domains blocked from IAP enrichment | N-U53-004 |
| VDR-U53-C020 | IAP error types | mail_plugin/controllers/mail_plugin.py:288-295 | except iap_tools.InsufficientCreditError | FACT | always | — | IAP returns structured error types: insufficient_credit, no_data, missing_data, other | N-U53-004 |
| VDR-U53-C021 | partner search route | mail_plugin/controllers/mail_plugin.py:195 | `@http.route('/mail_plugin/partner/search', type="jsonrpc", auth="outlook", cors="*")` | FACT | always | — | Search route accepts search_term, limit=30 | N-U53-004 |
| VDR-U53-C022 | search domain | mail_plugin/controllers/mail_plugin.py:209 | complete_name | FACT | when term is not email | — | Non-email search uses complete_name ilike, ref exact, email ilike | N-U53-004 |
| VDR-U53-C023 | log mail content | mail_plugin/controllers/mail_plugin.py:250 | `@http.route('/mail_plugin/log_mail_content', type="jsonrpc", auth="outlook", cors="*")` | FACT | always | — | Logs email body to target record via message_post | N-U53-004 |
| VDR-U53-C024 | model whitelist | mail_plugin/controllers/mail_plugin.py:432-437 | def _mail_content_logging_models_whitelist(self) | FACT | always | — | Base whitelist for log_mail_content is ['res.partner']; extensible | N-U53-004 |
| VDR-U53-C025 | enrich update company | mail_plugin/controllers/mail_plugin.py:60 | `@http.route('/mail_plugin/partner/enrich_and_update_company', type='jsonrpc', auth='outlook', cors='*')` | FACT | always | — | Enrich-update route requires partner to be a company | N-U53-004 |
| VDR-U53-C026 | image download timeout | mail_plugin/controllers/mail_plugin.py:100 | `response = requests.get(logo_url, timeout=2)` | FACT | during enrichment | — | Logo image downloaded with 2-second timeout; failure silently ignored | N-U53-004 |
| VDR-U53-C027 | chatter note on enrich | mail_plugin/controllers/mail_plugin.py:121-125 | partner.message_post_with_source | FACT | on company update | — | Enrichment posts internal note using iap_mail.enrich_company template | N-U53-004 |
| VDR-U53-C028 | partner iap model | mail_plugin/models/res_partner_iap.py:19 | `_name = 'res.partner.iap'` | FACT | always | — | Separate model res.partner.iap holds IAP cache | N-U53-005 |
| VDR-U53-C029 | unique constraint | mail_plugin/models/res_partner_iap.py:27-30 | _unique_partner_id = models.Constraint | FACT | always | — | DB-level unique constraint on partner_id | N-U53-005 |
| VDR-U53-C030 | cascade delete | mail_plugin/models/res_partner_iap.py:22 | partner_id = fields.Many2one | FACT | always | — | partner.iap deleted when partner deleted | N-U53-005 |
| VDR-U53-C031 | iap search domain | mail_plugin/controllers/mail_plugin.py:446-447 | `return ("@" + domain) if domain not in iap_tools._MAIL_DOMAIN_BLACKLIST else email` | FACT | always | — | Search key is @domain for non-blacklisted, full email for blacklisted domains | N-U53-005 |
| VDR-U53-C032 | partner compute fields | mail_plugin/models/res_partner.py:8-12 | iap_enrich_info | FACT | always | — | iap_enrich_info and iap_search_domain computed on res.partner from res.partner.iap | N-U53-005 |
| VDR-U53-C033 | wo model name | mrp/models/mrp_workorder.py:16 | `_name = 'mrp.workorder'` | FACT | always | — | Work order model _name is mrp.workorder | N-U53-006 |
| VDR-U53-C034 | wo order | mrp/models/mrp_workorder.py:18 | `_order = 'sequence, leave_id, date_start, id'` | FACT | always | — | Work orders ordered by sequence, leave_id, date_start, id | N-U53-006 |
| VDR-U53-C035 | wo state field | mrp/models/mrp_workorder.py:66-73 | state = fields.Selection | FACT | always | — | State has 5 values: blocked, ready, progress, done, cancel | N-U53-006 |
| VDR-U53-C036 | wo barcode | mrp/models/mrp_workorder.py:305-306 | `wo.barcode = f"{wo.production_id.name}/{wo.id}"` | FACT | always | — | Barcode computed as production name slash workorder id | N-U53-006 |
| VDR-U53-C037 | wo leave-based dates | mrp/models/mrp_workorder.py:270-274 | @api.depends('leave_id') | FACT | always | — | date_start and date_finished computed from resource.calendar.leaves leave_id | N-U53-006 |
| VDR-U53-C038 | wo costs_hour freeze | mrp/models/mrp_workorder.py:728 | `'costs_hour': workorder.workcenter_id.costs_hour` | FACT | on button_finish | — | costs_hour captured from workcenter at button_finish to freeze cost | N-U53-006 |
| VDR-U53-C039 | wo working users | mrp/models/mrp_workorder.py:422-437 | `no_date_end_times = order.time_ids.filtered(lambda time: not time.date_end)` | FACT | computed | — | working_user_ids derived from productivity records with no date_end | N-U53-006 |
| VDR-U53-C040 | wo cyclic dep check | mrp/models/mrp_workorder.py:298-301 | @api.constrains('blocked_by_workorder_ids') | FACT | always | — | Cyclic dependency in blocked_by_workorder_ids raises ValidationError | N-U53-006 |
| VDR-U53-C041 | wo qty remaining | mrp/models/mrp_workorder.py:803-809 | @api.depends('qty_production | FACT | computed | — | qty_remaining accounts for carried quantity from previous work orders | N-U53-006 |
| VDR-U53-C042 | wo btn start timer | mrp/models/mrp_workorder.py:671-673 | self.env['mrp.workcenter.productivity'].create | FACT | on button_start | — | Productivity timeline record created on button_start | N-U53-007 |
| VDR-U53-C043 | wo btn start guard | mrp/models/mrp_workorder.py:657-658 | if any(wo.working_state | FACT | on button_start | — | button_start raises UserError if any workcenter is blocked | N-U53-007 |
| VDR-U53-C044 | wo cancel clean | mrp/models/mrp_workorder.py:762-764 | self.leave_id.unlink() | FACT | on cancel | — | action_cancel unlinks leave slot and closes all productivity timelines | N-U53-007 |
| VDR-U53-C045 | wo pending pause | mrp/models/mrp_workorder.py:753-754 | def button_pending(self) | FACT | on pause | — | button_pending closes current user productivity timeline | N-U53-007 |
| VDR-U53-C046 | wo plan recursive | mrp/models/mrp_workorder.py:583-596 | self.ensure_one() | FACT | on _plan_workorder | — | _plan_workorder recurses on predecessor workorders first | N-U53-007 |
| VDR-U53-C047 | wo plan alternatives | mrp/models/mrp_workorder.py:599 | workcenters = self.workcenter_id | FACT | on _plan_workorder | — | Planning considers primary workcenter and all alternatives | N-U53-007 |
| VDR-U53-C048 | wo conflict detection | mrp/models/mrp_workorder.py:845-862 | self.flush_model | FACT | on _get_conflicted_workorder_ids | — | Conflict detection uses PostgreSQL OVERLAPS on date_start/date_finished | N-U53-007 |
| VDR-U53-C049 | wo MO date propagation | mrp/models/mrp_workorder.py:527-537 | # finished date of the last WO is update. | FACT | on write | — | First WO date_start propagated to MO; last WO date_finished propagated | N-U53-007 |
| VDR-U53-C050 | wo duration formula | mrp/models/mrp_workorder.py:835-836 | time_cycle = self.operation_id.time_cycle | FACT | computed | — | Duration expected = setup + cleanup + cycles × time_cycle × 100 / efficiency | N-U53-007 |
| VDR-U53-C051 | wc model name | mrp/models/mrp_workcenter.py:22 | `_name = 'mrp.workcenter'` | FACT | always | — | Workcenter model _name is mrp.workcenter | N-U53-008 |
| VDR-U53-C052 | wc resource mixin | mrp/models/mrp_workcenter.py:25 | `_inherit = ['mail.thread', 'resource.mixin']` | FACT | always | — | Workcenter inherits resource.mixin; links to resource_id | N-U53-008 |
| VDR-U53-C053 | wc material resource | mrp/models/mrp_workcenter.py:296-300 | `records = super(MrpWorkcenter, self.with_context(default_resource_type='material')).create(vals_list)` | FACT | on create | — | Workcenter created with resource_type='material' | N-U53-008 |
| VDR-U53-C054 | wc oee field | mrp/models/mrp_workcenter.py:64 | `oee = fields.Float(compute='_compute_oee', help='Overall Equipment Effectiveness, based on the last month')` | FACT | always | — | OEE field computed over last month | N-U53-008 |
| VDR-U53-C055 | wc oee formula | mrp/models/mrp_workcenter.py:264-265 | `workcenter.oee = float_round(productive_time * 100.0 / (productive_time + blocked_time), precision_digits=2)` | FACT | computed | — | OEE = productive_time * 100 / (productive_time + blocked_time) | N-U53-008 |
| VDR-U53-C056 | wc working state | mrp/models/mrp_workcenter.py:212-218 | workcenter.working_state = 'normal | FACT | computed | — | working_state driven by open productivity record loss_type | N-U53-008 |
| VDR-U53-C057 | wc capacity method | mrp/models/mrp_workcenter.py:427-437 | `def _get_capacity(self, product, unit, default_capacity=1):` | FACT | always | — | _get_capacity returns (capacity, setup, cleanup) tuple | N-U53-008 |
| VDR-U53-C058 | wc first slot | mrp/models/mrp_workcenter.py:339 | def _get_first_available_slot | FACT | always | — | First available slot method; forward and backward modes | N-U53-008 |
| VDR-U53-C059 | wc max iterations | mrp/models/mrp_workcenter.py:356 | `max_planning_iterations = max(int(ICP.get_param('mrp.workcenter_max_planning_iterations', '50')), 1)` | FACT | on slot search | — | Max planning iterations from ir.config_parameter, default 50 (700 days) | N-U53-008 |
| VDR-U53-C060 | wc unblock | mrp/models/mrp_workcenter.py:287-293 | def unblock(self) | FACT | on unblock | — | unblock() closes all open productivity timelines on the workcenter | N-U53-008 |
| VDR-U53-C061 | wc alternative guard | mrp/models/mrp_workcenter.py:90-94 | @api.constrains('alternative_workcenter_ids') | FACT | always | — | Workcenter cannot be alternative of itself | N-U53-008 |
| VDR-U53-C062 | routing model name | mrp/models/mrp_routing.py:9 | `_name = 'mrp.routing.workcenter'` | FACT | always | — | Routing operation model _name is mrp.routing.workcenter | N-U53-009 |
| VDR-U53-C063 | routing inherits mail | mrp/models/mrp_routing.py:12 | `_inherit = ['mail.thread', 'mail.activity.mixin']` | FACT | always | — | Routing operation inherits mail.thread and mail.activity.mixin | N-U53-009 |
| VDR-U53-C064 | routing time modes | mrp/models/mrp_routing.py:27-29 | time_mode = fields.Selection | FACT | always | — | time_mode is either Fixed (manual) or Computed (auto) | N-U53-009 |
| VDR-U53-C065 | routing auto cycle | mrp/models/mrp_routing.py:82-102 | data = self.env['mrp.workorder'].search | FACT | computed | — | Auto time_cycle computed from last N (time_mode_batch) done workorders | N-U53-009 |
| VDR-U53-C066 | routing dep cyclic | mrp/models/mrp_routing.py:138-141 | @api.constrains('blocked_by_operation_ids') | FACT | always | — | Cyclic operation dependencies raise ValidationError | N-U53-009 |
| VDR-U53-C067 | routing bom cascade | mrp/models/mrp_routing.py:23-24 | bom_id = fields.Many2one | FACT | always | — | Operation deleted when BoM deleted (cascade) | N-U53-009 |
| VDR-U53-C068 | routing cost mode | mrp/models/mrp_routing.py:60-64 | cost_mode = fields.Selection | FACT | always | — | Cost mode: actual time tracking vs estimated (theorical) | N-U53-009 |
| VDR-U53-C069 | routing create outdated | mrp/models/mrp_routing.py:144-147 | `res.bom_id.with_context(skip_bom_outdated_unmark=True)._set_outdated_bom_in_productions()` | FACT | on create | — | Creating routing operation marks linked MOs as outdated | N-U53-009 |
| VDR-U53-C070 | routing skip line | mrp/models/mrp_routing.py:198-209 | def _skip_operation_line | FACT | always | — | _skip_operation_line checks variant attribute match | N-U53-009 |
| VDR-U53-C071 | unbuild model | mrp/models/mrp_unbuild.py:12 | `_name = 'mrp.unbuild'` | FACT | always | — | Unbuild model _name is mrp.unbuild | N-U53-010 |
| VDR-U53-C072 | unbuild states | mrp/models/mrp_unbuild.py:79-81 | state = fields.Selection | FACT | always | — | Unbuild has only draft and done states | N-U53-010 |
| VDR-U53-C073 | unbuild seq | mrp/models/mrp_unbuild.py:132-136 | `vals['name'] = self.env['ir.sequence'].next_by_code('mrp.unbuild')` | FACT | on create | — | Reference auto-assigned from ir.sequence code mrp.unbuild | N-U53-010 |
| VDR-U53-C074 | unbuild mo state | mrp/models/mrp_unbuild.py:173-174 | if self.mo_id and self.mo_id.state != 'done | FACT | on action_unbuild | — | Can only unbuild from a done manufacturing order | N-U53-010 |
| VDR-U53-C075 | unbuild factor | mrp/models/mrp_unbuild.py:257 | `factor = unbuild.product_qty / unbuild.mo_id.product_uom_id._compute_quantity(unbuild.mo_id.qty_produced, unbuild.product_uom_id)` | FACT | on action_unbuild | — | Component quantities proportioned by unbuild_qty / mo_qty_produced | N-U53-010 |
| VDR-U53-C076 | unbuild lot tracking | mrp/models/mrp_unbuild.py:215-217 | if move in produce_moves and self.lot_id | FACT | on action_unbuild | — | Lot filtering uses produce_line_ids cross-reference; excludes previously unbuilt lots | N-U53-010 |
| VDR-U53-C077 | unbuild putaway | mrp/models/mrp_unbuild.py:230 | `unbuild_move_line._apply_putaway_strategy()` | FACT | on action_unbuild | — | Putaway strategy applied to each unbuild move line | N-U53-010 |
| VDR-U53-C078 | unbuild chatter | mrp/models/mrp_unbuild.py:241-249 | unbuild_msg = _ | FACT | on action_unbuild | — | Chatter note posted on MO on successful unbuild | N-U53-010 |
| VDR-U53-C079 | unbuild qty positive | mrp/models/mrp_unbuild.py:83-86 | _qty_positive = models.Constraint | FACT | always | — | DB constraint enforces positive unbuild quantity | N-U53-010 |
| VDR-U53-C080 | unbuild delete guard | mrp/models/mrp_unbuild.py:138-141 | @api.ondelete(at_uninstall=False) | FACT | on unlink | — | Done unbuild orders cannot be deleted | N-U53-010 |
| VDR-U53-C081 | unbuild insufficient qty | mrp/models/mrp_unbuild.py:320-342 | def action_validate(self) | FACT | on action_validate | — | Insufficient quantity opens stock.warn.insufficient.qty.unbuild wizard | N-U53-010 |
| VDR-U53-C082 | change_qty wizard | mrp/wizard/change_production_qty.py:57 | `def change_prod_qty(self):` | FACT | always | — | change_production_qty wizard updates raw moves, finished moves, and work order durations | N-U53-011 |
| VDR-U53-C083 | change_qty factor | mrp/wizard/change_production_qty.py:64 | `factor = new_production_qty / old_production_qty` | FACT | on change | — | Proportional factor applied to all component moves | N-U53-011 |
| VDR-U53-C084 | change_qty wo update | mrp/wizard/change_production_qty.py:85 | `wo.duration_expected = wo._get_duration_expected(ratio=new_production_qty / old_production_qty)` | FACT | on change | — | Work order duration_expected updated proportionally | N-U53-011 |
| VDR-U53-C085 | change_qty scheduler | mrp/wizard/change_production_qty.py:107 | `self.mo_id.filtered(lambda mo: mo.state in ['confirmed', 'progress']).move_raw_ids._trigger_scheduler()` | FACT | on change | — | Scheduler triggered on raw moves after qty change | N-U53-011 |
| VDR-U53-C086 | backorder wizard | mrp/wizard/mrp_production_backorder.py:16 | `_name = 'mrp.production.backorder'` | FACT | always | — | Backorder wizard handles per-MO to_backorder decision | N-U53-011 |
| VDR-U53-C087 | backorder action | mrp/wizard/mrp_production_backorder.py:38-43 | def action_backorder(self) | FACT | on confirm | — | Backorder creation driven by mo_ids_to_backorder context key | N-U53-011 |
| VDR-U53-C088 | split wizard | mrp/wizard/mrp_production_split.py:15 | `_name = 'mrp.production.split'` | FACT | always | — | Split wizard computes num_splits from max_batch_size | N-U53-011 |
| VDR-U53-C089 | split batch_size | mrp/wizard/mrp_production_split.py:35-36 | `wizard.max_batch_size = bom_id.batch_size if bom_id.enable_batch_size else wizard.product_qty` | FACT | computed | — | Batch size taken from BoM if enable_batch_size; else full qty | N-U53-011 |
| VDR-U53-C090 | consumption warning | mrp/wizard/mrp_consumption_warning.py:9 | `_name = 'mrp.consumption.warning'` | FACT | always | — | Consumption warning wizard surfaces deviation from BoM quantities | N-U53-011 |
| VDR-U53-C091 | consumption confirm | mrp/wizard/mrp_consumption_warning.py:33-35 | ctx = dict(self.env.context) | FACT | on confirm | — | User confirmation passes skip_consumption=True to bypass further check | N-U53-011 |
| VDR-U53-C092 | serial wizard | mrp/wizard/mrp_production_serial_numbers.py:8 | `_name = 'mrp.production.serials'` | FACT | always | — | Serial number assignment wizard for tracked products | N-U53-011 |
| VDR-U53-C093 | serial split | mrp/wizard/mrp_production_serial_numbers.py:53-61 | def action_split_and_assign_serials(self) | FACT | on action | — | Split-and-assign creates 1 MO per serial number | N-U53-011 |
| VDR-U53-C094 | expiry pre_button | mrp_product_expiry/models/mrp_production.py:10 | `def pre_button_mark_done(self):` | FACT | always | — | pre_button_mark_done overridden to check expired lots before MO finalization | N-U53-012 |
| VDR-U53-C095 | expiry alert field | mrp_product_expiry/models/mrp_production.py:21 | `expired_lot_ids = self.move_raw_ids.move_line_ids.filtered(lambda ml: ml.lot_id.product_expiry_alert).lot_id.ids` | FACT | on pre_button | — | product_expiry_alert field on stock.lot used to identify expired components | N-U53-012 |
| VDR-U53-C096 | expiry skip key | mrp_product_expiry/models/mrp_production.py:19 | if self.env.context.get('skip_expired') | FACT | with context | — | Context key skip_expired bypasses expiry check | N-U53-012 |
| VDR-U53-C097 | expiry wizard model | mrp_product_expiry/wizard/confirm_expiry.py:7 | class ExpiryPickingConfirmation | FACT | always | — | expiry.picking.confirmation wizard extended for MO context | N-U53-012 |
| VDR-U53-C098 | expiry wo field | mrp_product_expiry/wizard/confirm_expiry.py:11 | `workorder_id = fields.Many2one('mrp.workorder', readonly=True)` | FACT | always | — | Wizard has workorder_id field for work order expiry confirmation | N-U53-012 |
| VDR-U53-C099 | expiry confirm produce | mrp_product_expiry/wizard/confirm_expiry.py:36-38 | ctx = dict(self.env.context, skip_expired=True) | FACT | on confirm | — | confirm_produce sets skip_expired and calls button_mark_done | N-U53-012 |
| VDR-U53-C100 | expiry confirm workorder | mrp_product_expiry/wizard/confirm_expiry.py:40-43 | def confirm_workorder(self) | FACT | on confirm | — | confirm_workorder calls record_production on workorder with skip_expired | N-U53-012 |
| VDR-U53-C101 | landed cost override | mrp_subcontracting_landed_costs/models/stock_landed_cost.py:10 | `def _get_targeted_move_ids(self):` | FACT | always | — | _get_targeted_move_ids overridden to redirect subcontract moves | N-U53-013 |
| VDR-U53-C102 | landed subcontract check | mrp_subcontracting_landed_costs/models/stock_landed_cost.py:13-14 | for move in res | FACT | always | — | Subcontract moves replaced by their originating moves (move_orig_ids) | N-U53-013 |
| VDR-U53-C103 | landed non-subcontract | mrp_subcontracting_landed_costs/models/stock_landed_cost.py:15-16 | target_moves_ids.update(move.move_orig_ids.ids) | FACT | always | — | Non-subcontract moves pass through unchanged | N-U53-013 |
| VDR-U53-C104 | landed orderedset | mrp_subcontracting_landed_costs/models/stock_landed_cost.py:4 | `from odoo.tools import OrderedSet` | FACT | always | — | OrderedSet used for ordered deduplication of move IDs | N-U53-013 |
| VDR-U53-C105 | landed auto-install | mrp_subcontracting_landed_costs/__manifest__.py:17 | `'auto_install': True` | FACT | always | — | Landed costs module auto-installs when stock_landed_costs + mrp_subcontracting both installed | N-U53-013 |
| VDR-U53-C106 | repair bridge manifest | mrp_subcontracting_repair/__manifest__.py:11-14 | 'depends': | FACT | always | — | Repair bridge depends on mrp_subcontracting and repair | N-U53-014 |
| VDR-U53-C107 | repair bridge auto | mrp_subcontracting_repair/__manifest__.py:15 | `'auto_install': True` | FACT | always | — | mrp_subcontracting_repair auto-installs when dependencies present | N-U53-014 |
| VDR-U53-C108 | repair bridge no python | mrp_subcontracting_repair/__manifest__.py:16 | 'author': 'Odoo S.A.' | FACT | always | — | No Python model overrides in this revision; module is manifest and data only | N-U53-014 |
| VDR-U53-C109 | wc performance metric | mrp/models/mrp_workcenter.py:269-280 | def _compute_performance(self) | FACT | computed | — | Performance = expected duration * 100 / actual duration (last month done WOs) | N-U53-008 |
| VDR-U53-C110 | wo replan action | mrp/models/mrp_workorder.py:766-773 | def action_replan(self) | FACT | on action | — | action_replan replans all ready/blocked WOs on linked productions | N-U53-007 |
| VDR-U53-C111 | wo scrap action | mrp/models/mrp_workorder.py:776-789 | def button_scrap(self) | FACT | always | — | button_scrap opens stock.scrap wizard with workorder_id and production_id context | N-U53-007 |
| VDR-U53-C112 | wo progress | mrp/models/mrp_workorder.py:412-420 | @api.depends('duration | FACT | computed | — | Progress 100 when done; otherwise actual/expected * 100 | N-U53-006 |
| VDR-U53-C113 | wo set_duration split | mrp/models/mrp_workorder.py:393 | _prepare_timeline_vals | FACT | on duration set | — | Duration set splits timeline into productive and performance (reduced speed) records | N-U53-006 |
| VDR-U53-C114 | wo qty_ready | mrp/models/mrp_workorder.py:250-262 | def _compute_qty_ready(self) | FACT | computed | — | qty_ready limited by minimum produced across predecessor workorders | N-U53-006 |
| VDR-U53-C115 | wo cost calc | mrp/models/mrp_workorder.py:638-654 | `def _cal_cost(self, date=False):` | FACT | always | — | _cal_cost uses actual time or duration_expected depending on cost_mode | N-U53-006 |
| VDR-U53-C116 | consumption set_qty | mrp/wizard/mrp_consumption_warning.py:37-76 | `def action_set_qty(self):` | FACT | on action | — | action_set_qty resets consumed to expected; creates missing stock moves if needed | N-U53-011 |
| VDR-U53-C117 | serial dedup | mrp/wizard/mrp_production_serial_numbers.py:40-41 | `self.serial_numbers = '\n'.join(list(dict.fromkeys(lot_names)))` | FACT | on change | — | Serial numbers deduplicated preserving order via dict.fromkeys | N-U53-011 |
| VDR-U53-C118 | expiry multi lot msg | mrp_product_expiry/wizard/confirm_expiry.py:23-27 | else | FACT | computed | — | Multi-lot expiry shows generic message without listing lot names | N-U53-012 |
| VDR-U53-C119 | expiry single lot msg | mrp_product_expiry/wizard/confirm_expiry.py:28-33 | "\nDo you confirm you want to proceed? | FACT | computed | — | Single lot expiry shows product name and lot name in message | N-U53-012 |
| VDR-U53-C120 | wc kanban load | mrp/models/mrp_workcenter.py:134-150 | def _get_workcenter_load_per_week | FACT | computed | — | Kanban dashboard shows weekly load (expected duration sum) for active WOs | N-U53-008 |
| VDR-U53-C121 | mail_plugin translations | mail_plugin/controllers/mail_plugin.py:449-466 | def _translation_modules_whitelist(self) | FACT | always | — | Translation route fetches UI strings for plugin modules; extensible via _translation_modules_whitelist | N-U53-003 |
| VDR-U53-C122 | wc demo data | mrp/models/mrp_workcenter.py:137-141 | has_workorder = | OBSERVATION | when no workorders | — | Random demo data injected in kanban graph when no workorders exist | N-U53-008 |
| VDR-U53-C123 | wo json popover | mrp/models/mrp_workorder.py:189-235 | def _compute_json_popover(self) | FACT | computed | — | json_popover field drives scheduling conflict/warning popover in Gantt view | N-U53-006 |
| VDR-U53-C124 | routing copy_to_bom | mrp/models/mrp_routing.py:172-183 | def copy_to_bom(self) | FACT | on action | — | copy_to_bom action copies selected operations to a target BoM from context | N-U53-009 |
| VDR-U53-C125 | wo blocked_by state | mrp/models/mrp_workorder.py:152-160 | def _compute_state(self) | FACT | computed | — | State transitions blocked/ready driven by qty_ready > 0 | N-U53-006 |
