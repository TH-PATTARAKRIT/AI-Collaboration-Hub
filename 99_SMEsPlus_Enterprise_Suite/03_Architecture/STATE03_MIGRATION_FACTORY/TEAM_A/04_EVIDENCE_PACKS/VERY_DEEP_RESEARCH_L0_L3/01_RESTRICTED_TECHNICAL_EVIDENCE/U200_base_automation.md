# U200 — base_automation: Automated Actions / ir.actions.server Trigger Chain
## STATE03 VDR — Restricted Technical Evidence (L0–L3)

**Source tree**: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/`
**Modules**: `base_automation` (primary), `base` (`ir_actions.py`), `mail`, `sms`
**Evidence class**: RESTRICTED — line-level source pointers
**Date**: 2026-10-02

---

## 1. `base.automation` Model Definition

**File**: `base_automation/models/base_automation.py:141`

```
class BaseAutomation(models.Model):
    _name = 'base.automation'
    _description = 'Automation Rule'
    _inherit = ['mail.thread', 'mail.activity.mixin']
```

Inherits `mail.thread` and `mail.activity.mixin`, meaning automation rules have full chatter, tracking, and activity support.

---

## 2. Complete Trigger Types (v19)

**File**: `base_automation/models/base_automation.py:173–197` — `trigger` Selection field.

| Value | Label | Category |
|---|---|---|
| `on_stage_set` | Stage is set to | Write |
| `on_user_set` | User is set | Write |
| `on_tag_set` | Tag is added | Create+Write |
| `on_state_set` | State is set to | Write |
| `on_priority_set` | Priority is set to | Create+Write |
| `on_archive` | On archived | Write |
| `on_unarchive` | On unarchived | Write |
| `on_create` | On create | Create |
| `on_create_or_write` | On create and edit | Create+Write |
| `on_write` | On update (deprecated) | Write |
| `on_unlink` | On deletion | Unlink |
| `on_change` | On UI change | Onchange |
| `on_time` | Based on date field | Time |
| `on_time_created` | After creation | Time |
| `on_time_updated` | After last update | Time |
| `on_message_received` | On incoming message | Mail |
| `on_message_sent` | On outgoing message | Mail |
| `on_webhook` | On webhook | Webhook (NEW v19) |

**Trigger sets** defined at `base_automation.py:97–129`:

```python
CREATE_TRIGGERS = ['on_create', 'on_create_or_write', 'on_priority_set',
                   'on_stage_set', 'on_state_set', 'on_tag_set', 'on_user_set']

WRITE_TRIGGERS = ['on_write', 'on_archive', 'on_unarchive', 'on_create_or_write',
                  'on_priority_set', 'on_stage_set', 'on_state_set',
                  'on_tag_set', 'on_user_set']

MAIL_TRIGGERS = ("on_message_received", "on_message_sent")

TIME_TRIGGERS = ['on_time', 'on_time_created', 'on_time_updated']
```

---

## 3. `_process()` — Core Execution Method

**File**: `base_automation/models/base_automation.py:783–830`

```python
def _process(self, records, domain_post=None):
    """ Process automation ``self`` on the ``records`` that have not been done yet. """
    automation_done = self.env.context.get('__action_done', {})
    records_done = automation_done.get(self, records.browse())
    records -= records_done
    if not records:
        return
    ...
    records = records.filtered(self._check_trigger_fields)
    ...
    if records and 'date_automation_last' in records._fields:
        records.date_automation_last = self.env.cr.now()

    contexts = [
        {'active_model': record._name, 'active_ids': record.ids,
         'active_id': record.id, 'domain_post': domain_post}
        for record in records
    ]
    for action in self.sudo().action_server_ids:
        for ctx in contexts:
            try:
                action.with_context(**ctx).run()
            except Exception as e:
                self._add_postmortem(e)
                raise
