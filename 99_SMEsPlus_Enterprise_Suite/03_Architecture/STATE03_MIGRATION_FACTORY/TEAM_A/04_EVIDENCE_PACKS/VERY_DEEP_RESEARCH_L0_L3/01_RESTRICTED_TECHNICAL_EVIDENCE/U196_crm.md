# U196 — CRM: Lead/Opportunity Pipeline, Probability, Won/Lost, Team Assignment
**Unit:** U196 | **Group:** G05 | **Priority:** P1 | **Level:** L3  
**Source Base:** `odoo/addons/crm/` (Odoo 19.0.post20260921)  
**Prepared:** 2026-10-02

---

## 1. Model: `crm.lead` — Core Record Type

**File:** `crm/models/crm_lead.py`

### 1.1 Type Discriminator
```python
type = fields.Selection([('lead', 'Lead'), ('opportunity', 'Opportunity')],
    required=True, tracking=15, index=True,
    default=lambda self: 'lead' if self.env.user.has_group('crm.group_use_lead') else 'opportunity')
```
- A single model (`crm.lead`) handles both leads and opportunities.
- The `type` field (`lead` / `opportunity`) is the discriminator.
- Default type is `'lead'` when the user belongs to `crm.group_use_lead`; otherwise defaults to `'opportunity'`.

### 1.2 Stage
```python
stage_id = fields.Many2one('crm.stage', ...,
    domain="['|', ('team_ids', '=', False), ('team_ids', 'in', team_id)]")
```
- Stage is a `Many2one` to `crm.stage`, filtered to stages without a team assignment, or matching the lead's team.
- `_track_duration_field = 'stage_id'` — time spent per stage is tracked via `mail.tracking.duration.mixin`.
- `_compute_stage_id` resets the stage when the current stage doesn't belong to the new team.

### 1.3 Probability Fields
```python
probability = fields.Float('Probability', aggregator="avg", copy=False,
    compute='_compute_probabilities', readonly=False, store=True)
automated_probability = fields.Float('Automated Probability',
    compute='_compute_probabilities', readonly=True, store=True)
is_automated_probability = fields.Boolean(compute="_compute_is_automated_probability")
```
- `probability` is user-editable (readonly=False) but computed.
- `automated_probability` is read-only (ML-computed).
- `is_automated_probability` is True when `probability == automated_probability` (float compare to 2 decimals).

### 1.4 Won/Lost Status
```python
won_status = fields.Selection([('won','Won'),('lost','Lost'),('pending','Pending')],
    compute='_compute_won_status', store=True, tracking=70)
```
Derivation logic:
```python
def _compute_won_status(self):
    for lead in self:
        if lead.probability == 100 and lead.stage_id.is_won:
            lead.won_status = 'won'
        elif not lead.active and lead.probability == 0:
            lead.won_status = 'lost'
        else:
            lead.won_status = 'pending'
```
- **Won** = probability 100 AND stage marked as won.
- **Lost** = archived (`active=False`) AND probability 0.
- **Pending** = everything else.

### 1.5 Lost Reason
```python
lost_reason_id = fields.Many2one('crm.lost.reason', index=True, ondelete='restrict', tracking=71)
```
Stored on the lead; set when calling `action_set_lost()`.

### 1.6 Revenue Fields
```python
expected_revenue = fields.Monetary(...)
prorated_revenue = fields.Monetary(compute="_compute_prorated_revenue", store=True)
recurring_revenue = fields.Monetary(...)
recurring_plan = fields.Many2one('crm.recurring.plan', ...)
recurring_revenue_monthly = fields.Monetary(compute="_compute_recurring_revenue_monthly", store=True)
recurring_revenue_monthly_prorated = fields.Monetary(compute="...", store=True)
```
Prorated revenue formula:
```python
lead.prorated_revenue = round((lead.expected_revenue or 0.0) * (lead.probability or 0) / 100.0, 2)
```
Monthly recurring revenue = `recurring_revenue / recurring_plan.number_of_months`.  
Prorated MRR = `recurring_revenue_monthly * probability / 100`.

### 1.7 Key Date Fields
| Field | Description |
|---|---|
| `date_closed` | Set when probability >= 100 or when `active=False`; cleared when probability > 0 |
| `date_open` | Set when a salesperson is first assigned |
| `date_conversion` | Set when a lead is converted to an opportunity |
| `date_last_stage_update` | Updated on every stage change |
| `date_deadline` | Expected closing date (user-editable) |

`date_closed` is managed in the `write()` override:
```python
if vals.get('probability', 0) >= 100 or not vals.get('active', True):
    vals['date_closed'] = fields.Datetime.now()
elif vals.get('probability', 0) > 0:
    vals['date_closed'] = False
```

