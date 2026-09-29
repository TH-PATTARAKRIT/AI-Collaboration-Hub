# Source Map (candidate) — `im_livechat`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `im_livechat` |
| Display name | Live Chat |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `2451a511fe61b13a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/im_livechat/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `mail`, `rating`, `digest`, `utm`
- Direct dependents in 300-module list (5): `crm_livechat`, `hr_livechat`, `spreadsheet_dashboard_im_livechat`, `website_hr_recruitment_livechat`, `website_livechat`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_discuss_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Live Chat / Chat with your website visitors
- Inventory of user-facing artifacts (counts): menu items 15, views 40, window actions 11, server actions 0, reports 1, mail templates 0, scheduled jobs 0, wizards 0, web routes 17
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (10): `im_livechat.expertise` (Live Chat Expertise); `chatbot.script` (Chatbot Script); `chatbot.script.step` (Chatbot Script Step); `chatbot.message` (Chatbot Message); `im_livechat.conversation.tag` (Live Chat Conversation Tags); `chatbot.script.answer` (Chatbot Script Answer); `im_livechat.channel` (Livechat Channel); `im_livechat.channel.rule` (Livechat Channel Rules); `im_livechat.channel.member.history` (Keep the channel member history); `im_livechat.report.channel` (Livechat Support Channel Report)
- Objects extended from other modules (17): `rating.mixin`, `discuss.channel`, `digest.digest`, `image.mixin`, `utm.source.mixin`, `discuss.call.history`, `res.users.settings`, `discuss.channel.member`, `discuss.channel.rtc.session`, `res.groups`, `rating.parent.mixin`, `ir.qweb`, `res.users`, `rating.rating`, `ir.websocket`, `mail.message`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `chatbot.script` ← Community: `crm_livechat`, `website_livechat`; open-license custom/third-party scanned: —
- `chatbot.script.step` ← Community: `crm_livechat`, `website_crm_livechat`, `website_livechat`; open-license custom/third-party scanned: —
- `im_livechat.channel` ← Community: `website_livechat`; open-license custom/third-party scanned: —
- `im_livechat.report.channel` ← Community: `crm_livechat`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `rating.mixin`, `discuss.channel`, `digest.digest`, `image.mixin`, `utm.source.mixin`, `discuss.call.history`, `res.users.settings`, `discuss.channel.member`, `discuss.channel.rtc.session`, `res.groups`, `rating.parent.mixin`, `ir.qweb`, `res.users`, `rating.rating`, `ir.websocket`, `mail.message`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 3 declarative constraint method(s), 6 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 3 (`im_livechat.im_livechat_group_user`, `im_livechat_group_user`, `im_livechat_group_manager`); record rules 3 (of which company-scoped by text 0); access rows 15

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 66 of 66 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — im_livechat
Source revision: 19.0.post20260921 | Module: "Live Chat" (im_livechat/__manifest__.py:2) | Category Website/Live Chat (:6) | Application (skeleton) | License LGPL-3 (:197)
Basis: static reading of manifest, security XML/CSV, channel/session/chatbot models, controllers, selected tests (TEST).

## A. Capabilities; core vs optional vs conditional
- A1. Lets a business place a chat widget on web pages (own site or external site via script) and dispatch visitor requests among human operators or an automated scripted bot. im_livechat/__manifest__.py:5-19; im_livechat/models/im_livechat_channel.py:19-24
- A2. Depends on mail, rating, digest, utm; standalone app (not auto_install). im_livechat/__manifest__.py:74
- A3. Core: Live Chat Channel (widget settings, agents, rules), sessions (as a "livechat" type of discussion channel), ratings, operator dispatch. im_livechat/models/im_livechat_channel.py:33-79; im_livechat/models/discuss_channel.py:30
- A4. Core: scripted chatbot (steps, answers, forward-to-human). im_livechat/models/chatbot_script.py:11-25; im_livechat/models/chatbot_script_step.py:23-32
- A5. Optional (data-driven): expertise tags on operators and sessions; conversation tags; help request status between agents; calls during chats. im_livechat/models/im_livechat_expertise.py:8; im_livechat/models/im_livechat_conversation_tag.py:8; im_livechat/models/discuss_channel.py:104-115
- A6. Reporting: per-session report model, member-history model, digest KPIs (happiness %, conversations handled, time to answer). im_livechat/report/im_livechat_report_channel.py:8; im_livechat/models/im_livechat_channel_member_history.py:5; im_livechat/models/digest.py:10-15
- A7. Transcripts: email transcript (internal users only) and PDF download. im_livechat/controllers/main.py:247-277
- A8. Conditional: country-based rules need geolocation on the server; without it country is not used. im_livechat/models/im_livechat_channel.py:302 (help text), :655-657 (country branch); im_livechat/controllers/main.py:99-104
- A9. Conditional: chatbot on a rule can be always on, only when an operator is available, or only when none is. im_livechat/models/im_livechat_channel.py:621-629; :647-651
- A10. Demo data (sessions, bot scenarios) loaded only in demo mode. im_livechat/__manifest__.py:41-75 (demo section)
- A11. Cross-origin (CORS) route variants exist so the widget can run on an external website using a guest token. im_livechat/controllers/cors/*.py; im_livechat/controllers/main.py:16-19,29

## B. Business objects, relationships, lifecycle
- B1. Live Chat Channel: name, button text, welcome message, colors, per-operator session cap (unlimited/limited), no-chats-during-call option, optional review link; has agents (users), rules, sessions. im_livechat/models/im_livechat_channel.py:33-79
- B2. Rule: URL pattern, country list, button action (show / show with notification / open automatically after delay / hide), optional chatbot, chatbot condition, ordering. im_livechat/models/im_livechat_channel.py:607-635
- B3. Session = discussion channel of type livechat; carries visitor language, country, operator, end time, expertise, status (in progress / waiting for customer / looking for help), outcome (never answered / no one available / success / escalated), note, tags, rating. im_livechat/models/discuss_channel.py:30-135, 160-171
- B4. Session lifecycle: created when visitor opens chat (persisted or as a temporary non-stored thread) -> messages -> ends when visitor leaves or last agent leaves (end date set; status cleared) -> rating optional. im_livechat/controllers/main.py:82-186, 279-286; im_livechat/models/discuss_channel.py:546-568, 231-234
- B5. Guest identity: an anonymous visitor becomes a guest record with name, country, time zone; logged-in users are linked by partner. im_livechat/controllers/main.py:139-146; im_livechat/models/im_livechat_channel.py:305-330
- B6. Member history: one record per participant per session (agent/bot/visitor) used for reporting; unique per member; a history belongs either to a partner or a guest, never both. im_livechat/models/im_livechat_channel_member_history.py:79-95
- B7. Chatbot script: title, bot operator partner (required), ordered steps; step types text, question, email, phone, forward to operator, free input single/multi; steps can be conditional on prior answers. im_livechat/models/chatbot_script.py:24-27; im_livechat/models/chatbot_script_step.py:23-45
- B8. Chatbot lifecycle: welcome steps posted -> answers saved -> next step by triggering answers -> optional email/phone capture creates a contact for public visitors -> forward step invites a human and removes the bot; if nobody is available the chat continues with the bot and outcome becomes "no one available". im_livechat/models/chatbot_script_step.py:150-215; im_livechat/models/discuss_channel.py:876-935
- B9. Rating: one rating per session; a second submission updates it; posted as a message. im_livechat/controllers/main.py:207-238
- B10. Agent-facing settings on users: livechat username, spoken languages, expertise. im_livechat/models/res_users.py:14-40

## C. Validations, automation, security, multi-company
- C1. Groups: Live Chat "User" (implies internal user; can join channels) and "Administrator" (implies User and canned-response admin; can delete channels; preassigned to root and admin users). im_livechat/security/im_livechat_channel_security.xml:9-24
- C2. Access: users read channels; admins full. Rules: users create/write/read rules (no delete); chatbot scripts, steps, answers, chatbot messages admin-only; expertise readable by all internal users; conversation tags user rw-create, admin all; member history readable by users; report readable by admins. im_livechat/security/ir.model.access.csv:2-16
- C3. Record rules: Live Chat users can read all discussion channels/members/call histories of type livechat (not write/delete; members rule permits create). im_livechat/security/im_livechat_channel_security.xml:27-54
- C4. Constraints: max sessions per operator must be > 0; review link must be http/https; a livechat session must have an operator; a closed session cannot have a status; chatbot question step must have answers; history integrity (see B6). im_livechat/models/im_livechat_channel.py:83-85,138-145; im_livechat/models/discuss_channel.py:178-185; im_livechat/models/chatbot_script.py:33-38
- C5. Only operators (Live Chat group) can join a channel; joining is done with elevated rights on the channel's agent list. im_livechat/models/im_livechat_channel.py:250-257
- C6. Operator availability: online presence, under the concurrent cap (if limited), and not in a call when blocked. im_livechat/models/im_livechat_channel.py:147-183; (TEST) im_livechat/tests/test_get_operator.py:236-311
- C7. Operator selection preference order: same language + all expertises, language + some expertise, language, then country combos, then expertise only; then least busy; earlier operator preferred for continuity; random tie-break. im_livechat/models/im_livechat_channel.py:433-560, 393-431; (TEST) im_livechat/tests/test_get_operator.py:20-235
- C8. Rule matching: country-specific rules first, then rules without country; first pattern match by sequence; skips rules whose chatbot is archived/has no steps or whose availability condition fails. im_livechat/models/im_livechat_channel.py:635-665
- C9. Public routes are open to anonymous visitors (session start, feedback, history, transcript download, leave); the session search relies on standard access for guests/partners. im_livechat/controllers/main.py:63-70,82,207,240,255,279. Transcript email requires a logged-in internal user. :247-252; (TEST) im_livechat/tests/test_transcript.py:9-40
- C10. Automation (autovacuum): empty sessions older than 1 hour are deleted; bot-only sessions inactive over 1 day are closed. im_livechat/models/discuss_channel.py:509-535
- C11. Digest KPIs computed for the reporting period. im_livechat/models/digest.py:17-43
- C12. Multi-company: no company field on channel, rule, script, or report models (grep of "company" in models finds only transcript sender and digest hooks). Company appears only when sending transcripts (uses current user's company for sender). im_livechat/models/discuss_channel.py:574-592. Consequence: channels and rules are not company-scoped by this module; UNKNOWN — EVIDENCE INSUFFICIENT for website-level scoping (owned by website_livechat, not read).
- C13. Customer capture by chatbot: email step validated; for public visitors a contact is created with email/phone. im_livechat/models/chatbot_script_step.py:322-323, 175-190

## D. Handoffs
- D1. Discussion channels, guests, members, calls, presence, canned responses: mail. im_livechat/models/discuss_channel.py:22; im_livechat/security/im_livechat_channel_security.xml:22
- D2. Ratings and satisfaction computation (last 14 days): rating. im_livechat/models/im_livechat_channel.py:24-28; im_livechat/models/discuss_channel.py:571-572
- D3. Digest emails/KPIs: digest. im_livechat/models/digest.py:7
- D4. Tracking source per bot: utm. im_livechat/models/chatbot_script.py:13
- D5. Website integration (embedding on website pages, visitor info): website_livechat. website_livechat/__manifest__.py (dependent module; not read)
- D6. Lead/ticket creation from chat: crm_livechat (dependent, not read); employee-facing chat: hr_livechat, hr_holidays (out-of-office use), hr; slides: website_slides; recruitment: website_hr_recruitment_livechat; dashboards: spreadsheet_dashboard_im_livechat; test_discuss_full. (manifest grep only)
- D7. Chatbot uses customer-value helper so other modules can create leads/tickets from captured email/phone/conversation summary. im_livechat/models/chatbot_script_step.py:150-160

## E. Configuration / defaults that change outcomes
- E1. Per-operator concurrent session mode default "unlimited"; cap default 10 when limited. im_livechat/models/im_livechat_channel.py:49-58
- E2. Channel default: creator is the first agent; default welcome text and button text; default colors. im_livechat/models/im_livechat_channel.py:34-48,73
- E3. Rule default action "Show"; chatbot default "Always"; auto-popup delay 0; sequence 10. im_livechat/models/im_livechat_channel.py:607-631
- E4. Sample channel "YourWebsite.com" created on install (noupdate). im_livechat/data/im_livechat_channel_data.xml:3-6
- E5. Sessions are considered active for load counting when they had interest in the last 15 minutes and have no end date. im_livechat/models/im_livechat_channel.py:207-209
- E6. Chatbot language taken from a chatbot-language helper; visitor language from cookie. im_livechat/controllers/main.py:107-110,127-134

## F. Effective extension path (module names only)
- website_livechat, crm_livechat, hr_livechat, hr_holidays, hr, website_slides, website_hr_recruitment_livechat, spreadsheet_dashboard_im_livechat, test_discuss_full (dependents by manifest).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end widget behaviour (JavaScript not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: how operators are limited by website or company (dependent modules not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: guest visibility rules on the session/messages beyond mail module (owned by mail, not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: report SQL definitions and their access at row level (report file not read beyond model list).
- UNKNOWN — EVIDENCE INSUFFICIENT: detailed cross-origin route protections.

