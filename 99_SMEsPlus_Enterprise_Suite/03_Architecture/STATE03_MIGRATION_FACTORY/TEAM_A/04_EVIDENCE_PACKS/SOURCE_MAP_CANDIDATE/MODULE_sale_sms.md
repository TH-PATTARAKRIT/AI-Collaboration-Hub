# Source Map (candidate) — `sale_sms`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_sms` |
| Display name | Sale - SMS |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `0e3349030c21b3d8` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_sms/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale`, `sms`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Ease SMS integration with sales capabilities
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
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 10 of 10 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: sale_sms (revision 19.0.post20260921)
Scope: Odoo Community read-only study. Pointers `module/path:LINE`. Module has no Python models, views, or tests.

## A. Capabilities and activation
- Glue module: "ease SMS integration with sales capabilities" (sale_sms/__manifest__.py:6-7). Depends on sale and sms (sale_sms/__manifest__.py:10); auto_install, so it activates automatically once both are present (sale_sms/__manifest__.py:15).
- Its only content is access control for SMS templates (sale_sms/__manifest__.py:11-14). Actual SMS sending/templating is owned by the sms module.

## B. Business objects
- Only object touched: SMS template (owned by sms). No new fields, states, or transitions (module directory holds only manifest and security files).
- Sales managers gain full create/read/write/delete on the SMS template table (sale_sms/security/ir.model.access.csv:2).
- An accompanying rule limits what sales managers may create/change/delete to templates whose target document is a sales order or a contact/partner; the rule explicitly excludes the read permission (sale_sms/security/security.xml:3-9).

## C. Validations, security, multi-company
- Baseline in sms: all internal users read templates only; system group has full rights (sms/security/ir.model.access.csv:5-6); system group additionally holds an unrestricted rule (sms/security/sms_security.xml:3-8).
- Effect (from the two files): a sales manager who is not a system user can maintain sales-order and partner SMS templates but not templates for other documents. How this combines with other group rules at runtime: UNKNOWN — EVIDENCE INSUFFICIENT
- No company scoping is defined in this module (no company field or company-based domain in sale_sms/security/security.xml:7).

## D. Handoffs
- None to accounting, inventory, purchase or analytic. SMS delivery and credits are owned by sms and its gateway.

## E. Configuration
- None in this module (no settings, defaults or data records; sale_sms/__manifest__.py:11-14).

## F. Extension path
- No module lists sale_sms as a dependency (grep of __manifest__.py returned no match). Extends the sms template access model only via security data.

## G. Not verified
- Which sale/partner SMS templates or send actions exist and where they are triggered (belongs to sale/sms/other modules): UNKNOWN — EVIDENCE INSUFFICIENT
- Runtime combined effect of sms rules and this rule for manager users: UNKNOWN — EVIDENCE INSUFFICIENT

