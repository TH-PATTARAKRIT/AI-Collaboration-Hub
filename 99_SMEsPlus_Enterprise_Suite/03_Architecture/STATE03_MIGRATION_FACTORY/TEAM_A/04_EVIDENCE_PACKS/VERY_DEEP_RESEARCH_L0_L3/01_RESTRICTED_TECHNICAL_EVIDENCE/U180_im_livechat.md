# U180 — im_livechat: Restricted Technical Evidence
**Unit:** U180 | **Group:** G13 | **Priority:** P2 | **Status:** NOT_STUDIED → STUDIED
**Source base:** `odoo-19.0.post20260921/odoo/addons/im_livechat/`
**Evidence depth:** L0–L3 (source-verified, no fabrication)

---

## 1. Core Channel Model — `im_livechat.channel`
**File:** `models/im_livechat_channel.py`

The primary configuration record is `im_livechat.channel` (`_name = 'im_livechat.channel'`), which inherits `rating.parent.mixin`.

### Key fields
| Field | Type | Notes |
|---|---|---|
| `name` | Char | Channel name, required |
| `user_ids` | Many2many `res.users` | M2M via `im_livechat_channel_im_user` table; these are "Agents" |
| `available_operator_ids` | Many2many `res.users` (computed) | Filters `user_ids` by online status, max sessions, call status |
| `channel_ids` | One2many `discuss.channel` | All livechat sessions spawned by this channel |
| `rule_ids` | One2many `im_livechat.channel.rule` | URL-based rules that attach chatbot scripts |
| `max_sessions_mode` | Selection (unlimited / limited) | Controls per-operator concurrency limit |
| `max_sessions` | Integer | Max concurrent sessions per operator when mode = limited |
| `block_assignment_during_call` | Boolean | Prevents new chat assignment while operator is in RTC call |
| `chatbot_script_count` | Integer (computed) | Count of distinct chatbot scripts in rules |

**No `website_id` field** exists on `im_livechat.channel` in Community edition. The module declares no dependency on `website`. Multi-website scoping is an Enterprise/website bridge concern only.

---

## 2. `discuss.channel` Extension for Livechat Sessions
**File:** `models/discuss_channel.py`

Each livechat conversation is stored as a `discuss.channel` record with `channel_type = 'livechat'`. The model uses `_inherit = ['rating.mixin', 'discuss.channel']`.

### Livechat-specific fields added to `discuss.channel`
| Field | Type | Notes |
|---|---|---|
| `livechat_channel_id` | Many2one `im_livechat.channel` | Back-reference to parent configuration channel |
| `livechat_operator_id` | Many2one `res.partner` | The assigned operator's partner; NOT NULL constraint enforced |
| `livechat_end_dt` | Datetime | NULL while session is active; set on close |
| `chatbot_current_step_id` | Many2one `chatbot.script.step` | Tracks active chatbot step |
| `chatbot_message_ids` | One2many `chatbot.message` | All bot messages in this session |
| `livechat_status` | Selection (in_progress/waiting/need_help) | Cleared when session closes (`livechat_end_dt` set) |
| `livechat_failure` | Selection (no_answer/no_agent/no_failure) | Outcome tracking for sessions that failed |
| `livechat_outcome` | Selection (no_answer/no_agent/no_failure/escalated) | Computed from escalation and failure |
| `livechat_is_escalated` | Boolean (stored) | True when `len(livechat_agent_history_ids) > 1` |
| `country_id` | Many2one `res.country` | Visitor's country (GeoIP or authenticated user) |
| `livechat_lang_id` | Many2one `res.lang` | Visitor's language preference from cookie |
| `duration` | Float | Computed: `(livechat_end_dt or now - create_date)` in hours |

**DB constraint:** `CHECK((channel_type = 'livechat' and livechat_operator_id is not null) or (channel_type != 'livechat'))` — every livechat session must have an operator.

**Index:** `(livechat_end_dt) WHERE livechat_end_dt IS NULL` — partial index for ongoing sessions lookups.

---

## 3. Operator Availability Computation
**File:** `models/im_livechat_channel.py` — `_get_available_operators_by_livechat_channel()`

An operator is considered available if ALL of:
1. `user.sudo().presence_ids.status == "online"` (checked via `bus.presence` / `res.users.presence`)
2. If `max_sessions_mode == 'limited'`: ongoing active session count < `max_sessions` for that channel
3. If `block_assignment_during_call = True`: operator must not be in an RTC call (`user.sudo().is_in_call`)

