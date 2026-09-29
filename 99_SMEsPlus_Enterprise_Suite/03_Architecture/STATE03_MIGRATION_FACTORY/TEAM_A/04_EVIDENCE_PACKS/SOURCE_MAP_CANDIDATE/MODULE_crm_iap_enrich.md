# Source Map (candidate) — `crm_iap_enrich`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `crm_iap_enrich` |
| Display name | Lead Enrichment |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a0590812c60ec6b9` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/crm_iap_enrich/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `iap_crm`, `iap_mail`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_crm_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/CRM / Enrich Leads/Opportunities using email address domain
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 1, reports 0, mail templates 0, scheduled jobs 1, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `res.config.settings`, `crm.lead`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.config.settings`, `crm.lead`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: CRM: enrich leads (IAP) every 24 hours
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 31 of 31 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — crm_iap_enrich (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities; core / optional / conditional
- Enriches leads/opportunities with company data (name, address, phone, country/state, company id) looked up from the lead's email domain via the IAP (paid external service) (crm_iap_enrich/__manifest__.py:6; crm_iap_enrich/models/crm_lead.py:157-202).
- Depends on iap_crm and iap_mail; auto_install True; also installable from the CRM settings switch "Enrich your leads automatically…" (crm_iap_enrich/__manifest__.py:9-12, :21; crm/models/res_config_settings.py:42).
- Two modes via CRM setting "Enrich lead automatically": auto (default, scheduled job on) or manual/on-demand only (crm/models/res_config_settings.py:44-47; crm_iap_enrich/models/res_config_settings.py:10-21). A post-install step aligns the scheduled job with the stored setting (crm_iap_enrich/__init__.py:7-11).
- Manual entry points: "Enrich" button on lead/opportunity form and a bound "Enrich" server action for record selections (crm_iap_enrich/views/crm_lead_views.xml:8-16; crm_iap_enrich/data/ir_action.xml:4-12). Settings page adds a "buy more credits" widget for the reveal service (crm_iap_enrich/views/res_config_settings_view.xml:9-11).

## B. Business objects, relationships, lifecycle
- Adds two fields on crm.lead: "enrichment done" flag and a computed "allow manual enrich" (crm_iap_enrich/models/crm_lead.py:16-17). No new model.
- Button visible only if lead is active, has an email that is not marked incorrect, has not been enriched, has no reveal (mining/reveal) id, and probability is not 100 (won) (crm_iap_enrich/models/crm_lead.py:19-25).
- Processing rules per lead: skip if won or already done or no email; if email cannot be normalised or domain is a generic mail provider, mark done and post a note "not found/no email"; otherwise send domain to IAP (crm_iap_enrich/models/crm_lead.py:55-83).
- Response handling: no data -> mark done + note; data -> fill only EMPTY fields (company name, reveal id, street, city, zip, phone from first number, country, state), mark done, post a company-info note (crm_iap_enrich/models/crm_lead.py:157-202).
- Merge: the "done" flag is true if any merged lead had it (crm_iap_enrich/models/crm_lead.py:204-208) (TEST: crm_iap_enrich/tests/test_crm_lead_merge.py:15).

## C. Validations, automation, security, multi-company
- Scheduled job "CRM: enrich leads (IAP)" every 24 hours, runs as root user; selects leads not yet enriched, probability under 100 or unset, with email, without reveal id, created within the last 24 hours (default delay), active; batch size 50 (crm_iap_enrich/data/ir_cron.xml:3-11; crm_iap_enrich/models/crm_lead.py:27-39). In auto mode each lead creation also triggers the job (crm_iap_enrich/models/crm_lead.py:41-49).
- Batching locks leads for update; if locked, retried after 5 minutes (crm_iap_enrich/models/crm_lead.py:111-121).
- Credit handling: insufficient credit stops the run and (manual runs only) notifies user; other errors are logged, notification on manual runs; batches commit progress (crm_iap_enrich/models/crm_lead.py:87-107, :124-155). On failure leads remain un-enriched (TEST: crm_iap_enrich/tests/test_lead_enrich.py:41-47).
- Existing values never overwritten (TEST: crm_iap_enrich/tests/test_lead_enrich.py:24-39).
- Setting toggle activates/deactivates the job (TEST: crm_iap_enrich/tests/test_lead_enrich.py:49-60).
- No access CSV or record rules in this module; standard crm.lead access applies. Multi-company: no company logic; enrichment charges the IAP account resolved by the iap module: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs (module ownership)
- Leads/opportunities: crm. IAP request, credits and notifications: iap / iap_mail / iap_crm (enrichment call `iap.enrich.api` and notification helpers referenced at crm_iap_enrich/models/crm_lead.py:88-105). Generic-mail-provider list: iap tools (crm_iap_enrich/models/crm_lead.py:76). Chatter notes: mail. No accounting, inventory or sales-order handoff; IAP credits are purchased on the IAP side.

## E. Configuration/defaults that change outcomes
- System parameter crm.iap.lead.enrich.setting: default 'auto' (crm/models/res_config_settings.py:44-47).
- Cron delay window 24h and batch 50 (crm_iap_enrich/models/crm_lead.py:28); job interval 24 hours (crm_iap_enrich/data/ir_cron.xml:9-10).
- IAP credits must exist for the "reveal" service (crm_iap_enrich/models/crm_lead.py:93).

## F. Extension path (grep of _inherit)
- crm_iap_enrich extends crm.lead and res.config.settings (crm_iap_enrich/models/). Referenced as a dependency by test_crm_full (test module); no functional module depends on it.

## G. Not verified
- Contents of the mail templates for notes (crm_iap_enrich/data/mail_templates.xml): UNKNOWN — EVIDENCE INSUFFICIENT.
- Data returned by the external service and its accuracy/pricing: UNKNOWN — EVIDENCE INSUFFICIENT.
- Data-protection implication of sending email domains to a third party: UNKNOWN — EVIDENCE INSUFFICIENT.

