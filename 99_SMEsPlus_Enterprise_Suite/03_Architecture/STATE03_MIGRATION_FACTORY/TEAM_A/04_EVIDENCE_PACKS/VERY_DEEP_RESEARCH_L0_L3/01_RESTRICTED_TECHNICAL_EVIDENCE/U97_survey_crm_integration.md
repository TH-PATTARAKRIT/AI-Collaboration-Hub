# U97 — Survey + CRM Integration (L3/L4)
**Unit**: U97
**Phase**: Second-Pass Depth Closure — P2 Supporting Domains
**Scope**: Survey lifecycle, scoring, token access, CRM lead auto-creation from responses
**Modules**: survey, survey_crm
**Function-IDs targeted**: NEW:U97-F01 through U97-F20
**L-levels**: L3, L4
**Proof layers**: P4
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: U46, U58

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U97-001 | U97-F01 | survey/models/survey_survey.py:19 | `_name = 'survey.survey'` | DEF | | | The survey model is named `survey.survey`, inheriting `mail.thread` and `mail.activity.mixin`. | NR-U97-001 |
| U97-002 | U97-F01 | survey/models/survey_survey.py:39 | `survey_type = fields.Selection` | SCHEMA | | | `survey_type` has four values: `survey`, `live_session`, `assessment`, `custom`; default is `custom`. | NR-U97-002 |
| U97-003 | U97-F01 | survey/models/survey_survey.py:92 | `access_mode = fields.Selection` | SCHEMA | | | `access_mode` has two values: `public` (Anyone with the link) and `token` (Invited people only); default `public`. | NR-U97-003 |
| U97-004 | U97-F01 | survey/models/survey_survey.py:97 | `users_login_required = fields.Boolean` | SCHEMA | | | `users_login_required` Boolean field controls whether authenticated login is required even with a valid token. | NR-U97-004 |
| U97-005 | U97-F01 | survey/models/survey_survey.py:108 | `scoring_type = fields.Selection` | SCHEMA | | | `scoring_type` has four values: `no_scoring`, `scoring_with_answers_after_page`, `scoring_with_answers`, `scoring_without_answers`; required and stored. | NR-U97-005 |
| U97-006 | U97-F01 | survey/models/survey_survey.py:114 | `scoring_success_min = fields.Float` | SCHEMA | | | `scoring_success_min` stores the required pass percentage (default 80.0); used to determine `scoring_success` on user inputs. | NR-U97-006 |
| U97-007 | U97-F01 | survey/models/survey_survey.py:181 | `_certification_check = models.Constraint` | CONST | | | DB constraint enforces: `scoring_type != 'no_scoring'` is required for `certification=True`. | NR-U97-007 |
| U97-008 | U97-F02 | survey/models/survey_user_input.py:19 | `_name = 'survey.user_input'` | DEF | | | The response model is named `survey.user_input`, inheriting `mail.thread` and `mail.activity.mixin`. | NR-U97-008 |
| U97-009 | U97-F02 | survey/models/survey_user_input.py:32 | `state = fields.Selection` | SCHEMA | | | `state` has three values: `new`, `in_progress`, `done`; default is `new`. There is no `invalidated` state in Odoo 19. | NR-U97-009 |
| U97-010 | U97-F02 | survey/models/survey_user_input.py:45 | `access_token = fields.Char` | SCHEMA | | | Each user input has a unique `access_token` (UUID-based) and an optional `invite_token` for attempt pooling. | NR-U97-010 |
| U97-011 | U97-F02 | survey/models/survey_user_input.py:53 | `scoring_percentage = fields.Float` | SCHEMA | | | `scoring_percentage` and `scoring_total` are stored computed fields on `survey.user_input`; recomputed from answer scores. | NR-U97-011 |
| U97-012 | U97-F02 | survey/models/survey_user_input.py:88 | `user_input.scoring_success = user_input.scoring_percentage >= user_input.survey_id.scoring_success_min` | CALC | | | `scoring_success` is True when `scoring_percentage >= scoring_success_min` on the parent survey. | NR-U97-012 |
| U97-013 | U97-F03 | survey/models/survey_user_input.py:229 | `def _mark_in_progress(self):` | DEF | | | `_mark_in_progress()` writes `state='in_progress'` and sets `start_datetime` to current time. | NR-U97-013 |
| U97-014 | U97-F03 | survey/models/survey_user_input.py:236 | `def _mark_done(self):` | DEF | | | `_mark_done()` writes `state='done'` and `end_datetime`; sends certification email if survey is certification and user succeeded. | NR-U97-014 |
| U97-015 | U97-F03 | survey/models/survey_user_input.py:244 | `'state': 'done',` | ASSIGN | | | `_mark_done()` sets `state` to `done` via `self.write({'end_datetime': ..., 'state': 'done'})`. | NR-U97-015 |
| U97-016 | U97-F04 | survey/models/survey_survey.py:597 | `def _check_answer_creation(self` | DEF | | | `_check_answer_creation()` enforces access rules: checks `access_mode`, `users_can_signup`, attempt limits before creating a token. | NR-U97-016 |
| U97-017 | U97-F04 | survey/models/survey_survey.py:609 | `if self.access_mode == 'authentication':` | GUARD | C1 | | For `access_mode='authentication'`, user or partner must exist; public-only requests are rejected with `UserError`. | NR-U97-017 |
| U97-018 | U97-F04 | survey/models/survey_survey.py:616 | `if self.access_mode == 'internal'` | GUARD | C1 | | For `access_mode='internal'`, user must be an internal employee or `UserError` is raised. | NR-U97-018 |
| U97-019 | U97-F05 | survey_crm/models/survey_survey.py:7 | `_inherit = 'survey.survey'` | INHERIT | | | `survey_crm` extends `survey.survey` (no new model); adds `generate_lead`, `lead_count`, `lead_ids`, `team_id` fields. | NR-U97-019 |
| U97-020 | U97-F05 | survey_crm/models/survey_survey.py:9 | `generate_lead = fields.Boolean` | SCHEMA | | | `generate_lead` is a stored computed Boolean: True when `survey_type in ['survey','live_session','custom']` and at least one question has `generate_lead=True`. | NR-U97-020 |
| U97-021 | U97-F05 | survey_crm/models/survey_survey.py:11 | `lead_ids = fields.One2many('crm.lead', 'origin_survey_id')` | SCHEMA | | | `lead_ids` is a One2many inverse of `crm.lead.origin_survey_id`, tracking all leads generated from the survey. | NR-U97-021 |
| U97-022 | U97-F05 | survey_crm/models/survey_survey.py:12 | `team_id = fields.Many2one('crm.team'` | SCHEMA | | | `team_id` stores the assigned CRM sales team for auto-created leads; `ondelete='set null'`. | NR-U97-022 |
| U97-023 | U97-F06 | survey_crm/models/survey_question_answer.py:7 | `generate_lead = fields.Boolean` | SCHEMA | | | `survey.question.answer` gains `generate_lead` Boolean; when True on a selected answer, triggers lead creation on submission. | NR-U97-023 |
| U97-024 | U97-F06 | survey_crm/models/survey_question.py:8 | `generate_lead = fields.Boolean` | SCHEMA | | | `survey.question` gains computed `generate_lead`; True when `question_type in ['simple_choice','multiple_choice','matrix']` and any answer has `generate_lead=True`. | NR-U97-024 |
| U97-025 | U97-F07 | survey_crm/models/survey_user_input.py:9 | `lead_id = fields.Many2one('crm.lead'` | SCHEMA | | | `survey.user_input` gains `lead_id` Many2one to `crm.lead`; one user input creates at most one lead; `ondelete='set null'`. | NR-U97-025 |
| U97-026 | U97-F07 | survey_crm/models/survey_user_input.py:11 | `def _mark_done(self):` | OVERRIDE | | | `survey_crm` overrides `_mark_done()` on `survey.user_input`; after calling `super()`, filters inputs by `survey_type` and calls `_create_leads_from_generative_answers()`. | NR-U97-026 |
| U97-027 | U97-F07 | survey_crm/models/survey_user_input.py:25 | `user_input.survey_id.survey_type in ['survey', 'live_session', 'custom']` | GUARD | C1 | | Lead creation is triggered only for `survey_type` in `['survey', 'live_session', 'custom']`; `assessment` type is excluded. | NR-U97-027 |
| U97-028 | U97-F07 | survey_crm/models/survey_user_input.py:33 | `any(answer.generate_lead for answer in user_input.user_input_line_ids.suggested_answer_id)` | CHECK | C1 | | `_create_leads_from_generative_answers()` further filters: user input is included only if at least one selected answer has `generate_lead=True`. | NR-U97-028 |
| U97-029 | U97-F07 | survey_crm/models/survey_user_input.py:44 | `leads = self.env['crm.lead'].sudo().create` | CALL | | | Leads are created with `sudo()` in batch; `user_input.lead_id` is assigned to each created lead. | NR-U97-029 |
| U97-030 | U97-F07 | survey_crm/models/survey_user_input.py:65 | `'type': 'opportunity',` | ASSIGN | | | Created leads always have `type='opportunity'`; comment notes that survey responses are considered sufficiently qualified. | NR-U97-030 |
| U97-031 | U97-F08 | survey_crm/models/crm_lead.py:8 | `origin_survey_id = fields.Many2one('survey.survey'` | SCHEMA | | | `crm.lead` gains `origin_survey_id` Many2one to `survey.survey`; `index='btree_not_null'`, `ondelete='set null'`. | NR-U97-031 |
| U97-032 | U97-F05 | survey_crm/models/survey_survey.py:34 | `def action_end_session(self):` | OVERRIDE | | | For live sessions, lead creation is triggered by `action_end_session()` override on `survey.survey`, not by `_mark_done()`; it calls `_create_leads_from_generative_answers()` on session inputs. | NR-U97-032 |
