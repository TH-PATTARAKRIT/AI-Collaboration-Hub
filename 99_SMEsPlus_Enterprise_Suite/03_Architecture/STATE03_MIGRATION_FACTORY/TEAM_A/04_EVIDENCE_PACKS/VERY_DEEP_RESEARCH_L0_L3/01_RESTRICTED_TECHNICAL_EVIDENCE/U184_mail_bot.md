# U184 — mail_bot (OdooBot): Chatbot Onboarding & Conversation Routing
**Unit:** U184 | **Group:** G13 | **Priority:** P3 | **Status:** NOT_STUDIED → STUDIED
**Source Base:** `odoo/addons/mail_bot/` (Odoo 19.0.post20260921 Community)
**Evidence Level:** L0–L3 (source-verified, no fabrication)

---

## 1. Module Overview

`mail_bot` is a lightweight Odoo addon (version 1.2) that implements OdooBot — a conversational onboarding assistant embedded in the Discuss app. It depends solely on the `mail` module and is `auto_install: True`, meaning it installs automatically when `mail` is present.

**Source:** `mail_bot/__manifest__.py`

---

## 2. OdooBot Identity — `base.partner_root` / `base.user_root`

OdooBot is NOT a separate `res.users` record with a custom `bot` flag. It re-uses the pre-existing system partner `base.partner_root` (XML id) and its associated user `base.user_root` (id = 1, the technical admin account).

- **Partner record** (`base/data/res_partner_data.xml`):
  - `id`: `base.partner_root`
  - `name`: "System"
  - `email`: `odoobot@example.com`
  - `active`: False (hidden from normal partner lists)

- **User record** (`base/data/res_users_data.xml`):
  - `id`: `base.user_root`
  - Linked to `base.partner_root`
  - email: `odoobot@example.com`

- **Lookup at runtime** (`mail_bot.py` line 24, `res_users.py` line 35):
  ```python
  odoobot_id = self.env['ir.model.data']._xmlid_to_res_id("base.partner_root")
  ```
  The bot's identity is always resolved via `ir.model.data` external ID lookup — no hard-coded integer id.

- **`odoobot_state` override for system user** (`mailbot_data.xml`):
  ```xml
  <record id="base.user_root" model="res.users">
      <field name="odoobot_state">disabled</field>
  </record>
  ```
  The system user itself is set to `disabled` state so it never triggers its own onboarding loop.

---

## 3. Model Architecture — `mail.bot` (AbstractModel)

`mail_bot/models/mail_bot.py`:
- Class: `MailBot(models.AbstractModel)`
- `_name = 'mail.bot'`
- `_description = 'Mail Bot'`
- **No inheritance of `mail.channel` or `mail.thread`** — it is a pure abstract service model with no stored fields.
- Acts as a stateless logic dispatcher invoked from `discuss.channel` hooks.

---

## 4. Entry Points — `discuss.channel` Hooks

`mail_bot/models/discuss_channel.py` extends `discuss.channel` with two hooks:

### 4a. `_message_post_after_hook` (every message)
```python
def _message_post_after_hook(self, message, msg_vals):
    self.env["mail.bot"]._apply_logic(self, msg_vals)
    return super()._message_post_after_hook(message, msg_vals)
```
Fires on **every** `message_post` in a channel. The logic filters internally.

### 4b. `execute_command_help` (slash command)
```python
def execute_command_help(self, **kwargs):
    super().execute_command_help(**kwargs)
    self.env['mail.bot']._apply_logic(self, kwargs, command="help")
```
Fires when a user types `/help` in any channel.

---

## 5. `_apply_logic()` — Top-Level Router

```python
def _apply_logic(self, channel, values, command=None):
```
**Guard conditions (early return):**
1. `values.get("author_id") == odoobot_id` — prevents the bot from responding to its own messages.
2. `values.get("message_type") != "comment" and not command` — ignores non-comment messages (notifications, system messages) unless triggered by command.

**Body normalization:**
```python
body = values.get("body", "").replace("\xa0", " ").strip().lower().strip(".!")
```

**Routing:** calls `_get_answer()`. If answer is returned, posts it back via `channel.sudo().message_post(author_id=odoobot_id, ...)` with `silent=True`.

---

## 6. `_get_answer()` — Onboarding State Machine

Routing is scoped to `channel.channel_type == "chat"` AND OdooBot is a member of that channel's `channel_member_ids.partner_id`.

State machine reads `self.env.user.odoobot_state` (per-user field on `res.users`).

### Onboarding Sequence (state → trigger → next state):

