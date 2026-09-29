# Source Map (candidate) — `website_sms`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_sms` |
| Display name | Send SMS to Visitor |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `9b3fb924379a7569` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_sms/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `website`, `sms`
- Direct dependents in 300-module list (1): `website_crm_sms`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Allows to send sms to website visitor
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 14 of 15 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_sms (Send SMS to Visitor)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_sms.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: send an SMS to a website visitor when the visitor is linked to a contact (website_sms/__manifest__.py:7-9).

## A. Capabilities / functions
- Conditional: depends on website and sms with `auto_install` (website_sms/__manifest__.py:10,15), so it activates automatically when both exist.
- Core: "Send SMS" button on the visitor form, "SMS" button on the visitor kanban card and an SMS icon on the visitor list, each visible only when the visitor has a mobile number (website_sms/views/website_visitor_views.xml:9-10, 24-26, 40-41).
- Core: the mobile column is added to the kanban view (website_sms/views/website_visitor_views.xml:20-22).
- Core: action opens the SMS composer pre-filled for the visitor's contact in comment mode using the contact's phone (website_sms/models/website_visitor.py:17-23, 25-40).

## B. Business objects, relationships, lifecycle
- Visitor (owned by website) -> linked contact (partner). The visitor's "mobile" is computed from the contact's phone (website/models/website_visitor.py:54, 63, 104-119).
- No new model. The message is a normal SMS sent through the sms composer on the contact record (website_sms/models/website_visitor.py:18-21).

## C. Validations, automation, security, multi-company
- Sending is refused with a user-facing error unless the visitor has a contact with a phone number (website_sms/models/website_visitor.py:11-15, 27-28).
- The check is a hook that other modules extend, notably to refresh visitor data from linked leads (website_sms/models/website_visitor.py:12-15; website_crm_sms/models/website_visitor.py:10-28).
- Access: visitor records are visible to website designers and system administrators (read/write/delete, no create) (website/security/ir.model.access.csv:30-31). SMS sending itself is governed by sms; credits/IAP: UNKNOWN — EVIDENCE INSUFFICIENT.
- No access-control rows or record rules of its own; no company scoping in this module.

## D. Handoffs to other modules
- website (owner of visitor), sms (composer, sending, IAP account), website_crm_sms (lead-aware refinement) (website_crm_sms/models/website_visitor.py:10-28).

## E. Configuration / defaults that change outcomes
- Composer defaults: comment mode, number field "phone" of the contact (website_sms/models/website_visitor.py:18-22).
- The "mobile" field shows the contact's `phone`, not a separate mobile field (website/models/website_visitor.py:119). Impact for contacts that only have a mobile number: UNKNOWN — EVIDENCE INSUFFICIENT.

## F. Effective extension path (module names only)
- website.visitor extended by: website_crm, website_crm_sms, website_event, website_event_track, website_livechat, website_sale, website_sms.
- Hook methods for SMS extended by: website_crm_sms.

## G. Not verified
- Tests: none in this module. SMS delivery, opt-out and blacklist behaviour: UNKNOWN — EVIDENCE INSUFFICIENT.

