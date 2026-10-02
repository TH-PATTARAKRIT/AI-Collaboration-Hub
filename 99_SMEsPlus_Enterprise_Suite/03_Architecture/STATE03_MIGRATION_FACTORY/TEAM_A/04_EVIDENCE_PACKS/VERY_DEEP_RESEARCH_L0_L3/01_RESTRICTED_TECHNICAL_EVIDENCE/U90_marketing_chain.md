# U90 — Mass Mailing + Event + CRM Marketing Chain (L3/L4)
**Unit**: U90
**Phase**: Second-Pass Depth Closure — P2 Supporting Domains
**Scope**: mailing.mailing state machine, event registration→CRM lead, UTM tracking, marketing_automation presence
**Modules**: mass_mailing, event, event_crm (present), marketing_automation (absent — Enterprise-only)
**Function-IDs targeted**: NEW:U90-F01 through U90-F14
**L-levels**: L3, L4
**Proof layers**: P4
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: U18, U42, U62

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U90-001 | U90-F01 | mass_mailing/models/mailing.py:38 | `_name = 'mailing.mailing'` | DEF | always | | The mass mailing model is named mailing.mailing, inheriting mail.thread, mail.activity.mixin, mail.render.mixin, and utm.source.mixin | NR-U90-001 |
| U90-002 | U90-F01 | mass_mailing/models/mailing.py:40 | `_inherit = ['mail.thread',` | INHERIT | always | | mailing.mailing inherits from four mixins: mail.thread, mail.activity.mixin, mail.render.mixin, utm.source.mixin | NR-U90-002 |
| U90-003 | U90-F02 | mass_mailing/models/mailing.py:129 | `[('draft', 'Draft'), ('in_queue', 'In Queue'),` | DEF | always | | mailing.mailing.state is a Selection field with four values: draft, in_queue, sending, done; default is draft | NR-U90-003 |
| U90-004 | U90-F02 | mass_mailing/models/mailing.py:142 | `mailing_type = fields.Selection([('mail', 'Email')]` | DEF | always | | mailing_type is a Selection field with one Community value: mail (Email); default is mail | NR-U90-004 |
| U90-005 | U90-F02 | mass_mailing/models/mailing.py:177 | `contact_list_ids = fields.Many2many('mailing.list'` | DEF | always | | contact_list_ids is a Many2many to mailing.list via mail_mass_mailing_list_rel junction table | NR-U90-005 |
| U90-006 | U90-F02 | mass_mailing/models/mailing.py:212 | `mailing_trace_ids = fields.One2many('mailing.trace'` | DEF | always | | mailing.mailing links to traces via One2many mailing_trace_ids on field mass_mailing_id of mailing.trace | NR-U90-006 |
| U90-007 | U90-F02 | mass_mailing/models/mailing.py:123 | `campaign_id = fields.Many2one('utm.campaign'` | DEF | always | | mailing.mailing carries campaign_id (utm.campaign), medium_id (utm.medium), and source_id (via utm.source.mixin) for full UTM tracking | NR-U90-007 |
| U90-008 | U90-F03 | mass_mailing/models/mailing.py:662 | `def action_put_in_queue(self):` | DEF | always | | action_put_in_queue writes state='in_queue' and triggers cron ir_cron_mass_mailing_queue at schedule_date or now | NR-U90-008 |
| U90-009 | U90-F03 | mass_mailing/models/mailing.py:670 | `def action_cancel(self):` | DEF | always | | action_cancel writes state back to draft and clears schedule_date, schedule_type, next_departure | NR-U90-009 |
| U90-010 | U90-F04 | mass_mailing/models/mailing.py:1099 | `def action_send_mail(self, res_ids=None):` | DEF | always | | Public action_send_mail is a thin wrapper delegating to _action_send_mail; used by UI and wizard flows | NR-U90-010 |
| U90-011 | U90-F04 | mass_mailing/models/mailing.py:1147 | `mailing.write({` | ASSIGN | always | | After composer._action_send_mail completes, _action_send_mail writes state='done' and sent_date=now on the mailing | NR-U90-011 |
| U90-012 | U90-F04 | mass_mailing/models/mailing.py:1179 | `def _process_mass_mailing_queue(self):` | DEF | always | | Cron method _process_mass_mailing_queue searches state in (in_queue, sending) with schedule_date < now or False; transitions to sending then calls _action_send_mail | NR-U90-012 |
| U90-013 | U90-F04 | mass_mailing/models/mailing.py:1188 | `mass_mailing.state = 'sending'` | ASSIGN | when remaining recipients > 0 | | Cron sets state=sending before calling _action_send_mail; if no recipients remain, writes state=done directly | NR-U90-013 |
| U90-014 | U90-F05 | mass_mailing/models/mailing_trace.py:54 | `_name = 'mailing.trace'` | DEF | always | | mailing.trace model stores per-email delivery statistics separately from mail.mail to avoid bloat | NR-U90-014 |
| U90-015 | U90-F05 | mass_mailing/models/mailing_trace.py:87 | `trace_status = fields.Selection(selection=[` | DEF | always | | trace_status Selection has 9 states: outgoing, process, pending, sent, open, reply, bounce, error, cancel; default is outgoing | NR-U90-015 |
| U90-016 | U90-F05 | mass_mailing/models/mailing_trace.py:72 | `medium_id = fields.Many2one(related='mass_mailing_id.medium_id')` | DEF | always | | mailing.trace carries UTM medium_id, source_id, campaign_id as related fields from the parent mailing | NR-U90-016 |
| U90-017 | U90-F05 | mass_mailing/models/mailing_trace.py:115 | `links_click_ids = fields.One2many('link.tracker.click'` | DEF | always | | mailing.trace links to link.tracker.click via links_click_ids; click tracking updates links_click_datetime | NR-U90-017 |
| U90-018 | U90-F06 | event/models/event_event.py:33 | `_name = 'event.event'` | DEF | always | | event.event model named event.event, inheriting mail.thread and mail.activity.mixin | NR-U90-018 |
| U90-019 | U90-F06 | event/models/event_event.py:101 | `kanban_state = fields.Selection([` | DEF | always | | event.event uses kanban_state (normal/done/blocked/cancel) combined with stage_id (event.stage) for status management, not a simple state field | NR-U90-019 |
| U90-020 | U90-F07 | event/models/event_registration.py:13 | `_name = 'event.registration'` | DEF | always | | event.registration model inherits mail.thread and mail.activity.mixin; links to event.event, event.event.ticket, event.slot | NR-U90-020 |
| U90-021 | U90-F07 | event/models/event_registration.py:69 | `state = fields.Selection([` | DEF | always | | event.registration.state has four values: draft (Unconfirmed), open (Registered), done (Attended), cancel (Cancelled); default is open | NR-U90-021 |
| U90-022 | U90-F07 | event/models/event_registration.py:45 | `utm_campaign_id = fields.Many2one('utm.campaign'` | DEF | always | | event.registration captures UTM data via utm_campaign_id, utm_source_id, utm_medium_id fields (not via utm.mixin but via default_get from utm.mixin) | NR-U90-022 |
| U90-023 | U90-F08 | event/models/event_ticket.py:8 | `_name = 'event.event.ticket'` | DEF | always | | event.event.ticket model inherits event.type.ticket; linked to event.event via event_id Many2one; carries seats_reserved, seats_available, registration_ids | NR-U90-023 |
| U90-024 | U90-F09 | event_crm/models/event_registration.py:14 | `lead_ids = fields.Many2many(` | DEF | always | | event_crm extends event.registration with lead_ids Many2many to crm.lead; lead_count computed field; requires sales_team.group_sale_salesman | NR-U90-024 |
| U90-025 | U90-F09 | event_crm/models/event_registration.py:35 | `if not self.env.context.get('event_lead_rule_skip'):` | GUARD | on create | | On create, event_crm calls _apply_lead_generation_rules unless context key event_lead_rule_skip is set (used in import flows) | NR-U90-025 |
| U90-026 | U90-F09 | event_crm/models/event_registration.py:65 | `if vals.get('state') == 'open':` | TRIGGER | on write state=open | | On write, if state becomes open, event_crm searches and runs all event.lead.rule records with lead_creation_trigger='confirm' | NR-U90-026 |
| U90-027 | U90-F09 | event_crm/models/event_registration.py:67 | `elif vals.get('state') == 'done':` | TRIGGER | on write state=done | | On write, if state becomes done, event_crm runs all event.lead.rule records with lead_creation_trigger='done' | NR-U90-027 |
| U90-028 | U90-F10 | event_crm/models/event_lead_rule.py:67 | `_name = 'event.lead.rule'` | DEF | always | | event.lead.rule is the rule model governing automatic crm.lead creation from event registrations | NR-U90-028 |
| U90-029 | U90-F10 | event_crm/models/event_lead_rule.py:77 | `lead_creation_basis = fields.Selection([` | DEF | always | | lead_creation_basis controls per-attendee (one lead per registration) vs per-order (one lead per batch) creation mode | NR-U90-029 |
| U90-030 | U90-F10 | event_crm/models/event_lead_rule.py:82 | `lead_creation_trigger = fields.Selection([` | DEF | always | | lead_creation_trigger has three values: create (at attendee creation), confirm (at state=open), done (at state=done) | NR-U90-030 |
| U90-031 | U90-F10 | event_crm/models/event_lead_rule.py:196 | `return self.env['crm.lead'].create(lead_vals_list)` | RETURN | end of _run_on_registrations | | _run_on_registrations batches all lead_vals_list and creates crm.lead records in one call; returns newly-created leads | NR-U90-031 |
| U90-032 | U90-F11 | event_crm/models/crm_lead.py:10 | `event_lead_rule_id = fields.Many2one('event.lead.rule'` | DEF | always | | crm.lead is extended with event_lead_rule_id, event_id, and registration_ids Many2many to track the originating event registration context | NR-U90-032 |
| U90-033 | U90-F11 | event_crm/models/event_registration.py:191 | `'campaign_id': sorted_self._find_first_notnull('utm_campaign_id'),` | ASSIGN | in _get_lead_values | | UTM data propagates from event.registration (utm_campaign_id, utm_source_id, utm_medium_id) into crm.lead (campaign_id, source_id, medium_id) via _get_lead_values | NR-U90-033 |
| U90-034 | U90-F12 | mass_mailing/models/mailing.py:398 | `mailing.medium_id = self.env['utm.medium']._fetch_or_create_utm_medium('email').id` | ASSIGN | when mailing_type='mail' and no medium_id | | On compute of medium_id, mailing.mailing auto-assigns UTM medium 'email' when mailing_type is mail and medium is not set | NR-U90-034 |

## Absence Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U90-035 | U90-F13 | (directory check) | (not found) | CHECK | always | | marketing_automation module directory does not exist under addons in Odoo 19.0.post20260921 Community; the module is Enterprise-only and absent from the Community source tree | NR-U90-035 |
