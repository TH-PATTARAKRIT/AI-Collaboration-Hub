# U58 — Neutral Knowledge: Inventory Valuation, Survey, and UTM (Odoo 19 Community)

> NEUTRAL KNOWLEDGE — NOT RESTRICTED
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U58
- Modules: stock account, stock maintenance, stock sms, survey, survey crm, transifex, utm
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Purpose: Architecture and behavioral summary for planning use; no V-levels, no Gate PASS, no fabrication.

---

## ARCHITECTURE NOTE: Breaking Change in stock account (Odoo 19)

Odoo 19 Community completely redesigns inventory valuation. The stock valuation layer model that existed in Odoo 16/17 does NOT exist in Odoo 19. Valuation is stored directly on stock move value (a monetary field). Manual adjustments and price changes are tracked in a new product value model. Teams migrating from Odoo 16/17 must account for this data model change — there is no SVL to migrate, and any custom code referencing stock valuation layer will break.

---

## [N-U58-001]: Cost Methods (stock account)

**Neutral summary:**
Odoo 19 supports three inventory cost methods, configured at company level (default) and overrideable at product category level:

- **Standard Price**: Fixed cost per unit; value = qty * standard price. Easiest to operate. Changes tracked in product value.
- **AVCO (Average Cost)**: Weighted average recalculated with each incoming move. Stored incrementally for performance. Negative stock edge cases handled.
- **FIFO (First In First Out)**: Cost of outgoing stock taken from the earliest available incoming moves. FIFO stack maintained per product (and per lot for lot-valuated products).

All three are computed fields on product template; the actual configuration lives on product category or res company.

---

## [N-U58-002]: Valuation Modes (stock account)

**Neutral summary:**
Two modes:

- **Periodic**: No automatic journal entries on stock moves. Accounting entries are created manually (or by cron) when "closing" the inventory period. Simpler operationally; less real-time visibility.
- **Real-time (Perpetual)**: Journal entries posted automatically when stock moves are validated. Provides continuous accounting view. Required for Anglo-Saxon cost-of-goods-sold (COGS) at invoicing.

Mode is configured at company level (inventory valuation) and overrideable at product category level.

---

## [N-U58-003]: Lot-Level Valuation (stock account)

**Neutral summary:**
Products can enable lot valuated (Boolean on product template, disabled when tracking='none'). When active:

- Each stock lot has its own standard price (company-dependent), initialized from the product's standard price at lot creation.
- Lot value is computed independently using the product's cost method (standard, AVCO, or FIFO) restricted to moves with that lot.
- FIFO stack and AVCO computation operate per lot.
- Quant value for lot-valuated products: proportional share of lot total value.

---

## [N-U58-004]: Journal Entries and Account Mapping (stock account)

**Neutral summary:**
When valuation == 'real time' and a stock move affects a location with a valuation account id:

- _create_account_move posts one account move per validated batch to company account stock journal id.
- Debit and credit determined by move direction and location accounts.
- _should_create_account_move: conditions include storable product, valued, location has valuation account, non-zero quantity, real time mode.

Account resolution hierarchy:
1. Location's valuation account id (special locations)
2. Product category's property stock valuation account id
3. Company's account stock valuation id

Stock variation account: account general ledger account type stock variation id.

Landed costs feature enabled via module stock landed costs config setting (installs separate module).

---

## [N-U58-005]: AVCO and Standard Price Update (stock account)

**Neutral summary:**

**AVCO recomputation** has two paths:
- Full batch: _run_average_batch iterates all historical incoming and outgoing moves to compute current average. Used for display and reporting.
- Incremental fast path: _update_standard_price(extra value, extra qty) applies the AVCO formula incrementally after each new in-move, without reading historical data. Formula: new avg = (old qty * old avg + extra value) / new qty. This is the normal runtime path.

**AVCO on invoice post**: When a customer invoice is posted for real time products, the linked stock moves are re-valued using the invoice price, updating standard price accordingly.

**Standard price update** for lot-valuated FIFO: _update_standard_price computes total value / qty available and sets standard price. For standard cost, no update occurs (manual only).

---

## [N-U58-006]: Manual Valuation Override — product value (stock account)

**Neutral summary:**
The product value model (new in Odoo 19; replaces SVL revaluation wizard) tracks:

- Standard price changes (user updates product template standard price)
- Lot price changes (user updates stock lot standard price)
- Manual move value overrides (user edits stock move value manual)

Each record stores: product id, lot id (optional), move id (optional), value (monetary), date, user, description.

On creation: if move id is set, triggers _set_value() on that move to re-apply valuation. If lot id + product id set without move, triggers _update_standard_price() on the product.

---

## [N-U58-007]: FIFO Algorithm (stock account)

**Neutral summary:**
The FIFO stack:

