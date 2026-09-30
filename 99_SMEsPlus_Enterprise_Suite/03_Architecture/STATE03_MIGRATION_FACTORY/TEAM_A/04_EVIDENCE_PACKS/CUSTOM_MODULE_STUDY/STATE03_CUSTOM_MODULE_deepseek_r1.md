> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: deepseek_r1

## 0. Header
- Module: deepseek_r1
- License (confirmed in manifest): GPL-3 (deepseek_r1/__manifest__.py:24)
- Author (manifest): Hari (deepseek_r1/__manifest__.py:11)
- Version (manifest): 0.1 (deepseek_r1/__manifest__.py:13) - not in Odoo 19 series format
- Path: addons_Extramodule/addons_extra/deepseek_r1
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds an AI chat assistant persona ("DeepSeek R1") to the internal Discuss messaging: a dedicated channel, a bot user and partner, and a settings screen for an API key (deepseek_r1/data/mail_channel_data.xml:4-29; data/user_partner_data.xml:4-17; views/res_config_settings_views.xml:3-23; models/res_config_settings.py:7).
- When a message is posted, its text is sent to an external AI service and the reply is posted back into the same conversation as the bot user (models/mail_channel.py:23-46,48-72).
- Despite the name, the requested model identifier in code is a general-purpose GPT-type model reached through a third-party AI aggregator (models/mail_channel.py:52-55,64); the settings text points to DeepSeek documentation (views/res_config_settings_views.xml:15-16). The mismatch between name and model is noted (see section 6).

## 2. Attachment to CORE
- Depends on base, base_setup, mail (manifest:17) and on the Python library "openai" (manifest:14-16).
- Extends core discuss.channel (models/mail_channel.py:21).
- Override of core method _notify_thread: ADDS after core. It first calls core (core:mail/models/discuss/discuss_channel.py:944, which broadcasts the new message to the client bus), then for the message text calls the external AI and posts a reply (models/mail_channel.py:23-46). The condition at models/mail_channel.py:35 triggers whenever the author is not the bot, in ANY discuss conversation, not only in the DeepSeek channel; the second branch that would restrict to the bot channel references an undefined name (partner_chatgpt) at models/mail_channel.py:38 and is unreachable in practice. Business effect: message text from other channels and direct chats can be transmitted to the external service. ALTERS CORE CONTROL: it does not disable a core control, but it adds an outbound disclosure path for internal chat content that core does not have.
- Extends res.config.settings with a field bound to a system parameter (models/res_config_settings.py:7).
- Seed data adds a bot user (res.users) with a fixed password value set in the data file (a credential-like value exists at deepseek_r1/data/user_partner_data.xml:13; not reproduced) and a channel restricted to internal users (group link at data/mail_channel_data.xml:27-29); the administrator partner is added as channel member (data/mail_channel_data.xml:20-25).

## 3. New objects, security, automation, external calls
- New models: none. New system parameter: deepseek_r1.api_key (stored through the settings field; read with elevated rights at models/mail_channel.py:49-50). The key is masked in the form (views/res_config_settings_views.xml:13). A credential-like value is expected at runtime in that parameter; none was found in source.
- ACL file security/ir.model.access.csv references a model name (model_deepseek_r1_deepseek_r1) that this module does not define and is not listed in the manifest data (manifest:19-23), so it is not loaded.
- No record rules; no company scoping of the bot user beyond the main company (data/user_partner_data.xml:15-16).
- Automation: event-driven on every discuss message (see section 2); no cron.
- EXTERNAL CALL (business level): each qualifying message triggers an outbound HTTPS request from the server to a third-party AI gateway, sending the message text together with the accumulated conversation history, authenticated by the stored API key; the reply text is then posted into the conversation (models/mail_channel.py:48-72). The conversation history is kept in a process-wide list that is shared by all users and channels and never cleared (models/mail_channel.py:17-18,57-60), so context from different users and conversations is mixed and re-sent on later calls, and grows without bound.
- Package installation at import: if the openai library is missing, the code attempts to install it at runtime (models/mail_channel.py:5-13); the subprocess and sys modules used there are not imported in that file, so that path would fail.

## 4. Odoo 19 compatibility
- Core references exist in 19: discuss.channel with group_ids (core:mail/models/discuss/discuss_channel.py:106), discuss.channel.member fetched_message_id / seen_message_id (core:mail/models/discuss/discuss_channel_member.py:36-37), Command available in data files (core:tools/convert.py:45), method _notify_thread (core:mail/models/discuss/discuss_channel.py:944; core:mail/models/mail_thread.py:3279).
- models/mail_channel.py:28,30 read msg_vals with .get before any guard although the signature default is False; a call with msg_vals=False would raise before the protective try block.
- Errors are swallowed silently by a bare exception handler (models/mail_channel.py:42-44); the error branch returns the exception object itself as text (models/mail_channel.py:71-72).
- Settings field api_key is declared required (models/res_config_settings.py:7) on a general settings model: the effect on saving other settings is not verified.
- Version tag 0.1 and module name mail_channel.py file naming reflect older releases (file defines discuss.channel).

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether this module is actually installed in the target deployment and whether an API key is configured.
- UNKNOWN - EVIDENCE INSUFFICIENT: why the code requests a GPT-type model under a DeepSeek name (intent not stated in source).
- UNKNOWN - EVIDENCE INSUFFICIENT: legal/privacy acceptability of sending internal chat text to the third-party service (policy question, not derivable from source).