Active session count is measured by `_get_ongoing_session_count_by_agent_livechat_channel()`, which queries `discuss.channel.member` joined to `discuss.channel` where `livechat_end_dt IS NULL` and `last_interest_dt >= "-15M"` (last 15 minutes), grouped by `(partner_id, livechat_channel_id)`.

---

## 4. Operator Selection Algorithm — `_get_operator()`
**File:** `models/im_livechat_channel.py`

Priority-ordered operator selection:

**Step 1 — Previous operator sticky return**
If `previous_operator_id` is in `available_operator_ids` AND the previous operator has `count < 2` active chats OR is not in a call → return previous operator immediately.

**Step 2 — Buffer enforcement**
`BUFFER_TIME = 120` seconds. Operators who received a new session within the last 120 seconds are deprioritised (agents_failing_buffer). They are only excluded if a buffer-respecting candidate exists.

**Step 3 — Preference cascade (8 tiers)**
From highest to lowest priority:
1. `same_language AND all_expertises`
2. `same_language AND one_expertise`
3. `same_language`
4. `same_country AND all_expertises`
5. `same_country AND one_expertise`
6. `same_country`
7. `all_expertises`
8. `one_expertise`

For each tier, `_get_less_active_operator()` is called on the filtered set.

**Step 4 — _get_less_active_operator() logic**
SQL query fetches per-operator: `COUNT(DISTINCT h.channel_id)` active chats (sessions open in last 30 min) and `in_call` boolean. Ordered `ASC` by count, with call status as secondary sort. Selection rules:
- If any operator has no recent active chats → `random.choice()` among those "inactive" operators.
- Otherwise → random choice among operators sharing the best `(count, in_call)` status tuple.

**Not strictly round-robin**: uses random.choice() among equally-qualified candidates at each tier.

---

## 5. Chatbot Script Model — `chatbot.script`
**File:** `models/chatbot_script.py`

`_name = 'chatbot.script'`, inherits `image.mixin`, `utm.source.mixin`.

| Field | Type | Notes |
|---|---|---|
| `title` | Char | Required; also sets the `operator_partner_id.name` |
| `operator_partner_id` | Many2one `res.partner` | Auto-created inactive partner on script creation; acts as bot author |
| `script_step_ids` | One2many `chatbot.script.step` | Ordered steps |
| `active` | Boolean | Soft-delete |

**Step types** (`chatbot.script.step.step_type`):
| Value | UI label | Behaviour |
|---|---|---|
| `text` | Text | Bot posts message, no visitor input expected |
| `question_selection` | Question | Bot posts answers; visitor picks one; routes next step via `triggering_answer_ids` |
| `question_email` | Email | Expects visitor email input; validated by `email_normalize` |
| `question_phone` | Phone | Free phone input |
| `forward_operator` | Forward to Operator | Triggers `discuss_channel._forward_human_operator()`; removes bot from channel, adds human |
| `free_input_single` | Free Input | Single-line text answer |
| `free_input_multi` | Free Input (Multi-Line) | Multi-line text answer |

**Welcome steps** (`_get_welcome_steps()`): All leading `text` steps plus the first non-text step. These are displayed client-side without being persisted as `mail.message` records until the visitor first interacts.

**Chatbot operator_partner creation**: On `create()`, if no `operator_partner_id` is supplied, a `res.partner` with `active=False` is created automatically. This inactive partner is used as the `author_id` for all bot-posted messages.

