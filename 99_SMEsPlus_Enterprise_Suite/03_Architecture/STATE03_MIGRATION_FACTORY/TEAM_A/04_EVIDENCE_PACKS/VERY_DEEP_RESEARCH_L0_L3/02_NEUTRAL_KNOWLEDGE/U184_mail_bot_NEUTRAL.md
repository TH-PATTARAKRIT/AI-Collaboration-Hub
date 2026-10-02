# U184 — mail_bot (OdooBot): Neutral Knowledge Reference
**Unit:** U184 | **Group:** G13 | **Priority:** P3
**Scope:** Chatbot onboarding, conversation routing, state management

---

## VDR CLAIMS TABLE

| # | Claim ID | Claim Statement | Source File | Evidence Type | Confidence | Odoo Version | Migration Risk | Notes |
|---|----------|----------------|-------------|---------------|-----------|--------------|----------------|-------|
| 1 | U184-C01 | OdooBot is not a dedicated user account with a bot flag; it reuses the system technical partner record identified by the external ID base.partner_root (name "System", email odoobot@example.com, active=False) | base/data/res_partner_data.xml | Source-verified | HIGH | 19.0 | LOW — identity is stable across versions | No separate bot user record exists |
| 2 | U184-C02 | OdooBot's partner identifier is resolved at every call via ir.model.data._xmlid_to_res_id("base.partner_root") rather than a hard-coded integer, making the implementation database-instance independent | mail_bot/models/mail_bot.py:24, res_users.py:35 | Source-verified | HIGH | 19.0 | LOW | External-ID-based lookup is migration-safe |
| 3 | U184-C03 | The mail.bot model is an AbstractModel with no stored fields; it contains only service methods and never directly owns database rows or extends mail.thread or discuss.channel | mail_bot/models/mail_bot.py:10 | Source-verified | HIGH | 19.0 | LOW | Pure dispatcher — no table created |
| 4 | U184-C04 | OdooBot inserts itself into conversations via two hooks on discuss.channel: _message_post_after_hook fires on every message_post, and execute_command_help fires on the /help slash command | mail_bot/models/discuss_channel.py:9-15 | Source-verified | HIGH | 19.0 | MEDIUM — hook override pattern; must survive discuss.channel changes | No override of message_new |
| 5 | U184-C05 | Onboarding is triggered automatically when an internal user loads the web client and their odoobot_state is NULL or not_initialized; the hook _on_webclient_bootstrap creates the direct chat and posts the first message silently | mail_bot/models/res_users.py:28-50 | Source-verified | HIGH | 19.0 | LOW | Only fires for internal users |
| 6 | U184-C06 | The onboarding progresses through six sequential states stored per-user on res.users.odoobot_state: onboarding_emoji → onboarding_command → onboarding_ping → onboarding_attachement → onboarding_canned → idle | mail_bot/models/res_users.py:11-21, mail_bot.py:63-118 | Source-verified | HIGH | 19.0 | LOW | Note: "attachement" is the exact field value (one-t spelling) |
| 7 | U184-C07 | Each onboarding step teaches a distinct Discuss feature: emoji input, the /help slash command, the @mention ping, file attachment upload, and the :: canned-response shortcut | mail_bot/models/mail_bot.py:63-118 | Source-verified | HIGH | 19.0 | LOW — functional scope, not schema | Five distinct features demonstrated in sequence |
| 8 | U184-C08 | During the attachment-to-canned transition the bot programmatically creates a temporary mail.canned.response record owned by the onboarding user and automatically deletes it when the canned-response step is completed | mail_bot/models/mail_bot.py:90-105 | Source-verified | HIGH | 19.0 | LOW | Side-effect creates/removes a canned response record |
| 9 | U184-C09 | The odoobot_state field on res.users has eight possible values: not_initialized, onboarding_emoji, onboarding_attachement, onboarding_command, onboarding_ping, onboarding_canned, idle, disabled; the system user (base.user_root) is seeded to disabled to prevent self-triggering | mail_bot/models/res_users.py:11-21; data/mailbot_data.xml | Source-verified | HIGH | 19.0 | LOW | required=False so NULL is also a valid pre-init state |
| 10 | U184-C10 | A companion boolean field odoobot_failed on res.users tracks whether the user has failed the current onboarding step; when True, any subsequent message (even without matching keywords) returns a repeat-instruction response | mail_bot/models/res_users.py:22; mail_bot.py:329-333 | Source-verified | HIGH | 19.0 | LOW | Helper for forgiving UX — no state change on failure |
| 11 | U184-C11 | Once in the idle state a user can restart the onboarding tour at any time by sending the phrase "start the tour"; this resets odoobot_state to onboarding_emoji | mail_bot/models/mail_bot.py:127-129 | Source-verified | HIGH | 19.0 | LOW | Internationalized — uses _() for tour phrase |
| 12 | U184-C12 | Bot responses are posted via channel.sudo().message_post with silent=True and subtype mail.mt_comment, meaning they do not generate email notifications | mail_bot/models/mail_bot.py:31-37 | Source-verified | HIGH | 19.0 | LOW | Silent posting is intentional — no notification side-effects |
| 13 | U184-C13 | Emoji detection in user messages uses a static method _body_contains_emoji that scans against approximately one hundred Unicode ranges and individual codepoints covering the full emoji chart; text entered as shortcodes like :) is first converted by the client and thus reaches the server as rendered Unicode | mail_bot/models/mail_bot.py:196-327 | Source-verified | HIGH | 19.0 | LOW | Range-based scan, no regex |
| 14 | U184-C14 | Bot logic only activates for direct-chat channels (channel_type == "chat") where OdooBot is a member; messages in group channels or other channel types are silently ignored unless OdooBot is explicitly pinged | mail_bot/models/mail_bot.py:59 | Source-verified | HIGH | 19.0 | MEDIUM — channel_type scoping must be respected in migrations | No group-channel participation by default |
| 15 | U184-C15 | The module has no controllers directory logic that is relevant to bot operation; the static scss file provides CSS class styling for o_odoobot_command spans used to visually highlight command hints in bot messages | mail_bot/__manifest__.py; static/src/scss/ | Source-verified | MEDIUM | 19.0 | LOW | Frontend styling concern only |

---

## Key Architecture Summary

OdooBot operates as a stateless abstract service model (`mail.bot`) that intercepts `discuss.channel` message events through post-message hooks. State is maintained per-user on the `res.users` model via the `odoobot_state` Selection field. The bot identity resolves to the pre-existing system partner (`base.partner_root`) rather than a dedicated bot user. Onboarding proceeds through a linear five-step sequence teaching emoji, slash commands, @mentions, file attachments, and canned responses. The module auto-installs with the `mail` addon and requires no separate configuration.

## Migration Considerations

- `odoobot_state` field and its eight values must be preserved exactly (including the "attachement" typo) during any schema migration.
- The `odoobot_failed` boolean companion field must also migrate.
- The `base.partner_root` and `base.user_root` external IDs are foundational — they exist in base and must not be altered.
- Channel hook pattern (`_message_post_after_hook`) is version-sensitive; verify hook signature compatibility in target Odoo version.
- `mail.canned.response` model dependency must be present; if this model changes, the attachment→canned transition logic may require adjustment.
