# Source Map (candidate) — `website_livechat`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_livechat` |
| Display name | Website Live Chat |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a87ed5c093ac3983` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_livechat/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `website`, `im_livechat`
- Direct dependents in 300-module list (1): `website_crm_livechat`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `test_discuss_full`, `test_website_modules`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Live Chat / Chat with your website visitors
- Inventory of user-facing artifacts (counts): menu items 1, views 7, window actions 2, server actions 1, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (9): `discuss.channel`, `chatbot.script`, `chatbot.script.step`, `ir.http`, `website.page`, `im_livechat.channel`, `res.config.settings`, `website`, `website.visitor`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `discuss.channel`, `chatbot.script`, `chatbot.script.step`, `ir.http`, `website.page`, `im_livechat.channel`, `res.config.settings`, `website`, `website.visitor`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 50 of 51 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_livechat (Website Live Chat)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_livechat.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: lets website visitors chat with collaborators (website_livechat/__manifest__.py:5,7).

## A. Capabilities / functions
- Conditional: depends on website and im_livechat, `auto_install` (website_livechat/__manifest__.py:8,10); appears automatically once both are installed.
- Core: injects the live-chat loader into every website page head when the current website has a chat channel assigned and the page does not opt out (website_livechat/views/website_livechat.xml:8-17). A website holds one chat channel (website_livechat/models/website.py:10-21).
- Core: settings screen field to pick the website's chat channel, shown to live-chat managers (website_livechat/models/res_config_settings.py:10; website_livechat/views/res_config_settings_views.xml:8-14).
- Core: "New Channel" quick action from the website "new content" menu; creating a channel this way assigns it to the current website and adds a display rule using the welcome chatbot when available (website_livechat/views/im_livechat_channel_add.xml:4-23; website_livechat/models/im_livechat_channel.py:37-62).
- Core: visitor management on the website visitor form/kanban: operator currently speaking, session count ("Chats") with a list of the visitor's sessions that have messages, and "Send chat request" (website_livechat/models/website_visitor.py:13-43, 45-98; website_livechat/views/website_visitor_views.xml:3-25, 30-80).
- Core: chat request flow: an operator opens an empty pending chat addressed to a visitor; the visitor sees it on next page load (website_livechat/models/website_visitor.py:45-98; website_livechat/controllers/webclient.py:7-62).
- Core: each livechat conversation is tied to the visitor, and the visitor's recent history (last three pages) and up to five conversations of the last 7 days are shown to the operator (website_livechat/models/discuss_channel.py:15, 54-55, 68-91; website_livechat/models/website_visitor.py:128-136).
- Core: anonymous chatters are named "Visitor #id" (website_livechat/controllers/main.py:8-12).
- Core: "Test" button on chatbot scripts opens a private test conversation (`/chatbot/<id>/test`) for logged-in users (website_livechat/models/chatbot_script.py:10-16; website_livechat/controllers/chatbot.py:10-60; website_livechat/views/im_livechat_chatbot_script_view.xml:9-12).
- Core: chatbot steps that collect customer data fall back to the visitor's known email, phone and country (website_livechat/models/chatbot_script_step.py:10-20).
- Front-end: chat and translation bundle added (website_livechat/models/ir_http.py:10-13). Default website gets the default chat channel through data (website_livechat/data/website_livechat_data.xml:4-6).

## B. Business objects, relationships, lifecycle
- Visitor (website) 1..n conversations (discuss channel of type live chat, owned by im_livechat/mail) (website_livechat/models/discuss_channel.py:15; website_livechat/models/website_visitor.py:15). A visitor's current operator is the operator of their open conversation (website_livechat/models/website_visitor.py:26-34).
- Chat request lifecycle: pending request (operator-initiated, flagged) -> visitor loads a page -> request delivered and un-flagged -> conversation. If the visitor starts a chat themselves, the pending request is cancelled with a system note (website_livechat/models/im_livechat_channel.py:19-33; website_livechat/controllers/webclient.py:8-15). (TEST) (website_livechat/tests/test_livechat_request.py:28-60, 11-26).
- Empty operator-initiated chats are deleted when unpinned without messages, so a new request can be sent (website_livechat/models/discuss_channel.py:17-27).
- Visitor merge (anonymous -> identified) moves sessions to the main visitor and replaces the public contact by the real one (website_livechat/models/website_visitor.py:100-107). New visitors adopt the guest's earlier live-chat sessions (website_livechat/models/website_visitor.py:109-118).
- A visitor's activity timestamp is refreshed on every visitor/bot message, not operator messages (website_livechat/models/discuss_channel.py:93-103).

## C. Validations, automation, security, multi-company
- Chat request refused if the visitor already has an open conversation or if the visitor's website has no chat channel; the requesting operator is added to that channel's users automatically (website_livechat/models/website_visitor.py:51-61).
- Visitor and tracked-page rows are readable (read only) by live-chat users group (website_livechat/security/ir.model.access.csv:2-3). Visitor info in conversation data is included only if the reader can read visitors; (TEST) removing the live-chat user group removes visitor info (website_livechat/models/discuss_channel.py:29-43; website_livechat/tests/test_livechat_basic_flow.py:118-135).
- Elevated operations are annotated as intended for: visitor info for chatbot, guest linking, history reading (website_livechat/models/chatbot_script_step.py:12; website_livechat/models/website_visitor.py:112-116, 122-124).
- Chatbot test page requires a logged-in user (website_livechat/controllers/chatbot.py:11-12).
- Website scoping: one channel per website record; visitor rows belong to a website; the loader uses the request's website (website_livechat/models/website.py:10; website_livechat/views/website_livechat.xml:10). Behaviour for multi-company channel sharing: UNKNOWN — EVIDENCE INSUFFICIENT.
- Cached pages still trigger the channel-info preparation on response (website_livechat/models/website_page.py:9-12).

## D. Handoffs to other modules
- im_livechat (owner): channels, rules (URL/country/action), operators, chatbot engine, ratings; mail (discuss channels, guests); website (owner of visitor, tracks, layout).
- website_crm_livechat / crm_livechat: lead creation from chats; website_hr_recruitment_livechat: demo jobs bot; website_crm: visitor-lead links.
- The rating and satisfaction flows are exercised by UI tests (TEST) (website_livechat/tests/test_ui.py:19-54).

## E. Configuration / defaults that change outcomes
- Website-level chat channel (blank = no chat button) (website_livechat/models/website.py:10; website_livechat/views/website_livechat.xml:10).
- Rules on the channel (show, hide, auto-open, chatbot condition, countries, URL regex) decide the visitor experience (im_livechat/models/im_livechat_channel.py:600-650); (TEST) hide-button rule prevents new sessions (website_livechat/tests/test_livechat_basic_flow.py:181-198, 383-408).
- Pages can opt out via a `no_livechat` template flag (website_livechat/views/website_livechat.xml:10).
- Demo-only: chatbot demo data and demo session (website_livechat/__manifest__.py:20-23).

## F. Effective extension path (module names only)
- Modules touching the same models in this family: website.visitor (website_crm, website_crm_sms, website_event, website_event_track, website_livechat, website_sale, website_sms), website.page (website, website_hr_recruitment, website_livechat, website_project, website_sale), crm-side (website_crm_livechat, crm_livechat).

## G. Not verified
- Operator assignment, availability, forwarding and rating rules: UNKNOWN — EVIDENCE INSUFFICIENT (owned by im_livechat; not traced).
- Bot reliability, mobile UI, bus behaviour tests present but not analysed (TEST) (website_livechat/tests/test_lazy_frontend_bus.py; website_livechat/tests/test_chatbot_ui.py).

