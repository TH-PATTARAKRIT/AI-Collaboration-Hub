# Source Map (candidate) — `crm_iap_mine`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `crm_iap_mine` |
| Display name | Lead Generation |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d6dbc66888710e6b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/crm_iap_mine/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `iap_crm`, `iap_mail`
- Direct dependents in 300-module list (1): `website_crm_iap_reveal`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_crm_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/CRM / Generate Leads/Opportunities based on country, industries, size, etc.
- Inventory of user-facing artifacts (counts): menu items 2, views 8, window actions 1, server actions 0, reports 0, mail templates 1, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (5): `crm.iap.lead.industry` (CRM IAP Lead Industry); `crm.iap.lead.role` (People Role); `crm.iap.lead.mining.request` (CRM Lead Mining Request); `crm.iap.lead.helpers` (Helper methods for crm_iap_mine modules); `crm.iap.lead.seniority` (People Seniority)
- Objects extended from other modules (1): `crm.lead`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `crm.lead`

## 6. Actions / states / validation / automation / security
- State fields found: `crm.iap.lead.mining.request` → ['draft', 'error', 'done']
- Validation: 0 declarative constraint method(s), 3 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 5

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 38 of 38 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — crm_iap_mine (Lead Generation / lead mining) (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities; core / optional / conditional
- Generates new leads/opportunities (companies, optionally their contacts) from an external paid IAP database using filters on country, state, industry, company size and contact role/seniority (crm_iap_mine/__manifest__.py:5-6; crm_iap_mine/models/crm_iap_lead_mining_request.py:194-229).
- Depends on iap_crm and iap_mail; auto_install True; also switchable from CRM settings "Generate new leads based on their country, industries, size, etc." (crm_iap_mine/__manifest__.py:9-12, :26; crm/models/res_config_settings.py:41).
- Entry points: a "Lead Generation" menu under CRM configuration listing mining requests (crm_iap_mine/views/crm_menus.xml:4-14); a "Generate Leads" button on lead/opportunity lists and kanban, sales managers only, opening a modal request form (crm_iap_mine/views/crm_lead_views.xml:10-12, :37-38; crm_iap_mine/models/crm_lead.py:15-23). A CRM setting "lead mining in pipeline" exists for the pipeline entry (crm/models/res_config_settings.py:48).
- Settings page adds a "buy more credits" widget (crm_iap_mine/views/res_config_settings_views.xml:8-10).

## B. Business objects, relationships, lifecycle
- Lead Mining Request (crm.iap.lead.mining.request): numbered request with status Draft / Error / Done, number of leads, target (companies or companies with contacts), lead type, team, salesperson, tags, filters, and the generated leads (crm_iap_mine/models/crm_iap_lead_mining_request.py:36-72).
- Reference data: industries (name unique, external ids), roles, seniorities; shipped as data files (crm_iap_mine/models/crm_iap_lead_industry.py:13-21; crm_iap_mine/data/*.csv).
- Lead gains a link to its mining request; merge keeps the link (crm_iap_mine/models/crm_lead.py:10-13).
- Lifecycle: Draft -> Submit -> (Done if results returned | Error if credits insufficient | stays with "no result" error type) ; Retry from Error; action_draft resets name and state (crm_iap_mine/models/crm_iap_lead_mining_request.py:307-340; crm_iap_mine/views/crm_iap_lead_mining_request_views.xml:9-11). Request number taken from sequence prefix LMR on first submit (crm_iap_mine/models/crm_iap_lead_mining_request.py:314-315; crm_iap_mine/data/ir_sequence_data.xml:5-10).
- Lead creation from response: company data mapped to lead (name, company name, email, phone, website, address, country, state), assigned type/team/salesperson/tags of the request, external company id stored as reveal id; a chatter note with company details posted on each lead (crm_iap_mine/models/crm_iap_lead_helpers.py:32-66; crm_iap_mine/models/crm_iap_lead_mining_request.py:270-296). Contact-person data is put in the chatter note rather than on the lead (people list passed empty) (crm_iap_mine/models/crm_iap_lead_mining_request.py:302-303) (TEST: crm_iap_mine/tests/test_lead_mine.py:60 with-people, :97 with-company).
- "No result" leaves state unchanged and reports that no credits were used (crm_iap_mine/views/crm_iap_lead_mining_request_views.xml:21; crm_iap_mine/models/crm_iap_lead_mining_request.py:258-260).

## C. Validations, automation, security, multi-company
- Limits (form-level, onchange): leads per request 1..200, contacts per company 1..5, company size min/max kept consistent (crm_iap_mine/models/crm_iap_lead_mining_request.py:13-17, :153-181).
- State filter only offered for whitelisted countries because of sparse data (crm_iap_mine/models/crm_iap_lead_mining_request.py:123-151).
- Credit rule: 1 credit per company and 1 per contact; UI shows estimated credits (crm_iap_mine/models/crm_iap_lead_mining_request.py:19-20, :79-95). Existing leads' reveal ids are sent so already-known companies can be excluded by the service (crm_iap_mine/models/crm_iap_lead_mining_request.py:240-248).
- Errors: request failure raises a user error; credit error sets state Error (crm_iap_mine/models/crm_iap_lead_mining_request.py:250-264). Timeout 300s; endpoint overridable via system parameter reveal.endpoint (crm_iap_mine/models/crm_iap_lead_mining_request.py:266-268).
- Access: sales managers full rights on requests and reference data; helper model has no rights (crm_iap_mine/security/ir.model.access.csv:2-6). No record rules and no company field on requests: multi-company scoping UNKNOWN — EVIDENCE INSUFFICIENT; the request uses current company's country code and default account for the reveal service (crm_iap_mine/models/crm_iap_lead_mining_request.py:238, :247).
- Default lead type follows "use leads" group; default country = user's company country; team follows salesperson (crm_iap_mine/models/crm_iap_lead_mining_request.py:27-34, :108-121).
- Sending "no more credit" mails once via a stored flag parameter is available in the helper (crm_iap_mine/models/crm_iap_lead_helpers.py:9-30); who calls it: UNKNOWN — EVIDENCE INSUFFICIENT (not called in this module's request flow).
- No cron.

## D. Handoffs (module ownership)
- Leads and teams: crm / sales_team. IAP account, credits, JSON-RPC: iap (iap_crm, iap_mail bridges). Website visitor-based reveal: website_crm_iap_reveal (depends on crm_iap_mine, manifest grep). No accounting, inventory or sales-order handoff; credits are bought externally via URL action (crm_iap_mine/models/crm_iap_lead_mining_request.py:354-358).

## E. Configuration/defaults that change outcomes
- Defaults: 3 leads, target companies, 10 contacts, size 1..1000 (filter off), country = company country (crm_iap_mine/models/crm_iap_lead_mining_request.py:33-34, :40-41, :59-68).
- Filters change what is sent to the service: countries/states, industries (external ids), size, roles/seniority (crm_iap_mine/models/crm_iap_lead_mining_request.py:199-229).
- CRM settings switches: module install toggle and pipeline entry (crm/models/res_config_settings.py:41, :48).

## F. Extension path (grep of _inherit)
- crm_iap_mine extends crm.lead (crm_iap_mine/models/crm_lead.py:8). Manifest dependants: website_crm_iap_reveal, test_crm_full.

## G. Not verified
- Data content returned by the service and its licensing/accuracy: UNKNOWN — EVIDENCE INSUFFICIENT.
- Mail template text for no-credit notice (crm_iap_mine/data/mail_template_data.xml): UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether mined leads are deduplicated against existing leads beyond reveal-id exclusion sent to the service: UNKNOWN — EVIDENCE INSUFFICIENT.

