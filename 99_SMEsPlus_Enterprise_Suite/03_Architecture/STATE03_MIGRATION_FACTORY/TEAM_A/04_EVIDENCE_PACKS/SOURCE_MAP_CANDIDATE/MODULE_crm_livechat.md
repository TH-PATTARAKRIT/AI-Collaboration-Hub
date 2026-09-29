# Source Map (candidate) — `crm_livechat`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `crm_livechat` |
| Display name | CRM Livechat |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `3beb12f47b636ba9` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/crm_livechat/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `crm`, `im_livechat`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_discuss_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/CRM / Create lead from livechat conversation
- Inventory of user-facing artifacts (counts): menu items 0, views 4, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (6): `discuss.channel`, `chatbot.script`, `chatbot.script.step`, `res.users`, `crm.lead`, `im_livechat.report.channel`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `discuss.channel`, `chatbot.script`, `chatbot.script.step`, `res.users`, `crm.lead`, `im_livechat.report.channel`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 2 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 50 of 51 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: crm_livechat (CRM Livechat)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/crm_livechat.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge from live chat to CRM: create leads from a chat conversation (crm_livechat/__manifest__.py:7, 17-20). Conditional: auto-installs when crm and im_livechat are both present (crm_livechat/__manifest__.py:22).
- Operator command "/lead <title>" inside a chat: creates a lead titled from the text, whole chat transcript as description, referred-by = the operator's name, source = "Livechat", no team and no salesperson preset; confirms with a transient message containing a link (crm_livechat/models/discuss_channel.py:28-72; crm_livechat/static/src/core/channel_commands.js:4-8). Typing only "/lead" shows usage help (crm_livechat/models/discuss_channel.py:31-40). Command is offered when the user has livechat access (crm_livechat/static/src/core/channel_commands.js:5).
- Chatbot step type "Create Lead": at that step the bot builds a lead from the visitor's email/phone and the conversation; optional target sales team on the step (crm_livechat/models/chatbot_script_step.py:13-23, 59-82).
- Chatbot step type "Create Lead & Forward": creates the lead, then hands the chat to a human operator chosen among available members of eligible sales teams; the lead is assigned to that operator (crm_livechat/models/chatbot_script_step.py:84-127).
- Sample "Lead Generation Bot" script shipped as data: greeting free text, forward-to-operator, "none available" message, email question, then create-lead (crm_livechat/data/crm_livechat_chatbot_data.xml:10-47). Optional (starting point to copy/adapt) (crm_livechat/data/crm_livechat_chatbot_data.xml:4-8).
- UTM source "Livechat" seeded (crm_livechat/data/utm_data.xml:3-5).
- Lead form: "View chat" button for sales users when a lead has an origin chat (crm_livechat/views/crm_lead_views.xml:8-11; crm_livechat/models/crm_lead.py:39-43). Chatbot script form: "Leads" counter button opening leads of that script's source (crm_livechat/views/chatbot_script_views.xml:9-14; crm_livechat/models/chatbot_script.py:10-25).
- Live chat statistics report gains a "Leads created" measure per chat (crm_livechat/report/im_livechat_report_channel.py:10-25).
- Operator sidebar shows the visitor's opportunities when the user can read leads (crm_livechat/models/discuss_channel.py:74-84).

