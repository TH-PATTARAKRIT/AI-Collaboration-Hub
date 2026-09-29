# Source Map (candidate) — `website_crm_sms`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_crm_sms` |
| Display name | Send SMS to Visitor with leads |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `6fc503b03c7bf813` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_crm_sms/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `website_sms`, `crm`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Allows to send sms to website visitor that have lead
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `website.visitor`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `website.visitor`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 15 of 16 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_crm_sms (Send SMS to Visitor with leads)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_crm_sms.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: allows sending an SMS to a website visitor who has a lead but no contact (website_crm_sms/__manifest__.py:7-9).

## A. Capabilities / functions
- Conditional: depends on website_sms and crm with `auto_install` (website_crm_sms/__manifest__.py:10,12); activates automatically once both are present.
- Core: widens the "can we text this visitor?" check: besides a contact with a phone, a visitor qualifies if at least one of their leads has the same phone number as the visitor's displayed mobile number (website_crm_sms/models/website_visitor.py:10-16).
- Core: when the visitor has no contact but has leads, the SMS composer targets the best-ranked matching lead's phone instead of a contact (website_crm_sms/models/website_visitor.py:18-27). (TEST) without contact: composer opens on the lead using the phone field; with contact: on the contact (website_crm_sms/tests/test_website_visitor.py:21-46).

## B. Business objects, relationships, lifecycle
- Visitor (website) -> leads (link added by website_crm) -> lead phone. The visitor's displayed mobile falls back to the latest lead phone when no contact phone exists (website_crm/models/website_visitor.py:18-31).
- Lead choice: matching leads sorted by a confidence ranking owned by crm, best first (website_crm_sms/models/website_visitor.py:13, 20; crm/models/crm_lead.py:1943).
- No new stored object; message goes through the standard SMS composer on the lead (website_crm_sms/models/website_visitor.py:24-26).

## C. Validations, automation, security, multi-company
- If no lead's phone equals the visitor mobile and there is no contact phone, the base error is raised ("no contact and/or no phone") (website_sms/models/website_visitor.py:27-28).
- Note the composer field key for the lead case is given under a different context key than the contact case (website_crm_sms/models/website_visitor.py:26 vs website_sms/models/website_visitor.py:22); (TEST) asserts the lead key as given (website_crm_sms/tests/test_website_visitor.py:32). Whether the composer honours that key: UNKNOWN — EVIDENCE INSUFFICIENT.
- Lead access: lead links on visitors are for the salesman group (website_crm/models/website_visitor.py:10). The action itself has no group check here. No access-control rows, record rules or company scoping in this module.

## D. Handoffs to other modules
- website_sms (owner of the SMS action), website_crm (owner of visitor-lead link), crm (lead ranking), sms (composer).

## E. Configuration / defaults that change outcomes
- None of its own; SMS provider and credits are configured in sms. Tests use minimal data (TEST) (website_crm_sms/tests/test_website_visitor.py:4-19).

## F. Effective extension path (module names only)
- website.visitor extended by: website_crm, website_crm_sms, website_event, website_event_track, website_livechat, website_sale, website_sms.

## G. Not verified
- Behaviour when multiple leads share the same phone but different contacts: UNKNOWN — EVIDENCE INSUFFICIENT.

