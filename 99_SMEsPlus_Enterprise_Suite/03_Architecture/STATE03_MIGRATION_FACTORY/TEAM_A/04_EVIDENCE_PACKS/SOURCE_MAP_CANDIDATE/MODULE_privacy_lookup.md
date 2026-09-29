# Source Map (candidate) — `privacy_lookup`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `privacy_lookup` |
| Display name | Privacy |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `2d6d159e4303b48a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/privacy_lookup/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mail`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 2, views 5, window actions 4, server actions 4, reports 0, mail templates 0, scheduled jobs 0, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `privacy.lookup.wizard` (Privacy Lookup Wizard); `privacy.lookup.wizard.line` (Privacy Lookup Wizard Line); `privacy.log` (Privacy Log)
- Objects extended from other modules (1): `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 3

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 32 of 32 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: privacy_lookup (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities
- Data-subject search-and-erase helper: an administrator enters a person's name and email, the system lists every stored record that refers to them (contacts, users, messages, other business records), then lets the administrator archive or delete them, and keeps an anonymised log of what was done (privacy_lookup/wizard/privacy_lookup_wizard.py:11-19,164-171,297-316; privacy_lookup/models/privacy_log.py:8-21).
- CONDITIONAL: category Hidden, auto_install True, depends only on mail (privacy_lookup/__manifest__.py:6,8,15).
- Entry points: "Privacy Lookup" action on the partner form and on the user form (via the user's partner), restricted to system administrators (privacy_lookup/wizard/privacy_lookup_wizard_views.xml:90-111; privacy_lookup/models/res_partner.py:10-17). Also a "Privacy Logs" menu under technical settings (privacy_lookup/views/privacy_log_views.xml:61-72).
- Bulk actions on result lines: "Archive Selection" and "Delete Selection" (privacy_lookup/data/ir_actions_server_data.xml:3-23).

## B. Business objects and lifecycle
- Lookup Wizard (temporary, kept 24 hours, no count cap) with name, email, found lines, execution details, link to log (privacy_lookup/wizard/privacy_lookup_wizard.py:12-21).
- Lookup Line: which model/record was found, whether active, whether deleted, an execution note per action (privacy_lookup/wizard/privacy_lookup_wizard.py:214-249).
- Privacy Log (persistent): date, handled-by user, anonymised name and email, executed actions, found-records description, note (privacy_lookup/models/privacy_log.py:13-21).
- Lifecycle: prefill from contact -> lookup -> lines listed -> archive/unarchive by toggle or delete per line -> the first action creates one log, later actions update the same log (privacy_lookup/wizard/privacy_lookup_wizard.py:173-184,288-303; (TEST) privacy_lookup/tests/test_privacy_wizard.py:127-150).

## C. Validations, automation, security
- Email must be valid or the search refuses (privacy_lookup/wizard/privacy_lookup_wizard.py:50-51; (TEST) privacy_lookup/tests/test_privacy_wizard.py:152-159).
- Search covers: contacts matching normalised email or name; users matching login or linked contact; messages authored by matched contacts; then every stored non-temporary model with email/name-style fields or references to matched contacts (privacy_lookup/wizard/privacy_lookup_wizard.py:54-96,100-161). Tables auto-handled elsewhere (notifications, followers, channel membership) are skipped to avoid duplicates (privacy_lookup/wizard/privacy_lookup_wizard.py:33-44,142).
- Search runs as raw database query so it ignores record rules; opening a found record checks read access, and unreadable records (e.g. other company) show no link but are still listed ((TEST) privacy_lookup/tests/test_privacy_wizard.py:47-72; privacy_lookup/wizard/privacy_lookup_wizard.py:251-262).
- Archive and delete are performed with elevated rights, bypassing the user's own record-level limits (privacy_lookup/wizard/privacy_lookup_wizard.py:295,301). Deleting an already-deleted line is refused; UI asks confirmation on delete (privacy_lookup/wizard/privacy_lookup_wizard.py:299-300; privacy_lookup/wizard/privacy_lookup_wizard_views.xml:59).
- Privacy/audit: log stores only masked name (first letter kept) and masked email (common public domains kept, others masked except the top-level suffix) (privacy_lookup/models/privacy_log.py:23-48; (TEST) privacy_lookup/tests/test_privacy_wizard.py:141). Log records who handled it (privacy_lookup/models/privacy_log.py:16-18). Model names in the description show technical names only to users in debug/technical group (privacy_lookup/wizard/privacy_lookup_wizard.py:202).
- Access: wizard, lines and log restricted to system administrators; lines cannot be hard-deleted through access rights (privacy_lookup/security/ir.model.access.csv:2-4). Log has no unlink protection beyond access: administrators hold delete right (privacy_lookup/security/ir.model.access.csv:4). No record rules / company scoping.

## D. Handoffs
- Contacts and users (subjects of the lookup): base. Messages, followers, notifications: mail. Every other installed module's data is discovered generically by field names, not by explicit hooks (privacy_lookup/wizard/privacy_lookup_wizard.py:100-143). Mass-mailing traces treated specially by name (privacy_lookup/wizard/privacy_lookup_wizard.py:115), owner mass_mailing.

## E. Configuration
- None (no settings). Hard-coded exclusion list of models (privacy_lookup/wizard/privacy_lookup_wizard.py:33-44). Fields with cascade-on-delete contact links are not searched as indirect references (privacy_lookup/wizard/privacy_lookup_wizard.py:142).

## F. Extension path
- No Community module depends on it (manifest scan). Extends contact via its own partner method (privacy_lookup/models/res_partner.py:8).

## G. Not verified
- Legal sufficiency for erasure requests and completeness for models storing personal data in non-standard fields: UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether deleting linked records leaves business documents (e.g. invoices) consistent: UNKNOWN — EVIDENCE INSUFFICIENT.