### 1.8 Priority (Lead Scoring)
```python
priority = fields.Selection(crm_stage.AVAILABLE_PRIORITIES, string='Priority', index=True,
    default=crm_stage.AVAILABLE_PRIORITIES[0][0])
```
Values from `crm_stage.py`:
```python
AVAILABLE_PRIORITIES = [('0', 'Low'), ('1', 'Medium'), ('2', 'High'), ('3', 'Very High')]
```
- Default is `'0'` (Low).
- `color = fields.Integer('Color Index', default=0)` — UI kanban color, integer 0–11.

---

## 2. Probability Computation — PLS (Predictive Lead Scoring)

**Method:** `_compute_probabilities()` — triggered by `['stage_id', 'team_id'] + _pls_get_safe_fields()`

```python
def _compute_probabilities(self):
    lead_probabilities, _unused = self._pls_get_naive_bayes_probabilities()
    for lead in self:
        if lead.id in lead_probabilities:
            was_automated = lead.active and lead.is_automated_probability
            lead.automated_probability = lead_probabilities[lead.id]
            if was_automated:
                lead.probability = lead.automated_probability
```

### 2.1 Naive Bayes Algorithm
`_pls_get_naive_bayes_probabilities()` implements a Naive Bayes Classifier (NBC):

> P(Won | A∩B) ∝ P(A∩B | Won) * P(Won)  
> Probability = S(Won | conditions) / (S(Won | conditions) + S(Lost | conditions))

- A **frequency table** (`crm.lead.scoring.frequency`) stores won/lost counts per field-value pair, scoped by `team_id`.
- Zero-frequency problem is mitigated by adding `0.1` to all frequency counts.
- Fields included in PLS are configurable via `ir.config_parameter` key `crm.pls_fields` (comma-separated list, validated against actual model fields).
- A start date parameter `crm.pls_start_date` constrains the historical data window.

### 2.2 No External IAP Gate
- The `iap_tools` import is used only for `mail_prepare_for_domain_search()` (email domain deduplication), NOT to gate probability computation.
- PLS is entirely internal; there is no `iap_crm_ml` module in Community Odoo 19.

### 2.3 Frequency Table — Stage Increment Logic
For a **won** lead: all stage IDs are incremented.  
For a **lost** lead: only current stage + all prior stages (lower sequence) are incremented.

### 2.4 Live vs Rebuild
- **Live Increment**: triggered by `_handle_won_lost()` on every won/lost transition.
- **Cron Rebuild**: `_cron_update_automated_probabilities()` — rebuilds frequency table from all historical won/lost.

---

## 3. Won / Lost State Transitions

### 3.1 `action_set_won()`
```python
def action_set_won(self):
    self.action_unarchive()
    leads_by_won_stage = {}
    for lead in self:
        won_stages = self._stage_find(domain=[('is_won', '=', True)], limit=None)
        stage_id = next((stage for stage in won_stages if stage.sequence > lead.stage_id.sequence), None)
        if not stage_id:
            stage_id = next((stage for stage in reversed(won_stages) if stage.sequence <= lead.stage_id.sequence), won_stages)
        ...
    for won_stage_id, leads in leads_by_won_stage.items():
        leads.write({'stage_id': won_stage_id.id, 'probability': 100})
    return True
```
- Finds the nearest won stage (by sequence proximity to current stage).
- Sets `stage_id` to a won stage + `probability = 100`.
- `date_closed` is set automatically via `write()` override when `probability >= 100`.
- Calls `action_unarchive()` first (in case the lead was archived).

### 3.2 `action_set_lost()`
```python
def action_set_lost(self, **additional_values):
    res = self.action_archive()
    self.write({**additional_values, 'probability': 0, 'automated_probability': 0})
    return res
```
- Archives the lead (`active = False`) + sets `probability = 0`.
- Accepts keyword args — callers pass `lost_reason_id` here.
- `date_closed` is set via `write()` because `active=False`.

### 3.3 Restore / Unarchive
```python
def action_restore(self):
    self.action_unarchive()
    for lead in self:
        lead.probability = lead.automated_probability
```
- Reactivates, clears `lost_reason_id` (via `action_unarchive()`), resyncs probability to automated value.

### 3.4 Won Stage Constraint
```python
@api.constrains('probability', 'stage_id')
def _check_won_validity(self):
    for lead in self:
        if lead.stage_id.is_won and lead.probability != 100:
            raise ValidationError(...)
```
- A lead in a won stage MUST have probability = 100.

---

## 4. `crm.stage` Model

**File:** `crm/models/crm_stage.py`