```

Key behaviours:
- **Idempotency guard**: `__action_done` context dict prevents re-processing same records.
- **Trigger field check**: `_check_trigger_fields()` verifies at least one watched field changed (via `old_values` context).
- **Per-record context**: Each record gets `active_id`, `active_ids`, `active_model`, `domain_post`.
- **Raises**: exceptions are augmented with `base_automation` context then re-raised.

---

## 4. ORM Hook Registration — `_register_hook()`

**File**: `base_automation/models/base_automation.py:851–1082`

Four patched methods installed on model classes:

| ORM method patched | Trigger categories handled |
|---|---|
| `create` | `CREATE_TRIGGERS` — postcondition filter only |
| `write` | `WRITE_TRIGGERS` — pre + postcondition filter |
| `_compute_field_value` | `WRITE_TRIGGERS` — catch computed field changes |
| `unlink` | `on_unlink` — postcondition only, runs BEFORE actual unlink |
| `message_post` (mail.thread) | `MAIL_TRIGGERS` — post-message hook |
| `_onchange_methods` injection | `on_change` — per-field onchange registration |

Pattern for `write` (line 886–914):
1. Retrieve automations for `WRITE_TRIGGERS`.
2. Snapshot `pre = {a: a._filter_pre(records)}` (pre-filter before write).
3. Capture `old_values` (only stored fields mentioned in `vals`).
4. Call `write.origin(...)`.
5. For each automation: `_filter_post_export_domain(pre[automation])` then `_process(records, domain_post)`.

---

## 5. `filter_pre_domain` and `filter_domain` Semantics

**File**: `base_automation/models/base_automation.py:243–255` (field definitions), `745–771` (_filter_pre / _filter_post)

| Field | When evaluated | Purpose |
|---|---|---|
| `filter_pre_domain` | **Before** write/unlink | Must be TRUE before the change. Not checked on create. |
| `filter_domain` | **After** write/create | Must be TRUE after the change. |

Both are evaluated via `safe_eval(domain_str, self._get_eval_context())` — i.e., the domain string is evaluated as a Python expression returning a domain list, then used as `filtered_domain()`.

For `on_tag_set`, `filter_pre_domain` is auto-generated: `repr([(field, 'not in', [value])])` (line 402) — ensures the tag was NOT already present before the write.

`_filter_post_export_domain()` (line 760) also exports the resolved domain as `domain_post` for downstream context injection.

---

## 6. `ir.actions.server` — `state` Field (All Types)

**Source**: `base/models/ir_actions.py:612–629` (base states), `mail/models/ir_actions_server.py:24–38` (mail add), `sms/models/ir_actions_server.py:11–13` (SMS add).

| `state` value | Label | Source module |
|---|---|---|
| `object_write` | Update Record | `base` |
| `object_create` | Create Record | `base` |
| `object_copy` | Duplicate Record | `base` |
| `code` | Execute Code | `base` |
| `webhook` | Send Webhook Notification | `base` |
| `multi` | Multi Actions | `base` |
| `next_activity` | Create Activity | `mail` |
| `mail_post` | Send Email | `mail` |
| `followers` | Add Followers | `mail` |
| `remove_followers` | Remove Followers | `mail` |
| `sms` | Send SMS | `sms` |

**Runner dispatch** (`base/models/ir_actions.py:980–987`):
```python
def _get_runner(self):
    fn = getattr(t, f'_run_action_{self.state}_multi', None)
    if not fn:
        fn = getattr(t, f'_run_action_{self.state}', None)
    return fn, multi
```
The `_multi` suffix variant receives all `active_ids` in one call; the single variant loops per record.

---

## 7. `run()` Method — Execution Chain

**File**: `base/models/ir_actions.py:1151–1213`

```python
def run(self):
    res = False
    for action in self:
        eval_context = self._get_eval_context(action.sudo())
        records = eval_context.get('record') or eval_context['model']
        records |= eval_context.get('records') or eval_context['model']
        action._can_execute_action_on_records(records)
        res = action.sudo()._run(records, eval_context)
    return res
```

`_run()` (line 1182):
1. Checks `self.warning` — raises `ServerActionWithWarningsError` if warnings present.
2. Calls `_get_runner()` to find the correct `_run_action_{state}[_multi]` method.
3. If multi: single call with full eval_context.
4. If single: loops through `active_ids`, updating `eval_context['records']` and `eval_context['record']` per iteration.

Access check (`_can_execute_action_on_records`, line 1215):
- If `group_ids` set: user must be in one of those groups.
- Else: user must have `write` access on `model_id.model`.
- Additionally, real records checked for `write` access if no `group_ids`.

---

## 8. `_get_eval_context()` — Variables Exposed to Python Code

### 8a. Base level (`IrActionsActions`, `base/models/ir_actions.py:140–153`)
`uid`, `user`, `time`, `datetime`, `dateutil`, `timezone`, `float_compare`, `b64encode`, `b64decode`, `Command`

### 8b. `IrActionsServer` override (`base/models/ir_actions.py:1111–1148`)
Adds: `env`, `model`, `UserError`, `record` (active record), `records` (active records), `log` (insert into ir_logging), `_logger` (LoggerProxy)

### 8c. `base_automation.IrActionsServer` override (`base_automation/models/ir_actions_server.py:54–61`)
```python
def _get_eval_context(self, action=None):
    eval_context = super()._get_eval_context(action)
    if action and action.state == "code":
        eval_context['json'] = json_scriptsafe
        payload = get_webhook_request_payload()
        if payload:
            eval_context["payload"] = payload
    return eval_context
