# Source Map (candidate) — `crm`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `crm` |
| Display name | CRM |
| Manifest version | 1.9 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `2a7b1a3c1390eccd` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/crm/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`, `sales_team`, `mail`, `calendar`, `resource`, `utm`, `web_tour`, `contacts`, `digest`, `phone_validation`
- Direct dependents in 300-module list (11): `crm_livechat`, `crm_mail_plugin`, `crm_sms`, `event_crm`, `iap_crm`, `partnership`, `sale_crm`, `survey_crm`, `website_crm`, `website_crm_partner_assign`, `website_crm_sms`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `mass_mailing_crm`, `test_crm_full`, `test_discuss_full`, `test_main_flows`
- Custom / third-party modules that declare a dependency (name — license only) (1): `social_hub` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Sales/CRM / Track leads and close opportunities
- Inventory of user-facing artifacts (counts): menu items 26, views 55, window actions 33, server actions 2, reports 0, mail templates 1, scheduled jobs 2, wizards 6, web routes 3
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (12): `crm.lead.pls.update` (Update the probabilities); `crm.lead2opportunity.partner` (Convert Lead to Opportunity (not in mass)); `crm.lead.lost` (Get Lost Reason); `crm.lead2opportunity.partner.mass` (Convert Lead to Opportunity (in mass)); `crm.merge.opportunity` (Merge Opportunities); `crm.lost.reason` (Opp. Lost Reason); `crm.lead.scoring.frequency` (Lead Scoring Frequency); `crm.lead.scoring.frequency.field` (Fields that can be used for predictive lead scoring computation); `crm.recurring.plan` (CRM Recurring revenue plans); `crm.stage` (CRM Stages); `crm.lead` (Lead); `crm.activity.report` (CRM Activity Analysis)
- Objects extended from other modules (18): `digest.digest`, `mail.alias.mixin`, `crm.team`, `crm.team.member`, `calendar.event`, `utm.campaign`, `mail.activity`, `ir.config_parameter`, `res.users`, `res.config.settings`, `mail.thread.cc`, `mail.thread.blacklist`, `mail.thread.phone`, `mail.activity.mixin`, `utm.mixin`, `format.address.mixin`, `mail.tracking.duration.mixin`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 1 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `crm.lead` ← Community: `crm_iap_enrich`, `crm_iap_mine`, `crm_livechat`, `crm_mail_plugin`, `event_crm`, `iap_crm`, `mass_mailing_crm`, `sale_crm`, `survey_crm`, `website_crm` … (+3); open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `digest.digest`, `mail.alias.mixin`, `crm.team`, `crm.team.member`, `calendar.event`, `utm.campaign`, `mail.activity`, `ir.config_parameter`, `res.users`, `res.config.settings`, `mail.thread.cc`, `mail.thread.blacklist`, `mail.thread.phone`, `mail.activity.mixin`, `utm.mixin`, `format.address.mixin`, `mail.tracking.duration.mixin`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 4 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Predictive Lead Scoring: Recompute Automated Probabilities every 1 days; CRM: Lead Assignment every 1 days
- Security: groups declared 2 (`group_use_lead`, `group_use_recurring_revenues`); record rules 8 (of which company-scoped by text 2); access rows 32

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 98 of 101 source pointers resolve to an existing file and in-range line (3 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: crm (CRM)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/crm.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests (crm/tests).

## A. Capabilities / functions
- Core application: track leads and close opportunities in a sales pipeline (crm/__manifest__.py:6-10, 72). Depends on sales_team, mail, calendar, resource, utm, contacts, digest, phone_validation, base_setup, web_tour (crm/__manifest__.py:12-23).
- Core: one record type serves both an unqualified "lead" and a qualified "opportunity"; new records default to lead only when the user is in the optional "Show Lead Menu" group, otherwise opportunity (crm/models/crm_lead.py:123-125; crm/security/crm_security.xml:5-7).
- Core: pipeline stages, priority, expected revenue, expected closing date, tags, sales team and salesperson, lost reason, meetings, activities, chatter, campaign/medium/source tracking (crm/models/crm_lead.py:101-162, 227-244, 249-252).
- Optional: recurring-revenue fields and plans, gated by the "Show Recurring Revenues Menu" group; copies of a lead drop them when the group is off (crm/security/crm_security.xml:9-11; crm/models/crm_lead.py:143-150, 1027-1029).
- Optional: rule-based lead assignment to teams and salespeople, manual or repeated via a daily job that ships switched off (crm/models/res_config_settings.py:20-39; crm/data/ir_cron_data.xml:3-12; crm/models/crm_team.py:163-254).
- Optional: predictive lead scoring using won/lost history over chosen fields; its recompute job ships switched off; default scoring fields are phone quality, email quality, state, country, source, language, tags (crm/data/crm_lead_prediction_data.xml:26-29, 36-45; crm/models/crm_lead.py:2194-2215, 2397-2405).
- Optional (settings): lead mining, enrichment and website-visitor lead creation modules, membership/partnership module (crm/models/res_config_settings.py:18, 40-48).
- Conversion and cleanup tools: convert lead to opportunity (single or mass), merge duplicates, mark won or lost with reasons (crm/wizard/crm_lead_to_opportunity.py:9-177; crm/wizard/crm_lead_to_opportunity_mass.py:7-113; crm/wizard/crm_merge_opportunities.py:17-59; crm/wizard/crm_lead_lost.py:9-30).
- Inbound email creates leads through the sales team's mail alias (crm/models/crm_team.py:147-157; crm/models/crm_lead.py:2125-2146).
- Reporting: activity report and opportunity report views, digest KPIs (crm/__manifest__.py:52, 58-59; crm/report/crm_activity_report.py).

## B. Business objects, relationships, lifecycle
- Lead/Opportunity (crm.lead) -> optional customer contact, salesperson, sales team, company, stage, lost reason, tags, meetings, recurring plan (crm/models/crm_lead.py:104-119, 130-136, 171-173, 234-238). Sales Team (crm.team) extends the base team from sales_team with lead/pipeline switches, mail alias and assignment settings (crm/models/crm_team.py:18-35). Team member extended with capacity and assignment filters (crm/models/crm_team_member.py:15-29).
- Stages: named, ordered, optionally limited to certain teams, may be marked "won", may be folded, may define a rotting threshold in days (crm/models/crm_stage.py:25-33). Default stages: New, Qualified, Proposition, Won (crm/data/crm_stage_data.xml:3-24). Default lost reasons: Too expensive, no people/skills, not enough stock (crm/data/crm_lost_reason_data.xml:4-12).
- Won / lost / pending is derived, not typed: WON = probability 100 and current stage is a won stage; LOST = archived and probability 0; otherwise pending (crm/models/crm_lead.py:612-620).
- Mark won: reactivates, moves to the next won stage after the current one by stage order (else the nearest earlier won stage), sets probability 100 (crm/models/crm_lead.py:1127-1151). Entering a won stage forces active and probability 100 (crm/models/crm_lead.py:841-845); (TEST) (crm/tests/test_crm_pls.py:741-782).
- Mark lost: archives, sets probability 0 and stores the chosen reason; closing note is logged in chatter (crm/models/crm_lead.py:1121-1125; crm/wizard/crm_lead_lost.py:19-30). Restoring a lost record clears the reason and resets probability to the automated value (crm/models/crm_lead.py:1101-1119); (TEST) reactivated lead is pending again (crm/tests/test_crm_pls.py:782-798).
- Closed date is set when probability reaches 100 or the record is archived, cleared when reopened, kept when moving between two won stages, and set at creation when created in a won stage (crm/models/crm_lead.py:802-804, 855-861, 874-881); (TEST) (crm/tests/test_crm_lead.py:294-348).
- Stage change stamps a last-stage-update date; user change stamps an assignment date (crm/models/crm_lead.py:837-853).
- Conversion lead -> opportunity: skipped for archived or won records; sets type, conversion date, links or creates the customer, then assigns salesperson/team (round-robin across given salespeople) (crm/models/crm_lead.py:1833-1861, 1880-1902; crm/wizard/crm_lead_to_opportunity.py:121-177). Wizard refuses probability-100 leads (crm/wizard/crm_lead_to_opportunity.py:22-24). Mass convert can merge duplicates first (crm/wizard/crm_lead_to_opportunity_mass.py:84-107). (TEST) (crm/tests/test_crm_lead_convert.py:150-470).
- Merge: keeps the most confident record (not lost, opportunity over lead, higher stage, higher probability, newer) and folds others into it; text concatenated, relational first-non-empty prevails (crm/models/crm_lead.py:1479-1522, 1540-1594, 1943-1965); (TEST) (crm/tests/test_crm_lead_merge.py:159-300). Duplicates are matched on normalized email and/or customer; by default only active, pending records count (crm/models/crm_lead.py:1911-1941).
- Automatic assignment without rules: a userless lead in a team created from an incoming email goes to the team leader (also from livechat via crm_livechat); when rule-based assignment is on this step is skipped (crm/models/crm_lead.py:1442-1452, 2145, 2070-2073; crm_livechat/models/chatbot_script_step.py:81). Leads created by other means: UNKNOWN — EVIDENCE INSUFFICIENT.
- Rule-based assignment: unassigned, not-won leads created within a look-back window and matching each team's filter are spread across teams by weighted random choice on capacity, deduplicated/merged, then given to members according to daily quota (capacity/30) (crm/models/crm_team.py:323-441, 452-482; crm/models/crm_team_member.py:90-99); (TEST) (crm/tests/test_crm_lead_assignment.py:113-624).
- Probability: automated (statistical) value follows stage, team and chosen fields; the manual probability follows it only while both are equal (crm/models/crm_lead.py:552-566). Prorated revenue = revenue x probability (crm/models/crm_lead.py:568-586).

## C. Validations, automation, security, multi-company
- Probability must be 0-100 (crm/models/crm_lead.py:254-257). A lead in a won stage must be at 100 (crm/models/crm_lead.py:262-266); a lead cannot be both won and lost (crm/models/crm_lead.py:1003-1004); (TEST) (crm/tests/test_crm_pls.py:741-780).
- Stage must belong to the lead's team or be team-less; stage is recomputed if the team changes (crm/models/crm_lead.py:130-134, 353-357).
- Merge needs at least two records and, unless superuser, at most five at once (crm/models/crm_lead.py:1546-1550). Assignment domains on teams and members must parse and search (crm/models/crm_team.py:82-90; crm/models/crm_team_member.py:60-84). Rule-based assignment can only be started by sales managers or administrators (crm/models/crm_team.py:242-243). Recurring plan months cannot be negative (crm/models/crm_recurring_plan.py:17-20). Auto-assignment repeat frequency must be positive and under 100 (crm/models/res_config_settings.py:70-75).
- Access lists: salespeople read/write/create leads without delete; sales managers full control incl. delete; all internal users read stages and lost reasons; only managers edit stages, lost reasons, recurring plans and activity plans; conversion, merge and lost wizards for salespeople; scoring tables read-only; PLS update wizard for ERP managers (crm/security/ir.model.access.csv:2-33).
- Record rules: salespeople see only own or unassigned leads unless in the "all leads" group; a company rule limits leads to the user's allowed companies or company-less leads; the activity report follows the same personal/all/company pattern; managers manage lead activity plans (crm/security/crm_security.xml:19-73); (TEST) rights on lost reasons and wizards (crm/tests/test_crm_pls.py:982-1010).
- Company logic: a lead's company is proposed from the team's company, else the user's, else the customer's, and is reset when inconsistent with user or team (crm/models/crm_lead.py:316-351); (TEST) (crm/tests/test_crm_lead_multicompany.py:24-64). Leads with no company are visible across companies; currency shown follows the lead's company or the current company (crm/models/crm_lead.py:277-283).
- Partner and contact visibility: opportunity counts on contacts appear only for salespeople (crm/models/res_partner.py:26-30); salespeople also get create/write on partners and categories through this module (crm/security/ir.model.access.csv:8-9).
- Notifications and tracking: won, lost, restored, stage-change subtypes on the chatter; meetings created from a lead are logged on it (crm/models/crm_lead.py:2088-2100; crm/models/calendar.py:38-44).
- Deleting a lead detaches its meetings rather than deleting them (crm/models/crm_lead.py:1040-1052); deleting a team folds its scoring statistics into the no-team statistics (crm/models/crm_team.py:107-141); (TEST) (crm/tests/test_crm_pls.py:801-873).
- Lead has a "last action" date field that the automation engine stamps when a rule runs on it (crm/models/crm_lead.py:154; base_automation/models/base_automation.py:809-810).

## D. Handoffs
- Sales: sale_crm (auto-installed with sale and crm) adds opportunity link on orders, quotation creation from an opportunity, order counts/totals on the opportunity, and raises expected revenue to a confirmed order's untaxed amount when it is higher and same currency (sale_crm/__manifest__.py:19,28; sale_crm/models/sale_order.py:10-20; sale_crm/models/crm_lead.py:10-13, 103-109). Owner of orders and invoicing: sale and account, not crm.
- Teams, salesperson groups, default team lookup: owned by sales_team (crm/security/ir.model.access.csv:2-4; sales_team/models/crm_team.py:17).
- Meetings: calendar events link to opportunities (crm/models/calendar.py:26-28). Mail gateway aliases: mail via team alias (crm/models/crm_team.py:147-157). Campaign/source/medium: utm (crm/models/utm.py:7-30). Partner phone/email validation: phone_validation.
- Accounting handoff: none in crm; downstream via sale_crm -> sale -> account. Portal handoff: none in crm.
- Add-ons depending on crm in Community: crm_livechat, crm_mail_plugin, crm_sms, event_crm, iap_crm, mass_mailing_crm, partnership, sale_crm, survey_crm, website_crm, website_crm_partner_assign, website_crm_sms (reverse-dependency list of the source map).

## E. Configuration/defaults that change outcomes
- "Leads" group switch changes default record type and turns lead usage on/off across all teams that use the pipeline; team mail aliases are rebuilt (crm/models/res_config_settings.py:135-145; crm/models/crm_team.py:96-105, 153-156).
- Team switches "Leads" and "Pipeline"; alias name; assignment domain; opt-out from assignment (crm/models/crm_team.py:23-35).
- Member capacity default 30 leads per 30 days and preferred/own assignment filters; pause assignment (crm/models/crm_team_member.py:20-23).
- System parameters: rule-based assignment on/off; assignment delay in hours and commit batch size; scoring start date (default 8 days back) and scoring fields (crm/models/res_config_settings.py:20, 49-52; crm/models/crm_lead.py:2070-2073; crm/models/crm_team.py:365-381; crm/data/crm_lead_prediction_data.xml:26-33). Changing scoring fields reloads the lead model definition (crm/models/ir_config_parameter.py:11-32).
- Stage settings "is won", "fold", "rotting days", and team restriction (crm/models/crm_stage.py:27-32); changing "is won" recalculates probabilities of all leads in the stage (crm/models/crm_stage.py:55-70).
- Rule-based assignment jobs: daily by default, off until enabled in settings (crm/data/ir_cron_data.xml:8-11; crm/models/res_config_settings.py:147-161).

## F. Effective extension path
- sales_team (teams/groups); sale_crm (quotations); base_automation (rules on lead events); website_crm, crm_livechat, crm_mail_plugin, crm_sms, mass_mailing_crm, survey_crm, event_crm (lead sources); iap_crm and website_crm_partner_assign/partnership (enrichment, partner assignment); calendar, mail, utm, phone_validation (dependencies).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: details of the statistical probability computation beyond its documented method and controls (only outline and settings read).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of the base team model and default team choice (owned by sales_team; only its existence confirmed).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end forecast views and JavaScript behaviour (assets were listed but not traced).
- UNKNOWN — EVIDENCE INSUFFICIENT: precise output of the opportunity report model (crm_opportunity_report is referenced by the manifest but its model file was not among the files read).
- Revision `19.0.post20260921`; findings apply to this revision only and are not universal rules.

