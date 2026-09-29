# Source Map (candidate) — `website_crm`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_crm` |
| Display name | Contact Form |
| Manifest version | 2.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `f6475850bdc2d1a6` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_crm/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `website`, `crm`
- Direct dependents in 300-module list (2): `website_crm_iap_reveal`, `website_crm_livechat`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_crm_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Generate leads from a contact form
- Inventory of user-facing artifacts (counts): menu items 0, views 5, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `website`, `crm.lead`, `website.visitor`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `website`, `crm.lead`, `website.visitor`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 49 of 50 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_crm (Contact Form - lead capture)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_crm.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: website forms can create leads or opportunities in CRM once a form is set to that action in the website builder; includes phone number validation (website_crm/__manifest__.py:8-14).

## A. Capabilities / functions
- Conditional: depends on website and crm and is `auto_install` (website_crm/__manifest__.py:15,26): activates automatically when both are installed. It does nothing for a form until that form is configured in the builder (website_crm/__manifest__.py:12); (TEST) the tour first switches the contact-us form action to create an opportunity (website_crm/tests/test_website_crm.py:14-15).
- Core: makes the lead model an allowed website-form target, labelled "Create an Opportunity", with the description as default text field (website_crm/data/ir_model_data.xml:4-9).
- Core: whitelist of lead fields a public form may set: contact name, description, email, subject, company name, phone, sales team, salesperson, custom properties (website_crm/data/ir_model_data.xml:11-24).
- Core: the contact-us page pre-fills contact name, company name and description from request parameters (website_crm/views/website_templates_contactus.xml:4-11).
- Core: phone numbers submitted are reformatted to international format using the submitter's country (form country, else known visitor contact / company, else GeoIP country) (website_crm/controllers/website_form.py:11-21, 24-47).
- Core: state/province is auto-filled from GeoIP when not provided on a lead form (website_crm/controllers/website_form.py:49-55).
- Core: leads are linked to the website visitor; lead form shows a "Page views" stat button; visitor screens show a leads count, "Leads" filter and lead list (website_crm/models/crm_lead.py:10-39; website_crm/models/website_visitor.py:10-16; website_crm/views/crm_lead_views.xml:8-13; website_crm/views/website_visitor_views.xml:3-41).
- Core: an action item "Website Contact Form" opening `/contactus` is registered as a to-do launch action (website_crm/data/ir_actions_data.xml:4-13).
- Merge support: merged leads keep all visitors and the merge summary mail lists them (website_crm/models/crm_lead.py:41-45; website_crm/data/crm_lead_merge_template.xml:4-14).

## B. Business objects, relationships, lifecycle
- Form submission -> lead/opportunity (crm.lead, owned by crm) -> linked to visitor (many-to-many) -> visitor may be linked to a contact (partner). Leads belong to the website's company unless provided (website_crm/controllers/website_form.py:58-91).
- Contact linking rule: if the visitor already has a contact whose normalised email equals the submitted email, the lead is linked to that contact, but only when phone is absent on either side or both numbers match after formatting (website_crm/controllers/website_form.py:61-76); when a contact is linked, submitted email and phone are dropped from the lead so the contact's data prevails (website_crm/models/crm_lead.py:47-50). (TEST) unedited prefilled data of a logged-in user propagates the contact; edited data does not, and the contact's own email/phone stay unchanged (website_crm/tests/test_website_crm.py:32-57).
- Visitor naming: when the visitor has no leads and no contact yet, the visitor takes the lead's contact name (website_crm/controllers/website_form.py:84-90).
- Lead type: uses the team's "leads" flag when a team is set; else the current user's "use leads" setting decides lead versus opportunity (website_crm/models/crm_lead.py:59-62).
- Marketing attribution: medium defaults to the default, else a "website" medium is fetched/created; UTM source/medium/campaign from the landing URL are stored, unknown campaign names create a new campaign (website_crm/models/crm_lead.py:52-54); (TEST) (website_crm/tests/test_website_crm.py:11-30).
- Visitor contact info: when a visitor lacks email or phone, the latest linked lead's email/phone is used (website_crm/models/website_visitor.py:18-31); (TEST) (website_crm/tests/test_website_visitor.py:25).
- Language of the lead is the visitor's language unless given (website_crm/controllers/website_form.py:79-80).

