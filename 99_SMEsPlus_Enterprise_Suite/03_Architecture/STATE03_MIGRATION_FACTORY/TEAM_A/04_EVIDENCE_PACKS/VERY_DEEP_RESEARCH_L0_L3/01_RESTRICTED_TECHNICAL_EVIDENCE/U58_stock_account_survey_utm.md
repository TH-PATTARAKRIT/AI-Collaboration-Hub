# U58 — stock_account, stock bridges, survey, transifex, UTM (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U58
- Modules: stock_account, stock_maintenance, stock_sms, survey, survey_crm, transifex, utm
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: Full study for all 7 modules. stock_account is critical for Thai inventory accounting context. Source evidence only; RT flags for runtime unknowns. ARCHITECTURE NOTE: Odoo 19 stock_account has NO stock_valuation_layer.py file; valuation is stored directly on stock.move.value and a new product.value model tracks manual adjustments — this is a significant departure from Odoo 16/17 architecture.

---

## CAP-U58-01 Inventory Valuation Architecture (stock_account)

### D1 — Cost Method Definition
Three cost methods are declared on `product.template` in stock_account/models/product.py: `standard` (Standard Price), `fifo` (First In First Out), and `average` (Average Cost / AVCO). The method is computed from category or falls back to company default.

### D2 — Valuation Mode Definition
Two valuation modes are declared on `product.template`: `periodic` (at closing) and `real_time` (perpetual at invoicing). The mode is computed from product category or company-level `inventory_valuation` field.

### D3 — No Stock Valuation Layer in Odoo 19
Unlike Odoo 16/17, Odoo 19 Community has no `stock_valuation_layer.py` in stock_account/models/. Inventory value is stored directly on `stock.move.value` (monetary field). Manual price adjustments are tracked in a new `product.value` model.

### D4 — FIFO Stack Algorithm
The FIFO algorithm in `product.py._run_fifo` and `_run_fifo_get_stack` maintains a FIFO cost stack by searching incoming moves in reverse date order and popping them to match outgoing quantity.

### D5 — AVCO Computation
The AVCO batch computation in `product.py._run_average_batch` iterates all incoming/outgoing moves in date order, accumulating weighted average cost. It handles negative-quantity edge cases.

### D6 — Account Move Creation for Valuation
When a stock move is valued and `valuation == 'real_time'`, `_create_account_move` creates an account.move posted to `company.account_stock_journal_id`. Debit/credit accounts come from location `valuation_account_id` or product's stock valuation account.

### D7 — COGS Line Generation on Customer Invoice
On posting a customer invoice, `_stock_account_prepare_realtime_out_lines_vals` creates additional `cogs` display-type lines: debit COGS/variation account, credit stock valuation account.

### D8 — Lot-Level Valuation
Products can enable `lot_valuated` flag. When enabled, each lot has its own `standard_price` and total value is computed per lot. FIFO and AVCO both support lot-level valuation.

### D9 — Periodic Closing
`res_company.action_close_stock_valuation` computes the difference between physical stock value and accounting stock value and posts a journal entry. A cron `_cron_post_stock_valuation` can run daily or monthly.

### D10 — Lock Date Protection
`stock_picking._check_backdate_allowed` raises ValidationError if picking `date_done` falls within a locked fiscal period (unless `skip_lock_date_check` config parameter is set).

---

## CAP-U58-02 stock_maintenance Bridge

### D1 — Equipment Location Link
`MaintenanceEquipment` gains a `location_id` Many2one to `stock.location` (domain: internal locations only). Allows linking maintenance equipment to a warehouse location.

### D2 — Serial Number Matching
`_compute_match_serial` checks if the equipment's `serial_no` matches any `stock.lot.name`. Used to surface a smart button linking equipment to its inventory lot.

### D3 — Equipment Count on Location
`StockLocation` gains `equipment_count` computed field showing how many maintenance equipments are assigned to that location.

---

## CAP-U58-03 stock_sms Bridge

### D1 — SMS Confirmation on Delivery
When validating an outgoing delivery, `_pre_action_done_hook` checks if SMS confirmation is configured for the company. If yes and the company has not yet received the warning, it opens a wizard.

### D2 — SMS Template on Company
`res.company` gains `stock_sms_confirmation_template_id` pointing to an `sms.template` for `stock.picking`. Default references `stock_sms.sms_template_data_stock_delivery`.

### D3 — ConfirmStockSms Wizard
`confirm.stock.sms` wizard gives the user the choice to `send_sms` (proceed with validation and send SMS) or `dont_send_sms` (proceed without SMS and disable the feature for the company).

---

## CAP-U58-04 Survey Engine

### D1 — Survey Types
`survey.survey` has four types: `survey`, `live_session`, `assessment`, `custom`.

### D2 — Question Types
`survey.question` supports 9 types: `simple_choice`, `multiple_choice`, `text_box`, `char_box`, `numerical_box`, `scale`, `date`, `datetime`, `matrix`.

### D3 — Scoring System
`scoring_type` options: `no_scoring`, `scoring_with_answers_after_page`, `scoring_with_answers`, `scoring_without_answers`. `scoring_success_min` defines the threshold (default 80%). Score percentage and success are stored computed fields for performance.

### D4 — Certification
A survey can be marked as `certification` (requires non-no_scoring). Certifications can award a gamification badge. `certification_mail_template_id` sends a certificate email on success.

### D5 — Live Sessions
Live sessions have `session_state` (ready/in_progress), `session_code` (unique URL code), `session_question_id` (currently active question), and support speed-rating (bonus points for fast answers).

### D6 — Attempt Limiting
`is_attempts_limited` restricts how many times a user can attempt a survey. Disabled if `access_mode == 'public'` without login, or if conditional questions exist.

### D7 — Conditional Questions
`has_conditional_questions` is True when any question has `triggering_answer_ids`. Conditional question flow is incompatible with attempt limiting.

### D8 — User Input States
`survey.user_input` states: `new`, `in_progress`, `done`. Scoring fields (`scoring_percentage`, `scoring_total`, `scoring_success`) are stored for performance.

### D9 — Time Limiting
Both survey-level (`is_time_limited`, `time_limit` in minutes) and question-level (`is_time_limited`, `time_limit` in seconds for live sessions) time limits are supported.

---

## CAP-U58-05 survey_crm Bridge

