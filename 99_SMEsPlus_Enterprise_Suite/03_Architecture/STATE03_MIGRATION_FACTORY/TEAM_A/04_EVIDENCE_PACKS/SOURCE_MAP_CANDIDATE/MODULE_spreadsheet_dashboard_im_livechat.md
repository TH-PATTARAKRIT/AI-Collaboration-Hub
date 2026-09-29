# Source Map (candidate) — `spreadsheet_dashboard_im_livechat`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `spreadsheet_dashboard_im_livechat` |
| Display name | Spreadsheet dashboard for live chat |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e6323d7584165adb` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/spreadsheet_dashboard_im_livechat/` |
| auto_install / application | ['im_livechat'] / None |

## 2. Dependencies
- Direct dependencies (manifest): `spreadsheet_dashboard`, `im_livechat`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Dashboard / Spreadsheet
- Inventory of user-facing artifacts (counts): menu items 5, views 0, window actions 5, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 13 of 16 source pointers resolve to an existing file and in-range line (3 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: spreadsheet_dashboard_im_livechat (Live Chat dashboards)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/spreadsheet_dashboard_im_livechat.json. Pointers are `module/path:LINE`; JSON payload pointers cite the file (no meaningful line numbers). (TEST): module ships no tests.

## A. Capabilities / functions
- Ships two dashboards in the Dashboards app under the Website group: "Live Chat" (statistics) and "Live Chat - Ongoing Sessions" (real-time view) (spreadsheet_dashboard_im_livechat/data/dashboards.xml:4-13, 15-24; group defined spreadsheet_dashboard/data/dashboard.xml:19-22).
- Conditional-on-install: depends on the dashboard framework and live chat (spreadsheet_dashboard_im_livechat/__manifest__.py:9); auto_install on im_livechat (spreadsheet_dashboard_im_livechat/__manifest__.py:15), so it is added automatically with live chat. Not an application; no settings.
- "Live Chat" content: sessions count, session duration, time to respond, messages per session, rating gauge, sessions with calls (count and share), call duration, handled by bot / by agent, escalated, not answered, no one available; breakdowns by agent, country, language, expertise and chatbot answer; filters period, agents, countries, languages, channels, expertises (spreadsheet_dashboard_im_livechat/data/files/livechat_dashboard.json).
- "Ongoing Sessions" content: currently open sessions (no end time), split by bot / agent / escalated / in call, per-agent response time with a call indicator, plus country, language, expertise and chatbot-answer breakdowns; same filters minus period (spreadsheet_dashboard_im_livechat/data/files/livechat_ongoing_dashboard.json).
- Adds five technical "Sessions" menu entries (ongoing: all, escalated, agents in call, handled by agent, handled by bot) that open the session list with pre-set filters, used as drill-downs from the ongoing dashboard (spreadsheet_dashboard_im_livechat/data/livechat_ongoing_sessions_actions.xml:3-20, 21-37, 38-54, 55-71, 72-88). The "all" action restricts to live-chat type sessions (:5); the others rely on filters defined in live chat (the pre-set filters ongoing, escalated, handled by agent, handled by bot and in call exist in live chat's session search: im_livechat/views/discuss_channel_views.xml:17, 43-46; the last four are hidden, technical filters).

## B. Business objects, relationships, lifecycle
- Reads the live-chat report model and the agent participation history model (livechat_dashboard.json; livechat_ongoing_dashboard.json); declared main data model is the report (spreadsheet_dashboard_im_livechat/data/dashboards.xml:7, 18).
- "Ongoing" is defined as sessions with no end time (livechat_ongoing_dashboard.json, data-source filters). Escalated = flagged as escalated on the channel (same file).
- Chatbot-only sessions are excluded from the per-agent tables in the statistics dashboard (livechat_dashboard.json, agent pivots filter on partners without chatbot scripts).
- Sample dashboard variants are provided for empty databases (dashboards.xml:8, 19; framework: spreadsheet_dashboard/models/spreadsheet_dashboard.py:59-73).
- No lifecycle of its own.

## C. Validations, automation, security, multi-company
- Visibility of both dashboards: live-chat manager group only (spreadsheet_dashboard_im_livechat/data/dashboards.xml:10, 21). Drill-down menus are also manager-only (spreadsheet_dashboard_im_livechat/data/livechat_ongoing_sessions_actions.xml:19, 36, 53, 70, 87).
- Framework rules: group-intersection visibility and manager override (spreadsheet_dashboard/security/security.xml:4-9, 31-36); company-less dashboards pass the multi-company rule (:11-15). No company set on these records.
- Agent-side "My Team" filter is a separate bridge (hr_livechat) and is not applied to these dashboards.
- Cell-level data exposure vs underlying access rights: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Accounting / payroll / analytic handoffs
- None. Owned entirely by live chat reporting; no accounting, payroll or analytic link.

## E. Configuration / defaults that change outcomes
- Group assignment on the dashboard records (dashboards.xml:10, 21); publication flag on (dashboards.xml:12, 23); sequences 100 and 125 (dashboards.xml:11, 22).
- Rating, bot vs agent and escalation figures depend on live-chat channel configuration owned by im_livechat (not traced here).

## F. Effective extension path (module names only)
- Extends spreadsheet_dashboard and im_livechat (menus placed under im_livechat's technical menu: spreadsheet_dashboard_im_livechat/data/livechat_ongoing_sessions_actions.xml:18; parent defined im_livechat/views/im_livechat_channel_views.xml:345). Sibling dashboard modules listed in the spreadsheet_dashboard_account note. Manifest dependents: none found.

## G. Not verified
- Definitions of session_outcome categories (escalated / not answered / no one available): UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether the hidden filters behave identically to the dashboard's own ongoing/escalated definitions: UNKNOWN — EVIDENCE INSUFFICIENT.
- Revision `19.0.post20260921`.