## C. Validations, automation, security, multi-company
- Standard form-controller checks apply (model must be enabled for website forms; whitelisted fields only; required fields; captcha on the route) (website/controllers/form.py:31, 62-64, 250-257). Creation runs with elevated rights (website/controllers/form.py:263-275).
- Integrity errors during creation return a generic failure (website/controllers/form.py:87-90). Phone formatting never raises errors; unformattable numbers are passed through as typed (website_crm/controllers/website_form.py:41-47 with `raise_exception=False`).
- Assignment automation: team and salesperson default to the current website's default team/user unless the form gives them (website_crm/models/crm_lead.py:55-58). Website fields exist for default team (restricted to teams that use leads or opportunities according to the lead setting) and default salesperson (internal users only) (website_crm/models/website.py:10-21). No view in this tree edits these two fields: where they are set: UNKNOWN — EVIDENCE INSUFFICIENT.
- Company scoping: lead company = the website's company (website_crm/controllers/website_form.py:77-78); visitors are per website (website/models/website_visitor.py).
- Access: sales users (salesman group) can read visitors and tracked page hits, no write/create/delete (website_crm/security/ir.model.access.csv:2-3). Lead links on visitors are visible only to the salesman group (website_crm/models/website_visitor.py:10-11; website_crm/views/website_visitor_views.xml:10, 49).
- Retention: visitors attached to leads are never purged as inactive, and leads follow when duplicate visitors are merged (website_crm/models/website_visitor.py:45-56); (TEST) (website_crm/tests/test_website_visitor.py:74-105).
- Visitor "message" flow: if a visitor has leads but no contact, a contact is created from the best lead so an email can be composed (website_crm/models/website_visitor.py:33-43, 58-69).
- Page-view count uses a direct database aggregation (website_crm/models/crm_lead.py:13-30); visibility not filtered by user access there: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs to other modules
- crm (owner): lead, team, stages, merge, properties, partner assignment; website (owner): form controller, visitor, tracking; utm (source/medium/campaign) (website_crm/models/crm_lead.py:52-54).
- phone_validation: number formatting (website_crm/controllers/website_form.py:4).
- website_sms / website_crm_sms / website_crm_livechat: consume visitor-lead links for SMS and chat (see their notes).
- Partner assignment of leads to resellers is owned by website_crm_partner_assign.

## E. Configuration / defaults that change outcomes
- Per-form: form action set in builder ("Create an Opportunity") (website_crm/data/ir_model_data.xml:8). Per-website: default sales team and salesperson (website_crm/models/website.py:15-21). User setting "use leads" (group) decides lead vs opportunity when no team (website_crm/models/crm_lead.py:62).
- GeoIP presence changes country/state defaults (website_crm/controllers/website_form.py:18-20, 49-55).

## F. Effective extension path (module names only)
- Website form controller extended by: website_crm, website_crm_iap_reveal, website_hr_recruitment, website_mass_mailing, website_project, website_sale.
- crm.lead extended by: crm_iap_enrich, crm_iap_mine, crm_livechat, crm_mail_plugin, event_crm, iap_crm, mass_mailing_crm, sale_crm, survey_crm, website_crm, website_crm_iap_reveal, website_crm_livechat, website_crm_partner_assign.
- website.visitor extended by: website_crm, website_crm_sms, website_event, website_event_track, website_livechat, website_sale, website_sms. website extended (model) by this family: website_crm, website_crm_partner_assign (plus others).

## G. Not verified
- Effect on record rules of lead ownership for public submissions; duplicate-lead detection: UNKNOWN — EVIDENCE INSUFFICIENT.
- `test_form_properties` outcome (custom properties on the form): UNKNOWN — EVIDENCE INSUFFICIENT (UI tour without extracted assertions) (website_crm/tests/test_website_crm.py:59-66).

