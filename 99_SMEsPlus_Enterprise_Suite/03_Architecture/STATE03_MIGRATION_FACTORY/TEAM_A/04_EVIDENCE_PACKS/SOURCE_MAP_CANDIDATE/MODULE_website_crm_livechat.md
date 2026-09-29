# Source Map (candidate) — `website_crm_livechat`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_crm_livechat` |
| Display name | Lead Livechat Sessions |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `44fc1e115b51f657` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_crm_livechat/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `website_crm`, `website_livechat`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_crm_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / View livechat sessions for leads
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `discuss.channel`, `chatbot.script.step`, `crm.lead`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `discuss.channel`, `chatbot.script.step`, `crm.lead`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 17 of 18 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_crm_livechat (Lead Livechat Sessions)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_crm_livechat.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: view live-chat sessions from a lead via a stat button (website_crm_livechat/__manifest__.py:6-8).

## A. Capabilities / functions
- Conditional: depends on website_crm and website_livechat with `auto_install` (website_crm_livechat/__manifest__.py:9,14); activates automatically when both exist.
- Core: "Sessions" stat button on the lead form counting live-chat conversations of the lead's linked visitors; clicking lists those sessions that have at least one message (website_crm_livechat/views/website_crm_lead_views.xml:8-13; website_crm_livechat/models/crm_lead.py:10-21).
- Core: a lead created by an operator with the chat "/lead" command is linked to the chat's visitor; the lead's country defaults to the visitor's country (website_crm_livechat/models/discuss_channel.py:10-19). The command itself is defined in crm_livechat (crm_livechat/models/discuss_channel.py:28-44, 46-72).
- Core: a lead created by a chatbot "create lead" step gets a name from the visitor's display name and is linked to the visitor (website_crm_livechat/models/chatbot_script_step.py:11-16). The base step logic (name from first free-text answer, team compatibility with company, lead vs opportunity by team) is in crm_livechat (crm_livechat/models/chatbot_script_step.py:29-48).

## B. Business objects, relationships, lifecycle
- Lead (crm) <-> visitors (website_crm) -> live-chat conversations (discuss channels via website_livechat) (website_crm_livechat/models/crm_lead.py:12-15).
- Lifecycle: chat -> lead created by operator command or chatbot step -> lead joined to visitor -> sessions visible from the lead. Leads created by the base command are unassigned (no salesperson or team) with chat history as description (crm_livechat/models/discuss_channel.py:62-72).

## C. Validations, automation, security, multi-company
- Session count and stat button are visible only to live-chat users group (`im_livechat.im_livechat_group_user`) (website_crm_livechat/models/crm_lead.py:10; website_crm_livechat/views/website_crm_lead_views.xml:10).
- The link to visitor is written with elevated rights (website_crm_livechat/models/discuss_channel.py:15-17).
- Team assigned by a chatbot step is dropped when its company differs from the acting user's contact company (crm_livechat/models/chatbot_script_step.py:34-36).
- No access-control rows or record rules of its own; no company scoping added.

## D. Handoffs to other modules
- website_crm (visitor-lead link), website_livechat (visitor sessions action `website_livechat.website_visitor_livechat_session_action`, website_livechat/views/website_visitor_views.xml:3), crm_livechat (lead creation commands and chatbot step logic), crm, im_livechat.

## E. Configuration / defaults that change outcomes
- Chatbot step type "create lead" and its sales team are configured in the chatbot script (crm_livechat/models/chatbot_script_step.py:20-23). UTM source of live-chat leads comes from a crm_livechat record (crm_livechat/models/discuss_channel.py:62, 71).

## F. Effective extension path (module names only)
- crm.lead: also extended by crm_livechat, website_crm, website_crm_partner_assign and others. discuss.channel and chatbot.script.step extended by: crm_livechat, website_crm_livechat (plus im_livechat/website_livechat for channel).

## G. Not verified
- Tests: none in this module. Behaviour when a visitor has no linked channels or when the lead has several visitors: UNKNOWN — EVIDENCE INSUFFICIENT.

