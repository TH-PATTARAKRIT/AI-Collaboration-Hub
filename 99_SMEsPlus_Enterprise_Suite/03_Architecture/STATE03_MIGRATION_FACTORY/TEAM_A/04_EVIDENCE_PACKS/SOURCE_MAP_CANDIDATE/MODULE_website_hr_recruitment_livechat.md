# Source Map (candidate) — `website_hr_recruitment_livechat`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_hr_recruitment_livechat` |
| Display name | Website IM Livechat HR Recruitment |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `eebbea36275cde06` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_hr_recruitment_livechat/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `website_hr_recruitment`, `im_livechat`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Live Chat / Chatbot for the HR Recruitment
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 16 of 17 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_hr_recruitment_livechat (Website IM Livechat HR Recruitment)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_hr_recruitment_livechat.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: a chatbot to guide candidates to the right job position (website_hr_recruitment_livechat/__manifest__.py:4,10-12).

## A. Capabilities / functions
- Optional add-on: depends on website_hr_recruitment and im_livechat; no `auto_install` (website_hr_recruitment_livechat/__manifest__.py:6-9). It contains no Python and no non-demo data files; the manifest's only data entry is a demo file (website_hr_recruitment_livechat/__manifest__.py:14-16). So the guided "Jobs Bot" exists only when demo data is loaded; installing without demo adds no behaviour by evidence in this module.
- Demo content: a script titled "Jobs Bot" (website_hr_recruitment_livechat/data/website_hr_recruitment_livechat_chatbot_demo.xml:4-7), a live chat rule that auto-opens the chat after 2 seconds on the jobs list page URL pattern (website_hr_recruitment_livechat/data/website_hr_recruitment_livechat_chatbot_demo.xml:9-15).
- Demo conversation: welcome, then choice of department (Sales, Services, R&D), then a suggested position, then an offer to chat with HR; "yes" hands over to a human operator, with a fallback to asking for the visitor's email and a thank-you; "no" gives a link to the matching job page (website_hr_recruitment_livechat/data/website_hr_recruitment_livechat_chatbot_demo.xml:17-407 for the steps; links at 108, 215, 304, 395).

## B. Business objects, relationships, lifecycle
- Objects are owned by im_livechat: chatbot script, script steps, answers, and channel rule (im_livechat/models/im_livechat_channel.py:600-640). The script is attached to the default livechat channel through the rule (website_hr_recruitment_livechat/data/website_hr_recruitment_livechat_chatbot_demo.xml:14).
- Lifecycle of a chat is owned by im_livechat; the collected email is stored by the chatbot step (step type "email") (website_hr_recruitment_livechat/data/website_hr_recruitment_livechat_chatbot_demo.xml:85-89). Where the email lands (lead/applicant/contact): UNKNOWN — EVIDENCE INSUFFICIENT.

## C. Validations, automation, security, multi-company
- Rule matching: first matching rule by sequence and URL pattern; a rule with an inactive or empty script is skipped (im_livechat/models/im_livechat_channel.py:632-650).
- Demo answers redirect to fixed job page paths (e.g. marketing-and-community-manager-6, consultant-3, experienced-developer-4), which exist only if demo jobs of website_hr_recruitment exist (website_hr_recruitment_livechat/data/website_hr_recruitment_livechat_chatbot_demo.xml:108,215,304,395). Existence: UNKNOWN — EVIDENCE INSUFFICIENT.
- No access-control rows, record rules or company scoping in this module. Data records are `noupdate` (website_hr_recruitment_livechat/data/website_hr_recruitment_livechat_chatbot_demo.xml:3).

## D. Handoffs to other modules
- im_livechat: chat channels, operators, chatbot engine; website_hr_recruitment: jobs list and job detail pages (website_hr_recruitment/controllers/main.py:29-30).
- Related, separate livechat glue for the website: website_livechat; for CRM: website_crm_livechat.

## E. Configuration / defaults that change outcomes
- Rule URL pattern (jobs page only), action "open automatically" and 2-second delay are set in the demo rule (website_hr_recruitment_livechat/data/website_hr_recruitment_livechat_chatbot_demo.xml:10-13). Chatbot enabling condition defaults to always in the rule model (im_livechat/models/im_livechat_channel.py:618-625).
- Operator availability drives the "none of our operators are available" branch (website_hr_recruitment_livechat/data/website_hr_recruitment_livechat_chatbot_demo.xml:75-83). Exact routing logic: UNKNOWN — EVIDENCE INSUFFICIENT.

## F. Effective extension path (module names only)
- Nothing in this module extends code. Rules/scripts are edited by users in im_livechat's configuration. Related modules: im_livechat, website_livechat, website_hr_recruitment.

## G. Not verified
- Behaviour with demo data disabled in production: UNKNOWN — EVIDENCE INSUFFICIENT. Tests: none.

