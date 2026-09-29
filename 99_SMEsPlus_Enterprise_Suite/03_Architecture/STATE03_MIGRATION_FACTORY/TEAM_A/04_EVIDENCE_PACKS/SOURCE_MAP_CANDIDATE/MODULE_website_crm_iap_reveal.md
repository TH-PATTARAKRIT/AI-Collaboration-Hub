# Source Map (candidate) — `website_crm_iap_reveal`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_crm_iap_reveal` |
| Display name | Lead Generation From Website Visits |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a4ba1a274669e6ef` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_crm_iap_reveal/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `iap_crm`, `iap_mail`, `crm_iap_mine`, `website_crm`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `test_crm_full`, `test_website_modules`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/CRM / Generate Leads/Opportunities from your website's traffic
- Inventory of user-facing artifacts (counts): menu items 2, views 14, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 1, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `crm.reveal.view` (CRM Reveal View); `crm.reveal.rule` (CRM Lead Generation Rules)
- Objects extended from other modules (2): `ir.http`, `crm.lead`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.http`, `crm.lead`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Lead Generation: Leads/Opportunities Generation every 1 days
- Security: groups declared 0 (—); record rules 4 (of which company-scoped by text 0); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 40 of 40 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_crm_iap_reveal (revision 19.0.post20260921)
Scope: Odoo Community read-only study. Pointers `module/path:LINE`; (TEST) = test-derived. Relies on a paid external enrichment service (IAP credits).

## A. Capabilities and activation
- Turns anonymous website visits into CRM leads/opportunities: matches visitor location and page against user-defined rules, then asks an external Odoo IAP "reveal" service to identify the company behind the visitor IP and creates a lead from the answer (website_crm_iap_reveal/__manifest__.py:5-6; website_crm_iap_reveal/models/crm_reveal_rule.py:207-226).
- Optional: not auto_install (website_crm_iap_reveal/__manifest__.py:4-27). Installed from the CRM setting "Visits to Leads" (crm/models/res_config_settings.py:43; crm/views/res_config_settings_views.xml:102-103). Depends on iap_crm, iap_mail, crm_iap_mine, website_crm (website_crm_iap_reveal/__manifest__.py:9-14).
- Menu of rules sits under the CRM lead-generation menu; raw visit records menu is technical-mode only (website_crm_iap_reveal/views/crm_menus.xml:3-13). Credit-purchase widget is added to the settings block (website_crm_iap_reveal/views/res_config_settings_views.xml:8-10).

## B. Objects, relationships, lifecycle
- Lead Generation Rule: filters by countries, states, website, URL regex, company size, industries; contact filter by role or seniority; number of contacts 1-5; whether to track companies only or companies plus contacts; resulting lead type (default opportunity), sales team, salesperson, tags, priority, name suffix (website_crm_iap_reveal/models/crm_reveal_rule.py:28-62). Rule order set by sequence (website_crm_iap_reveal/models/crm_reveal_rule.py:36,26).
- Reveal View (visit record): visitor IP, matched rule, state "To Process" or "Not Found"; one record per rule and IP (unique) (website_crm_iap_reveal/models/crm_reveal_view.py:17-23).
- Lead extension: visitor IP, credits consumed, originating rule; these fields are carried over when leads are merged (website_crm_iap_reveal/models/crm_lead.py:10-15).
- Stage 1, page view: on a served page with status 200 for a public visitor whose visitor record has no lead yet and whose country is known, matching rules produce "To Process" records; rules already matched are remembered in an optional cookie; any failure is logged and never breaks the page (website_crm_iap_reveal/models/ir_http.py:16-45; website_crm_iap_reveal/models/crm_reveal_view.py:38-53; rule matching website_crm_iap_reveal/models/crm_reveal_rule.py:190-205).
- Contact form link: the visitor IP is attached to leads created by the website contact form so no second lead is generated for that IP; the field is whitelisted for the form builder (website_crm_iap_reveal/controllers/website_form.py:11-18; website_crm_iap_reveal/data/ir_model_data.xml:3-6).
- Stage 2, scheduled job (daily, run as the system user): purge old "Not Found" views (default 5 weeks) and views whose IP already produced a lead within 6 months, then send batches of up to 25 IPs to the service until credits run out (website_crm_iap_reveal/data/ir_cron_data.xml:5-13; website_crm_iap_reveal/models/crm_reveal_rule.py:19-20,207-261; website_crm_iap_reveal/models/crm_reveal_view.py:8,25-36).
- Stage 3, response: for each identified company a lead is created unless the external company id is already known on an existing lead or no rule matched; a note "Opportunity created by Odoo Lead Generation" with company/contact data is posted on it; unidentified IPs become "Not Found"; if the service reports no credit, a notice is raised once and processing stops, leaving views "To Process" (website_crm_iap_reveal/models/crm_reveal_rule.py:327-350,356-387) (TEST: website_crm_iap_reveal/tests/test_lead_reveal.py:76-190, covering credit error, service exception, no result, and normal creation of three leads).
- Lead content: type, team, tags, salesperson from the rule; priority; source label "Website Visitor"; credits used; suffix appended to name (website_crm_iap_reveal/models/crm_reveal_rule.py:390-407).