| # | From State | Trigger | Next State | Bot Response |
|---|-----------|---------|-----------|-------------|
| 1 | `onboarding_emoji` | Body contains emoji (unicode range check) | `onboarding_command` | "Great! 👍 To access special commands, start with /. Try getting help." |
| 2 | `onboarding_command` | `command == 'help'` | `onboarding_ping` | "Wow you are a natural! Ping someone with @username. Try @OdooBot." |
| 3 | `onboarding_ping` | OdooBot's partner_id in `values["partner_ids"]` | `onboarding_attachement` [sic] | "Yep, I am here! 🎉 Now try sending an attachment..." |
| 4 | `onboarding_attachement` | `values.get("attachment_ids")` non-empty | `onboarding_canned` | Creates a `mail.canned.response`, responds with "Wonderful! 😇 Try typing :: for canned responses." |
| 5 | `onboarding_canned` | `context.get("canned_response_ids")` non-empty | `idle` | Deletes the temporary canned response, returns 2-message list: canned response info + tour end message. |

**Note:** The field name is `onboarding_attachement` (one 't' spelling) — preserved exactly as in source.

### Failure / Retry Responses:
When a user sends the wrong input during onboarding, `odoobot_failed` is set to `True` and a repeat-instruction message is returned. The `_is_help_requested()` method also returns `True` when `odoobot_failed` is set.

### Tour Restart:
```python
elif odoobot_state in (False, "idle", "not_initialized") and (_('start the tour') in body.lower()):
    self.env.user.odoobot_state = "onboarding_emoji"
    return _("To start, try to send me an emoji :)")
```
Any user in `False/idle/not_initialized` state can restart onboarding by typing "start the tour".

### Easter Eggs (idle state):
- ❤️ / "i love you" / "love" → friendly rejection
- "fuck" (any language) → "That's not nice! I'm a bot but I have feelings... 💔"

### Help / Fallback:
- If `_is_help_requested()` returns True OR state is `idle` → documentation/video links response.
- Random fallback pool (4 responses) for unrecognized input.

---

## 7. `_body_contains_emoji()` — Emoji Detection

Static method scanning body against ~100+ Unicode ranges and individual codepoints sourced from `https://unicode.org/emoji/charts/full-emoji-list.html`. Ranges cover emoji blocks 0x231A–0x1FA00. Returns `True` on first match.

---

## 8. Onboarding Initialization — `_init_odoobot()`

`res_users.py`:
```python
def _on_webclient_bootstrap(self):
    super()._on_webclient_bootstrap()
    if self._is_internal() and self.odoobot_state in [False, "not_initialized"]:
        self._init_odoobot()
```

On first web client load for any internal user whose `odoobot_state` is unset or `not_initialized`:
1. Creates or retrieves the direct chat channel between OdooBot and the user via `discuss.channel._get_or_create_chat([odoobot_id, self.partner_id.id])`.
2. Posts the welcome message as OdooBot with `silent=True`.
3. Sets `odoobot_state = 'onboarding_emoji'`.

**Welcome message content:**
```
Hello,
Odoo's chat helps employees collaborate efficiently. I'm here to help you discover its features.
Try to send me an emoji :)
```

---

## 9. `odoobot_state` Field — All States

`res_users.py` `odoobot_state` Selection field on `res.users`:

| Value | Label |
|-------|-------|
| `not_initialized` | Not initialized |
| `onboarding_emoji` | Onboarding emoji |
| `onboarding_attachement` | Onboarding attachment |
| `onboarding_command` | Onboarding command |
| `onboarding_ping` | Onboarding ping |
| `onboarding_canned` | Onboarding canned |
| `idle` | Idle |
| `disabled` | Disabled |

- `required=False` — field can be `NULL/False` (treated as `not_initialized` in logic).
- `readonly=True` — user cannot directly edit.
- `odoobot_failed = fields.Boolean(readonly=True)` — tracks whether user failed the current step.
- `odoobot_state` is in `SELF_READABLE_FIELDS` so user can read their own state.

---

## 10. `mail.canned.response` Integration

During `onboarding_attachement` → `onboarding_canned` transition, the bot creates a temporary canned response:
```python
self.env["mail.canned.response"].create({
    "source": _("Thanks"),
    "substitution": _("Thanks for your feedback. Goodbye!"),
})
```
This is automatically deleted when the user successfully uses canned responses (completes step 5).

---

## 11. Module Does NOT Use/Override

- `message_new()` — not overridden; bot uses `_message_post_after_hook` instead.
- `mail.thread` inheritance — not used.
- `mail.channel` inheritance — not used; hooks into `discuss.channel`.
- No separate `res.users` record for OdooBot — reuses `base.user_root`.
- No `share` or `bot` boolean flag on the user record.

---

## Source Files Verified

| File | Lines | Notes |
|------|-------|-------|
| `mail_bot/models/mail_bot.py` | 334 | Core logic |
| `mail_bot/models/res_users.py` | 51 | State field + init |
| `mail_bot/models/discuss_channel.py` | 16 | Hooks |
| `mail_bot/__manifest__.py` | 24 | Module metadata |
| `mail_bot/data/mailbot_data.xml` | 8 | System user state disabled |
| `base/data/res_partner_data.xml` | (excerpt) | partner_root definition |
| `base/data/res_users_data.xml` | (excerpt) | user_root definition |