1. _run_fifo_get_stack builds the stack by searching incoming done moves (DESC date order, limit 100 initially, expands as needed). Tracks remaining qty per move.
2. _run_fifo pops stack entries to cover the requested outgoing quantity. Uses proportional pricing for partial quantities. If stack exhausted, extrapolates using last known price.
3. Concurrent batch handling: when multiple moves validated simultaneously, fifo qty already processed context prevents double-counting.

FIFO remaining value: for FIFO products, remaining qty / valued qty * move value (proportional).

---

## [N-U58-008]: COGS and Anglo-Saxon Accounting (stock account)

**Neutral summary:**
Anglo-Saxon accounting mode (company-level setting) generates Cost of Goods Sold journal entries on customer invoice posting (rather than at shipment):

- account move _post override calls _stock_account_prepare_realtime_out_lines_vals
- For each customer invoice line with a real time, storable, non-dropshipped product:
  - Debit: COGS / stock variation / expense account
  - Credit: stock valuation account
- COGS value sourced from _get_cogs_value on the invoice line, which calls _get_cogs_price_unit on linked stock moves.
- COGS lines can be unwound on button draft / button cancel.

On purchase bill posting (Anglo-Saxon): _compute_account_id sets the account to stock valuation for perpetual storable products.

---

## [N-U58-009]: Stock Move Valuation Engine (stock account)

**Neutral summary:**
stock move _set_value is the central valuation engine:

1. For incoming moves: calls _get_value(quantity, move line) which dispatches via _get_value_data priority chain.
2. For outgoing moves: FIFO uses _run_fifo; AVCO and standard cost uses standard price * valued qty.
3. For lot-valuated products: in-moves trigger lot recompute; out-moves use lot standard price * move line quantity.
4. Correction mode: _set_value(correction quantity=delta) called when move lines are edited post-validation.

_get_value_data priority chain for incoming:
1. Manual override (product value with move id)
2. Invoice or bill line (purchase price)
3. Production context
4. Sale or purchase quotation or order price
5. Returns (proportional from origin move)
6. Standard price fallback

---

## [N-U58-010]: Dropship and Consignment (stock account)

**Neutral summary:**

**Dropship**: Source=supplier, destination=customer (both non-company locations). Detected by _is_dropshipped(). Dropshipped moves create their own journal entries (different logic). COGS is skipped on invoice for dropshipped lines.

**Consignment**: Goods owned by a third party stored in company location. _is_consigned_valued_line detects these. Consigned goods excluded from company valuation but still influence AVCO weighted average for COGS calculation.

---

## [N-U58-011]: Location Valuation (stock account)

**Neutral summary:**
_should_be_valued() on stock location: True for internal and transit locations that have a company id. Locations without a company id (e.g. inter-company transit routes) are NOT valued.

Locations can have a specific valuation account id. When present, moves source and destination that location create journal entries against that account. Without this, standard internal moves do not generate accounting entries.

is valued internal / is valued external are computed Boolean flags for display and filtering.

---

## [N-U58-012]: Periodic Inventory Closing (stock account)

**Neutral summary:**
res company action close stock valuation:
1. Computes physical stock value by account (stock value()).
2. Computes accounting balance by account (stock accounting value()).
3. Posts adjustment journal entry to reconcile differences.
4. Updates _get_last_closing_date.

_cron_post_stock_valuation: Runs for companies with inventory period = 'daily' (every day) or 'monthly' (last day of month only). Companies with inventory period = 'manual' are excluded.

_get_continental_realtime_variation_vals: For continental (non-Anglo-Saxon) companies with perpetual valuation, posts variation entry over the period.

---

## [N-U58-013]: Lock Date and Backdating (stock account)

**Neutral summary:**
stock picking _check_backdate_allowed: Raises ValidationError when date done falls within a locked fiscal period (accounting lock date). Can be bypassed via skip lock date check ir config parameter for exceptional cases.

stock quant accounting date: Allows specifying an accounting date different from the physical inventory date. Used with force period date context in _apply_inventory.

Inventory adjustment wizard (stock inventory adjustment name) gains accounting date field for setting the accounting period independently of the physical date.

---

## [N-U58-014]: AVCO Audit Report (stock account)

**Neutral summary:**
stock avco report is an abstract SQL view (read-only) that unions stock move data with product value data for AVCO and FIFO cost method products only. Useful for auditing the cost history and understanding how average costs evolved over time. Available as a backend report.

---

## [N-U58-015]: stock maintenance Bridge

**Neutral summary:**
stock maintenance (auto install=True, depends: stock + maintenance) links maintenance equipment to inventory:

- maintenance equipment gains location id (internal locations only) to track where equipment is physically deployed.
- match serial smart button appears when equipment serial no matches a stock lot name (requires production lot group permission).
- stock location gains equipment count smart button to view all equipment assigned to that location.