```python
class CrmStage(models.Model):
    _name = 'crm.stage'
    _order = "sequence, name, id"

    name = fields.Char('Stage Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=1)
    is_won = fields.Boolean('Is Won Stage?')
    rotting_threshold_days = fields.Integer('Days to rot', default=0)
    requirements = fields.Text('Requirements')
    team_ids = fields.Many2many('crm.team', string='Sales Teams', ondelete='restrict')
    fold = fields.Boolean('Folded in Pipeline')
    color = fields.Integer(string='Color')
```

- Stages are shared by default (`team_ids` empty = global). Team-specific stages have `team_ids` set.
- `is_won = True` makes the stage a "won" stage; only one or a few stages typically carry this flag.
- `write()` override: when `is_won` changes to `True`, sets all leads in those stages to `probability = 100`. When changed from `True` to `False`, triggers `_compute_probabilities()` on those leads.
- `rotting_threshold_days`: leads not updated beyond this threshold are visually flagged.
- `_onchange_is_won()` warns users of mass probability recalculation.

---

## 5. Lead Merge — `_merge_opportunity()`

**Method:** `merge_opportunity()` → `_merge_opportunity()` (private, relaxed limits)

### 5.1 Sort by Confidence Level
```python
def opps_key(opportunity):
    return opportunity.type == 'opportunity' or opportunity.active,
           opportunity.type == 'opportunity',
           opportunity.stage_id.sequence,
           opportunity.probability,
           -opportunity._origin.id
```
Head = highest confidence (most advanced stage/type/probability/newer ID).

### 5.2 Field Merge Priority Rules
From `_merge_data()`:
- **Text** (`description`): all values concatenated with `<br/>`.
- **M2O / scalar**: first non-null wins (head record priority).
- **M2M / O2M**: skipped (not merged by default).
- **Address fields**: taken from the lead with the most populated address fields.
- **Special fields** (`_merge_get_fields_specific()`):
  - `type`: `'opportunity'` if ANY record is an opportunity.
  - `priority`: maximum value across all.
  - `tag_ids`: union of all tags.
  - `lost_reason_id`: carried only if head has `probability = 0`.

### 5.3 Post-Merge
- Tail leads' messages, activities, attachments, and calendar events are transferred to head.
- Followers active in last 30 days are transferred.
- Tail records are unlinked (sudo) when `auto_unlink=True`.
- Maximum 5 records per merge via UI (enforced; relaxed for `_merge_opportunity()` direct calls).

---

## 6. `crm.team` — Sales Team

**File:** `crm/models/crm_team.py`  
**Inherits:** `['mail.alias.mixin', 'crm.team']` (crm.team base defined in `sales_team`)

### 6.1 Key Fields (CRM extension)
```python
use_leads = fields.Boolean('Leads')
use_opportunities = fields.Boolean('Pipeline', default=True)
alias_id = fields.Many2one(help="Email address for inbound lead creation")
assignment_enabled = fields.Boolean(compute='_compute_assignment_enabled')
assignment_auto_enabled = fields.Boolean(compute='_compute_assignment_enabled')
assignment_optout = fields.Boolean('Skip auto assignment')
assignment_max = fields.Integer('Lead Average Capacity', compute='_compute_assignment_max')
assignment_domain = fields.Char('Assignment Domain')
lead_properties_definition = fields.PropertiesDefinition('Lead Properties')
```

### 6.2 Multi-Company
From `sales_team/models/crm_team.py`:
```python
company_id = fields.Many2one('res.company', ...)
```
- `company_id` is defined on the base `crm.team` in `sales_team` module.
- `_get_default_team_id()` filters by `('company_id', 'in', [False] + active_companies)`.
- When a team has a `company_id`, leads assigned to it inherit that company: `lead.company_id = lead.team_id.company_id`.
- Members of a company-scoped team must have that company in their `company_ids`.

### 6.3 Assignment — Rule-Based
Activated by `ir.config_parameter` key `crm.lead.auto.assignment`.
```python
def _is_rule_based_assignment_activated(self):
    return self.env['ir.config_parameter'].sudo().get_param('crm.lead.auto.assignment', False)
```

### 6.4 Assignment Cron — `_cron_assign_leads()`
- Runs on all teams where `use_leads=True` or `use_opportunities=True` and `assignment_optout=False`.
- Two phases: **allocate** (`_allocate_leads`) → assign team to unowned leads; then **assign** (`_assign_and_convert_leads`) → round-robin salesperson assignment.

### 6.5 Lead Allocation (`_allocate_leads`)
- Finds unassigned leads (no `team_id`, no `user_id`, `won_status != 'won'`, created within `creation_delta_days`).
- Weighted random team selection by `assignment_max`.
- Deduplicates leads on assignment (merges duplicates before assigning).