**Step transition logic** (`_fetch_next_step()`): Finds the next step whose `triggering_answer_ids` are ALL satisfied by visitor answers (AND across different parent steps; OR within the same parent step's answers). If no triggering answers required on the step, it matches unconditionally.

---

## 6. Visitor / Anonymous User Tracking
**Files:** `models/discuss_channel.py`, `models/discuss_channel_member.py`, `controllers/main.py`

There is **no** `im_livechat.visitor` model in Community edition. Anonymous visitors are tracked using `mail.guest` (defined in `mail` module).

**Flow:**
1. `get_session` controller calls `mail.guest._get_or_create_guest()` for public users.
2. Guest is identified by cookie: `guest._format_auth_cookie()` returns a signed token stored in the browser.
3. The guest record carries: `name` (defaulting to "Visitor"), `country_id`, `timezone`, `offline_since`, `avatar_128`.
4. `_get_guest_from_context()` resolves the guest from the request context throughout the session.
5. On `discuss.channel.member` creation for livechat channels, member type is set: if the guest is already in `livechat_customer_guest_ids` → `livechat_member_type = "visitor"`, otherwise defaults to `"agent"`.

**Authenticated visitors** use `partner_id` directly; anonymous visitors use `guest_id`. The `im_livechat.channel.member.history` model stores both paths with a `CHECK(partner_id IS NULL OR guest_id IS NULL)` constraint.

---

## 7. Session Close Logic
**File:** `models/discuss_channel.py` — `_close_livechat_session()`, `_action_unfollow()`

**Explicit close (`_close_livechat_session()`):**
1. If `livechat_end_dt` is already set, no-op.
2. If current user is a member, calls `member.sudo()._rtc_leave_call()` to exit any active RTC session.
3. Sets `self.sudo().livechat_end_dt = fields.Datetime.now()`.
4. Broadcasts `livechat_end_dt` update via bus (`Store(bus_channel=self).add(self, "livechat_end_dt").bus_send()`).
5. Posts "Visitor left the conversation." system notification message (unless the channel has no messages).

**Auto-close on last operator leaving (`_action_unfollow()`):**
When a member unfollows and the channel is a livechat with `member_count == 1` remaining (only the visitor left) → sets `livechat_end_dt` and broadcasts.

**Auto-vacuum:**
- `_gc_empty_livechat_sessions()` (autovacuum): Deletes `discuss.channel` livechat records with no messages and `write_date` older than 1 hour.
- `_gc_bot_only_ongoing_sessions()` (autovacuum): Closes bot-only sessions (`livechat_agent_partner_ids = False`) with `last_interest_dt` older than 1 day.
- `_gc_unpin_livechat_sessions()` (autovacuum, via `discuss.channel.member`): Unpins and closes sessions where `last_seen_dt <= now - 1 day` and no unread messages.

---

## 8. CRM Lead Creation
**Status: Not present in core `im_livechat` Community module.**

The method `_convert_visitor_to_lead()` does not exist in `models/discuss_channel.py` or any other file under `im_livechat/models/`. CRM lead creation from chatbot conversations is implemented in the bridge module `im_livechat_crm` (separate addon). The `chatbot.script.step.step_type` does not include a `create_lead` value in Community; that is an Enterprise step type added by `im_livechat_crm`.

The evidence shows `_chatbot_prepare_customer_values()` in `chatbot_script_step.py` which extracts email, phone, and partner — this is used by downstream bridge modules to create leads/tickets but does no CRM work itself.

---

## 9. Multi-Website Scoping
**Status: Not present in Community `im_livechat`.**

There is no `website_id` field on `im_livechat.channel`. The module's `__manifest__.py` does not declare `website` as a dependency. The channel is accessible via `web_page` URL (`/im_livechat/support/<id>`) and the embed script — both are Odoo-instance-wide, not website-scoped.

Multi-website restriction (per-website channel visibility) is an Enterprise feature delivered by `website_livechat` or similar bridge modules.

---

## 10. Operator Agent Relationship — `user_ids`
**File:** `models/im_livechat_channel.py`

```
user_ids = fields.Many2many(
    'res.users',
    'im_livechat_channel_im_user',
    'channel_id', 'user_id',
    string='Agents',
    default=_default_user_ids
)
```

- Junction table: `im_livechat_channel_im_user`
- Default: creator user is auto-added.
- Operators can join via `action_join()` (requires group `im_livechat.im_livechat_group_user`) or be removed via `action_quit()`.
- When a user loses the livechat group, `res.users.write()` override automatically removes them from all livechat channels.

---

## 11. Operator Notification on New Chat Request
**File:** `controllers/main.py` — `get_session()` route; `models/discuss_channel.py` — `_broadcast()`

Flow:
1. Visitor calls `POST /im_livechat/get_session` (JSON-RPC, auth=public).
2. Controller selects operator, creates `discuss.channel` with `livechat_operator_id = operator_partner`.
3. Calls `channel._broadcast([channel.livechat_operator_id.id])`.
4. `_broadcast()` (inherited from `discuss.channel` in `mail` module) pushes a bus message to each listed partner's bus channel.
5. The operator's browser receives a `discuss.channel/notifications` bus event via the Odoo long-polling / websocket bus, causing the discuss app to open or badge the new chat.

For chatbot-initiated sessions where the chatbot IS the operator, `_broadcast()` is skipped (no human notification needed). The condition: `if not is_chatbot_script or chatbot_script.operator_partner_id != channel.livechat_operator_id`.

---

## 12. Channel Rules — `im_livechat.channel.rule`
**File:** `models/im_livechat_channel.py`

Each rule defines:
- `regex_url`: regex matched against the visitor's page URL.
- `action`: display_button / display_button_and_text / auto_popup / hide_button.
- `auto_popup_timer`: seconds delay before auto-open.
- `chatbot_script_id`: Many2one `chatbot.script` — if set, bot takes operator role for this URL.
- `chatbot_enabled_condition`: always / only_if_no_operator / only_if_operator.
- `country_ids`: optional country filter (requires GeoIP).
- `sequence`: lower = higher priority.

`match_rule()` tries country-specific rules first, then country-agnostic rules. A chatbot rule is skipped if the script is inactive or has no steps.

---

## 13. `im_livechat.channel.member.history` — Audit Trail
**File:** `models/im_livechat_channel_member_history.py`

One history record per `discuss.channel.member` in a livechat session. Stores:
- `livechat_member_type`: agent / visitor / bot (stored, not computed at query time)
- `partner_id` / `guest_id`: resolved from member
- `chatbot_script_id`: for bot members
- `response_time_hour`: time from history creation to first agent message
- `message_count`: messages by this member
- `session_duration_hour`: time from history creation to session close
- `rating_id`: linked `rating.rating` for agent/bot members

Unique constraints: one history per `member_id`; one partner per channel; one guest per channel.

---

## 14. Chatbot Forwarding — `_forward_human_operator()`
**File:** `models/discuss_channel.py`

When a `forward_operator` step fires:
1. `_get_human_operator()` calls `livechat_channel_id._get_operator()` with expertise filter from the chatbot step.
2. If a human operator is found and is not the current user:
   - The chatbot step's message is posted.
   - The human operator is added to the channel as `livechat_member_type = "agent"`.
   - The bot partner is removed via `_action_unfollow(partner=bot_partner_id, post_leave_message=False)`.
   - `livechat_operator_id` is updated to the human operator's partner.
   - Channel is renamed to include the human operator's name.
   - `_broadcast(human_operator.partner_id.ids)` notifies the human operator.
3. If no operator found: `livechat_failure = "no_agent"` is set.

**Escalation detection:** `livechat_is_escalated = len(livechat_agent_history_ids) > 1` (more than one unique agent has been in the session).

---

## 15. Mail Guest — Anonymous Visitor Identity
**Source:** `mail` module (`mail/models/mail_guest.py`)

The `mail.guest` model provides:
- `name`: display name ("Visitor" by default)
- `country_id`, `timezone`: set from GeoIP and request
- `offline_since`: used for presence detection
- `avatar_128`: randomly generated

The `_get_or_create_guest()` method searches for an existing guest by access token cookie, creates one if missing. Cookie is signed to prevent tampering.

---

## 16. Expertise System — `im_livechat.expertise`
**File:** `models/im_livechat_expertise.py` (implied from field references)

Operators declare expertise areas via `res.users.livechat_expertise_ids`. The operator selection algorithm uses these to match visitor intent. Chatbot `forward_operator` steps can specify `operator_expertise_ids` to target operators with matching skills.

---

## 17. Chatbot Script Answer Branching
**File:** `models/chatbot_script_step.py`

Steps with `step_type = 'question_selection'` present answer options to the visitor. Each `chatbot.script.answer` belongs to one step (`script_step_id`). Subsequent steps use `triggering_answer_ids` (Many2many to `chatbot.script.answer`) to conditionally appear.

Logic in `_fetch_next_step()`:
- Groups `triggering_answer_ids` by their parent step.
- Requires at least one answer from EACH parent step's group to be selected (AND across steps).
- Within one parent step's answers, any match is sufficient (OR within step).

---

## 18. Session Status Transitions
**File:** `models/discuss_channel.py`

`livechat_status` transitions:
- Created: `"in_progress"` (set in `_get_livechat_discuss_channel_vals()`)
- Agent posts message: stays `"in_progress"`, sets `livechat_failure = "no_failure"`
- `livechat_end_dt` set: `_compute_livechat_status()` clears status to `False` (closed sessions have no status)
- DB constraint: `CHECK(livechat_end_dt IS NULL or livechat_status IS NULL)` enforces this.

`livechat_failure` transitions:
- Created with agent operator: `"no_answer"` (agent not yet responded)
- Agent posts first message: `"no_failure"`
- No operator found during forward: `"no_agent"`
- Escalation: `livechat_outcome` = `"escalated"` (overrides failure in computed outcome field)

---

## 19. `res.users` Livechat Extensions
**File:** `models/res_users.py`

Fields added to `res.users`:
- `livechat_channel_ids`: inverse of `im_livechat.channel.user_ids` (M2M).
- `livechat_username`: stored in `res.users.settings.livechat_username`; shown to visitors instead of real name.
- `livechat_lang_ids`: preferred languages for operator matching.
- `livechat_expertise_ids`: operator expertise for matching.
- `livechat_ongoing_session_count`: computed from history records with active sessions (last 15 min).
- `livechat_is_in_call`: whether operator is in active RTC call.

---

## Claims Summary Table

| # | Claim | Source File | Line | Confidence |
|---|---|---|---|---|
| C1 | `im_livechat.channel` has no `website_id`; no website module dependency | `im_livechat_channel.py`, `__manifest__.py` | lines 18–85 | HIGH |
| C2 | `available_operator_ids` computed field checks: online presence, max_sessions limit, call status | `im_livechat_channel.py` | lines 133–183 | HIGH |
| C3 | Operator selection uses SQL activity query then `random.choice()` — not strict round-robin | `im_livechat_channel.py` | lines 433–559 | HIGH |
| C4 | BUFFER_TIME=120s prevents same operator getting consecutive sessions | `im_livechat_channel.py` | line 15, 508–522 | HIGH |
| C5 | Chatbot has 7 step types; forward_operator removes bot and adds human | `chatbot_script_step.py` | lines 23–31, 344–356 | HIGH |
| C6 | Visitor tracked via `mail.guest`; no `im_livechat.visitor` model | `controllers/main.py` | lines 87, 145–151 | HIGH |
| C7 | `_close_livechat_session()` sets `livechat_end_dt` and posts notification message | `discuss_channel.py` | lines 546–568 | HIGH |
| C8 | CRM lead creation absent from Community; `_convert_visitor_to_lead()` does not exist | All model files | — | HIGH |
| C9 | Multi-website scoping absent; no `website_id` field on channel | `im_livechat_channel.py` | lines 18–85 | HIGH |
| C10 | `user_ids` M2M to `res.users` via `im_livechat_channel_im_user` junction | `im_livechat_channel.py` | line 72 | HIGH |
| C11 | New chat notifies operator via `_broadcast([livechat_operator_id.id])` bus call | `controllers/main.py` | line 165 | HIGH |
| C12 | `discuss.channel` extended with `channel_type='livechat'` and `livechat_operator_id` NOT NULL constraint | `discuss_channel.py` | lines 31, 178–181 | HIGH |
| C13 | Session auto-closed when last operator leaves (`_action_unfollow`, member_count==1) | `discuss_channel.py` | lines 849–862 | HIGH |
| C14 | `im_livechat.channel.member.history` tracks agent/visitor/bot history with reporting fields | `im_livechat_channel_member_history.py` | lines 5–199 | HIGH |
| C15 | Chatbot answer branching uses AND-across-steps / OR-within-step logic in `_fetch_next_step()` | `chatbot_script_step.py` | lines 227–270 | HIGH |
| C16 | `livechat_status` cleared to False when `livechat_end_dt` set; enforced by DB constraint | `discuss_channel.py` | lines 182–185, 231–233 | HIGH |
| C17 | Operator selection has 8-tier preference cascade (language, country, expertise) | `im_livechat_channel.py` | lines 525–558 | HIGH |
| C18 | Bot partner created as inactive `res.partner` on chatbot script creation | `chatbot_script.py` | lines 110–124 | HIGH |
| C19 | Garbage collection: empty sessions deleted after 1h; bot-only after 1d; unpinned after 1d | `discuss_channel.py` | lines 510–536 | HIGH |
| C20 | Escalation = `livechat_is_escalated = len(agent_history) > 1` | `discuss_channel.py` | lines 235–238 | HIGH |