### D1 — Lead-Generating Answers
`survey.question.answer` gains `generate_lead` Boolean. When a respondent selects such an answer, a CRM lead is created on survey completion.

### D2 — Lead Creation on Submission
`survey.user_input._mark_done` calls `_create_leads_from_generative_answers`. For live sessions, `survey.survey.action_end_session` calls the same.

### D3 — Lead Values from Survey
The UTM medium is set to 'Survey', the UTM source to the survey title. The lead type is always 'opportunity'. The sales team from `survey.survey.team_id` is assigned to the lead.

### D4 — CRM Lead Origin
`crm.lead` gains `origin_survey_id` Many2one to `survey.survey` with btree index.

---

## CAP-U58-06 Transifex Integration

### D1 — Project URL Lookup
`transifex.translation._get_transifex_projects` parses `.tx/config` files in addon paths to map module names to Transifex project names.

### D2 — Translation URL Generation
`_update_transifex_url` adds `transifex_url` to translation dicts. URL format: `{base_url}/{project}/translate/#{lang_iso}/{module}/42?q=text%3A{source}`. Requires `transifex.project_url` system parameter.

### D3 — Code Translation Model
`transifex.code.translation` stores code-level translations with module, lang, source, and value. Can be loaded from `CodeTranslations._get_code_translations` and reloaded on demand.

---

## CAP-U58-07 UTM Tracking

### D1 — Three Tracking Dimensions
`utm.mixin` provides `campaign_id`, `source_id`, `medium_id` fields. `tracking_fields()` maps URL params `utm_campaign`, `utm_source`, `utm_medium` to cookies `odoo_utm_campaign`, `odoo_utm_source`, `odoo_utm_medium`.

### D2 — Cookie Persistence
`ir.http._set_utm` saves UTM URL parameters to cookies in `_post_dispatch`. Max age is 31 days. Cookie domain is `request.httprequest.host`.

### D3 — Auto-Create Records
`_find_or_create_record` searches case-insensitively for existing UTM records by name and creates one if not found. For campaigns, sets `is_auto_campaign=True`.

### D4 — Name Uniqueness
Campaign, source, and medium names are enforced unique by DB constraints. `_get_unique_names` adds counter suffixes (e.g., `[2]`, `[3]`) to avoid collisions.

### D5 — Required Mediums
Six mediums are protected from deletion: Email, Direct, Website, X (Twitter), Facebook, LinkedIn.

