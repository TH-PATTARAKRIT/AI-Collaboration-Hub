# U86 — CRM Lead Full Pipeline (L4/L5)
**Unit**: U86
**Phase**: Second-Pass Depth Closure — P2 Supporting Domains
**Scope**: crm.lead states, lead→opportunity, won/lost, CRM→sale.order linkage, analytic propagation
**Modules**: crm, sale_crm
**Function-IDs targeted**: NEW:U86-F01 through U86-F22
**L-levels**: L4, L5
**Proof layers**: P4
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: U18, U38

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U86-001 | U86-F01 | crm/models/crm_lead.py:85 | `_name = 'crm.lead'` | DEF | always | | The CRM lead model is named crm.lead | NR-U86-001 |
| U86-002 | U86-F01 | crm/models/crm_lead.py:123 | `('lead', 'Lead'), ('opportunity'` | SCHEMA | always | | crm.lead.type is a Selection field with values 'lead' and 'opportunity'; default is 'lead' when group_use_lead is active, else 'opportunity' | NR-U86-002 |
| U86-003 | U86-F01 | crm/models/crm_lead.py:130 | `'crm.stage', string='Stage'` | SCHEMA | always | | crm.lead.stage_id is a Many2one to crm.stage; domain restricts to team_ids=False or team_ids in team_id | NR-U86-003 |
| U86-004 | U86-F01 | crm/models/crm_lead.py:222 | `'Probability', aggregator="avg"` | SCHEMA | always | | crm.lead.probability is a Float field computed by _compute_probabilities (PLS naive Bayes); stored; user-editable | NR-U86-004 |
| U86-005 | U86-F01 | crm/models/crm_lead.py:225 | `'Automated Probability', compute` | SCHEMA | always | | crm.lead.automated_probability is a Float field computed by the same PLS method; read-only | NR-U86-005 |
| U86-006 | U86-F01 | crm/models/crm_lead.py:228 | `won_status = fields.Selection` | SCHEMA | always | | crm.lead.won_status is a Selection [won, lost, pending] computed and stored, tracking=70 | NR-U86-006 |
| U86-007 | U86-F02 | crm/models/crm_lead.py:613 | `@api.depends('active', 'probabili` | TRIGGER | always | | _compute_won_status depends on active, probability, stage_id | NR-U86-007 |
| U86-008 | U86-F02 | crm/models/crm_lead.py:615 | `lead.probability == 100 and lead.stage_id.is_won` | CALC | probability==100 and stage_id.is_won | | won_status='won' when probability==100 AND stage_id.is_won is True | NR-U86-008 |
| U86-009 | U86-F02 | crm/models/crm_lead.py:617 | `not lead.active and lead.probability == 0` | CALC | not active and probability==0 | | won_status='lost' when active=False AND probability==0 | NR-U86-009 |
| U86-010 | U86-F02 | crm/models/crm_lead.py:619 | `lead.won_status = 'pending'` | ASSIGN | all other cases | | won_status='pending' in all other states (active opportunity in pipeline) | NR-U86-010 |
| U86-011 | U86-F03 | crm/models/crm_lead.py:1121 | `def action_set_lost(self, **additio` | DEF | always | | action_set_lost() implements lost semantic | NR-U86-011 |
| U86-012 | U86-F03 | crm/models/crm_lead.py:1123 | `res = self.action_archive()` | CALL | always | | action_set_lost calls action_archive() to set active=False | NR-U86-012 |
| U86-013 | U86-F03 | crm/models/crm_lead.py:1124 | `'probability': 0, 'automated_probability': 0` | ASSIGN | always | | action_set_lost writes probability=0 and automated_probability=0; accepts **additional_values (e.g. lost_reason_id) | NR-U86-013 |
| U86-014 | U86-F04 | crm/models/crm_lead.py:1127 | `def action_set_won(self):` | DEF | always | | action_set_won() implements won semantic | NR-U86-014 |
| U86-015 | U86-F04 | crm/models/crm_lead.py:1129 | `self.action_unarchive()` | CALL | always | | action_set_won calls action_unarchive() first (restores active=True) | NR-U86-015 |
| U86-016 | U86-F04 | crm/models/crm_lead.py:1133 | `won_stages = self._stage_find(domain=[('is_won', '=', True)]` | CALL | always | | action_set_won finds won stages via _stage_find; selects closest by sequence | NR-U86-016 |
| U86-017 | U86-F04 | crm/models/crm_lead.py:1150 | `leads.write({'stage_id': won_stage_id.id, 'probability': 100}` | ASSIGN | always | | action_set_won writes stage_id to won stage and probability=100 | NR-U86-017 |
| U86-018 | U86-F05 | crm/models/crm_lead.py:1833 | `def _convert_opportunity_data(self` | DEF | always | | _convert_opportunity_data() extracts values for lead→opportunity conversion | NR-U86-018 |
| U86-019 | U86-F05 | crm/models/crm_lead.py:1839 | `'type': 'opportunity',` | ASSIGN | always | | _convert_opportunity_data sets type='opportunity' and date_conversion=now | NR-U86-019 |
| U86-020 | U86-F06 | crm/models/crm_lead.py:1850 | `def convert_opportunity(self, partner` | DEF | always | | convert_opportunity() is the public method for lead→opportunity conversion; skips if not active or already won | NR-U86-020 |
| U86-021 | U86-F06 | crm/models/crm_lead.py:1853 | `if not lead.active or lead.won_status == 'won':` | GUARD | won or archived | | convert_opportunity skips leads that are inactive or already won | NR-U86-021 |
| U86-022 | U86-F07 | crm/models/crm_lead.py:104 | `'res.users', string='Salesperson'` | SCHEMA | always | | user_id is Many2one res.users, default=env.user, check_company=True, index=True, tracking=True | NR-U86-022 |
| U86-023 | U86-F07 | crm/models/crm_lead.py:111 | `'crm.team', string='Sales Team'` | SCHEMA | always | | team_id is Many2one crm.team, check_company=True, computed+stored from user_id | NR-U86-023 |
| U86-024 | U86-F07 | crm/models/crm_lead.py:141 | `'Expected Revenue', currency_field` | SCHEMA | always | | expected_revenue is Monetary, currency_field=company_currency, tracking=True, default=0.0 | NR-U86-024 |
| U86-025 | U86-F07 | crm/models/crm_lead.py:171 | `'res.partner', string='Contact'` | SCHEMA | always | | partner_id is Many2one res.partner, check_company=True, index=True, tracking=10 | NR-U86-025 |
| U86-026 | U86-F08 | crm/models/crm_lead.py:843 | `vals.update({'active': True, 'probability': 100, 'automated_probability': 100}` | ASSIGN | stage.is_won during write | | On write() when new stage.is_won=True, vals is augmented with active=True, probability=100, automated_probability=100 | NR-U86-026 |
| U86-027 | U86-F08 | crm/models/crm_lead.py:856 | `if vals.get('probability', 0) >= 100 or not vals.get('active', True):` | GUARD | probability>=100 or deactivation | | write() sets date_closed=Datetime.now() when probability>=100 or active=False | NR-U86-027 |
| U86-028 | U86-F09 | crm/models/crm_stage.py:27 | `is_won = fields.Boolean('Is Won Stage?'` | SCHEMA | always | | crm.stage.is_won is a Boolean field marking a stage as the won stage | NR-U86-028 |
| U86-029 | U86-F09 | crm/models/crm_stage.py:55 | `def write(self, vals):` | OVERRIDE | is_won in vals | | crm.stage.write() override: when is_won changes, updates all leads in affected stages to probability=100 or recomputes probabilities | NR-U86-029 |
| U86-030 | U86-F10 | sale_crm/models/crm_lead.py:7 | `_inherit = 'crm.lead'` | INHERIT | always | | sale_crm module extends crm.lead | NR-U86-030 |
| U86-031 | U86-F10 | sale_crm/models/crm_lead.py:13 | `order_ids = fields.One2many('sale.order', 'opportunity_id'` | SCHEMA | always | | crm.lead.order_ids is a One2many to sale.order via opportunity_id inverse field | NR-U86-031 |
| U86-032 | U86-F10 | sale_crm/models/crm_lead.py:10 | `sale_amount_total = fields.Monetary(compute='_compute_sale_data'` | SCHEMA | always | | sale_crm adds sale_amount_total, quotation_count, sale_order_count computed fields on crm.lead | NR-U86-032 |
| U86-033 | U86-F11 | sale_crm/models/sale_order.py:10 | `opportunity_id = fields.Many2one` | SCHEMA | always | | sale.order gains opportunity_id Many2one to crm.lead via sale_crm module; index=btree_not_null | NR-U86-033 |
| U86-034 | U86-F11 | sale_crm/models/sale_order.py:12 | `domain="[('type', '=', 'opportunity')` | CONFIG | always | | opportunity_id domain restricts to type='opportunity' records only | NR-U86-034 |
| U86-035 | U86-F12 | sale_crm/models/crm_lead.py:35 | `def action_new_quotation(self):` | DEF | always | | action_new_quotation() creates a new sale.order quotation linked to the lead | NR-U86-035 |
| U86-036 | U86-F12 | sale_crm/models/crm_lead.py:37 | `action['context'] = self._prepare_opportunity_quotation_context()` | CALL | always | | action_new_quotation builds context via _prepare_opportunity_quotation_context() | NR-U86-036 |
| U86-037 | U86-F13 | sale_crm/models/crm_lead.py:77 | `def _prepare_opportunity_quotation_context(self):` | DEF | always | | _prepare_opportunity_quotation_context() sets default_opportunity_id, default_partner_id, default_campaign_id, default_medium_id, default_source_id, default_origin on the new quotation | NR-U86-037 |
| U86-038 | U86-F13 | sale_crm/models/crm_lead.py:82 | `'default_opportunity_id': self.id,` | ASSIGN | always | | Quotation context passes default_opportunity_id=self.id linking SO to lead | NR-U86-038 |
| U86-039 | U86-F14 | sale_crm/models/sale_order.py:14 | `def action_confirm(self):` | OVERRIDE | always | | sale_crm overrides SaleOrder.action_confirm(); after confirming calls opportunity_id._update_revenues_from_so(order) | NR-U86-039 |
| U86-040 | U86-F14 | sale_crm/models/crm_lead.py:103 | `def _update_revenues_from_so(self, order):` | DEF | always | | _update_revenues_from_so() updates expected_revenue on the opportunity if SO amount_untaxed > current expected_revenue and currency matches | NR-U86-040 |
| U86-041 | U86-F15 | crm/models/crm_lead.py:2194 | `def _pls_get_naive_bayes_probabilities` | DEF | always | | Lead scoring uses naive Bayes classifier (_pls_get_naive_bayes_probabilities); reads crm_lead_scoring_frequency table | NR-U86-041 |
| U86-042 | U86-F15 | crm/models/crm_lead.py:2646 | `def _pls_get_safe_fields(self):` | DEF | always | | PLS scoring fields are configurable via ir.config_parameter 'crm.pls_fields'; defaults include stage_id and team_id | NR-U86-042 |
| U86-043 | U86-F16 | crm/models/crm_lead.py:88 | `'mail.thread.cc',` | INHERIT | always | | crm.lead inherits mail.thread.cc, mail.thread.blacklist, mail.thread.phone, mail.activity.mixin, utm.mixin; full chatter and activity support | NR-U86-043 |
| U86-044 | U86-F16 | crm/models/crm_lead.py:153 | `date_closed = fields.Datetime('Closed Date', readonly=True` | SCHEMA | always | | date_closed is Datetime, readonly, copy=False; set automatically on won/lost events | NR-U86-044 |
| U86-045 | U86-F17 | crm/models/crm_lead.py:161 | `date_conversion = fields.Datetime('Conversion Date', readonly=True` | SCHEMA | always | | date_conversion is Datetime, readonly; set by convert_opportunity when type changes from lead to opportunity | NR-U86-045 |
| U86-046 | U86-F18 | crm/models/crm_lead.py:250 | `campaign_id = fields.Many2one(ondelete='set null'` | SCHEMA | always | | utm.mixin fields (campaign_id, medium_id, source_id) on crm.lead use ondelete='set null' | NR-U86-046 |
| U86-047 | U86-F19 | crm/models/crm_lead.py:254 | `_check_probability = models.Constraint(` | GUARD | always | | DB constraint enforces probability between 0 and 100 | NR-U86-047 |
| U86-048 | U86-F19 | crm/models/crm_lead.py:262 | `@api.constrains('probability', 'stage_id')` | GUARD | always | | _check_won_validity raises ValidationError if lead is in won stage but probability != 100 | NR-U86-048 |
| U86-049 | U86-F20 | sale_crm/models/crm_lead.py:29 | `def action_sale_quotations_new(self):` | DEF | always | | action_sale_quotations_new(): if no partner_id, opens partner selection dialog; else calls action_new_quotation() | NR-U86-049 |
| U86-050 | U86-F21 | crm/models/crm_lead.py:234 | `'crm.lost.reason', string='Lost Reason'` | SCHEMA | always | | lost_reason_id is Many2one crm.lost.reason, index=True, ondelete='restrict', tracking=71 | NR-U86-050 |
| U86-051 | U86-F22 | crm/models/crm_lead.py:1016 | `leads_reach_won_ids._pls_increment_frequencies(to_state='won'` | CALL | on won status change | | _handle_won_lost() increments PLS frequency table entries when leads transition won/lost states | NR-U86-051 |