```
Adds `json` (script-safe JSON) for `code` state; adds `payload` dict if called from a webhook HTTP request.

### 8d. `base.automation._get_eval_context()` (`base_automation/models/base_automation.py:710–726`)
Used for domain evaluation (not code execution):
`datetime`, `dateutil`, `time`, `uid`, `user`, `model` [, `payload` if provided]

---

## 9. Cron-Triggered Automations

### Cron record
**File**: `base_automation/data/base_automation_data.xml:4–13`
```xml
<record id="ir_cron_data_base_automation_check" model="ir.cron">
    <field name="name">Automation Rules: check and execute</field>
    <field name="code">model._cron_process_time_based_actions()</field>
    <field name="interval_number">4</field>
    <field name="interval_type">hours</field>
    <field name="active" eval="False" />
</record>
```
Activated only when TIME_TRIGGERS automations exist (`_update_cron`, line 664).

### Frequency auto-tuning (`_get_cron_interval`, line 728–743)
```
interval = min(max(1, min_delay // 10), 4 * 60)  # minutes
```
The cron runs at 10% of the shortest automation delay, clamped between 1 minute and 4 hours.

### `_cron_process_time_based_actions()` (`base_automation.py:1183–1220`)
- Searches all active automations with `trigger in TIME_TRIGGERS`.
- Per automation: calls `_search_time_based_automation_records(until=now)`.
- Calls `_process(record)` per matching record.
- Writes `last_run = now` after processing.
- Uses `ir.cron._commit_progress()` for partial commit support.

### `_search_time_based_automation_records()` (`base_automation.py:1104–1181`)
- Computes relative date window: `[last_run + offset, now + offset]`.
- Supports calendar-based day calculation via `trg_date_calendar_id`.
- Handles `date` vs `datetime` field types.
- Handles `is_date_automation_last` fallback to `create_date` if `date_automation_last` field is empty.

---

## 10. `action_server_ids` — Multiple Chained Actions

**File**: `base_automation/models/base_automation.py:153–159`

```python
action_server_ids = fields.One2many("ir.actions.server", "base_automation_id",
    context={'default_usage': 'base_automation'},
    string="Actions",
    compute="_compute_action_server_ids",
    store=True,
    readonly=False,
)
```

- One automation rule → multiple `ir.actions.server` records (One2many via `base_automation_id` FK).
- Executed in sequence in `_process()` (line 824): `for action in self.sudo().action_server_ids`.
- Sequence controlled by `ir.actions.server.sequence` field (default 5).
- Constraint (`_check_action_server_model`, line 275): all child actions must have the same `model_id` as the rule.
- Multi-actions child actions CANNOT link to other automation rule actions (`_get_children_domain`, `base_automation/models/ir_actions_server.py:40–43`): `Domain("base_automation_id", "=", False)`.

---

## 11. Webhook Trigger (NEW in v19)

**File**: `base_automation/models/base_automation.py:161–163`, `619–662`

- `url` computed: `{base_url}/web/hook/{webhook_uuid}`.
- `record_getter` field: Python expression evaluated via `safe_eval` to find the record.
- `_execute_webhook(payload)` (line 619): evaluates `record_getter`, calls `_process(record)`.
- Default `record_getter`: `model.env[payload.get('_model')].browse(int(payload.get('_id')))`.
- Optional `log_webhook_calls` flag writes to `ir.logging`.

---

## 12. Migration Flags v16/v17 → v19

| Change | Type | Evidence |
|---|---|---|
| `on_webhook` trigger NEW | Added | `base_automation.py:196` |
| `on_message_received` / `on_message_sent` triggers (mail integration) | Added/formalized | `base_automation.py:120`, `193-194` |
| `on_archive` / `on_unarchive` triggers (separate from generic write) | Added | `base_automation.py:181-182` |
| `on_time_created` / `on_time_updated` TIME_TRIGGERS | Added/renamed | `base_automation.py:125-128` |
| `object_copy` (Duplicate Record) state | Added in base | `ir_actions.py:615` |
| `webhook` state in `ir.actions.server` | Added | `ir_actions.py:617` |
| `remove_followers` state in `ir.actions.server` | Added | `mail/ir_actions_server.py:30` |
| `action_server_ids` One2many replacing legacy `action_ids` | Renamed/restructured | `base_automation.py:153` |
| `_check` deprecated: `@api.deprecated("Since 19.0, use _cron_process_time_based_automations")` | Deprecated | `base_automation.py:1098–1102` |
| `on_write` trigger DEPRECATED (use `on_create_or_write`) | Deprecated | `base_automation.py:184` comment |
| `ir.cron._commit_progress()` in cron loop | Added (progress commits) | `base_automation.py:1217` |
| `_keep_to_compute()` context manager for computed fields | Added | `base_automation.py:57–70` |