### D6 — UtmSourceMixin
`utm.source.mixin` is an abstract model that auto-creates a linked `utm.source` on record creation. The source name is generated from record content (max 20 chars + ellipsis + model + date).

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U58-C001 | CAP-U58-01 | stock_account/models/product.py:14 | `cost_method = fields.Selection(` | FACT | always | — | ProductTemplate.cost_method Selection field with values standard/fifo/average, computed from category or company default | N-U58-001 |
| VDR-U58-C002 | CAP-U58-01 | stock_account/models/product.py:16 | `('standard', "Standard Price"),` | FACT | always | — | Standard Price is first option in cost_method selection | N-U58-001 |
| VDR-U58-C003 | CAP-U58-01 | stock_account/models/product.py:17 | `('fifo', "First In First Out (FIFO)"),` | FACT | always | — | FIFO (First In First Out) is second option in cost_method selection | N-U58-001 |
| VDR-U58-C004 | CAP-U58-01 | stock_account/models/product.py:18 | `('average', "Average Cost (AVCO)"),` | FACT | always | — | Average Cost (AVCO) is third option in cost_method selection | N-U58-001 |
| VDR-U58-C005 | CAP-U58-01 | stock_account/models/product.py:23 | `valuation = fields.Selection(` | FACT | always | — | ProductTemplate.valuation Selection field with periodic/real_time options | N-U58-002 |
| VDR-U58-C006 | CAP-U58-01 | stock_account/models/product.py:25 | `('periodic', 'Periodic (at closing)'),` | FACT | always | — | Periodic valuation: accounting entries created manually at closing | N-U58-002 |
| VDR-U58-C007 | CAP-U58-01 | stock_account/models/product.py:26 | `('real_time', 'Perpetual (at invoicing)'),` | FACT | always | — | Real-time (perpetual) valuation: accounting entries created automatically on stock moves | N-U58-002 |
| VDR-U58-C008 | CAP-U58-01 | stock_account/models/product.py:31 | `lot_valuated = fields.Boolean(` | FACT | always | — | ProductTemplate.lot_valuated Boolean enables per-lot/serial valuation; computed/stored/editable | N-U58-003 |
| VDR-U58-C009 | CAP-U58-01 | stock_account/models/product.py:54 | `def _compute_lot_valuated(self):` | FACT | always | — | lot_valuated is forced to False when product tracking is 'none' | N-U58-003 |
| VDR-U58-C010 | CAP-U58-01 | stock_account/models/product.py:60 | `@api.depends_context('company')` | FACT | always | — | cost_method is company-context-dependent: computed from categ_id.property_cost_method or company.cost_method | N-U58-001 |
| VDR-U58-C011 | CAP-U58-01 | stock_account/models/product.py:130 | `def _get_product_accounts(self):` | FACT | always | — | _get_product_accounts adds stock_valuation account from category or company, and stock_variation from valuation account | N-U58-004 |
| VDR-U58-C012 | CAP-U58-01 | stock_account/models/product.py:136 | `accounts['stock_valuation'] = (` | FACT | always | — | stock_valuation account resolved: categ property > categ fallback > company.account_stock_valuation_id | N-U58-004 |
| VDR-U58-C013 | CAP-U58-01 | stock_account/models/product.py:257 | `elif cost_method == 'average':` | FACT | always | — | _compute_value routes to _run_average_batch for AVCO products | N-U58-005 |
| VDR-U58-C014 | CAP-U58-01 | stock_account/models/product.py:261 | `std_prices, total_values = products_to_value._run_fifo_batch(at_date=at_date)` | FACT | always | — | _compute_value routes to _run_fifo_batch for FIFO products | N-U58-005 |
| VDR-U58-C015 | CAP-U58-01 | stock_account/models/product.py:302 | `def _change_standard_price(self, old_price):` | FACT | always | — | When standard_price changes (non-FIFO), a product.value record is created recording date, user, old/new price description | N-U58-006 |
| VDR-U58-C016 | CAP-U58-01 | stock_account/models/product.py:307 | `if product.cost_method == 'fifo' or product.standard_price == old_price.get(product):` | FACT | always | — | No product.value created for FIFO products or when price unchanged | N-U58-006 |
| VDR-U58-C017 | CAP-U58-01 | stock_account/models/product.py:393 | `def _run_standard_batch(self, at_date=None, lot=None):` | FACT | always | — | Standard cost batch: value = qty_available * standard_price; supports historical price at date | N-U58-001 |
| VDR-U58-C018 | CAP-U58-01 | stock_account/models/product.py:404 | `def _run_average_batch(self, at_date=None, lot=None, force_recompute=False):` | FACT | always | — | AVCO batch: returns current standard_price without recompute unless force_recompute=True or at_date is set | N-U58-005 |
| VDR-U58-C019 | CAP-U58-01 | stock_account/models/product.py:490 | `if move.is_in:` | FACT | always | — | AVCO accumulation on in-move: new_avg = (prev_qty * prev_avg + in_value) / new_qty | N-U58-005 |
| VDR-U58-C020 | CAP-U58-01 | stock_account/models/product.py:504 | `elif previous_qty <= 0:` | FACT | always | — | AVCO negative-stock edge case: average_cost taken from last receipt value/qty | N-U58-005 |
| VDR-U58-C021 | CAP-U58-01 | stock_account/models/product.py:507 | `if move.is_out:` | FACT | always | — | AVCO out-move: out_value = out_qty * average_cost (no stack lookup) | N-U58-005 |
| VDR-U58-C022 | CAP-U58-01 | stock_account/models/product.py:540 | `def _run_fifo(self, quantity, lot=None, at_date=None, location=None):` | FACT | always | — | _run_fifo: returns monetary cost for given quantity using FIFO stack | N-U58-007 |
| VDR-U58-C023 | CAP-U58-01 | stock_account/models/product.py:555 | `while quantity > 0 and fifo_stack:` | FACT | always | — | FIFO pops earliest incoming moves from stack; extrapolates with last known price if stack exhausted | N-U58-007 |
| VDR-U58-C024 | CAP-U58-01 | stock_account/models/product.py:583 | `def _run_fifo_get_stack(self, lot=None, at_date=None, location=None):` | FACT | always | — | _run_fifo_get_stack searches incoming done moves in DESC date order to build FIFO stack (initial limit 100, expands) | N-U58-007 |
| VDR-U58-C025 | CAP-U58-01 | stock_account/models/product.py:594 | `if self.env.context.get('fifo_qty_already_processed'):` | FACT | always | — | FIFO stack adjusts for concurrently validated moves via context 'fifo_qty_already_processed' | N-U58-007 |
| VDR-U58-C026 | CAP-U58-01 | stock_account/models/product.py:636 | `def _update_standard_price(self, extra_value=None, extra_quantity=None):` | FACT | always | — | _update_standard_price: incremental fast-path for AVCO (uses extra_value/extra_qty); full recompute for FIFO | N-U58-005 |
| VDR-U58-C027 | CAP-U58-01 | stock_account/models/product.py:669 | `new_avg_cost = (previous_qty * product.standard_price + added_value) / product.qty_available` | FACT | always | — | Incremental AVCO formula: new_avg = (old_qty * old_avg + added_value) / new_qty | N-U58-005 |
| VDR-U58-C028 | CAP-U58-01 | stock_account/models/product.py:728 | `anglo_saxon_accounting = fields.Boolean(` | FACT | always | — | ProductCategory.anglo_saxon_accounting computed from company.anglo_saxon_accounting | N-U58-008 |
| VDR-U58-C029 | CAP-U58-01 | stock_account/models/product.py:731 | `property_valuation = fields.Selection(` | FACT | always | — | ProductCategory.property_valuation is company-dependent, copied, tracked | N-U58-002 |
| VDR-U58-C030 | CAP-U58-01 | stock_account/models/product.py:741 | `property_cost_method = fields.Selection(` | FACT | always | — | ProductCategory.property_cost_method is company-dependent, default from company.cost_method | N-U58-001 |
| VDR-U58-C031 | CAP-U58-01 | stock_account/models/product.py:756 | `property_stock_journal = fields.Many2one(` | FACT | always | — | ProductCategory.property_stock_journal: company-dependent journal for automated inventory entries | N-U58-004 |
| VDR-U58-C032 | CAP-U58-01 | stock_account/models/product.py:759 | `property_stock_valuation_account_id = fields.Many2one(` | FACT | always | — | ProductCategory.property_stock_valuation_account_id: company-dependent stock valuation account | N-U58-004 |
| VDR-U58-C033 | CAP-U58-01 | stock_account/models/stock_move.py:22 | `value = fields.Monetary(` | FACT | always | — | StockMove.value: Monetary field in company currency storing current valuation; zero if not valued | N-U58-009 |
| VDR-U58-C034 | CAP-U58-01 | stock_account/models/stock_move.py:43 | `remaining_qty = fields.Float(` | FACT | always | — | StockMove.remaining_qty: computed FIFO remaining quantity on incoming moves | N-U58-007 |
| VDR-U58-C035 | CAP-U58-01 | stock_account/models/stock_move.py:136 | `if move.product_id.cost_method == 'fifo':` | FACT | always | — | remaining_value for FIFO: ratio * move.value; for others: remaining_qty * standard_price | N-U58-007 |
| VDR-U58-C036 | CAP-U58-01 | stock_account/models/stock_move.py:145 | `def _inverse_value_manual(self):` | FACT | always | — | Writing value_manual creates a product.value record to override move valuation | N-U58-006 |
| VDR-U58-C037 | CAP-U58-01 | stock_account/models/stock_move.py:177 | `def _action_done(self, cancel_backorder=False):` | FACT | always | — | _action_done: out moves valued BEFORE super() (to capture pre-done FIFO state), in moves valued AFTER super() | N-U58-009 |
| VDR-U58-C038 | CAP-U58-01 | stock_account/models/stock_move.py:186 | `moves_in.with_context(std_price_incremental_recompute=not moves_out)._set_value()` | FACT | always | — | Incremental std price recompute enabled for in-moves when no out-moves validated in same batch | N-U58-005 |
| VDR-U58-C039 | CAP-U58-01 | stock_account/models/stock_move.py:193 | `def _create_account_move(self):` | FACT | always | — | _create_account_move creates one account.move per batch of valued moves, posts it immediately | N-U58-004 |
| VDR-U58-C040 | CAP-U58-01 | stock_account/models/stock_move.py:209 | `'journal_id': self.company_id.account_stock_journal_id.id,` | FACT | always | — | Journal for stock account moves taken from company.account_stock_journal_id | N-U58-004 |
| VDR-U58-C041 | CAP-U58-01 | stock_account/models/stock_move.py:229 | `def _get_account_move_line_vals(self):` | FACT | always | — | AML creation: if source location has valuation_account, debit stock_valuation + credit location_account; else reversed | N-U58-004 |
| VDR-U58-C042 | CAP-U58-01 | stock_account/models/stock_move.py:292 | `def _set_value(self, correction_quantity=None):` | FACT | always | — | _set_value: main valuation engine; for FIFO out uses _run_fifo; for others uses standard_price * valued_qty | N-U58-009 |
| VDR-U58-C043 | CAP-U58-01 | stock_account/models/stock_move.py:315 | `if move.product_id.lot_valuated:` | FACT | always | — | For lot-valuated products: in-moves trigger lot recompute; out-moves value from lot.standard_price * move_line.qty | N-U58-003 |
| VDR-U58-C044 | CAP-U58-01 | stock_account/models/stock_move.py:346 | `if move.product_id.cost_method == 'fifo':` | FACT | always | — | For FIFO outgoing: _run_fifo called with fifo_qty_already_processed context for concurrent batch handling | N-U58-007 |
| VDR-U58-C045 | CAP-U58-01 | stock_account/models/stock_move.py:351 | `move.value = move.product_id.standard_price * move._get_valued_qty()` | FACT | always | — | For standard/AVCO outgoing: value = standard_price * valued_qty (no stack lookup) | N-U58-001 |
| VDR-U58-C046 | CAP-U58-01 | stock_account/models/stock_move.py:363 | `def _get_value_data(` | FACT | always | — | _get_value_data: priority chain: 1.manual_override, 2.invoice/bill, 3.production, 4.SO/PO quotation, 5.returns, 6.standard_price | N-U58-009 |
| VDR-U58-C047 | CAP-U58-01 | stock_account/models/stock_move.py:462 | `def _get_manual_value(self, quantity, at_date=None):` | FACT | always | — | _get_manual_value: searches product.value by move_id DESC date, returns first match | N-U58-006 |
| VDR-U58-C048 | CAP-U58-01 | stock_account/models/stock_move.py:501 | `def _get_value_from_std_price(self, quantity, std_price=False, at_date=None):` | FACT | always | — | For lot_valuated products with single lot: uses lot.standard_price; for FIFO at_date: uses value/valued_qty | N-U58-003 |
| VDR-U58-C049 | CAP-U58-01 | stock_account/models/stock_move.py:545 | `def _is_in(self):` | FACT | always | — | _is_in: returns True if any move_line flows from non-valued to valued location (and not dropshipped returned) | N-U58-009 |
| VDR-U58-C050 | CAP-U58-01 | stock_account/models/stock_move.py:575 | `def _is_out(self):` | FACT | always | — | _is_out: returns True if any move_line flows from valued to non-valued location (and not dropshipped) | N-U58-009 |
| VDR-U58-C051 | CAP-U58-01 | stock_account/models/stock_move.py:585 | `def _is_dropshipped(self):` | FACT | always | — | Dropship: source=supplier and dest=customer (both can be transit without company) | N-U58-010 |
| VDR-U58-C052 | CAP-U58-01 | stock_account/models/stock_move.py:659 | `def _should_create_account_move(self):` | FACT | always | — | Account move created only when: storable + valued + location has valuation_account + non-zero qty + real_time valuation | N-U58-004 |
| VDR-U58-C053 | CAP-U58-01 | stock_account/models/stock_move.py:664 | `and (self.location_dest_id.valuation_account_id or self.location_id.valuation_account_id)` | FACT | always | — | Account moves only for location-specific valuation — standard internal moves without location valuation_account do not create entries | N-U58-004 |
| VDR-U58-C054 | CAP-U58-01 | stock_account/models/stock_move.py:266 | `def _get_cogs_price_unit(self, quantity=0):` | FACT | always | — | COGS price unit: for FIFO/AVCO uses weighted average of valued moves; for standard uses standard_price | N-U58-008 |
| VDR-U58-C055 | CAP-U58-01 | stock_account/models/account_move.py:8 | `stock_move_ids = fields.One2many('stock.move', 'account_move_id', string='Stock Move')` | FACT | always | — | AccountMove gains reverse relation to stock.move via account_move_id | N-U58-004 |
| VDR-U58-C056 | CAP-U58-01 | stock_account/models/account_move.py:36 | `self.env['account.move.line'].create(self._stock_account_prepare_realtime_out_lines_vals())` | FACT | always | — | On _post: COGS lines created BEFORE posting for customer invoices | N-U58-008 |
| VDR-U58-C057 | CAP-U58-01 | stock_account/models/account_move.py:42 | `self.line_ids._get_stock_moves().filtered(lambda m: m.is_in or m.is_dropship)._set_value()` | FACT | always | — | On invoice post: in/dropship moves re-value to capture invoice price for AVCO/standard | N-U58-005 |
| VDR-U58-C058 | CAP-U58-01 | stock_account/models/account_move.py:68 | `def _stock_account_prepare_realtime_out_lines_vals(self):` | FACT | always | — | COGS generation: only for sale documents; creates two paired AML lines with display_type='cogs' | N-U58-008 |
| VDR-U58-C059 | CAP-U58-01 | stock_account/models/account_move.py:115 | `stock_account = accounts['stock_valuation']` | FACT | always | — | COGS credit: stock_valuation account; COGS debit: expense account | N-U58-008 |
| VDR-U58-C060 | CAP-U58-01 | stock_account/models/account_move_line.py:7 | `cogs_origin_id = fields.Many2one(` | FACT | always | — | AccountMoveLine.cogs_origin_id: technical back-link from COGS line to its originating invoice line | N-U58-008 |
| VDR-U58-C061 | CAP-U58-01 | stock_account/models/account_move_line.py:23 | `if line.product_id.valuation == 'real_time' and accounts['stock_valuation']:` | FACT | always | — | On purchase bill line: account set to stock_valuation account for perpetual-valued storable products | N-U58-004 |
| VDR-U58-C062 | CAP-U58-01 | stock_account/models/account_move_line.py:51 | `def _get_cogs_value(self):` | FACT | always | — | _get_cogs_value: for standard/AVCO uses original invoice price if credit note; otherwise uses stock move COGS price | N-U58-008 |
| VDR-U58-C063 | CAP-U58-01 | stock_account/models/stock_location.py:11 | `valuation_account_id = fields.Many2one(` | FACT | always | — | StockLocation.valuation_account_id: optional account for location-specific valuation entries | N-U58-004 |
| VDR-U58-C064 | CAP-U58-01 | stock_account/models/stock_location.py:15 | `is_valued_internal = fields.Boolean('Is valued inside the company', compute="_compute_is_valued"` | FACT | always | — | is_valued_internal: True when location usage is internal or transit AND has a company_id | N-U58-011 |
| VDR-U58-C065 | CAP-U58-01 | stock_account/models/stock_location.py:36 | `def _should_be_valued(self):` | FACT | always | — | _should_be_valued: True for internal and transit locations WITH a company (excludes company-less transit = inter-company) | N-U58-011 |
| VDR-U58-C066 | CAP-U58-01 | stock_account/models/res_company.py:12 | `account_stock_journal_id = fields.Many2one('account.journal', string='Stock Journal'` | FACT | always | — | ResCompany.account_stock_journal_id: journal for automated inventory valuation entries | N-U58-004 |
| VDR-U58-C067 | CAP-U58-01 | stock_account/models/res_company.py:19 | `inventory_period = fields.Selection(` | FACT | always | — | ResCompany.inventory_period: manual/daily/monthly; controls cron closing frequency | N-U58-012 |
| VDR-U58-C068 | CAP-U58-01 | stock_account/models/res_company.py:29 | `inventory_valuation = fields.Selection(` | FACT | always | — | ResCompany.inventory_valuation: periodic/real_time default; fallback when category has no property | N-U58-002 |
| VDR-U58-C069 | CAP-U58-01 | stock_account/models/res_company.py:38 | `cost_method = fields.Selection(` | FACT | always | — | ResCompany.cost_method: standard/fifo/average default; required; default='standard' | N-U58-001 |
| VDR-U58-C070 | CAP-U58-01 | stock_account/models/res_company.py:49 | `def action_close_stock_valuation(self, at_date=None, auto_post=False):` | FACT | always | — | action_close_stock_valuation: computes diff between inventory value and accounting value; creates closing journal entry | N-U58-012 |
| VDR-U58-C071 | CAP-U58-01 | stock_account/models/res_company.py:138 | `def _cron_post_stock_valuation(self):` | FACT | always | — | Cron: runs for companies with inventory_period='daily' or 'monthly' (monthly only on last day of month) | N-U58-012 |
| VDR-U58-C072 | CAP-U58-01 | stock_account/models/res_company.py:89 | `def stock_value(self, accounts_by_product=None, at_date=None):` | FACT | always | — | stock_value(): physical inventory value by account, using product.total_value | N-U58-012 |
| VDR-U58-C073 | CAP-U58-01 | stock_account/models/res_company.py:100 | `def stock_accounting_value(self, accounts_by_product=None, at_date=None):` | FACT | always | — | stock_accounting_value(): sum of posted AML balances on stock valuation accounts | N-U58-012 |
| VDR-U58-C074 | CAP-U58-01 | stock_account/models/res_company.py:274 | `def _get_continental_realtime_variation_vals(self, accounts_by_product, at_date=None, extra_aml_vals_list=None):` | FACT | always | — | Continental perpetual: variation journal entry posts stock variation over fiscal period | N-U58-012 |
| VDR-U58-C075 | CAP-U58-01 | stock_account/models/stock_quant.py:10 | `value = fields.Monetary('Value', compute='_compute_value', groups='stock.group_stock_manager')` | FACT | always | — | StockQuant.value: computed monetary field (manager-only); proportional allocation of product/lot total value | N-U58-009 |
| VDR-U58-C076 | CAP-U58-01 | stock_account/models/stock_quant.py:57 | `if quant.product_id.lot_valuated:` | FACT | always | — | Quant value: for lot-valuated products uses lot.total_value / lot.product_qty * quant.quantity | N-U58-003 |
| VDR-U58-C077 | CAP-U58-01 | stock_account/models/stock_quant.py:80 | `def _apply_inventory(self, date=None):` | FACT | always | — | When accounting_date set on quant, inventory adjustment uses that date for accounting entries (force_period_date context) | N-U58-013 |
| VDR-U58-C078 | CAP-U58-01 | stock_account/models/stock_lot.py:9 | `lot_valuated = fields.Boolean(related='product_id.lot_valuated'` | FACT | always | — | StockLot.lot_valuated: related read-only field showing whether per-lot valuation is active | N-U58-003 |
| VDR-U58-C079 | CAP-U58-01 | stock_account/models/stock_lot.py:13 | `standard_price = fields.Float(` | FACT | always | — | StockLot.standard_price: company-dependent cost per lot; auto-initialized to product standard_price on lot creation | N-U58-003 |
| VDR-U58-C080 | CAP-U58-01 | stock_account/models/stock_lot.py:39 | `elif valuated_product.cost_method == 'average':` | FACT | always | — | Lot value for AVCO: calls _run_avco with lot context; for FIFO: calls _run_fifo_batch with lot | N-U58-003 |
| VDR-U58-C081 | CAP-U58-01 | stock_account/models/stock_lot.py:57 | `if product.lot_valuated:` | FACT | always | — | On lot create: if product is lot_valuated and lot has no standard_price, it is initialized to product.standard_price | N-U58-003 |
| VDR-U58-C082 | CAP-U58-01 | stock_account/models/stock_picking.py:13 | `@api.constrains("date_done")` | FACT | always | — | StockPicking: backdate constraint checks against accounting lock date (fiscal year hard lock); bypass via ir.config_parameter | N-U58-013 |
| VDR-U58-C083 | CAP-U58-01 | stock_account/models/stock_move_line.py:19 | `valuation_fields = ['quantity', 'location_id', 'location_dest_id', 'owner_id', 'quant_id', 'lot_id']` | FACT | always | — | SML write: changes to these five fields trigger _update_stock_move_value() re-valuation | N-U58-009 |
| VDR-U58-C084 | CAP-U58-01 | stock_account/models/stock_move_line.py:58 | delta = sum | FACT | always | — | Consigned goods (owner != company) excluded from valuation but qty still influences COGS weighted average | N-U58-010 |
| VDR-U58-C085 | CAP-U58-01 | stock_account/models/account_account.py:7 | `account_stock_variation_id = fields.Many2one(` | FACT | always | — | AccountAccount gains account_stock_variation_id for stock variation at closing, and account_stock_expense_id | N-U58-012 |
| VDR-U58-C086 | CAP-U58-01 | stock_account/models/product_value.py:4 | `class ProductValue(models.Model):` | FACT | always | — | product.value model: tracks history of manual price updates (standard price change, lot price change, move value override) | N-U58-006 |
| VDR-U58-C087 | CAP-U58-01 | stock_account/models/product_value.py:19 | `move_id = fields.Many2one('stock.move', string='Move', index='btree_not_null')` | FACT | always | — | product.value.move_id: optional link to a specific stock.move; when set, overrides that move's valuation | N-U58-006 |
| VDR-U58-C088 | CAP-U58-01 | stock_account/models/product_value.py:72 | `def create(self, vals_list):` | FACT | always | — | On product.value create: if move_id set calls _set_value() on moves; if lot+product set calls _update_standard_price() | N-U58-006 |
| VDR-U58-C089 | CAP-U58-01 | stock_account/wizard/stock_inventory_adjustment_name.py:7 | `accounting_date = fields.Date(` | FACT | always | — | Inventory adjustment wizard gains accounting_date field (separate from physical date) for automated valuation | N-U58-013 |
| VDR-U58-C090 | CAP-U58-01 | stock_account/report/stock_avco_audit_report.py:37 | `def init(self):` | FACT | always | — | stock.avco.report: SQL view unioning stock_move + product_value for AVCO/FIFO products; excludes standard cost method | N-U58-014 |
| VDR-U58-C091 | CAP-U58-02 | stock_maintenance/models/maintenance.py:9 | `location_id = fields.Many2one('stock.location', 'Location', domain="[('usage', '=', 'internal')]")` | FACT | always | — | MaintenanceEquipment.location_id: links equipment to internal stock location | N-U58-015 |
| VDR-U58-C092 | CAP-U58-02 | stock_maintenance/models/maintenance.py:10 | `match_serial = fields.Boolean(compute='_compute_match_serial')` | FACT | always | — | match_serial: True when equipment.serial_no matches a stock.lot.name; requires stock.group_production_lot group | N-U58-015 |
| VDR-U58-C093 | CAP-U58-02 | stock_maintenance/models/maintenance.py:14 | `if not self.env['stock.lot'].has_access('read') or not self.env.user.has_group('stock.group_production_lot'):` | FACT | always | — | match_serial computation gated behind stock lot read access AND production lot group | N-U58-015 |
| VDR-U58-C094 | CAP-U58-02 | stock_maintenance/models/stock_location.py:7 | `equipment_count = fields.Integer('Equipment Count', compute='_compute_equipment_count')` | FACT | always | — | StockLocation.equipment_count: computed via _read_group on maintenance.equipment by location_id | N-U58-015 |
| VDR-U58-C095 | CAP-U58-03 | stock_sms/models/stock_picking.py:10 | `def _pre_action_done_hook(self):` | FACT | always | — | _pre_action_done_hook: intercepts validate; if SMS configured and not in test, opens wizard for first-time warning | N-U58-016 |
| VDR-U58-C096 | CAP-U58-03 | stock_sms/models/stock_picking.py:21 | `is_delivery = picking.company_id._get_text_validation('sms')` | FACT | always | — | SMS trigger condition: company has SMS text validation enabled AND picking is outgoing AND partner has phone | N-U58-016 |
| VDR-U58-C097 | CAP-U58-03 | stock_sms/models/stock_picking.py:46 | `def _send_confirmation_email(self):` | FACT | always | — | _send_confirmation_email extended: if SMS enabled, sends template SMS to partner on outgoing delivery | N-U58-016 |
| VDR-U58-C098 | CAP-U58-03 | stock_sms/models/res_company.py:16 | `stock_sms_confirmation_template_id = fields.Many2one(` | FACT | always | — | ResCompany.stock_sms_confirmation_template_id: SMS template (model=stock.picking); default = sms_template_data_stock_delivery | N-U58-016 |
| VDR-U58-C099 | CAP-U58-03 | stock_sms/models/res_company.py:21 | `has_received_warning_stock_sms = fields.Boolean()` | FACT | always | — | has_received_warning_stock_sms: one-time flag; once True, wizard no longer shown for that company | N-U58-016 |
| VDR-U58-C100 | CAP-U58-03 | stock_sms/wizard/confirm_stock_sms.py:13 | `def send_sms(self):` | FACT | always | — | send_sms: marks company as warned, then validates picking (via button_validate_picking_ids context) | N-U58-016 |
| VDR-U58-C101 | CAP-U58-03 | stock_sms/wizard/confirm_stock_sms.py:21 | `def dont_send_sms(self):` | FACT | always | — | dont_send_sms: marks company warned AND disables stock_text_confirmation; validates picking | N-U58-016 |
| VDR-U58-C102 | CAP-U58-04 | survey/models/survey_survey.py:19 | `_name = 'survey.survey'` | FACT | always | — | survey.survey: inherits mail.thread and mail.activity.mixin | N-U58-017 |
| VDR-U58-C103 | CAP-U58-04 | survey/models/survey_survey.py:39 | survey_type = fields.Selection | FACT | always | — | survey_type: 4 options; default='custom' | N-U58-017 |
| VDR-U58-C104 | CAP-U58-04 | survey/models/survey_survey.py:75 | `questions_layout = fields.Selection([` | FACT | always | — | questions_layout: page_per_question / page_per_section / one_page; required, default='page_per_question' | N-U58-018 |
| VDR-U58-C105 | CAP-U58-04 | survey/models/survey_survey.py:80 | questions_selection = fields.Selection | FACT | always | — | questions_selection: all or random; random ignored in live session mode | N-U58-018 |
| VDR-U58-C106 | CAP-U58-04 | survey/models/survey_survey.py:92 | access_mode = fields.Selection | FACT | always | — | access_mode: public or token-only | N-U58-019 |
| VDR-U58-C107 | CAP-U58-04 | survey/models/survey_survey.py:108 | `scoring_type = fields.Selection([` | FACT | always | — | scoring_type: no_scoring / scoring_with_answers_after_page / scoring_with_answers / scoring_without_answers | N-U58-020 |
| VDR-U58-C108 | CAP-U58-04 | survey/models/survey_survey.py:114 | `scoring_success_min = fields.Float('Required Score (%)', default=80.0)` | FACT | always | — | scoring_success_min: default 80.0%; check constraint 0-100 | N-U58-020 |
| VDR-U58-C109 | CAP-U58-04 | survey/models/survey_survey.py:123 | `certification = fields.Boolean('Is a Certification'` | FACT | always | — | certification: requires non-no_scoring (DB CHECK constraint enforced) | N-U58-021 |
| VDR-U58-C110 | CAP-U58-04 | survey/models/survey_survey.py:144 | `certification_badge_id = fields.Many2one('gamification.badge'` | FACT | always | — | certification_badge_id: unique badge per survey (UNIQUE DB constraint) | N-U58-021 |
| VDR-U58-C111 | CAP-U58-04 | survey/models/survey_survey.py:148 | session_state = fields.Selection | FACT | always | — | session_state: ready/in_progress; session_code is unique (UNIQUE constraint) | N-U58-022 |
| VDR-U58-C112 | CAP-U58-04 | survey/models/survey_survey.py:167 | `session_speed_rating = fields.Boolean("Reward quick answers"` | FACT | always | — | session_speed_rating: bonus points for fast answers; requires positive session_speed_rating_time_limit | N-U58-022 |
| VDR-U58-C113 | CAP-U58-04 | survey/models/survey_question.py:87 | `question_type = fields.Selection([` | FACT | always | — | question_type: 9 options — simple_choice, multiple_choice, text_box, char_box, numerical_box, scale, date, datetime, matrix | N-U58-023 |
| VDR-U58-C114 | CAP-U58-04 | survey/models/survey_question.py:121 | matrix_subtype = fields.Selection | FACT | always | — | matrix_subtype: simple (one answer per row) or multiple (multiple answers per row) | N-U58-023 |
| VDR-U58-C115 | CAP-U58-04 | survey/models/survey_question.py:128 | `scale_min = fields.Integer("Scale Minimum Value", default=0)` | FACT | always | — | Scale question: min/max/mid labels configurable; min default 0, max default 10 | N-U58-023 |
| VDR-U58-C116 | CAP-U58-04 | survey/models/survey_user_input.py:32 | state = fields.Selection | FACT | always | — | user_input state machine: new → in_progress → done | N-U58-024 |
| VDR-U58-C117 | CAP-U58-04 | survey/models/survey_user_input.py:53 | `scoring_percentage = fields.Float("Score (%)", compute="_compute_scoring_values", store=True` | FACT | always | — | scoring_percentage and scoring_total are stored computed fields (performance optimization) | N-U58-020 |
| VDR-U58-C118 | CAP-U58-04 | survey/models/survey_user_input.py:66 | `def _compute_scoring_values(self):` | FACT | always | — | Scoring: for simple_choice uses max positive answer score; for multiple_choice sums all positive; for other scored questions uses question.answer_score | N-U58-020 |
| VDR-U58-C119 | CAP-U58-04 | survey/models/survey_user_input.py:91 | `user_input.scoring_success = user_input.scoring_percentage >= user_input.survey_id.scoring_success_min` | FACT | always | — | scoring_success: True when scoring_percentage >= survey scoring_success_min | N-U58-020 |
| VDR-U58-C120 | CAP-U58-05 | survey_crm/models/survey_user_input.py:9 | `lead_id = fields.Many2one('crm.lead', ondelete='set null')` | FACT | always | — | user_input.lead_id: at most one CRM lead per submission; set null on lead deletion | N-U58-025 |
| VDR-U58-C121 | CAP-U58-05 | survey_crm/models/survey_user_input.py:30 | `def _create_leads_from_generative_answers(self):` | FACT | always | — | _create_leads_from_generative_answers: batch creates leads for inputs where any suggested_answer.generate_lead is True | N-U58-025 |
| VDR-U58-C122 | CAP-U58-05 | survey_crm/models/survey_user_input.py:61 | `'medium_id': self.env['utm.medium']._fetch_or_create_utm_medium('Survey').id,` | FACT | always | — | Survey-generated leads: UTM medium set to 'Survey' (fetched/created from utm.medium model) | N-U58-025 |
| VDR-U58-C123 | CAP-U58-05 | survey_crm/models/survey_user_input.py:63 | `'source_id': self.env['utm.mixin']._find_or_create_record('utm.source', survey.title).id,` | FACT | always | — | Survey-generated leads: UTM source set to survey title (find-or-create) | N-U58-025 |
| VDR-U58-C124 | CAP-U58-05 | survey_crm/models/survey_user_input.py:65 | `'type': 'opportunity',` | FACT | always | — | All survey-generated CRM records created as opportunities (not raw leads) | N-U58-025 |
| VDR-U58-C125 | CAP-U58-05 | survey_crm/models/survey_question.py:15 | `question.generate_lead = question.question_type in ['simple_choice', 'multiple_choice', 'matrix']` | FACT | always | — | Only choice-type questions (simple_choice, multiple_choice, matrix) can have lead-generating answers | N-U58-025 |
| VDR-U58-C126 | CAP-U58-05 | survey_crm/models/survey_question_answer.py:7 | `generate_lead = fields.Boolean('Lead creation'` | FACT | always | — | survey.question.answer.generate_lead: individual answer flag; creates lead when selected by respondent | N-U58-025 |
| VDR-U58-C127 | CAP-U58-05 | survey_crm/models/crm_lead.py:8 | `origin_survey_id = fields.Many2one('survey.survey', string='Survey', index='btree_not_null', ondelete='set null')` | FACT | always | — | crm.lead.origin_survey_id: btree index; set null on survey deletion | N-U58-025 |
| VDR-U58-C128 | CAP-U58-05 | survey_crm/models/survey_survey.py:34 | `def action_end_session(self):` | FACT | always | — | action_end_session creates leads for all user inputs created after session_start_time | N-U58-025 |
| VDR-U58-C129 | CAP-U58-06 | transifex/models/transifex_translation.py:17 | `@tools.ormcache()` | FACT | always | — | _get_transifex_projects is ORM-cached; reads .tx/config files from addon paths | N-U58-026 |
| VDR-U58-C130 | CAP-U58-06 | transifex/models/transifex_translation.py:37 | `if len(sec.split(":")) != 6:` | FACT | always | — | Supports both old TX config format (module.project) and new format (o:org:p:project:r:resource) | N-U58-026 |
| VDR-U58-C131 | CAP-U58-06 | transifex/models/transifex_translation.py:55 | `base_url = self.env['ir.config_parameter'].sudo().get_param('transifex.project_url')` | FACT | always | — | Transifex base URL read from ir.config_parameter 'transifex.project_url'; no URL means no Transifex links | N-U58-026 |
| VDR-U58-C132 | CAP-U58-06 | transifex/models/transifex_translation.py:83 | `translation['transifex_url'] = f"{base_url}/{project}/translate/#{lang_iso}/{translation['module']}/42?q=text%3A{source}"` | FACT | always | — | Generated Transifex URL: base/project/translate/#lang/module/42?q=text:source (arbitrary ID 42) | N-U58-026 |
| VDR-U58-C133 | CAP-U58-06 | transifex/models/transifex_code_translation.py:10 | `class TransifexCodeTranslation(models.Model):` | FACT | always | — | transifex.code.translation: persistent table of code-level translations with source, value, module, lang, transifex_url | N-U58-026 |
| VDR-U58-C134 | CAP-U58-06 | transifex/models/transifex_code_translation.py:32 | `self.env.cr.execute(f'LOCK TABLE {self._table} IN EXCLUSIVE MODE NOWAIT')` | FACT | always | — | Code translation load: table-level exclusive lock (NOWAIT) prevents concurrent duplicate loading | N-U58-026 |
| VDR-U58-C135 | CAP-U58-07 | utm/models/utm_mixin.py:13 | `class UtmMixin(models.AbstractModel):` | FACT | always | — | utm.mixin: abstract model providing campaign_id, source_id, medium_id fields | N-U58-027 |
| VDR-U58-C136 | CAP-U58-07 | utm/models/utm_mixin.py:48 | `def tracking_fields(self):` | FACT | always | — | tracking_fields returns 3 tuples: (utm_campaign, campaign_id, odoo_utm_campaign), (utm_source, source_id, odoo_utm_source), (utm_medium, medium_id, odoo_utm_medium) | N-U58-027 |
| VDR-U58-C137 | CAP-U58-07 | utm/models/utm_mixin.py:26 | def default_get(self, fields) | FACT | always | — | UTM default_get: UTM cookies ignored for salesperson users (except superuser) | N-U58-027 |
| VDR-U58-C138 | CAP-U58-07 | utm/models/utm_mixin.py:88 | `def _find_or_create_record(self, model_name, name):` | FACT | always | — | _find_or_create_record: case-insensitive search (ilike) with active_test=False; creates if not found | N-U58-027 |
| VDR-U58-C139 | CAP-U58-07 | utm/models/ir_http.py:21 | `response.set_cookie(cookie_name, request.params[url_parameter], max_age=31 * 24 * 3600, domain=domain, cookie_type='optional')` | FACT | always | — | UTM cookies: 31-day max_age, type='optional'; stored in _post_dispatch | N-U58-027 |
| VDR-U58-C140 | CAP-U58-07 | utm/models/utm_campaign.py:13 | `name = fields.Char(string='Campaign Identifier'` | FACT | always | — | Campaign has two name fields: title (display name, translatable) and name (unique identifier, not translated, computed from title) | N-U58-028 |
| VDR-U58-C141 | CAP-U58-07 | utm/models/utm_campaign.py:28 | `is_auto_campaign = fields.Boolean(default=False` | FACT | always | — | is_auto_campaign flag distinguishes automatically created campaigns from manually created ones | N-U58-028 |
| VDR-U58-C142 | CAP-U58-07 | utm/models/utm_medium.py:53 | `def _fetch_or_create_utm_medium(self, name, module='utm'):` | FACT | always | — | _fetch_or_create_utm_medium: normalizes name (spaces/dots → underscores, lowercase), tries env.ref, creates + ir.model.data if not found | N-U58-028 |
| VDR-U58-C143 | CAP-U58-07 | utm/models/utm_medium.py:43 | `def _unlink_except_utm_medium_record(self):` | FACT | always | — | 6 required mediums protected from deletion (at_uninstall=False): Email, Direct, Website, X, Facebook, LinkedIn | N-U58-028 |
| VDR-U58-C144 | CAP-U58-07 | utm/models/utm_source.py:51 | `class UtmSourceMixin(models.AbstractModel):` | FACT | always | — | utm.source.mixin: abstract model for records that auto-create their utm.source on creation (e.g. mass mailings) | N-U58-029 |
| VDR-U58-C145 | CAP-U58-07 | utm/models/utm_source.py:32 | `def _generate_name(self, record, content):` | FACT | always | — | UTM source name generation: content truncated to 20 chars + ellipsis + model description + create_date | N-U58-029 |
| VDR-U58-C146 | CAP-U58-01 | stock_account/models/res_company.py:371 | `self.env['ir.default'].set('product.category', 'property_valuation', company.inventory_valuation, company_id=company.id)` | FACT | always | — | _set_category_defaults: propagates company valuation/cost_method/journal/account as defaults to product.category | N-U58-002 |
| VDR-U58-C147 | CAP-U58-04 | survey/models/survey_survey.py:381 | `survey.session_available = survey.survey_type in {'live_session', 'custom'} and not survey.certification` | FACT | always | — | Live sessions available only for live_session and custom survey types AND only when not a certification | N-U58-022 |
| VDR-U58-C148 | CAP-U58-04 | survey/models/survey_user_input.py:44 | `access_token = fields.Char('Identification token', default=lambda self: str(uuid.uuid4())` | FACT | always | — | user_input access_token: UUID4, readonly, unique, not copied | N-U58-024 |
| VDR-U58-C149 | CAP-U58-01 | stock_account/models/analytic_account.py:33 | `def _perform_analytic_distribution(self, distribution, amount, unit_amount, lines, obj, additive=False):` | FACT | always | — | Stock moves distribute amounts to analytic accounts; rounding correction applied per plan to prevent total drift | N-U58-030 |
| VDR-U58-C150 | CAP-U58-01 | stock_account/models/res_config_settings.py:7 | `module_stock_landed_costs = fields.Boolean("Landed Costs"` | FACT | always | — | Landed costs enabled via module_stock_landed_costs setting (installs stock_landed_costs module) | N-U58-004 |