## C. Validations, security, multi-company
- Contact count limited to 1-5 (website_crm_iap_reveal/models/crm_reveal_rule.py:66-69); URL expression must be a valid pattern (website_crm_iap_reveal/models/crm_reveal_rule.py:80-86). Rule cache is cleared when countries, URL, or active state change (website_crm_iap_reveal/models/crm_reveal_rule.py:88-103).
- Access: sales managers full, salesmen read on rules and views (website_crm_iap_reveal/security/ir.model.access.csv:2-5). Record rules: users with all-leads visibility see everything; other salesmen see rules/views that are personal or global, based on the rule's salesperson (website_crm_iap_reveal/security/ir_rules.xml:3-27).
- Multi-company: rules and views carry no company field (website_crm_iap_reveal/models/crm_reveal_rule.py:28-62), so no company rule exists in this module. The company country used in the service request is the current company's (website_crm_iap_reveal/models/crm_reveal_rule.py:286,305). Which company owns created leads: UNKNOWN — EVIDENCE INSUFFICIENT
- Data-protection note: visitor IP addresses and location are stored in the database and sent to the external service; endpoint is a configurable system parameter defaulting to the vendor service (website_crm_iap_reveal/models/crm_reveal_rule.py:18,318-325,352-354).

## D. Handoffs
- Leads/opportunities and notes: crm / mail. Credits and account token: iap (website_crm_iap_reveal/models/crm_reveal_rule.py:320-323). Enrichment note layout: iap_mail (website_crm_iap_reveal/models/crm_reveal_rule.py:381-385). Accounting, inventory, purchase, analytic: none.

## E. Configuration that changes outcomes
- System parameters: service endpoint, view retention weeks, lead-dedup months (website_crm_iap_reveal/models/crm_reveal_rule.py:18,235,353; website_crm_iap_reveal/models/crm_reveal_view.py:28). Batch size 25 is a fixed constant (website_crm_iap_reveal/models/crm_reveal_rule.py:19). Rule fields listed in section B; IAP credit balance.

## F. Extension path
- Extends crm.lead, ir.http (website_crm_iap_reveal/models/crm_lead.py:8; website_crm_iap_reveal/models/ir_http.py:14) and the website form controller (website_crm_iap_reveal/controllers/website_form.py:9). No other module inherits crm.reveal.rule/view (grep). Referenced by test-only modules test_website_modules and test_crm_full.

## G. Not verified
- External service behaviour and pricing per credit: UNKNOWN — EVIDENCE INSUFFICIENT
- Cookie-consent interaction beyond the cookie type being optional (website_crm_iap_reveal/models/ir_http.py:41): UNKNOWN — EVIDENCE INSUFFICIENT
- Company assignment of generated leads: UNKNOWN — EVIDENCE INSUFFICIENT

