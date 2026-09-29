# Source Map (candidate) — `mail_bot`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mail_bot` |
| Display name | OdooBot |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `7eceb3e49e4fd91b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mail_bot/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mail`
- Direct dependents in 300-module list (1): `mail_bot_hr`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `test_discuss_full`, `test_mail_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Discuss / Add OdooBot in discussions
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `mail.bot` (Mail Bot)
- Objects extended from other modules (2): `discuss.channel`, `res.users`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `discuss.channel`, `res.users`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 28 of 28 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — mail_bot
Source revision: 19.0.post20260921 | Module: "OdooBot" v1.2, category Productivity/Discuss, LGPL-3 (mail_bot/__manifest__.py:5-7,23). Basis: static reading; no tests, no security files in this module.

## A. Capabilities and optionality
- A1. Adds a virtual assistant ("OdooBot") to the internal chat. It greets each internal user in a private chat and walks them through a short guided tour (emoji, slash command, mention, attachment, canned response), then answers in an "idle" mode with help pointers and a few canned replies. mail_bot/models/res_users.py:28-50; mail_bot/models/mail_bot.py:54-193
- A2. Conditional: auto_install on, depends only on mail; present wherever mail is installed. mail_bot/__manifest__.py:10-11
- A3. No settings switch. A user can be opted out by setting their bot status to "Disabled"; that field is editable on the user form only in developer mode and hidden for portal/share users. mail_bot/views/res_users_views.xml:10-13; mail_bot/models/res_users.py:11-21. The administrator-root account (OdooBot's own user) is preset to Disabled. mail_bot/data/mailbot_data.xml:4-6

## B. Objects and lifecycle
- B1. No new business model. Adds two fields to the user: onboarding status (not started, emoji, attachment, command, ping, canned, idle, disabled) and a "failed last step" flag. Both read-only in code paths. mail_bot/models/res_users.py:11-22
- B2. Bot logic object is an internal stateless helper; state is kept on the user. mail_bot/models/mail_bot.py:10-14
- B3. Lifecycle: on web client start for an internal user whose status is empty/"not initialized", a chat with the bot is created (or reused) and a first message asks for an emoji; status becomes "emoji". mail_bot/models/res_users.py:28-50
- B4. Step order: emoji -> slash-command "help" -> mention the bot -> send an attachment (creates a temporary canned response "Thanks") -> use a canned response (the temporary one is deleted) -> idle. A wrong action repeats the hint and raises the failed flag. mail_bot/models/mail_bot.py:59-118,144-176
- B5. In idle mode, typing "start the tour" restarts; help requests or questions get a documentation/videos pointer. mail_bot/models/mail_bot.py:127-143
- B6. Extra scripted replies to affection and to profanity. mail_bot/models/mail_bot.py:131-134

## C. Validations, automation, security
- C1. The bot answers only in one-to-one "chat" channels that include the bot, when the message is a comment not written by the bot (or when the help command is run). mail_bot/models/mail_bot.py:25,59; mail_bot/models/discuss_channel.py:9-15
- C2. Bot posts run with elevated rights, as the bot's partner, silently (no notification). mail_bot/models/mail_bot.py:31-37
- C3. Only internal users are onboarded. mail_bot/models/res_users.py:30
- C4. Users can read their own bot status via the self-readable field list. mail_bot/models/res_users.py:24-26
- C5. Temporary canned response is created under the current user's rights and later removed by matching creator + source text "Thanks" — this could also remove a user's own canned response with that source. mail_bot/models/mail_bot.py:90-93,102-105. Effect on real data: UNKNOWN — EVIDENCE INSUFFICIENT beyond this reading.
- C6. Message posting endpoint is extended only to pass the chosen canned-response ids into context so the tour can detect their use. mail_bot/controllers/thread.py:8-12
- C7. No external service calls; links point to public Odoo documentation and video pages (static text). mail_bot/models/mail_bot.py:47-50
- C8. Company scoping: none defined here.

## D. Handoffs
- D1. Chat channels, commands and message posting: mail (discuss.channel, help command). mail_bot/models/discuss_channel.py:7-15
- D2. Canned responses: mail. mail_bot/models/mail_bot.py:90,102
- D3. Bot's partner and user records: base (base.partner_root, base.user_root). mail_bot/models/mail_bot.py:24; mail_bot/data/mailbot_data.xml:4

## E. Configuration that changes outcomes
- E1. Per-user onboarding status (Disabled stops the bot greeting that user). mail_bot/models/res_users.py:30. Language: bot text is translatable and keyword matching (e.g. "help", "start the tour") uses translated text as well as English for some phrases. mail_bot/models/mail_bot.py:127,131,333
- E2. Bot's only global off-switch found is uninstalling the module: UNKNOWN — EVIDENCE INSUFFICIENT for any system-wide setting.

## F. Extension path
- Modules that inherit mail.bot or call its logic: UNKNOWN — EVIDENCE INSUFFICIENT (not searched beyond this module).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end behaviour (only one stylesheet asset registered, mail_bot/__manifest__.py:17-21).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour for multi-company or guest users.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether other Community modules extend the tour steps.

