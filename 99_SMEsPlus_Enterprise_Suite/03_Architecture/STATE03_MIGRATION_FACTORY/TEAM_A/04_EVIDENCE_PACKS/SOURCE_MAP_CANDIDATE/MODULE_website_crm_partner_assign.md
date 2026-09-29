# Source Map (candidate) — `website_crm_partner_assign`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_crm_partner_assign` |
| Display name | Resellers |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `29b4b9a0ffea8bc0` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_crm_partner_assign/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base_geolocalize`, `crm`, `account`, `partnership`, `website_partner`, `website_google_map`, `portal`
- Direct dependents in 300-module list (1): `website_customer`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_crm_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Publish your resellers/partners and forward leads to them
- Inventory of user-facing artifacts (counts): menu items 2, views 22, window actions 4, server actions 0, reports 0, mail templates 1, scheduled jobs 0, wizards 2, web routes 5
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (4): `crm.lead.forward.to.partner` (Lead forward to partner); `crm.lead.assignation` (Lead Assignation); `res.partner.activation` (Partner Activation); `crm.partner.report.assign` (CRM Partnership Analysis)
- Objects extended from other modules (5): `website`, `crm.lead`, `res.partner`, `res.partner.grade`, `website.published.mixin`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `website`, `crm.lead`, `res.partner`, `res.partner.grade`, `website.published.mixin`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 4 (of which company-scoped by text 0); access rows 11

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 55 of 56 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_crm_partner_assign (Resellers)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_crm_partner_assign.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: publish resellers/partners on the website and forward incoming leads/opportunities to them, with automatic assignment by partner level weight and location (website_crm_partner_assign/__manifest__.py:7, 9-21).

## A. Capabilities / functions
- Optional add-on (no `auto_install`): depends on base_geolocalize, crm, account, partnership, website_partner, website_google_map and portal (website_crm_partner_assign/__manifest__.py:24-25). Partner levels (grades) themselves are owned by partnership (partnership/models/res_partner_grade.py:7-17).
- Core: public reseller directory `/partners` with filters by level (grade) and country, by industry of implemented customers, free-text search, pager (40 per page), map view, partner detail page; country is pre-selected from the visitor's location, falling back to all countries when none is found there (website_crm_partner_assign/controllers/main.py:233-381, 384-409).
- Core: partner level published flag (default published) makes a level visible to public and portal (website_crm_partner_assign/models/res_partner_grade.py:8-20; website_crm_partner_assign/security/ir_rule.xml:18-22).
- Core: activation status list (Fully Operational, Ramp-up, First Contact), level weight, partnership dates, latest and next review, "implemented by" reference between customers and resellers (website_crm_partner_assign/data/res_partner_activation_data.xml:3-14; website_crm_partner_assign/models/res_partner.py:21-38).
- Core: lead geolocation and assigned partner fields with date of assignment, and a list of partners who declined (website_crm_partner_assign/models/crm_lead.py:14-34).
- Core: automatic assignment ("Automatic Assignment" button) by location and weight; manual or mass forwarding by email through a wizard, including bulk action on selected leads (website_crm_partner_assign/models/crm_lead.py:79-112, 145-216; website_crm_partner_assign/views/crm_lead_views.xml:20-32; website_crm_partner_assign/wizard/crm_forward_to_partner.py:56-105; website_crm_partner_assign/wizard/crm_forward_to_partner_view.xml:48-55).
- Core portal for resellers: "My leads" and "My opportunities" lists with sort/filter, lead and opportunity pages, accept/decline lead, edit opportunity values, contact details, stage, activity, and create own opportunity (website_crm_partner_assign/controllers/main.py:23-185; website_crm_partner_assign/models/crm_lead.py:218-325).
- Core: analysis report of partner, level, activation, opportunities count and invoiced turnover (website_crm_partner_assign/report/crm_partner_report.py:8-58).
- Core: opportunity counter on a contact aggregates opportunities of the contact and its assigned ones through the hierarchy for sales users (website_crm_partner_assign/models/res_partner.py:57-82).
- Data: tags "No more partner available", "Spam", "Created by Partner" and the forward email template (website_crm_partner_assign/data/crm_tag_data.xml:5-13; website_crm_partner_assign/data/mail_template_data.xml:5-6).

## B. Business objects, relationships, lifecycle
- Lead/opportunity (crm.lead, owned by crm) -> assigned reseller (contact) <- partner level (grade) with weight; reseller -> customers it implemented (website_crm_partner_assign/models/crm_lead.py:16; website_crm_partner_assign/models/res_partner.py:31-37; website_crm_partner_assign/models/res_partner_grade.py:11-12).
- Assignment lifecycle: lead created -> assigned automatically (nearest eligible partner) or manually -> forwarded by email with portal link -> reseller accepts (becomes opportunity, comment logged) or declines (unassigned, reseller and its contacts unfollow and are recorded as declined, optional spam tag) -> reseller works the opportunity on the portal (website_crm_partner_assign/models/crm_lead.py:94-112, 218-249, 251-297). (TEST) accept turns lead into opportunity; decline clears assignment and records the decliner; spam decline adds the spam tag (website_crm_partner_assign/tests/test_partner_assign.py:131-157).
- Automatic-assignment rules: a partner is eligible if its level weight is above zero, it is in the lead's country, it has not declined the lead; search widens in steps (about 2 x 1.5 degrees, 4 x 3, 8 x 8, whole country, nearest anywhere), then picks randomly among candidates with probability proportional to weight (website_crm_partner_assign/models/crm_lead.py:145-216). If nobody is found the lead gets the "no more partner available" tag (website_crm_partner_assign/models/crm_lead.py:102-106). Leads without country are skipped with a warning to the user (website_crm_partner_assign/models/crm_lead.py:79-92). (TEST) automatic assignment chose the partner in the lead's country over one in another country, stored the lead's coordinates and set the assignment date (website_crm_partner_assign/tests/test_partner_assign.py:50-99).
- Assigning a partner also sets the salesperson to that partner's salesperson when it has one, and the date of assignment is refreshed; clearing the partner clears the date (website_crm_partner_assign/models/crm_lead.py:28-34, 108-111, 68-77, 101-102).
- Merging leads keeps location, assigned partner and assignment date (website_crm_partner_assign/models/crm_lead.py:63-66; website_crm_partner_assign/data/crm_lead_merge_template.xml).

## C. Validations, automation, security, multi-company
- Portal write control: a portal user may act on a lead only if the assigned partner is under the user's commercial partner; otherwise "only users with commercial partner which is a parent of the assigned partner can edit this lead" (website_crm_partner_assign/models/crm_lead.py:36-41). (TEST) another portal user cannot accept a lead not theirs (website_crm_partner_assign/tests/test_partner_assign.py:158-170).
- Record rules: portal users can read only leads assigned to their commercial partner group (read-only rule, edits go through controlled methods with elevated rights after the check); public and portal read published partner levels only; sales report visibility follows sales groups (all leads group sees all; salesmen see personal or unassigned) (website_crm_partner_assign/security/ir_rule.xml:6-36).
- Access rows: portal can read leads and stages; public/portal read levels; internal users read activation; partner managers edit activation; account users read levels; salesmen use forward wizards and read the report (website_crm_partner_assign/security/ir.model.access.csv:2-12).
- Portal edit limits: contact update only for a fixed field list (name, phone, email, address); stage update by portal id; opportunity values editable (revenue, probability, priority, deadline, own activity); an error is raised for other fields (website_crm_partner_assign/models/crm_lead.py:251-296).
- Portal users who write on a record must be able to read every related record they set (website_crm_partner_assign/models/crm_lead.py:55-61).
- Creating an opportunity from the portal requires the user to have a partner level; all of contact, title and description are mandatory; it is created priority "2", assigned to the reseller's company, tagged "Created by Partner", salesperson taken from the reseller, and converted to opportunity (website_crm_partner_assign/models/crm_lead.py:299-325). (TEST) team follows the reseller's salesperson (website_crm_partner_assign/tests/test_partner_assign.py:171-183).
- Forward wizard: partners must have an email; portal status of the partner decides a wording flag in the email; forwarded leads set assigned partner and salesperson and subscribe the partner (website_crm_partner_assign/wizard/crm_forward_to_partner.py:56-105).
- Reseller directory: public route with elevated reads; only company-type contacts with a level, published, on an active and (for non-editors) published level (website_crm_partner_assign/controllers/main.py:244-246, 373-381). Restricted website editors may also see unpublished levels; publishing rights depend on groups (TEST) (website_crm_partner_assign/tests/test_partner_assign.py:436-480). Contact details of published resellers are public by design (see website_partner note).
- Access to portal pages requires login and 404 for wrong type (website_crm_partner_assign/controllers/main.py:52, 164-173). The mail-thread posting on assigned leads is downgraded to read-level so portal users can comment (website_crm_partner_assign/models/crm_lead.py:356-366); (TEST) (website_crm_partner_assign/tests/test_partner_assign.py:255-330).
- Company scoping: assigned partner domain restricted to the lead's company or shared contacts (website_crm_partner_assign/models/crm_lead.py:16). Multi-website: not by evidence.

## D. Handoffs to other modules
- crm (owner of leads, stages, teams, convert-to-opportunity, salesperson assignment); partnership (grades, pricelist per grade, partner menu); base_geolocalize (coordinates); website_google_map (map and directory map); website_partner (partner page, publication); account (invoice report used for turnover); portal (portal home counters and layout); mail (forward email, followers); website (layout, GeoIP, sitemap).
- Related module: website_customer (customer references) uses the same "implemented by" relation and map (website_google_map/controllers/main.py; website_customer/controllers/main.py:15-32).

## E. Configuration / defaults that change outcomes
- Partner level weight (0 means never assigned) and per-partner "Level Weight" (computed from the level, editable) (website_crm_partner_assign/models/res_partner_grade.py:11-12; website_crm_partner_assign/models/res_partner.py:21-24, 52-55).
- Level published flag decides public visibility; activation status is informational in this module (website_crm_partner_assign/models/res_partner_grade.py:19-20).
- Geographic search windows and random weighted pick are fixed in code (website_crm_partner_assign/models/crm_lead.py:157-214).
- Forward email body comes from a template and can be edited in the wizard (website_crm_partner_assign/wizard/crm_forward_to_partner.py:37-40).
- Default level/activation applied when a reseller is created on the fly from a lead (website_crm_partner_assign/models/res_partner.py:9-19).

## F. Effective extension path (module names only)
- crm.lead: crm_iap_enrich, crm_iap_mine, crm_livechat, crm_mail_plugin, event_crm, iap_crm, mass_mailing_crm, sale_crm, survey_crm, website_crm, website_crm_iap_reveal, website_crm_livechat, website_crm_partner_assign. res.partner.grade: partnership and website_crm_partner_assign. res.partner: in this family website, website_partner, website_customer, partnership, website_crm_partner_assign. Controllers: WebsitePartnerPage and GoogleMap subclassed (website_crm_partner_assign/controllers/main.py:188).

## G. Not verified
- Email template content and layout: UNKNOWN — EVIDENCE INSUFFICIENT.
- Commission or contract terms for resellers: UNKNOWN — EVIDENCE INSUFFICIENT (not present in this module).
- Behaviour of the sixth-step "nearest anywhere" search under very large data: UNKNOWN — EVIDENCE INSUFFICIENT.