### 6.6 Salesperson Assignment (`_assign_and_convert_leads`)
- Round-robin across members sorted by `(quota, random)` descending.
- Members with `assignment_domain_preferred` get first-pass priority leads.
- Leads sorted by descending `probability` within each pass.
- When assigned, lead is converted to opportunity via `convert_opportunity()`.

### 6.7 Manual Round-Robin (`_handle_salesmen_assignment`)
```python
for idx in range(0, steps):
    subset_ids = lead_ids[idx:len(lead_ids):steps]
    update_vals['user_id'] = user_ids[idx]
    self.env['crm.lead'].browse(subset_ids).write(update_vals)
```
- Explicitly implements round-robin for batch convert/assign.

---

## 7. Email Alias — Inbound Lead Creation

### 7.1 `_alias_get_creation_values()` on `crm.team`
```python
values['alias_model_id'] = self.env['ir.model']._get('crm.lead').id
defaults['type'] = 'lead' if has_group_use_lead and self.use_leads else 'opportunity'
defaults['team_id'] = self.id
```
- Each team can have an email alias; inbound emails create `crm.lead` records.
- Default type is `'lead'` or `'opportunity'` depending on team config.

### 7.2 `message_new()` Override on `crm.lead`
```python
@api.model
def message_new(self, msg_dict, custom_values=None):
    self = self.with_context(default_user_id=False)
    defaults = {
        'name':  msg_dict.get('subject') or _("No Subject"),
        'email_from': msg_dict.get('from'),
        'partner_id': msg_dict.get('author_id', False),
    }
    if msg_dict.get('priority') in dict(crm_stage.AVAILABLE_PRIORITIES):
        defaults['priority'] = msg_dict.get('priority')
    defaults.update(custom_values)
    new_lead = super().message_new(msg_dict, custom_values=defaults)
    new_lead._assign_userless_lead_in_team(_('incoming email'))
    return new_lead
```
- `default_user_id=False` prevents gateway user (root) being set as responsible.
- Lead name = email subject; email_from = sender; partner_id = author if known.
- Priority header (if present and valid) is mapped to CRM priority.
- After creation, `_assign_userless_lead_in_team()` assigns to team leader if rule-based assignment is off.

---

## 8. Action: `action_schedule_meeting()`

```python
def action_schedule_meeting(self, smart_calendar=True):
    action = self.env["ir.actions.actions"]._for_xml_id("calendar.action_calendar_event")
    partner_ids = self.env.user.partner_id.ids
    if self.partner_id:
        partner_ids.append(self.partner_id.id)
    current_opportunity_id = self.id if self.type == 'opportunity' else False
    action['context'] = {
        'search_default_opportunity_id': current_opportunity_id,
        'default_opportunity_id': current_opportunity_id,
        ...
    }
    if current_opportunity_id and smart_calendar:
        mode, initial_date = self._get_opportunity_meeting_view_parameters()
        action['context'].update({'default_mode': mode, 'initial_date': initial_date})
    return action
```
- Opens `calendar.action_calendar_event` with the opportunity pre-filtered.
- "Smart" calendar: picks `week` or `month` mode based on existing meetings (upcoming ones take priority over past ones).
- `opportunity_id` is only set for `type='opportunity'`; leads do not pre-filter calendar.

---

## 9. Prorated vs Expected Revenue

| Field | Formula | Use |
|---|---|---|
| `expected_revenue` | User input | Absolute deal value |
| `prorated_revenue` | `expected_revenue * probability / 100` | Weighted pipeline value |
| `recurring_revenue_monthly` | `recurring_revenue / recurring_plan.number_of_months` | MRR |
| `recurring_revenue_monthly_prorated` | `recurring_revenue_monthly * probability / 100` | Weighted MRR |

Pipeline forecast views use `prorated_revenue` to aggregate probability-weighted pipeline totals.

---

## 10. Constraint: DB Integrity
```python
_check_probability = models.Constraint(
    'check(probability >= 0 and probability <= 100)',
    'The probability of closing the deal should be between 0% and 100%!',
)
```
DB-level constraint enforced on every write.

---

## 11. Multi-Company Summary

- `crm.lead.company_id` is computed from `team_id.company_id` > `user_id.company_id` > `partner_id.company_id`.
- `crm.team.company_id` (from `sales_team`) scopes the team to a company; `False` = global.
- The team's `_get_default_team_id()` filters by active companies in context.
- `_check_company_auto = True` on `crm.lead` triggers automatic company consistency checks.
- PLS frequency table (`crm.lead.scoring.frequency`) is scoped by `team_id`, which itself may be company-scoped.
