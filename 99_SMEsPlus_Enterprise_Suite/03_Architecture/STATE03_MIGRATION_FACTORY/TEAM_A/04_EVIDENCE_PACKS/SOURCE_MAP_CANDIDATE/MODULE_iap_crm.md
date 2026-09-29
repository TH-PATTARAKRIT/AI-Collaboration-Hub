# Source Map (candidate) — `iap_crm`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `iap_crm` |
| Display name | IAP / CRM |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c2dc6dbadfe5b55d` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/iap_crm/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `crm`, `iap_mail`
- Direct dependents in 300-module list (3): `crm_iap_enrich`, `crm_iap_mine`, `website_crm_iap_reveal`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / Bridge between IAP and CRM
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `crm.lead`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `crm.lead`

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

# Source Map trace note: iap_crm (IAP / CRM)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/iap_crm.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. No tests exist in this module.

## A. Capabilities / functions
- Technical bridge between the IAP (in-app purchase / paid external service) layer and CRM; described only as "Bridge between IAP and CRM" (iap_crm/__manifest__.py:7-8). Category is hidden tooling, not a user-facing app (iap_crm/__manifest__.py:9).
- Depends on crm and iap_mail (iap_crm/__manifest__.py:11-14); `auto_install` true, so it activates automatically once both are present (iap_crm/__manifest__.py:16).
- Adds one technical field to leads: a "Reveal ID" text reference to the external lookup request that produced the lead (iap_crm/models/crm_lead.py:10).
- Makes that reference survive a lead merge (iap_crm/models/crm_lead.py:12-13).
- No views, menus, data, security or settings are shipped (manifest has no data list: iap_crm/__manifest__.py:5-19).

## B. Business objects, relationships, lifecycle
- Object touched: lead/opportunity (owned by crm). The new field is an indexed free-text identifier, indexed only where set (iap_crm/models/crm_lead.py:10).
- Lifecycle: the identifier is written at lead creation by other modules; during merge of duplicate leads the field is included in the merge field set (iap_crm/models/crm_lead.py:12-13). How the merged value is chosen: UNKNOWN — EVIDENCE INSUFFICIENT (rule sits in crm's merge logic, not read here).

## C. Validations, automation, security, multi-company
- No constraints, automation, groups, access entries or record rules in this module (skeleton: "access": [], "rules": []; iap_crm/models/crm_lead.py:1-13).
- Company scoping: none added; follows crm: UNKNOWN — EVIDENCE INSUFFICIENT for detail.

## D. Handoffs to other modules
- crm: owns lead model and merge mechanism (iap_crm/models/crm_lead.py:8, 12).
- iap_mail / iap: own credit accounting and service notifications (dependency iap_crm/__manifest__.py:13).
- Other modules that also use the same identifier (outside this module, for reference): crm_iap_enrich (crm_iap_enrich/models/crm_lead.py) and crm_iap_mine (crm_iap_mine/models/crm_iap_lead_mining_request.py) reference it; which of them defines vs consumes it beyond this bridge: UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration / defaults that change outcomes
- None. No settings, defaults or data.

## F. Effective extension path
- Modules involved: crm (lead, merge), iap_mail (dependency), then downstream consumers crm_iap_enrich and crm_iap_mine (names only).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: what triggers population of the Reveal ID and its business meaning beyond "technical ID of the request" (comment at iap_crm/models/crm_lead.py:10).
- UNKNOWN — EVIDENCE INSUFFICIENT: any user-visible effect of the field.