## B. Business objects, relationships, lifecycle
- Lead -> originating chat channel (many-to-one, read-only, indexed) (crm_livechat/models/crm_lead.py:11-16); channel -> its leads (one-to-many, visible to sales group only) plus a stored "has lead" flag (crm_livechat/models/discuss_channel.py:13-26).
- Chatbot script -> leads via shared marketing source (crm_livechat/models/chatbot_script.py:14-15). Step -> optional sales team (crm_livechat/models/chatbot_script_step.py:20-23).
- Lead naming: /lead uses the typed title (crm_livechat/models/discuss_channel.py:65); bot uses the visitor's first free-text answer truncated to 100 chars, else "<bot title>'s New Lead" (crm_livechat/models/chatbot_script_step.py:30-32). (TEST) default name confirmed (crm_livechat/tests/test_chatbot_lead.py:90).
- Customer linking on /lead: participants that are external (not internal users) are considered; if an anonymous/public participant is present no customer is set; otherwise the first external participant is used (crm_livechat/models/discuss_channel.py:51-60, 66). (TEST) guest gives no customer; portal user becomes customer (crm_livechat/tests/test_crm_lead.py:29-93).
- Bot lead: public visitor -> lead carries the captured email and phone only; logged-in user -> lead linked to that user's contact and the contact's email/phone updated if different (crm_livechat/models/chatbot_script_step.py:69-77). (TEST) portal user keeps email, phone updated (crm_livechat/tests/test_chatbot_lead.py:85-96).
- Lead type/team: with a team, type is "lead" if the team uses leads, else "opportunity"; lead starts with no salesperson, then auto-assignment from the team is attempted (crm_livechat/models/chatbot_script_step.py:42-46, 81). (TEST) team with leads gives type lead (crm_livechat/tests/test_chatbot_lead.py:96).
- Forward variant: candidate teams = the lead's team, else all teams not opted out of assignment that use leads or opportunities, have a positive assignment capacity and whose domain matches the lead; candidate users = members not opted out, with quota left, matching member domain; then available operators among them (crm_livechat/models/chatbot_script_step.py:85-115). If the operator changes, lead gets that user and their team, and a notice is sent (crm_livechat/models/chatbot_script_step.py:116-126). (TEST) forwarded lead assigned to available member (crm_livechat/tests/test_chatbot_lead.py:22-83).
- If no operator is available, the lead stays unassigned and the chat continues with the script's next steps: inferred from the sample script (crm_livechat/data/crm_livechat_chatbot_data.xml:28-33); exact fallback UNKNOWN — EVIDENCE INSUFFICIENT.

## C. Validations, automation, security, multi-company
- Lead cannot be created or re-linked to a chat the actor cannot read; error message shown (crm_livechat/models/crm_lead.py:18-37). (TEST) (crm_livechat/tests/test_discuss_channel_access.py:41-68).
- Sales users (basic salesman group) may read any chat that has at least one lead; no write/create/delete from this rule; and may read and add participants to such chats (not edit/remove) (crm_livechat/security/crm_livechat_security.xml:3-20). (TEST) only salesman-with-lead case can read; internal users without sales group, portal and public cannot (crm_livechat/tests/test_discuss_channel_access.py:9-39). Rules are loaded once (noupdate) (crm_livechat/security/crm_livechat_security.xml:2).
- Multi-company on bot leads: if the visitor contact's company and the step's team company both exist and differ, the team is dropped (lead unassigned to team); forward variant keeps only teams with no company or matching the contact's company (crm_livechat/models/chatbot_script_step.py:35-36, 97-101). (TEST) matrix of contact/team company combinations (crm_livechat/tests/test_chatbot_lead.py:98-131, 133-189).
- "Leads" counters use elevated read across companies and include archived leads (crm_livechat/models/chatbot_script.py:14).
- Client flag telling the UI whether the user can create leads is based on the salesman group (crm_livechat/models/res_users.py:10).
- Access entries: none added; groups defined: none (skeleton).

## D. Handoffs to other modules
- crm: owns lead object, team assignment (`_assign_userless_lead_in_team` called here, crm_livechat/models/chatbot_script_step.py:81), team capacities and domains.
- im_livechat: owns chat sessions, operators, chatbot scripts/steps, operator forwarding (crm_livechat/models/chatbot_script_step.py:116) and reporting base.
- mail (discuss): owns channel, members, transient bus messages.
- sales_team: owns sales groups and teams.
- utm: owns marketing source record. No accounting, analytic, sale or timesheet handoff.

## E. Configuration / defaults that change outcomes
- Step's sales team drives lead type and initial assignment; empty team -> unassigned, type from crm defaults (crm_livechat/models/chatbot_script_step.py:42-46).
- Team assignment capacity, opt-out flags, assignment domains (crm) decide who receives forwarded leads (crm_livechat/models/chatbot_script_step.py:88-107).
- Operator availability from the live chat channel decides forward success (crm_livechat/models/chatbot_script_step.py:111-115).
- Leads via chatbot carry the script's own marketing source; via /lead carry "Livechat" source (crm_livechat/models/chatbot_script_step.py:41; crm_livechat/models/discuss_channel.py:62, 71).

## F. Effective extension path
- Extends crm.lead, discuss.channel, chatbot script/step, live chat report, users' client data. Modules: crm, im_livechat, mail, sales_team, utm.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour when the source record for a script is empty (counter grouping).
- UNKNOWN — EVIDENCE INSUFFICIENT: exact lead deduplication for repeat visitors.
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end-only pieces (assets under static) beyond the command registration.