Use case: cross-reference equipment serial numbers with inventory lots; navigate from equipment form to its lot record.

---

## [N-U58-016]: stock sms Bridge

**Neutral summary:**
stock sms (auto install=True, depends: stock + sms) adds SMS confirmation for outgoing deliveries:

- First time a company validates an outgoing delivery with a partner phone number and SMS enabled, a wizard appears asking whether to enable SMS confirmation.
- confirm stock sms wizard: "Send SMS" enables the feature and validates; "Don't Send" disables the feature and validates without SMS.
- The one-time warning is controlled by has received warning stock sms Boolean on res company.
- After activation, _send_confirmation_email sends SMS using stock sms confirmation template id template on every outgoing delivery validation.

---

## [N-U58-017]: Survey Engine Overview

**Neutral summary:**
survey survey supports 4 types:
- survey: Standard questionnaire
- live session: Real-time group sessions (presenter-controlled)
- assessment: Scored assessment
- custom: General purpose

All types share the same question and answer model. Differences are in available features: live sessions add session code, speed rating, real-time question control. Assessments and certifications add scoring thresholds and badge awards.

Survey inherits mail thread + mail activity mixin (full chatter).

---

## [N-U58-018]: Survey Layout and Question Selection

**Neutral summary:**
questions layout (required):
- page per question: Each question on its own page
- page per section: Questions grouped by section or page dividers
- one page: All questions on a single page

questions selection:
- all: Every question shown
- random: Random subset per section (uses random questions count on the section or page question record); randomization ignored for live sessions

---

## [N-U58-019]: Survey Access Control

**Neutral summary:**
access mode:
- public: Anyone with the link can access (no authentication required)
- token: Only invited users (access via invite token)

is attempts limited (Boolean + attempts limit): Restricts how many times the same user can complete the survey. Incompatible with public+unauthenticated mode. Incompatible with conditional questions (because attempt counting uses invite token pooling).

---

## [N-U58-020]: Survey Scoring

**Neutral summary:**
Scoring types:
- no scoring: No scores calculated
- scoring with answers after page: Score and correct answers shown after each page
- scoring with answers: Score and answers shown at end
- scoring without answers: Score shown but not correct answers

scoring success min (default 80.0%): Threshold for "pass".

Scoring computation:
- simple choice: uses highest positive-scored answer selected
- multiple choice: sums all positive-scored answers selected
- Other question types: uses question answer score directly

scoring percentage, scoring total, scoring success are stored computed fields on survey user input (performance optimization to avoid full recompute on every read).

---

## [N-U58-021]: Survey Certification

**Neutral summary:**
certification requires scoring type != 'no scoring' (DB CHECK constraint). When enabled:

- certification badge id: Unique gamification badge awarded on passing (UNIQUE constraint: one badge per survey).
- certification mail template id: Email template for certificate delivery.
- certification report layout: Layout for the PDF certificate.
- Live session mode is NOT available for certifications.

---

## [N-U58-022]: Live Sessions

**Neutral summary:**
Live session mode enables real-time group survey sessions:

- session state: ready (waiting for participants) / in progress (question active)
- session code: Short unique code attendees use to join (UNIQUE constraint)
- session question id: Currently displayed question (presenter controls progression)
- session speed rating: Optional bonus points for fast answers (requires positive session speed rating time limit)
- session available: Only for survey type in {live session, custom} AND NOT certification

Lead generation from live sessions triggered via action end session (survey crm).

---

## [N-U58-023]: Question Types

**Neutral summary:**
Nine question types:
- simple choice: Single-select from answers
- multiple choice: Multi-select from answers
- text box: Free-form multi-line text
- char box: Single-line text (can save as email or nickname)
- numerical box: Numeric input
- scale: Range slider (configurable minimum and maximum, default 0-10)
- date: Date picker
- datetime: Date + time picker
- matrix: Grid of rows × columns (simple or multiple choice per row)

Conditional display: triggering answer ids — question only shown if specified answer(s) were previously selected.

---

## [N-U58-024]: Survey User Input

**Neutral summary:**
survey user input represents one survey completion attempt:

- State machine: new → in progress → done
- access token (UUID4): URL token for respondent access; unique, not copied
- invite token: Groups attempts from the same invitation pool (used for attempt counting)
- is session answer: True for live session participants

Time limits:
- Survey-level: is time limited + time limit (minutes); checked by _compute_survey_time_limit_reached
- Question-level: is time limited (live sessions only); checked by _compute_question_time_limit_reached

Attempt tracking uses raw SQL for performance (_compute_attempts_info).

---

## [N-U58-025]: survey crm Bridge

**Neutral summary:**
survey crm (depends: survey + crm) adds lead generation from survey responses:

- Per-answer flag: survey question answer generate lead (Boolean)
- Only choice-type questions can have lead-generating answers (simple choice, multiple choice, matrix)
- On survey completion (_mark_done) OR live session end (action end session): leads created for respondents who selected lead-generating answers
- Lead values: type=opportunity, medium='Survey', source=survey title, team=survey team id, description=HTML of all answers
- crm lead origin survey id: back-link to originating survey (btree index, set null on delete)
- crm team origin survey ids: back-link from team to surveys using that team

---

## [N-U58-026]: Transifex Integration

**Neutral summary:**
transifex module provides links from Odoo's translation UI to Transifex translation interface.

- Parses .Transifex configuration files in addon paths to map module names to Transifex projects; ORM-cached.
- Supports both old format (odoo-16.base) and new format (o:odoo:p:odoo-16:r:base).
- When transifex project url system parameter is set, translation records gain a transifex url field linking directly to the relevant string in the Transifex editor.
- URL format: {base url}/{project}/translate/#{lang iso}/{module}/42?q=text:{source}
- transifex code translation: stores code-level translations loaded from addon source. Loading uses table-level EXCLUSIVE LOCK NOWAIT to prevent concurrent duplicates.

---

## [N-U58-027]: UTM Mixin

**Neutral summary:**
utm mixin (abstract) provides campaign, source, and medium tracking to any model that inherits it:

- Three Many2one fields: campaign id, source id, medium id (btree not null index on each)
- tracking fields(): returns mapping of URL params → ORM fields → cookie names
- default get(): auto-populates UTM fields from browser cookies on record creation (ignored for salesperson users)
- _find_or_create_record(): case-insensitive find-or-create for UTM models

Cookie flow (ir http):
1. Visitor hits URL with ?utm campaign=X&utm source=Y&utm medium=Z
2. _post_dispatch calls _set_utm() which saves cookies for 31 days
3. Next form open: default get reads cookies and pre-fills UTM fields

---

## [N-U58-028]: UTM Models

**Neutral summary:**

**utm campaign**: Has both title (display, translatable) and name (unique identifier, computed from title). is auto campaign flag distinguishes auto-created campaigns. stage id and tag ids for kanban management. Ordered by name.

**utm medium**: name required, unique, NOT translated. Protected mediums (cannot delete): Email, Direct, Website, X, Facebook, LinkedIn. _fetch_or_create_utm_medium(name): normalizes to lowercase+underscores, tries env ref, creates + ir model data if not found.

**utm source**: name unique. _generate_name truncates content to 20 chars + model description + date.

**utm stage**: ordered by sequence. **utm tag**: random color 1-11.

---

## [N-U58-029]: UtmSourceMixin

**Neutral summary:**
utm source mixin (abstract): For models that auto-create their own utm source record on creation (e.g. mass mailings, campaigns). Provides name + source id fields. On create(), auto-generates and links a utm source using _generate_name.

---

## [N-U58-030]: Analytic Distribution on Stock Moves

**Neutral summary:**
stock the analytics model account provides _perform_analytic_distribution and _calculate_distribution_amount. When stock moves have analytic distribution configured, amounts are distributed across analytic accounts. A rounding correction is applied per analytic plan to prevent the sum of distributed amounts drifting from the total (the last distribution line absorbs any floating-point rounding error).

---

## SUMMARY TABLE

| Area | Key Points | Migration Alert |
|---|---|---|
| stock account valuation | 3 cost methods, 2 valuation modes, new product value replaces SVL | CRITICAL: no SVL in Odoo 19 |
| FIFO algorithm | Stack per product and lot, concurrent batch handling, exhaustion extrapolation | FIFO stack different from Odoo 16/17 |
| AVCO | Incremental fast path + full historical batch; negative stock handled | AVCO formula unchanged but implementation restructured |
| Lot valuation | Per-lot standard price, initialized on create, full FIFO and AVCO and standard cost support | New capability in Odoo 19 |
| COGS (Anglo-Saxon) | Created at invoice posting, not shipment; debit COGS and credit stock valuation | Verify COGS account mapping on migration |
| Periodic closing | action close stock valuation + cron; posts difference entry | New UX vs Odoo 16/17 |
| stock maintenance | Equipment ↔ location link, serial matching | Auto-installs with stock+maintenance |
| stock sms | One-time warning wizard, company SMS template | Auto-installs with stock+sms |
| Survey engine | 4 types, 9 question types, scoring and certification, live sessions | Feature-complete in Community |
| survey crm | Per-answer lead generation, UTM medium='Survey' | Requires both survey + crm modules |
| Transifex | TX config parsing, URL generation, code translation table | Only useful when TX project URL configured |
| UTM | Cookie persistence 31d, mixin pattern, 3-dimension tracking, protected mediums | utm mixin widely used across CRM, email, and website |
